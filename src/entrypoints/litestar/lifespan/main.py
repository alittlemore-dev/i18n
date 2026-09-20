import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager, suppress

from litestar import Litestar

from infra.config.initializers import init_sentry, monitor_event_loop_lag


@asynccontextmanager
async def app_lifespan(app: Litestar) -> AsyncIterator[None]:
    monitor: asyncio.Task[None] | None = None
    try:
        init_sentry()
        monitor = asyncio.create_task(monitor_event_loop_lag(), name="i18n-event-loop-lag")
        yield
    finally:
        if monitor is not None:
            monitor.cancel()
            with suppress(asyncio.CancelledError):
                await monitor
        await app.state.dishka_container.close()
