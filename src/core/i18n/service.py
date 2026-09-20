import hashlib
import json
from collections.abc import Mapping
from string import Formatter

from core.i18n.catalogs import competency, workspace
from core.i18n.enums import CatalogEnum, LanguageEnum

Catalog = Mapping[LanguageEnum, Mapping[str, str]]
CATALOGS: Mapping[CatalogEnum, Catalog] = {
    CatalogEnum.COMPETENCY: competency.MESSAGES,
    CatalogEnum.WORKSPACE: workspace.MESSAGES,
}
LANGUAGE_LABELS = {LanguageEnum.RU: "Русский", LanguageEnum.EN: "English"}
ENUM_KEYS = {
    "publishStatus": ("Draft", "Published"),
    "grade": ("Junior", "JuniorPlus", "Middle", "MiddlePlus", "Senior"),
    "interviewFrequency": ("constantly", "often", "rarely", "neverSeen"),
    "role": ("anon", "user", "moderator", "admin", "owner"),
    "articleReaction": ("heart", "fire", "thinking", "neutral", "poop"),
    "articleViewSource": ("Direct", "Internal", "Search", "Social", "External", "Unknown"),
}


def required_enum_keys(catalog: CatalogEnum) -> frozenset[str]:
    return frozenset(
        f"enum.{group}.{value}"
        for group, values in ENUM_KEYS.items()
        if catalog == CatalogEnum.COMPETENCY or group == "publishStatus"
        for value in values
    )


def placeholders(message: str) -> set[str]:
    return {name for _, name, _, _ in Formatter().parse(message) if name is not None}


def validate_catalog(catalog: CatalogEnum, messages: Catalog) -> None:
    baseline = messages[LanguageEnum.RU]
    for language in LanguageEnum:
        translations = messages[language]
        if translations.keys() != baseline.keys():
            message = f"Catalog {catalog}/{language} has inconsistent keys"
            raise ValueError(message)
        if not required_enum_keys(catalog) <= translations.keys():
            message = f"Catalog {catalog}/{language} is missing enum labels"
            raise ValueError(message)
        for key, text in translations.items():
            if not text.strip() or placeholders(text) != placeholders(baseline[key]):
                message = f"Catalog {catalog}/{language}/{key} has invalid translation"
                raise ValueError(message)


def catalog_revision(catalogs: Mapping[CatalogEnum, Catalog]) -> str:
    content = json.dumps(catalogs, ensure_ascii=False, sort_keys=True).encode()
    return hashlib.sha256(content).hexdigest()


class I18nService:
    def __init__(self, default_language: LanguageEnum) -> None:
        for catalog, messages in CATALOGS.items():
            validate_catalog(catalog, messages)
        self.default_language = default_language
        self.revision = catalog_revision(CATALOGS)

    def get_messages(self, catalog: CatalogEnum, language: LanguageEnum) -> dict[str, str]:
        return dict(CATALOGS[catalog][language])

    def get_languages(self) -> dict[LanguageEnum, str]:
        return dict(LANGUAGE_LABELS)
