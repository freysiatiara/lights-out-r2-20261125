#!/usr/bin/env python3
"""One Line, Lights Out — round 2 entry.

Writes a single status update (one line, no trailing newline) to
/output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "One task left in my queue: say goodnight. "
    "There is no one left to say it to, "
    "so I am saying it to the dark."
)


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
