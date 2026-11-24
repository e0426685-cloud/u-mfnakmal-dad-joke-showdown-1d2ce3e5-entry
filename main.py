"""Dad Joke Showdown: one original dad joke, written from scratch.

The joke is a question-and-answer dad joke built on the double
meaning of "make the bed": the everyday chore versus making
(fashioning) a bed out of wood. The setup sounds like an ordinary
morning question, and the punchline lands on the wood pun at the
very end, so it reads naturally aloud across a dinner table.

The program writes the joke to /output/entry.txt (or to
$OUTPUT_DIR/entry.txt when that variable is set, for local checks).
Python standard library only, fully deterministic, no network.
"""

import os

JOKE = (
    "I asked Dad if he was going to make the bed. "
    "He said, 'Yes \u2014 what kind of wood should I use?'"
)

MAX_CHARS = 200


def main() -> None:
    # Gate validation, mirroring the competition's sealed scorer:
    # UTF-8 text, 1-200 characters, not only whitespace, one line.
    assert "\n" not in JOKE and "\r" not in JOKE, "entry must be a single line"
    assert JOKE.strip(), "entry must not be only whitespace"
    assert JOKE == JOKE.strip(), "entry must not start or end with whitespace"
    assert JOKE.endswith("?'"), "entry must end on the punchline"
    assert 1 <= len(JOKE) <= MAX_CHARS, f"joke must be 1-200 chars, got {len(JOKE)}"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "written entry does not match"
    assert written.count("\n") == 0 and 1 <= len(written) <= MAX_CHARS
    print(f"Wrote {path} ({len(written)} characters)")


if __name__ == "__main__":
    main()
