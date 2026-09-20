# i18n

Standalone localization service infrastructure. Python 3.14, uv, Litestar, Granian, Dishka,
Pydantic Settings, Valkey, structlog/ECS and Sentry.

## Boundaries

- This repository owns the application, container image, test runtime and CI. Shared deployment
  and nginx configuration belong to the sibling infra repository.
- The current milestone is infrastructure only. Catalogs, language/domain contracts and translation
  handlers remain in their existing owners until an explicit migration task.
- HTTP entrypoints live under src/entrypoints/litestar; configuration and concrete infrastructure
  under src/infra. Keep business behavior out of HTTP handlers and DI providers.
- All current routes under /api/i18n are public operational endpoints. Classify new handlers as
  public, admin or internal before implementation.
- Do not change Git state (stage, commit, push, branch, reset or checkout) without explicit request.
- Keep task plans in the conversation; do not create workflow artifacts solely for a skill.

## Development

- Use pyproject.toml as the source of lint, formatting and typing configuration.
- Keep Makefiles thin: command logic belongs in scripts/.
- Use existing Make targets for installation, local runs, tests, quality, security and image checks.
  Checks must fail on errors, prepare their dependencies and clean up only resources they own.
- Test commands use .env.test and a dedicated Valkey port. Never flush shared databases.
- Require environment-backed settings explicitly; keep operational constants in
  src/infra/config/constants.py. Do not commit production secrets.
- Test HTTP behavior, failure handling, resource cleanup and container startup. Avoid tests that
  merely duplicate source text, tool versions or exact commands.
- Readiness checks Valkey on every call; liveness must work during a Valkey outage.
- Preserve privacy in logging and Sentry: do not export request bodies, cookies, authorization
  headers, raw query values or local variables.
- Close clients and cancel background tasks when the application shuts down.
- Change uv.lock only when dependencies intentionally change; update matching technology badges.
- Keep README translations short: description, technology table and essential starter commands.
  Operational detail belongs in docs/.
- Preserve unrelated work and keep changes scoped to the requested outcome.
