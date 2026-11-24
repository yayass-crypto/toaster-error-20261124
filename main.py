"""The Funniest Toaster Error Message — one-line entry.

Writes the toaster's error message to /output/entry.txt.
"""

import os

ENTRY = "911 has been called. They hung up when I said it was about toast."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
