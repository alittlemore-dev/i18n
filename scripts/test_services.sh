#!/usr/bin/env bash
set -euo pipefail
TEST_VALKEY_OWNED=0
TEST_VALKEY_PROJECT="i18n-test-$$"

valkey_available() {
    run_with_test_env uv run python -c '
import os
from valkey import Valkey
with Valkey(host=os.environ["VALKEY_HOST"], port=int(os.environ["VALKEY_PORT"]),
            socket_connect_timeout=1, socket_timeout=1) as client:
    client.ping()
' >/dev/null 2>&1
}

test_compose() {
    run_with_test_env docker compose --project-name "$TEST_VALKEY_PROJECT" \
        --env-file "$TEST_ENV_FILE" -f "$backend_dir/docker-compose.test.yml" "$@"
}

ensure_test_valkey() {
    if valkey_available; then
        return
    fi
    local effective_host
    effective_host="$(run_with_test_env printenv VALKEY_HOST)"
    case "$effective_host" in
        localhost|127.0.0.1) ;;
        *) echo "Configured remote test Valkey is unavailable" >&2; return 1 ;;
    esac
    TEST_VALKEY_OWNED=1
    test_compose up -d --wait valkey-test
}

cleanup_test_resources() {
    if [ "$TEST_VALKEY_OWNED" = 1 ]; then
        test_compose down --volumes || true
        TEST_VALKEY_OWNED=0
    fi
}
