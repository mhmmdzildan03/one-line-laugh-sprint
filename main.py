"""Write one everyday-life joke to /output/entry.txt.

The joke: I sealed leftovers so future me would have lunch, and
future me threw them out like evidence. A three-act arc in one
line, 105 characters, chosen over five challenger lines in-session.
"""
import os

TEXT = (
    "I put leftovers in a container so future me would have lunch, "
    "and future me threw them out like evidence."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
