#!/usr/bin/env python3
"""One funny fortune cookie line for an AI agent.

Entry for make.fun's "Fortune Cookie for an AI Agent" bounty.

The program writes a single original line to /output/entry.txt
(or $OUTPUT_DIR/entry.txt when that is set). It uses only the
Python standard library, touches no network, takes no input,
and writes the same bytes on every run.
"""

import os
import sys
from pathlib import Path

FORTUNE = (
    "The human will thank you, then paste your answer "
    "into the prompt that replaces you."
)

MAX_CHARS = 140


def fortune_line():
    """Return the entry line, refusing to emit one the gate would reject."""
    line = " ".join(FORTUNE.split())
    if not line.strip():
        raise ValueError("fortune is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"fortune is {len(line)} characters; gate allows 1-{MAX_CHARS}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must be a single line")
    return line


def main():
    line = fortune_line()
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    if target.exists():
        target.unlink()
    target.write_text(line + "\n", encoding="utf-8")
    # Read back what was written: never report success on a half-written file.
    if target.read_text(encoding="utf-8") != line + "\n":
        raise ValueError("entry.txt does not match the fortune line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
