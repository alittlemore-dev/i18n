from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from core.i18n.enums import BundleEnum, LanguageEnum


class CamelCaseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class LanguageResponseSchema(CamelCaseSchema):
    code: LanguageEnum
    label: str


class LanguagesResponseSchema(CamelCaseSchema):
    default_language: LanguageEnum
    languages: list[LanguageResponseSchema]


class I18nBundleResponseSchema(CamelCaseSchema):
    bundle: BundleEnum
    language: LanguageEnum
    messages: dict[str, str]
