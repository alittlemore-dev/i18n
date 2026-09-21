from dishka import FromDishka
from dishka.integrations.litestar import DishkaRouter
from litestar import Controller, get

from core.i18n.service import I18nService
from entrypoints.litestar.api.i18n.cache import create_i18n_cache_key
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
