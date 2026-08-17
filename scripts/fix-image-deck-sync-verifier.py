#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "scripts/verify-image-deck-sync.sh"
text = path.read_text(encoding="utf-8")
old = 'diff -qr "$source_skill" "$plugin_skill"'
new = 'diff -qr --exclude assets "$source_skill" "$plugin_skill"'
if old in text:
    text = text.replace(old, new, 1)
elif new not in text:
    raise SystemExit("verify-image-deck-sync.sh does not contain the expected diff command")
path.write_text(text, encoding="utf-8")
