# i18n

Сервис локализации alittlemore.dev с отдельными русским и английским каталогами переводов для Competency Trainer и Personal Workspace.

[English version](./README.md)

| Категория | Технологии |
| --- | --- |
| Покрытие | ![coverage-backend](./badges/coverage-backend.svg) |
| Backend | ![python](./badges/python.svg) ![litestar](./badges/litestar.svg) ![pydantic](./badges/pydantic.svg) ![dishka](./badges/dishka.svg) ![granian](./badges/granian.svg) ![uv](./badges/uv.svg) |
| Кэш | ![valkey](./badges/valkey.svg) |
| Тестирование | ![pytest](./badges/pytest.svg) |
| Логирование | ![structlog](./badges/structlog.svg) ![ecs-logging](./badges/ecs-logging.svg) ![sentry](./badges/sentry.svg) |
| Качество | ![ruff](./badges/ruff.svg) ![mypy](./badges/mypy.svg) ![bandit](./badges/bandit.svg) ![pip-audit](./badges/pip-audit.svg) ![vulture](./badges/vulture.svg) ![trivy](./badges/trivy.svg) ![hadolint](./badges/hadolint.svg) ![dockle](./badges/dockle.svg) |
| Доставка | ![docker](./badges/docker.svg) ![docker-compose](./badges/docker-compose.svg) ![github-actions](./badges/github-actions.svg) ![dependabot](./badges/dependabot.svg) |

## Начало работы

```sh
cp .env.example .env
make install
docker compose --env-file .env.test -f docker-compose.test.yml up -d --wait
make run-local
make tests-fast
make build
```

Контракт контейнера: `start_application.sh run`, порт `8080`, readiness `/api/i18n/healthcheck/ready`. CI публикует проверенный образ `ghcr.io/alittlemore-dev/i18n` с тегами SHA и `latest`.

[Запуск, настройки и проверки](../docs/runtime.md). Общий deployment принадлежит репозиторию infra.
