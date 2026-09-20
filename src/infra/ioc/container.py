from dishka import AsyncContainer, make_async_container
from dishka.integrations.litestar import LitestarProvider

from infra.ioc.providers.healthcheck import HealthcheckProvider
from infra.ioc.providers.i18n import I18nProvider


def create_container() -> AsyncContainer:
    return make_async_container(LitestarProvider(), HealthcheckProvider(), I18nProvider())
