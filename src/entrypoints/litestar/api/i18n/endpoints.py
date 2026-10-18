from dishka import FromDishka
from dishka.integrations.litestar import DishkaRouter
from litestar import Controller, get

from core.i18n.service import I18nService
from entrypoints.litestar.api.i18n.cache import create_i18n_cache_key
from entrypoints.litestar.api.i18n.openapi import error_responses
from entrypoints.litestar.api.i18n.parameters import I18nBundlePath, I18nLanguagePath
from entrypoints.litestar.api.i18n.schemas import (
    I18nBundleResponseSchema,
    LanguageResponseSchema,
    LanguagesResponseSchema,
)
from infra.config.constants import constants
from infra.config.settings import settings


class I18nController(Controller):
    path = ""

    @get(
        "/languages",
        summary="List supported interface languages",
        description=(
            "Return every supported interface language, its native display label and the "
            "configured default language. This public list is not paginated and requires "
            "no authentication. Use the returned codes in the bundle endpoint."
        ),
        responses=error_responses(),
        cache=constants.response_cache.default_ttl_seconds if settings.app.use_cache else False,
        cache_key_builder=create_i18n_cache_key(settings.i18n.default_language),
    )
    async def languages(self, service: FromDishka[I18nService]) -> LanguagesResponseSchema:
        return LanguagesResponseSchema(
            default_language=service.default_language,
            languages=[
                LanguageResponseSchema(code=code, label=label)
                for code, label in service.get_languages().items()
            ],
        )

    @get(
        "/bundles/{bundle:str}/{language:str}",
        summary="Get localized interface messages",
        description=(
            "Return the complete flat map of message keys to localized text for the requested "
            "bundle and language. Message keys are stable application identifiers and may "
            "contain dots; values may include placeholders such as {username}, which clients "
            "must interpolate. The response does not fall back to the default language. "
            "Unsupported path values return 400. This public endpoint requires no authentication."
        ),
        responses=error_responses(validation=True),
        cache=constants.response_cache.default_ttl_seconds if settings.app.use_cache else False,
        cache_key_builder=create_i18n_cache_key(settings.i18n.default_language),
    )
    async def bundle(
        self,
        bundle: I18nBundlePath,
        language: I18nLanguagePath,
        service: FromDishka[I18nService],
    ) -> I18nBundleResponseSchema:
        return I18nBundleResponseSchema(
            bundle=bundle, language=language, messages=service.get_messages(bundle, language)
        )


api_router = DishkaRouter("", route_handlers=[I18nController], opt={"auth_public": True})
