from core.i18n.catalogs import BUNDLES
from core.i18n.enums import BundleEnum, LanguageEnum


class I18nService:
    def __init__(self, default_language: LanguageEnum) -> None:
        self.default_language = default_language

    def get_messages(self, bundle: BundleEnum, language: LanguageEnum) -> dict[str, str]:
        return dict(BUNDLES[bundle][language])

    def get_languages(self) -> dict[LanguageEnum, str]:
        return {LanguageEnum.RU: "Русский", LanguageEnum.EN: "English"}
