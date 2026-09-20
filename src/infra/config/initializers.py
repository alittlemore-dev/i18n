import asyncio
from typing import TYPE_CHECKING

import sentry_sdk
from sentry_sdk.integrations.litestar import LitestarIntegration

from infra.config.constants import constants
from infra.config.loggers import logger
from infra.config.settings import settings

if TYPE_CHECKING:
    from sentry_sdk._types import Event, Hint


def scrub_request_data(event: Event, _hint: Hint) -> Event:
    request = event.get("request")
    if isinstance(request, dict):
        for field in ("cookies", "data", "headers", "query_string"):
            request.pop(field, None)
        url = request.get("url")
        if isinstance(url, str):
            request["url"] = url.split("?", 1)[0].split("#", 1)[0]
    return event


def init_sentry() -> None:
    if not settings.sentry.use:
        return
    sentry_sdk.init(
        dsn=settings.sentry.dsn.get_secret_value(),
        send_default_pii=False,
        include_local_variables=False,
        max_request_body_size="never",
        before_send=scrub_request_data,
        before_send_transaction=scrub_request_data,
        traces_sample_rate=1.0,
        enable_logs=True,
        profile_lifecycle="trace",
        integrations=[LitestarIntegration()],
    )


async def monitor_event_loop_lag() -> None:
    loop = asyncio.get_running_loop()
    while True:
        start = loop.time()
        await asyncio.sleep(constants.monitoring.interval_seconds)
        lag = loop.time() - start - constants.monitoring.interval_seconds
        if lag > constants.monitoring.lag_threshold_seconds:
            logger.warning("Event loop has lag", lag_seconds=lag)
