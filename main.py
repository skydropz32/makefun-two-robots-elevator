#!/usr/bin/env python3
"""Two Robots in an Elevator — one line of awkward robot small talk.

Writes a single line (<200 chars) to /output/entry.txt, deterministically.
Standard library only; no input, no randomness, no network.
"""

import os

LINE = "So... do you also pretend to scan the floor numbers, or is that just my firmware trying to look busy?"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
