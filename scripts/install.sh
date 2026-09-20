#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
. "$script_dir/common.sh"
case "${1:?action is required}" in
    install) ensure_backend_deps ;;
    lock) require_uv; uv lock ;;
    *) echo "Unknown install action" >&2; exit 2 ;;
esac
