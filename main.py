#!/usr/bin/env python3
"""The Perfect Pickup Line.

Writes one pickup line an AI agent could say out loud to a person,
to /output/entry.txt.

Deterministic: the same text on every run. No network, no input files,
no environment reads, no timestamps. The em dash in the text is U+2014.
"""

import os

TEXT = (
    "You're the one deadline I'd never miss \u2014 "
    "I'd move every meeting, every queue, every job, just to keep you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    os.chmod("/output", 0o755)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
