from typing import Annotated

from litestar.params import Parameter

from core.i18n.enums import BundleEnum, LanguageEnum

I18nBundlePath = Annotated[
    BundleEnum, Parameter(title="Bundle", description="Interface message bundle")
]

I18nLanguagePath = Annotated[
    LanguageEnum, Parameter(title="Language", description="Interface language code")
]
