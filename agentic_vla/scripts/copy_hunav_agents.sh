#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  printf 'Usage: %s <hunav_agent_manager/config_dir>\n' "$0" >&2
  exit 2
fi

package_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target_dir="$1"

install -d "${target_dir}"
cp "${package_dir}/config/hunav_agents_factory.yaml" "${target_dir}/agents_factory.yaml"
cp "${package_dir}/config/hunav_agents_office_mixed.yaml" "${target_dir}/agents_office_mixed.yaml"

printf 'Copied HuNavSim agent configs to %s\n' "${target_dir}"
