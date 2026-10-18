from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from core.i18n.enums import BundleEnum, LanguageEnum


class CamelCaseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class LanguageResponseSchema(CamelCaseSchema):
    code: LanguageEnum = Field(
        description="Language code accepted by the bundle endpoint.",
        examples=["en"],
    )
    label: str = Field(
        description="Language name in its own language, suitable for a language selector.",
        examples=["English", "Русский"],
    )


class LanguagesResponseSchema(CamelCaseSchema):
    default_language: LanguageEnum = Field(
        description="Configured default language, suitable for the initial interface selection.",
        examples=["ru"],
    )
    languages: list[LanguageResponseSchema] = Field(
        description="Complete supported language list; no pagination.",
        examples=[[{"code": "ru", "label": "Русский"}, {"code": "en", "label": "English"}]],
    )


class I18nBundleResponseSchema(CamelCaseSchema):
    bundle: BundleEnum = Field(
        description="Requested interface message bundle identifier.",
        examples=["personal-workspace"],
    )
    language: LanguageEnum = Field(
        description="Language of every returned message.",
        examples=["en"],
    )
    messages: dict[str, str] = Field(
        description=(
            "Flat dictionary of message keys to localized text. Values can contain client-side "
            "interpolation placeholders; the service returns them unchanged."
        ),
        examples=[
            {"workspace.title": "Workspace", "workspaceDashboard.calendar.title": "Calendar"}
        ],
    )
