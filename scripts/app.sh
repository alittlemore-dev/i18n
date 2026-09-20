#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
. "$script_dir/common.sh"
require_uv
case "${1:?action is required}" in
    run)
        PYTHONPATH=src uv run --locked bash start_application.sh run
        ;;
    run-local)
        PYTHONPATH=src uv run --locked --group dev granian --interface asgi --factory \
            --host localhost --port 8000 --reload main:create_app
        ;;
    *) echo "Unknown app action" >&2; exit 2 ;;
esac
