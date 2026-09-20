import pytest
from litestar.stores.memory import MemoryStore
from litestar.testing import TestClient
from pydantic import ValidationError

from core.i18n.enums import CatalogEnum, LanguageEnum
from core.i18n.service import CATALOGS, I18nService, catalog_revision, validate_catalog
from infra.config.constants import constants
from infra.config.settings import I18nSettings, settings
from main import create_app


@pytest.mark.parametrize("catalog", list(CatalogEnum))
def test_catalog_languages_keys_and_placeholders(catalog: CatalogEnum) -> None:
    validate_catalog(catalog, CATALOGS[catalog])


@pytest.mark.parametrize("defect", ["missing_key", "missing_enum", "placeholder", "empty"])
def test_catalog_validation_rejects_broken_translations(defect: str) -> None:
    messages = {
        language: dict(bundle) for language, bundle in CATALOGS[CatalogEnum.WORKSPACE].items()
    }
    if defect == "missing_key":
        del messages[LanguageEnum.EN]["app.siteName"]
    elif defect == "missing_enum":
        for bundle in messages.values():
            del bundle["enum.publishStatus.Draft"]
    elif defect == "placeholder":
        messages[LanguageEnum.EN]["app.siteName"] = "{unexpected}"
    else:
        messages[LanguageEnum.EN]["app.siteName"] = " "
    with pytest.raises(ValueError, match="Catalog"):
        validate_catalog(CatalogEnum.WORKSPACE, messages)


def test_revision_changes_with_translations() -> None:
    changed = {
        catalog: {language: dict(bundle) for language, bundle in messages.items()}
        for catalog, messages in CATALOGS.items()
    }
    changed[CatalogEnum.WORKSPACE][LanguageEnum.EN]["app.siteName"] = "Changed"
    assert catalog_revision(changed) != catalog_revision(CATALOGS)
    assert catalog_revision(dict(reversed(list(CATALOGS.items())))) == catalog_revision(CATALOGS)


def test_returned_messages_do_not_mutate_catalog() -> None:
    service = I18nService(LanguageEnum.RU)
    returned = service.get_messages(CatalogEnum.WORKSPACE, LanguageEnum.EN)
    returned["app.siteName"] = "Changed"
    assert (
        service.get_messages(CatalogEnum.WORKSPACE, LanguageEnum.EN)["app.siteName"]
        == "Personal workspace"
    )


def test_default_language_setting(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("I18N_DEFAULT_LANGUAGE", "en")
    monkeypatch.setattr(settings, "i18n", I18nSettings())
    with TestClient(create_app()) as client:
        assert client.get("/api/i18n/languages").json()["defaultLanguage"] == "en"
    monkeypatch.setenv("I18N_DEFAULT_LANGUAGE", "de")
    with pytest.raises(ValidationError):
        I18nSettings()


@pytest.mark.parametrize("enabled", [True, False])
def test_bundle_cache_isolated_and_optional(monkeypatch: pytest.MonkeyPatch, enabled: bool) -> None:
    monkeypatch.setattr(settings.app, "use_cache", enabled)
    app = create_app()
    app.stores.register(constants.valkey.store_name, MemoryStore(), allow_override=True)
    calls: list[tuple[CatalogEnum, LanguageEnum]] = []
    original = I18nService.get_messages

    def counted(self: I18nService, catalog: CatalogEnum, language: LanguageEnum) -> dict[str, str]:
        calls.append((catalog, language))
        return original(self, catalog, language)

    monkeypatch.setattr(I18nService, "get_messages", counted)
    with TestClient(app) as client:
        for prefix in ("", "/personal-workspace"):
            for language in ("ru", "en"):
                path = f"/api/i18n{prefix}/bundles/{language}"
                first = client.get(path)
                second = client.get(path + "?irrelevant=value")
                assert first.status_code == second.status_code == 200
                assert first.json() == second.json()
                assert first.json()["language"] == language
        assert (
            client.get("/api/i18n/bundles/en").json()["messages"]["app.siteName"]
            == "Competency Trainer"
        )
        assert (
            client.get("/api/i18n/personal-workspace/bundles/en").json()["messages"]["app.siteName"]
            == "Personal workspace"
        )
    assert len(calls) == (4 if enabled else 10)
