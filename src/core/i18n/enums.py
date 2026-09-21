from enum import StrEnum


class LanguageEnum(StrEnum):
    RU = "ru"
    EN = "en"


class BundleEnum(StrEnum):
    SHARED = "shared"
    HOW_THIS_SITE_IS_BUILT = "how-this-site-is-built"
    ARTICLES = "articles"
    COMPETENCY_MATRIX = "competency-matrix"
    UPDATES = "updates"
    SITEMAP = "sitemap"
    ACCOUNT = "account"
    ADMIN_PANEL = "admin-panel"
    PERSONAL_WORKSPACE = "personal-workspace"
