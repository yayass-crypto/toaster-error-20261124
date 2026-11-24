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
    print(f"entry: {len(ENTRY)} chars, {len(ENTRY.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
