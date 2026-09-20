from dishka import AsyncContainer, make_async_container
from dishka.integrations.litestar import LitestarProvider

from infra.ioc.providers.healthcheck import HealthcheckProvider


def create_container() -> AsyncContainer:
    return make_async_container(LitestarProvider(), HealthcheckProvider())
