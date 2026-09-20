import os
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


def test_run_loads_file_secret_and_executes_granian(tmp_path: Path) -> None:
    secret = tmp_path / "dsn"
    secret.write_text("test-dsn\n")
    binary = tmp_path / "granian"
    binary.write_text(
        '#!/bin/sh\nprintf "%s\\n" "$SENTRY_DSN" "${SENTRY_DSN_FILE-unset}" "$@"\n',
    )
    binary.chmod(0o755)
    environment = {
        **os.environ,
        "PATH": f"{tmp_path}:{os.environ['PATH']}",
        "SENTRY_DSN_FILE": str(secret),
        "SENTRY_DSN": "previous",
    }
    result = subprocess.run(  # noqa: S603
        ["/bin/bash", str(ROOT / "start_application.sh"), "run"],
        env=environment,
        check=False,
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.splitlines() == [
        "test-dsn",
        "unset",
        "--interface",
        "asgi",
        "--factory",
        "--host",
        "0.0.0.0",  # noqa: S104
        "--port",
        "8080",
        "main:create_app",
    ]


@pytest.mark.parametrize("action", ["init", "taskiq-worker", "unknown"])
def test_unknown_action_fails(action: str) -> None:
    environment = {k: v for k, v in os.environ.items() if k != "SENTRY_DSN_FILE"}
    result = subprocess.run(  # noqa: S603
        ["/bin/bash", str(ROOT / "start_application.sh"), action],
        env=environment,
        check=False,
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 2


def test_unreadable_secret_fails(tmp_path: Path) -> None:
    result = subprocess.run(  # noqa: S603
        ["/bin/bash", str(ROOT / "start_application.sh"), "run"],
        env={**os.environ, "SENTRY_DSN_FILE": str(tmp_path / "missing")},
        check=False,
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 1
    assert "unreadable" in result.stderr
