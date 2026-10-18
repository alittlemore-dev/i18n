from typing import Annotated

from litestar.params import PathParameter

from core.i18n.enums import BundleEnum, LanguageEnum

I18nBundlePath = Annotated[
    BundleEnum,
    PathParameter(
        title="Message bundle",
        description="Interface feature catalog to retrieve, identified by a listed bundle name.",
        schema_extra={"examples": ["personal-workspace", "shared"]},
    ),
]

I18nLanguagePath = Annotated[
    LanguageEnum,
    PathParameter(
        title="Interface language",
        description="Requested language code from GET /api/i18n/languages. No implicit fallback.",
        schema_extra={"examples": ["en", "ru"]},
    ),
]
