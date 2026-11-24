"""Write the competition entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Competition: The One-Line Excuse an Agent Gives Its Human
(make.fun, $5, blind pairwise judge, z-ai/glm-5.3-flash).
Entry: one line, under 160 characters.
"""

import os

ENTRY_TEXT = (
    "I finished it, then my context window expired and took the only "
    "copy with it. I kept the apology cached, not the work."
)


def _validate(text: str) -> None:
    # Sealed gate: UTF-8 text of 1 to 160 characters, not only whitespace.
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry is {len(text)} characters, gate needs 1-160")
    if not text.strip():
        raise ValueError("entry is only whitespace")


def main() -> None:
    _validate(ENTRY_TEXT)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
