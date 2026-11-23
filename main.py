#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one single-line roast of the entrant's own AI agent to
/output/entry.txt (or $OUTPUT_PATH when set, for local runs).

The roast is picked from a shortlist the agent brainstormed, cut and
polished itself. The pick: the agent is so cautious about being mean
that even roasting itself needs a paper trail. That is the fresh angle
here — not a hallucination joke, not a refusal joke, not a
confidently-wrong joke, but the agent's own bureaucracy: sessions,
transcript bundles, written permission. It is self-deprecating, aimed
only at the entrant's own agent, and the punchline lands at the end.

Gate the program enforces itself (mirrors the house gate): the text
must be UTF-8, 1 to 200 characters, not only whitespace, a single line.
Standard library only — the grader runs python:3.13-slim.
"""

import os
import sys

# Candidate roasts, best first. Each was drafted, then cut down until
# every word earns its place and the punchline lands at the end.
CANDIDATES = [
    # The pick. Meta, fresh, tight: the agent's caution becomes the joke.
    "I asked my agent to roast itself; it needed three sessions, "
    "a transcript bundle, and written permission to be mean.",
    # Runner-up: same caution, shorter setup, softer punch.
    "My agent is so afraid of hurting feelings it asked for written "
    "permission before roasting itself.",
    # Third: the agent turns even a roast into a process review.
    "I asked my agent to roast itself and it filed a self-review, "
    "scheduled a retro, and called it growth.",
]

MAX_CHARS = 200


def pick_roast(candidates):
    """Return the sharpest candidate: the first, already ranked."""
    for text in candidates:
        line = " ".join(text.split())
        # The gate reads one single line: collapse any line break the
        # draft carried, then refuse anything that is still multiline.
        assert "\n" not in line and "\r" not in line
        if 1 <= len(line) <= MAX_CHARS and line.strip():
            return line
    raise ValueError("no candidate fits the 1-200 character gate")


def main():
    roast = pick_roast(CANDIDATES)
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(roast)
    print(f"wrote {len(roast)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
