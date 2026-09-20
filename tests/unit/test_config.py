from unittest.mock import AsyncMock, Mock, patch

import ecs_logging
import pytest
import structlog
from pydantic import ValidationError

from infra.config.initializers import init_sentry, monitor_event_loop_lag, scrub_request_data
from infra.config.loggers import build_project_logging_config
from infra.config.settings import AppSettings, Settings, ValkeySettings, settings


def test_settings_load_explicit_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("VALKEY_HOST", "cache.example.test")
    monkeypatch.setenv("VALKEY_PORT", "6380")
    assert Settings().valkey.url == "valkey://cache.example.test:6380/0"


def test_required_app_settings(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("APP_DEBUG")
    monkeypatch.delenv("APP_USE_CACHE")
    with pytest.raises(ValidationError):
        AppSettings(_env_file=None)


@pytest.mark.parametrize("port", ["0", "65536", "bad"])
def test_invalid_valkey_port(monkeypatch: pytest.MonkeyPatch, port: str) -> None:
    monkeypatch.setenv("VALKEY_PORT", port)
    with pytest.raises(ValidationError):
        ValkeySettings()


@pytest.mark.parametrize("enabled", [False, True])
def test_sentry_privacy(monkeypatch: pytest.MonkeyPatch, enabled: bool) -> None:
    monkeypatch.setattr(settings.sentry, "use", enabled)
    with patch("infra.config.initializers.sentry_sdk.init") as initialize:
        init_sentry()
    if not enabled:
        initialize.assert_not_called()
        return
    options = initialize.call_args.kwargs
    assert options["send_default_pii"] is False
    assert options["include_local_variables"] is False
    assert options["max_request_body_size"] == "never"
    for callback in ("before_send", "before_send_transaction"):
        event = {
            "request": {
                "url": "https://example.test/path?secret=hidden#hidden",
                "cookies": {"session": "hidden"},
                "headers": {"Authorization": "hidden"},
                "data": "hidden",
                "query_string": "secret=hidden",
            }
        }
        assert options[callback](event, {}) == {"request": {"url": "https://example.test/path"}}


def test_sentry_event_without_request() -> None:
    assert scrub_request_data({}, {}) == {}


@pytest.mark.parametrize("debug", [True, False])
def test_logging_renderer(debug: bool) -> None:
    config = build_project_logging_config(debug=debug)
    expected = structlog.dev.ConsoleRenderer if debug else ecs_logging.StructlogFormatter
    assert isinstance(config.processors[-1], expected)


async def test_lag_monitor_reports_only_delays() -> None:
    loop = Mock()
    loop.time.side_effect = [0, 1, 1, 4, 4]
    with (
        patch("infra.config.initializers.asyncio.get_running_loop", return_value=loop),
        patch("infra.config.initializers.asyncio.sleep", new_callable=AsyncMock) as sleep,
        patch("infra.config.initializers.logger") as logger,
    ):
        sleep.side_effect = [None, None, RuntimeError("stop monitor")]
        with pytest.raises(RuntimeError, match="stop monitor"):
            await monitor_event_loop_lag()
    logger.warning.assert_called_once_with("Event loop has lag", lag_seconds=2.0)
