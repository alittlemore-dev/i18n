from litestar import Router

from entrypoints.litestar.api.healthcheck.endpoints import api_router as healthcheck_router

api_router = Router("/api/i18n", route_handlers=[healthcheck_router], tags=["i18n"])
