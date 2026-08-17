#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_skill="$repo_root/skills/image-deck"
plugin_skill="$repo_root/plugins/image-deck/skills/image-deck"
target_dir="${CODEX_IMAGE_DECK_DIR:-$HOME/.codex/skills/image-deck}"

if [[ ! -d "$source_skill" ]]; then
  echo "Missing source skill: $source_skill" >&2
  exit 1
fi

rm -rf "$target_dir"
mkdir -p "$target_dir"
cp -R "$source_skill/." "$target_dir/"

diff -qr "$source_skill" "$plugin_skill"
echo "Synced image-deck to $target_dir"
