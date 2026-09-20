from collections.abc import AsyncIterator

from dishka import Provider, Scope, provide
from valkey.asyncio import Valkey

from infra.config.constants import constants
from infra.config.settings import settings
from infra.healthcheck import ReadinessChecker


class HealthcheckProvider(Provider):
    @provide(scope=Scope.APP)
    async def provide_valkey(self) -> AsyncIterator[Valkey]:
        client = Valkey.from_url(
            settings.valkey.url,
            socket_timeout=constants.valkey.timeout_seconds,
            socket_connect_timeout=constants.valkey.timeout_seconds,
        )
        try:
            yield client
        finally:
            await client.aclose()

    @provide(scope=Scope.REQUEST)
    def provide_readiness_checker(self, valkey: Valkey) -> ReadinessChecker:
        return ReadinessChecker(valkey=valkey)
