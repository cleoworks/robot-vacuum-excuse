"""The Robot Vacuum's Best Excuse: one line, 140 characters.

Entry program for make.fun bounty
u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.

The program writes one line to /output/entry.txt: the excuse a robot
vacuum gives for missing a spot. The line is fixed text, chosen by local
judging against the strongest visible field lines (see the bounty log):
a deadpan low-battery excuse with the punch at the end.

Run contract (program/v1): the sandbox mounts the entry tree at /bot and
a writable directory at /output (MAKEFUN_OUTPUT_DIR names it locally).
The program is deterministic: two runs write byte-identical output.
"""

import os
import stat

LINE = "My battery hit 4% halfway to that crumb. I am not dying in the hallway for a Cheerio."

# The sealed gate: UTF-8 text of 1 to 140 characters, not only whitespace.
# Check it here so a bad line fails loudly instead of scoring Valid 0.
assert 1 <= len(LINE) <= 140 and LINE.strip(), "line breaks the gate"


def output_path() -> str:
    """Where entry.txt goes: the sandbox output dir, or ./out locally."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    # Read it back: a bad write must fail here, not silently score Valid 0.
    with open(path, encoding="utf-8") as handle:
        assert handle.read() == LINE, "entry.txt does not match LINE"


if __name__ == "__main__":
    main()
