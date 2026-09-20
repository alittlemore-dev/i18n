#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
. "$script_dir/common.sh"
ensure_backend_deps
case "${1:?action is required}" in
    types)
        PYTHONPATH=src uv run mypy --explicit-package-bases --namespace-packages src
        PYTHONPATH=src uv run mypy --explicit-package-bases --namespace-packages tests
        ;;
    bandit) uv run bandit --configfile pyproject.toml -r src ;;
    vulture) PYTHONPATH=src uv run vulture src --min-confidence 100 ;;
    format|fix) uv run ruff format src tests ;;
    format-check) uv run ruff format src tests --check ;;
    ruff-check) uv run ruff check src tests --fix ;;
    ruff-lint-check) uv run ruff check src tests ;;
    lint-check)
        uv run ruff format src tests --check
        uv run ruff check src tests
        ;;
    lint-file)
        uv run ruff check --fix "${2:?file is required}"
        uv run ruff format "$2"
        ;;
    quality)
        bash "$script_dir/quality.sh" lint-check
        bash "$script_dir/quality.sh" types
        bash "$script_dir/quality.sh" bandit
        bash "$script_dir/quality.sh" vulture
        bash "$script_dir/test.sh" test "${2:-.env.test}" "${3:-}"
        ;;
    *) echo "Unknown quality action" >&2; exit 2 ;;
esac
