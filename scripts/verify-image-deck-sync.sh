#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_skill="$repo_root/skills/image-deck"
plugin_skill="$repo_root/plugins/image-deck/skills/image-deck"

diff -qr "$source_skill" "$plugin_skill"
echo "image-deck source and OpenAI plugin bundle are in sync."
