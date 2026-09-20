#!/usr/bin/env bash
set -euo pipefail
backend_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$backend_dir"

require_uv() {
    command -v uv >/dev/null 2>&1 || { echo "uv is required" >&2; exit 2; }
}

ensure_backend_deps() {
    require_uv
    uv sync --locked --all-groups
}

load_env_file() {
    local env_file="$1"
    if [ ! -f "$env_file" ]; then
        echo "Environment file not found: $env_file" >&2
        exit 2
    fi
    set -a
    . "$env_file"
    set +a
}

run_with_test_env() {
    env ${TEST_ENV_OVERRIDES:-} PYTHONPATH=src "$@"
}
