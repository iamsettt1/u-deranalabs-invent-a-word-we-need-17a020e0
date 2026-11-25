#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Writes one invented English word and its one-line definition to
/output/entry.txt (or $OUTPUT_DIR/entry.txt).

The word: doorjog — the awkward little jog you break into when someone
holds a door open for you from twenty metres away.

Why this word: English has no name for the hurried half-jog politeness
forces on you when a stranger holds a door from twenty metres away.
Everyone has done it, nobody has named it. "Doorjog" is built from two
plain English words, so it is sayable on first sight, spellable on first
hearing, and memorable after one use.
"""

import os

ENTRY = (
    "doorjog \u2014 the awkward little jog you break into when someone "
    "holds a door open for you from twenty metres away."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-140")
    if "\n" in text or text != text.strip():
        raise SystemExit("entry must be a single non-blank line")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
