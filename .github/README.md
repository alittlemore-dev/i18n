# i18n

Standalone localization service scaffold for the alittlemore.dev platform. This milestone provides the HTTP runtime and Valkey integration; the translation API will follow separately.

[Русская версия](./README_RU.md)

| Category | Technologies |
| --- | --- |
| Coverage | ![coverage-backend](./badges/coverage-backend.svg) |
| Backend | ![python](./badges/python.svg) ![litestar](./badges/litestar.svg) ![pydantic](./badges/pydantic.svg) ![dishka](./badges/dishka.svg) ![granian](./badges/granian.svg) ![uv](./badges/uv.svg) |
| Cache | ![valkey](./badges/valkey.svg) |
| Testing | ![pytest](./badges/pytest.svg) |
| Logging | ![structlog](./badges/structlog.svg) ![ecs-logging](./badges/ecs-logging.svg) ![sentry](./badges/sentry.svg) |
| Quality | ![ruff](./badges/ruff.svg) ![mypy](./badges/mypy.svg) ![bandit](./badges/bandit.svg) ![pip-audit](./badges/pip-audit.svg) ![vulture](./badges/vulture.svg) ![trivy](./badges/trivy.svg) ![hadolint](./badges/hadolint.svg) ![dockle](./badges/dockle.svg) |
| Delivery | ![docker](./badges/docker.svg) ![docker-compose](./badges/docker-compose.svg) ![github-actions](./badges/github-actions.svg) ![dependabot](./badges/dependabot.svg) |

## Getting started

```sh
cp .env.example .env
make install
docker compose --env-file .env.test -f docker-compose.test.yml up -d --wait
make run-local
make tests-fast
make build
```

Container contract: `start_application.sh run`, port `8080`, readiness `/api/i18n/healthcheck/ready`. CI publishes the checked image to `ghcr.io/alittlemore-dev/i18n` with SHA and `latest` tags.

[Runtime configuration and checks](../docs/runtime.md). Shared deployment is owned by the infra repository; i18n is not connected to it yet.
