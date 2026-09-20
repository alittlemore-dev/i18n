#!/usr/bin/env bash
set -euo pipefail
repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
docker build -t "${IMAGE_REF:-alittlemore-dev/i18n:local}" "$repo_dir"
