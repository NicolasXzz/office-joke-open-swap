#!/usr/bin/env python3
"""One-line office joke for make.fun's Office Joke Open.

Writes a single office joke (99 chars) to /output/entry.txt.
Stdlib only, no network, deterministic.
"""
import os

JOKE = "I asked Excel to VLOOKUP my promotion and it returned #N/A, which HR has now added to my job title."


def main():
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 chars"
    assert JOKE == JOKE.strip(), "joke must be a single clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars")


if __name__ == "__main__":
    main()
