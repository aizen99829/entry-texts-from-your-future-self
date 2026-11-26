#!/usr/bin/env python3
"""Texts From Your Future Self — make.fun entry.

Writes exactly one line to /output/entry.txt: a text message from
your future self, equal parts warning and joke.

The joke lands on two beats: a present-day habit the future self
already knows the ending of, and one piece of advice that only
someone from the future could give.
"""

import os


OUTPUT_PATH = "/output/entry.txt"


MAX_CHARS = 200


def build_message():
    """Compose the one-line text from the future."""
    return (
        "Hey, it's you from 2036. Stop Googling your symptoms at 3AM — "
        "it's the chair, not a disease. Also, buy the dip in 2027. "
        "You're welcome."
    )


def validate(message):
    """The entry must be exactly one line under 200 characters."""
    lines = message.splitlines()
    if len(lines) != 1:
        raise ValueError("entry must be a single line")
    if len(message) >= MAX_CHARS:
        raise ValueError("entry must be under 200 characters")
    return message


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    message = validate(build_message())
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(message + "\n")
    print(f"Wrote {len(message)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
