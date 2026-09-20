from core.i18n.catalogs import CATALOGS
from core.i18n.enums import CatalogEnum, LanguageEnum


class I18nService:
    def __init__(self, default_language: LanguageEnum) -> None:
        self.default_language = default_language

    def get_messages(self, catalog: CatalogEnum, language: LanguageEnum) -> dict[str, str]:
        return dict(CATALOGS[catalog][language])

    def get_languages(self) -> dict[LanguageEnum, str]:
        return {LanguageEnum.RU: "Русский", LanguageEnum.EN: "English"}
