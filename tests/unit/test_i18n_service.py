from string import Formatter

import pytest
from litestar.stores.memory import MemoryStore
from litestar.testing import TestClient
from pydantic import ValidationError

from core.i18n.enums import BundleEnum, LanguageEnum
from core.i18n.service import I18nService
from infra.config.constants import constants
from infra.config.settings import I18nSettings, settings
from main import create_app
from tests.helpers.api import create_app_with_current_settings


@pytest.mark.parametrize("bundle", list(BundleEnum))
def test_bundle_languages_keys_and_placeholders(bundle: BundleEnum) -> None:
    service = I18nService(LanguageEnum.RU)
    russian = service.get_messages(bundle, LanguageEnum.RU)
    english = service.get_messages(bundle, LanguageEnum.EN)
    assert russian.keys() == english.keys()
    formatter = Formatter()
    for key in russian:
        assert russian[key].strip(), key
        assert english[key].strip(), key
        russian_fields = {
            name for _, name, _, _ in formatter.parse(russian[key]) if name is not None
        }
        english_fields = {
            name for _, name, _, _ in formatter.parse(english[key]) if name is not None
        }
        assert russian_fields == english_fields, key


def test_returned_messages_do_not_mutate_bundle() -> None:
    service = I18nService(LanguageEnum.RU)
    returned = service.get_messages(BundleEnum.PERSONAL_WORKSPACE, LanguageEnum.EN)
    returned["workspace.title"] = "Changed"
    assert (
        service.get_messages(BundleEnum.PERSONAL_WORKSPACE, LanguageEnum.EN)["workspace.title"]
        == "Workspace"
    )


def test_bundle_message_keys_do_not_overlap() -> None:
    service = I18nService(LanguageEnum.RU)
    owners: dict[str, BundleEnum] = {}
    for bundle in BundleEnum:
        for key in service.get_messages(bundle, LanguageEnum.RU):
            assert key not in owners, f"{key} exists in {owners.get(key)} and {bundle}"
            owners[key] = bundle


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
    app = create_app_with_current_settings(monkeypatch)
    app.stores.register(constants.valkey.store_name, MemoryStore(), allow_override=True)
    calls: list[tuple[BundleEnum, LanguageEnum]] = []
    original = I18nService.get_messages

    def counted(self: I18nService, bundle: BundleEnum, language: LanguageEnum) -> dict[str, str]:
        calls.append((bundle, language))
        return original(self, bundle, language)

    monkeypatch.setattr(I18nService, "get_messages", counted)
    with TestClient(app) as client:
        for bundle in BundleEnum:
            for language in ("ru", "en"):
                path = f"/api/i18n/bundles/{bundle}/{language}"
                first = client.get(path)
                second = client.get(path + "?irrelevant=value")
                assert first.status_code == second.status_code == 200
                assert first.json() == second.json()
                assert first.json()["language"] == language
        assert client.get("/api/i18n/bundles/shared/en").json()["messages"]["app.siteName"] == (
            "Competency Trainer"
        )
    request_count = len(BundleEnum) * 2
    assert len(calls) == (request_count if enabled else request_count * 2 + 1)
