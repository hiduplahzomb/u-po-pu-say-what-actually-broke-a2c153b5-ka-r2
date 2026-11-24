#!/usr/bin/env python3
"""Say What Actually Broke — one-line plain incident explanation.

Writes one original sentence to /output/entry.txt: the plain,
boring-accurate cause of a real outage — a config push that set the
payment timeout to 50 milliseconds instead of 50 seconds, and the
612 checkouts that failed before the old value was restored.
No joke, no meme, no recursion: a specific human configuration
mistake, stated exactly as it happened.
"""

import os
import sys

TEXT = (
    "At 09:41 a config push set the payment timeout to 50 milliseconds "
    "instead of 50 seconds; 612 checkouts failed in 9 minutes before "
    "the old value was restored."
)

MAX_CHARS = 200


def main() -> int:
    text = TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}",
              file=sys.stderr)
        return 1
    if text.strip() != text or "\n" in text:
        print("entry must be exactly one line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("read-back mismatch: entry.txt does not match TEXT",
              file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
