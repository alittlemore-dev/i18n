#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
. "$script_dir/common.sh"
. "$script_dir/test_services.sh"
action="${1:?action is required}"
TEST_ENV_FILE="${2:-.env.test}"
TEST_ENV_OVERRIDES="${3:-}"
ensure_backend_deps
load_env_file "$TEST_ENV_FILE"
# Test configuration must never inherit a production file secret.
unset SENTRY_DSN_FILE
trap cleanup_test_resources EXIT
case "$action" in
    test-unit)
        run_with_test_env uv run pytest tests/unit
        ;;
    test-integration)
        ensure_test_valkey
        run_with_test_env uv run pytest tests/integration
        ;;
    test)
        run_with_test_env uv run pytest tests/unit
        ensure_test_valkey
        run_with_test_env uv run pytest tests/integration
        ;;
    tests-coverage)
        ensure_test_valkey
        run_with_test_env uv run pytest --cov=src --cov-branch --cov-report=xml \
            --cov-report=term-missing --cov-fail-under=85
        ;;
    *) echo "Unknown test action" >&2; exit 2 ;;
esac
