from typing import Annotated

from litestar.params import Parameter

from core.i18n.enums import LanguageEnum

I18nLanguagePath = Annotated[
    LanguageEnum, Parameter(title="Language", description="Interface language code")
]
