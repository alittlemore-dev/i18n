import asyncio
from unittest.mock import AsyncMock, Mock, patch

import pytest
import structlog.contextvars
from litestar import Litestar
from litestar.testing import TestClient
from valkey.exceptions import ConnectionError as ValkeyConnectionError

from entrypoints.litestar.lifespan.main import app_lifespan
from entrypoints.litestar.middlewares.logging import RequestIdLoggingMiddleware
from infra.config.settings import settings
from infra.healthcheck import ReadinessChecker, ReadinessCheckError
from main import create_app


async def test_readiness_wraps_connection_failure() -> None:
    client = Mock()
    client.ping = AsyncMock(side_effect=ValkeyConnectionError("unavailable"))
    with pytest.raises(ReadinessCheckError):
        await ReadinessChecker(valkey=client).check()


def test_clients_closed_on_shutdown(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(settings.app, "use_cache", True)
    with (
        patch("valkey.asyncio.Valkey.ping", new_callable=AsyncMock),
        patch("valkey.asyncio.Valkey.aclose", new_callable=AsyncMock) as close,
    ):
        with TestClient(create_app()) as client:
            assert client.get("/api/i18n/healthcheck/ready").status_code == 200
        assert close.await_count == 2


async def test_lifespan_cancels_monitor_and_closes_container() -> None:
    app = Litestar()
    app.state.dishka_container = Mock(close=AsyncMock())
    async with app_lifespan(app):
        await asyncio.sleep(0)
        monitors = [t for t in asyncio.all_tasks() if t.get_name() == "i18n-event-loop-lag"]
        assert len(monitors) == 1
    assert monitors[0].cancelled()
    app.state.dishka_container.close.assert_awaited_once()


async def test_failed_startup_closes_container() -> None:
    app = Litestar()
    app.state.dishka_container = Mock(close=AsyncMock())
    with (
        patch(
            "entrypoints.litestar.lifespan.main.init_sentry", side_effect=RuntimeError("bad dsn")
        ),
        pytest.raises(RuntimeError, match="bad dsn"),
    ):
        async with app_lifespan(app):
            pytest.fail("startup should fail")
    app.state.dishka_container.close.assert_awaited_once()


async def test_request_id_restored_even_after_error() -> None:
    structlog.contextvars.bind_contextvars(request_id="parent")
    seen = []

    async def downstream(*_args: object) -> None:
        seen.append(structlog.contextvars.get_contextvars()["request_id"])
        message = "failure"
        raise RuntimeError(message)

    try:
        with pytest.raises(RuntimeError, match="failure"):
            await RequestIdLoggingMiddleware().handle(
                scope=Mock(),
                receive=AsyncMock(),
                send=AsyncMock(),
                next_app=downstream,
            )
        assert seen[0] != "parent"
        assert structlog.contextvars.get_contextvars()["request_id"] == "parent"
    finally:
        structlog.contextvars.clear_contextvars()
