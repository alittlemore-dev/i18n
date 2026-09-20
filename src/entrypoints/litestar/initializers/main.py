from dishka import AsyncContainer
from dishka.integrations.litestar import setup_dishka
from litestar import Litestar
from litestar.config.response_cache import ResponseCacheConfig
from litestar.logging import StructLoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin
from litestar.plugins.pydantic import PydanticPlugin
from litestar.plugins.structlog import StructlogConfig, StructlogPlugin
from litestar.stores.base import Store
from litestar.stores.valkey import ValkeyStore
from valkey.asyncio import Valkey

from entrypoints.litestar.api.routers import create_api_router
from entrypoints.litestar.exception_handlers import get_litestar_exception_handlers
from entrypoints.litestar.lifespan.main import app_lifespan
from entrypoints.litestar.middlewares.logging import RequestIdLoggingMiddleware
from infra.config import loggers
from infra.config.constants import constants
from infra.config.settings import settings


def create_litestar_app(*, container: AsyncContainer) -> Litestar:
    logging = loggers.configure_project_logging(debug=settings.app.debug)
    stores: dict[str, Store] = (
        {
            constants.valkey.store_name: ValkeyStore(
                valkey=Valkey.from_url(
                    settings.valkey.url,
                    socket_timeout=constants.valkey.timeout_seconds,
                    socket_connect_timeout=constants.valkey.timeout_seconds,
                ),
                namespace=constants.valkey.namespace,
                handle_client_shutdown=True,
            ),
        }
        if settings.app.use_cache
        else {}
    )
    app = Litestar(
        route_handlers=[create_api_router()],
        debug=settings.app.debug,
        lifespan=[app_lifespan],
        exception_handlers=get_litestar_exception_handlers(),
        middleware=[RequestIdLoggingMiddleware()],
        stores=stores,
        response_cache_config=(
            ResponseCacheConfig(store=constants.valkey.store_name)
            if settings.app.use_cache
            else None
        ),
        plugins=[
            PydanticPlugin(prefer_alias=True),
            StructlogPlugin(
                config=StructlogConfig(
                    structlog_logging_config=StructLoggingConfig(
                        log_exceptions="never",
                        processors=logging.processors,
                        wrapper_class=logging.wrapper_class,
                        logger_factory=logging.logger_factory,
                        cache_logger_on_first_use=logging.cache_logger_on_first_use,
                    ),
                    middleware_logging_config=LoggingMiddlewareConfig(
                        request_log_fields=["path", "method", "path_params"],
                        response_log_fields=["status_code"],
                    ),
                ),
            ),
        ],
        openapi_config=OpenAPIConfig(
            title="i18n",
            version="1.0.0",
            path="/api/i18n/docs",
            render_plugins=[SwaggerRenderPlugin()],
        ),
    )
    setup_dishka(container=container, app=app)
    return app
