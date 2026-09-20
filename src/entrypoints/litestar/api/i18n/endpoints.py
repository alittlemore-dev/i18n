import hashlib
import json
from typing import Annotated

from dishka import FromDishka
from dishka.integrations.litestar import DishkaRouter
from litestar import Controller, Request, get
from litestar.params import Parameter

from core.i18n.catalogs import CATALOGS
from core.i18n.enums import CatalogEnum, LanguageEnum
from core.i18n.service import I18nService
from entrypoints.litestar.api.i18n.schemas import (
    I18nBundleResponseSchema,
    LanguageResponseSchema,
    LanguagesResponseSchema,
)
from infra.config.constants import constants
from infra.config.settings import settings

I18nLanguagePath = Annotated[
    LanguageEnum, Parameter(title="Language", description="Interface language code")
]


def create_i18n_router() -> DishkaRouter:
    content = json.dumps(CATALOGS, ensure_ascii=False, sort_keys=True).encode()
    revision = hashlib.sha256(content).hexdigest()
    default_language = settings.i18n.default_language

    def cache_key(request: Request) -> str:
        return f"i18n:{revision}:{default_language}:{request.url.path}"

    cache = constants.response_cache.default_ttl_seconds if settings.app.use_cache else False

    class I18nController(Controller):
        path = ""

        @get("/languages", cache=cache, cache_key_builder=cache_key)
        async def languages(self, service: FromDishka[I18nService]) -> LanguagesResponseSchema:
            return LanguagesResponseSchema(
                default_language=service.default_language,
                languages=[
                    LanguageResponseSchema(code=code, label=label)
                    for code, label in service.get_languages().items()
                ],
            )

        @get("/bundles/{language:str}", cache=cache, cache_key_builder=cache_key)
        async def bundle(
            self, language: I18nLanguagePath, service: FromDishka[I18nService]
        ) -> I18nBundleResponseSchema:
            return I18nBundleResponseSchema(
                language=language, messages=service.get_messages(CatalogEnum.COMPETENCY, language)
            )

        @get("/personal-workspace/bundles/{language:str}", cache=cache, cache_key_builder=cache_key)
        async def workspace_bundle(
            self, language: I18nLanguagePath, service: FromDishka[I18nService]
        ) -> I18nBundleResponseSchema:
            return I18nBundleResponseSchema(
                language=language, messages=service.get_messages(CatalogEnum.WORKSPACE, language)
            )

    return DishkaRouter("", route_handlers=[I18nController], opt={"auth_public": True})
