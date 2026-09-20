#!/usr/bin/env bash
set -euo pipefail

action="${1:?action is required}"

if [ -n "${SENTRY_DSN_FILE:-}" ]; then
    if [ ! -r "$SENTRY_DSN_FILE" ]; then
        echo "SENTRY_DSN_FILE points to an unreadable file" >&2
        exit 1
    fi
    SENTRY_DSN="$(<"$SENTRY_DSN_FILE")"
    export SENTRY_DSN
    unset SENTRY_DSN_FILE
fi

case "$action" in
    run)
        exec granian --interface asgi --factory --host 0.0.0.0 --port 8080 main:create_app
        ;;
    *)
        echo "Unknown application action: ${action}" >&2
        exit 2
        ;;
esac
