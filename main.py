#!/usr/bin/env python3
"""Dad Joke Showdown entry: one dad joke, written to /output/entry.txt.

The joke: a father at the family barbecue, three beats, twist on the
last word. The pun ("medium-rare") lands cleanly on the first read,
the scene is concrete and embodied, and the punchline arrives at the
very end so it reads naturally aloud across a dinner table.
"""

JOKE = (
    "At the barbecue I told my kids the burgers were done. "
    "My son said, 'Dad, they're still pink.' "
    "I said, 'That's not pink \u2014 that's medium-rare. "
    "And son, so is my patience.'"
)


def main() -> None:
    import os

    # Enforce the bounty gate in the program itself: 1-200 characters.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
