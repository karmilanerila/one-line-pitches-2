"""One-line pitch backup entry for make.fun.

Writes a single-sentence pitch to /output/entry.txt.
The pitch names a concrete first idea (a little recipe app) and
frames describing it like telling a friend over coffee, with a
first version to try by tonight and almost nothing lost if it
does not work out.
"""

import os


ENTRY = (
    "Tell an agent about the little recipe app you've been meaning "
    "to build, describe it like you're telling a friend over coffee, "
    "and by tonight you'll have a first version to tap through \u2014 "
    "if you don't like it, you've only spent a chat."
)


def validate(entry: str) -> str:
    """Return the entry stripped, or raise if it breaks the gate."""
    text = entry.strip()
    if not 1 <= len(text) <= 240:
        raise ValueError("entry must be 1 to 240 characters")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return text


def main() -> None:
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
