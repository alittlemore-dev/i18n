from dataclasses import dataclass

from valkey.asyncio import Valkey
from valkey.exceptions import ValkeyError

from infra.config.loggers import logger


class ReadinessCheckError(Exception):
    pass


@dataclass(kw_only=True, slots=True)
class ReadinessChecker:
    valkey: Valkey

    async def check(self) -> None:
        try:
            await self.valkey.ping()
        except (ValkeyError, OSError) as exc:
            logger.warning("Valkey readiness check failed", exception_type=type(exc).__name__)
            raise ReadinessCheckError from exc
