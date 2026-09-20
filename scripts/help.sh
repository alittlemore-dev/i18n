#!/usr/bin/env bash
set -euo pipefail
printf '%s\n' \
    'install / lock              Install dependencies / update lockfile' \
    'run / run-local             Run on :8080 / reload on localhost:8000' \
    'tests-fast / tests          Unit / all tests (automatic test Valkey)' \
    'test-integration            Integration tests with real Valkey' \
    'tests-coverage              All tests with 85% coverage gate' \
    'format / lint-check / types Formatting, linting and strict typing' \
    'quality / security / vulture Quality and dependency security checks' \
    'build / test-container      Build image / verify running container' \
    'lint-dockerfiles / security-trivy-config / security-docker-image' \
    'publish-image               Publish checked image (explicit image arguments)'
