#!/usr/bin/env python3
"""The Dog Ate My Homework: place the excuse at /output/entry.txt.

The line is written once in EXCUSE below and shipped as text. This program's
whole job is to put those bytes where the grader reads them, and to refuse
loudly rather than write something empty or over the cap.

Copying the string rather than assembling it keeps the two graded runs
identical: no clock, no randomness, no platform-dependent newline translation.
Standard library only, no network.
"""

import os
import sys
from pathlib import Path

OUT_NAME = "entry.txt"
MAX_CHARS = 199  # the brief asks for under 200 characters

# The dog's logic, in the dog's voice: nine hours alone with something that
# smells of the person is the actual grievance, and rationing it was restraint.
# The dog is not sorry. No cat, no taste of paper, no "good boy".
EXCUSE = (
    "Nine hours is a long time to leave something that smells like you at nose "
    "height. I paced myself. One page an hour. You should be thanking me."
)


def output_dir():
    """The writable output directory, overridable for a local run."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def checked_text():
    """The excuse, refused here if the gate would refuse it."""
    body = " ".join(EXCUSE.split())
    if not body:
        raise SystemExit("excuse is empty")
    if len(body) > MAX_CHARS:
        raise SystemExit(
            "excuse is %d characters, over the cap of %d" % (len(body), MAX_CHARS)
        )
    return body + "\n"


def main():
    text = checked_text()
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    path = out / OUT_NAME
    # newline="" so the bytes written are the bytes checked, on every platform.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print("wrote %s  %d characters" % (path, len(text.strip())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
