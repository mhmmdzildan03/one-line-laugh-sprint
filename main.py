"""Write one everyday-life joke to /output/entry.txt.

The joke: at midnight the fridge lights up bright when opened,
as if it wants both of us to get a clear look at my life choices.
One line, 117 characters.
"""
import os

TEXT = (
    "At midnight my fridge lights up bright when I open it, as if it "
    "wants us both to get a clear look at my life choices."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
