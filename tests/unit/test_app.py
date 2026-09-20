import json
from unittest.mock import AsyncMock, patch

import pytest
from litestar import get
from litestar.testing import TestClient
from structlog.testing import capture_logs
from valkey.exceptions import ConnectionError as ValkeyConnectionError

from infra.config.settings import settings
from main import create_app


@pytest.mark.parametrize("cache_enabled", [True, False])
def test_health_and_routes(monkeypatch: pytest.MonkeyPatch, cache_enabled: bool) -> None:
    monkeypatch.setattr(settings.app, "use_cache", cache_enabled)
    with TestClient(create_app()) as client:
        health = client.get("/api/i18n/healthcheck")
        assert health.status_code == 200
        assert health.content == b""
        assert client.get("/api/i18n/docs").status_code == 200
        for path in (
            "/api/healthcheck",
            "/api/docs",
            "/api/i18n/languages",
            "/api/i18n/bundles/ru",
            "/api/i18n/bundles/en",
            "/api/auth/login",
        ):
            assert client.get(path).status_code == 404


def test_readiness_recovers_and_is_not_cached(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(settings.app, "use_cache", True)
    with (
        patch("valkey.asyncio.Valkey.ping", new_callable=AsyncMock) as ping,
        TestClient(create_app()) as client,
    ):
        ping.side_effect = [True, ValkeyConnectionError("private-detail"), True]
        for code in (200, 503, 200):
            response = client.get("/api/i18n/healthcheck/ready")
            assert response.status_code == code
            assert response.content == b""
        assert ping.await_count == 3
        assert client.get("/api/i18n/healthcheck").status_code == 200
        assert ping.await_count == 3


def test_unexpected_error_does_not_expose_details() -> None:
    @get("/failure")
    async def failure() -> str:
        message = "sensitive-exception-detail"
        raise RuntimeError(message)

    app = create_app()
    app.register(failure)
    with TestClient(app, raise_server_exceptions=False) as client:
        response = client.get("/failure")
    assert response.status_code == 500
    assert "sensitive-exception-detail" not in response.text


def test_app_factories_have_independent_containers() -> None:
    first = create_app()
    second = create_app()
    assert first.state.dishka_container is not second.state.dishka_container
    with TestClient(first) as client:
        assert client.get("/api/i18n/healthcheck").status_code == 200
    with TestClient(second) as client:
        assert client.get("/api/i18n/healthcheck").status_code == 200


def test_request_logging_does_not_export_credentials() -> None:
    with TestClient(create_app()) as client, capture_logs() as logs:
        response = client.get(
            "/api/i18n/healthcheck?token=private-query",
            headers={"Authorization": "Bearer private-header", "Cookie": "session=private-cookie"},
        )
    assert response.status_code == 200
    assert logs
    serialized = json.dumps(logs)
    for value in ("private-query", "private-header", "private-cookie"):
        assert value not in serialized
