from litestar import Router

from entrypoints.litestar.api.healthcheck.endpoints import api_router as healthcheck_router
from entrypoints.litestar.api.i18n.endpoints import create_i18n_router


def create_api_router() -> Router:
    return Router(
        "/api/i18n", route_handlers=[healthcheck_router, create_i18n_router()], tags=["i18n"]
    )
