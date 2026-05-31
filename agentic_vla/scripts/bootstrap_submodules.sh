#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${repo_root}"

git submodule sync --recursive
git submodule update --init --recursive
git submodule foreach 'git fetch origin agentic-vla && git checkout agentic-vla && git pull --ff-only origin agentic-vla'
