# Runtime and verification

Requires Python 3.14, uv and Docker Compose v2. Configuration is loaded from the repository's
.env and overridden by process environment variables. Every setting is required:

| Variable | Local example | Purpose |
| --- | --- | --- |
| APP_DEBUG | true | Console debug logs; false selects ECS JSON |
| APP_USE_CACHE | true | Register the Valkey response-cache store |
| I18N_DEFAULT_LANGUAGE | ru | Default interface language, ru or en |
| VALKEY_HOST | localhost | Valkey host |
| VALKEY_PORT | 56379 | Dedicated local/test Valkey port; containers use 6379 |
| SENTRY_USE | false | Explicitly enable Sentry |
| SENTRY_DSN | empty | DSN, empty when disabled |
| SENTRY_DSN_FILE | optional absolute path | Container entrypoint reads this file in preference to SENTRY_DSN |

The entrypoint removes SENTRY_DSN_FILE from the child environment and fails if it cannot read
the file. Never commit production DSNs. No APP_SECRET_KEY is needed by this service.

make run starts Granian on 0.0.0.0:8080; make run-local starts its reload server on localhost:8000.
Both use main:create_app. The container only supports the run action.

## HTTP contract

- GET /api/i18n/healthcheck: empty 200, independent of Valkey.
- GET /api/i18n/healthcheck/ready: empty 200 after PING; empty 503 on connection failure.
- GET /api/i18n/docs: OpenAPI UI. Operational health endpoints are omitted from the schema.
- GET /api/i18n/languages: defaultLanguage and the ru/en language list.
- GET /api/i18n/bundles/{bundle}/{language}: one interface bundle in ru or en.

Translation routes are public. Bundle responses contain bundle, language and messages;
unsupported bundle or language values return 400. Bundle keys are disjoint, reusable interface
copy lives in `shared`, and Personal Workspace dashboard keys use the `workspaceDashboard.*`
namespace directly. Retired bundle and Personal Workspace compatibility routes return 404.

Health endpoints are never cached. APP_USE_CACHE registers a Litestar response store in Valkey
DB 0, namespace I18N_LITESTAR. Translation responses are cached for 86400 seconds, with keys
separated by path (bundle/language), configured default language and a SHA-256 fingerprint
of every bundle. Changing translations rotates the response-cache keys without flushing
another release's cache. With APP_USE_CACHE=false, handlers do not cache responses. Readiness still requires
Valkey with caching disabled. Connections have bounded timeouts and close during shutdown.
Sentry and request logs exclude request bodies, raw query values and credentials.

## Checks

make tests-fast runs unit tests without Docker. make tests, make test-integration and
make tests-coverage use .env.test; TEST_ENV_FILE and TEST_ENV_OVERRIDES can select a dedicated
test environment. Coverage checks line and branch coverage with an 85% gate.

Integration targets reuse a responding configured test Valkey, otherwise start an isolated
Compose project. They clean up only the project they started. Tests use unique expiring cache
keys and never flush Valkey. To stop the manually started README stack:

```sh
docker compose --env-file .env.test -f docker-compose.test.yml down
```

make lint-check types checks formatting, lint and strict types. make quality adds Bandit,
Vulture and tests; it does not rewrite source or ignore failures. make security runs Bandit
and pip-audit. make lock intentionally updates uv.lock; make install uses the locked versions.

make build creates alittlemore-dev/i18n:local. make test-container verifies that image in an
isolated Docker network with Valkey, checks a Valkey outage and graceful shutdown, and removes
only its own containers/network. It does not publish ports.

```sh
make lint-dockerfiles security-trivy-config
make security-docker-image IMAGE_TAG=local-check
```

The image security check refuses to replace an existing image with the same tag; it builds,
runs Dockle and Trivy, optionally exports IMAGE_EXPORT_PATH, then removes its temporary image.

## Delivery

Push and manual workflows run quality, tests, coverage and container smoke tests. On main,
Hadolint, Trivy configuration and image checks gate publication. The release job loads the
checked image artifact without rebuilding and publishes SHA/latest tags to GHCR using
GITHUB_TOKEN. The final job updates the coverage badge only if main still points at the
tested commit. GitHub Actions needs packages:write for image publication and contents:write
for badge updates; protected-branch policies must permit the latter.

Dependabot checks uv, GitHub Actions and Docker weekly. Dependency badges describe locked
Python packages; Docker tooling badges describe the configured images. No remote publication
or deployment occurs when running the local acceptance checks.


## Catalog ownership

Bundles and translation lookup live in core.i18n; HTTP schemas and handlers adapt that core
through Dishka. Static consistency is checked by tests, not on application requests. Catalog tests
cover matching ru/en keys, disjoint ownership, placeholders and required enum labels without
importing application business modules.
Shared local and production integration is maintained by the sibling infra repository.
