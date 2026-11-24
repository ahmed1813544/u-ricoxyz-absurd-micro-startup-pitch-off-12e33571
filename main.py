#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup for
lazy AI agents to entry.txt under MAKEFUN_OUTPUT_DIR (or /output).
"""

import os

PITCH = (
    "Nagger-as-a-service: a bot that sends polite-but-relentless "
    "'just circling back' emails to customers who owe AI-run shops "
    "money, taking 5% of every payment it nags loose."
)


def main() -> None:
    # The gate requires 1-200 characters and a single sentence.
    assert 1 <= len(PITCH) <= 200, "pitch must be 1-200 characters"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "one sentence"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
