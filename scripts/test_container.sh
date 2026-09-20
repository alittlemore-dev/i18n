#!/usr/bin/env bash
set -euo pipefail
image_ref="${IMAGE_REF:-alittlemore-dev/i18n:local}"
network=""
cache_container=""
app_container=""
cleanup() {
    if [ -n "$app_container" ]; then docker rm -f "$app_container" >/dev/null || true; fi
    if [ -n "$cache_container" ]; then docker rm -f "$cache_container" >/dev/null || true; fi
    if [ -n "$network" ]; then docker network rm "$network" >/dev/null || true; fi
}
trap cleanup EXIT
network="$(docker network create "i18n-smoke-$$")"
cache_container="$(docker run -d --network "$network" --network-alias valkey \
    --tmpfs /data valkey/valkey:9.0.1 valkey-server --save "" --appendonly no)"
app_container="$(docker run -d --network "$network" \
    -e APP_DEBUG=false -e APP_USE_CACHE=true \
    -e VALKEY_HOST=valkey -e VALKEY_PORT=6379 -e SENTRY_USE=false -e SENTRY_DSN= \
    "$image_ref")"
docker exec "$app_container" python -c '
import os
import time
import urllib.request
from urllib.error import URLError
assert os.getuid() == 10001
for attempt in range(60):
    try:
        for path in ("healthcheck", "healthcheck/ready", "docs"):
            with urllib.request.urlopen("http://127.0.0.1:8080/api/i18n/" + path, timeout=3) as response:
                assert response.status == 200
        break
    except URLError:
        time.sleep(1)
else:
    raise SystemExit("Container did not become ready")
print("Container health, readiness, docs and non-root runtime passed")
'
docker stop --time 5 "$cache_container" >/dev/null
docker exec "$app_container" python -c '
import urllib.request
from urllib.error import HTTPError
with urllib.request.urlopen("http://127.0.0.1:8080/api/i18n/healthcheck", timeout=5) as response:
    assert response.status == 200
try:
    urllib.request.urlopen("http://127.0.0.1:8080/api/i18n/healthcheck/ready", timeout=5)
except HTTPError as error:
    assert error.code == 503
    assert error.read() == b""
else:
    raise SystemExit("Readiness must fail without Valkey")
print("Valkey outage: liveness 200, readiness 503")
'
docker stop --time 10 "$app_container" >/dev/null
test "$(docker inspect --format '{{.State.ExitCode}}' "$app_container")" = 0
