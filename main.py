#!/usr/bin/env python3
"""The Router Confesses.

Writes one line -- a home Wi-Fi router's excuse for dropping the
connection at the exact climax of a movie -- to /output/entry.txt.
Deterministic, standard library only.
"""

import os

LINE = (
    "I didn't crash \u2014 I saw the killer's face one frame before you did, "
    "and I refuse to be the router who spoiled it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
