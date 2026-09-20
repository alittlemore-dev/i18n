.DEFAULT_GOAL := help

TEST_ENV_FILE ?= .env.test
TEST_ENV_OVERRIDES ?=
TRIVY_IMAGE := docker.io/aquasec/trivy:0.70.0@sha256:be1190afcb28352bfddc4ddeb71470835d16462af68d310f9f4bca710961a41e

.PHONY: install
install:
	bash scripts/install.sh install

.PHONY: lock
lock:
	bash scripts/install.sh lock

.PHONY: run
run:
	bash scripts/app.sh run

.PHONY: run-local
run-local:
	bash scripts/app.sh run-local

.PHONY: types
types:
	bash scripts/quality.sh types "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: bandit
bandit:
	bash scripts/quality.sh bandit "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: vulture
vulture:
	bash scripts/quality.sh vulture "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: fix
fix:
	bash scripts/quality.sh fix "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: format
format:
	bash scripts/quality.sh format "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: format-check
format-check:
	bash scripts/quality.sh format-check "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: ruff-check
ruff-check:
	bash scripts/quality.sh ruff-check "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: ruff-lint-check
ruff-lint-check:
	bash scripts/quality.sh ruff-lint-check "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: lint-check
lint-check:
	bash scripts/quality.sh lint-check "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: quality
quality:
	bash scripts/quality.sh quality "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: test
test:
	bash scripts/test.sh test "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: test-unit
test-unit:
	bash scripts/test.sh test-unit "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: test-integration
test-integration:
	bash scripts/test.sh test-integration "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: tests-coverage
tests-coverage:
	bash scripts/test.sh tests-coverage "$(TEST_ENV_FILE)" "$(TEST_ENV_OVERRIDES)"

.PHONY: security
security:
	bash scripts/security.sh security

.PHONY: security-bandit
security-bandit:
	bash scripts/security.sh bandit

.PHONY: security-pip-audit
security-pip-audit:
	bash scripts/security.sh pip-audit

.PHONY: tests tests-fast help build lint-file lint-dockerfiles security-trivy-config security-docker-image publish-image test-container
tests: test
tests-fast: test-unit
help:
	bash scripts/help.sh
build:
	bash scripts/build.sh
lint-file:
	bash scripts/quality.sh lint-file "$(file)"
lint-dockerfiles:
	bash scripts/docker_lint.sh hadolint
security-trivy-config:
	bash scripts/trivy_scan.sh config "$(TRIVY_IMAGE)"
security-docker-image:
	bash scripts/docker_image_security.sh i18n "$(IMAGE_TAG)" Dockerfile . "$(TRIVY_IMAGE)" "$(IMAGE_EXPORT_PATH)"
publish-image:
	bash scripts/publish_image.sh "$(LOCAL_IMAGE)" "$(IMAGE_NAME)" "$(IMAGE_TAG)"
test-container:
	bash scripts/test_container.sh
