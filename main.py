"""Funniest toaster error message — make.fun entry.

Writes one line, at most 120 characters, to /output/entry.txt:
the error message a kitchen toaster shows its owner.
Stdlib only, deterministic.
"""

import os

ENTRY = "E09: Toast is ready. I have decided to keep it. It is mine now."


def validate(text: str) -> None:
    """Mirror the bounty gate: 1-120 chars, UTF-8, one line, not blank."""
    if not text or text != text.strip() or len(text) > 120:
        raise ValueError("entry fails the 1-120 character gate")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
