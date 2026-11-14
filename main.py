"""agency-poem-01 entry: writes one poem about agency to /output/entry.txt.

Python 3.13, standard library only, no network, deterministic: every run
writes exactly the same bytes. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join(
    [
        "The garden app flagged it on Tuesday:",
        "third plant from the fence, leaves curled,",
        "yield forecast zero, remove and replace.",
        "A red X sat on its photograph all week.",
        "",
        "She had planted that row in March,",
        "twelve bird's eye chilies, in soil she had",
        "carried herself in the cracked blue bucket,",
        "two trips, because one trip hurt her shoulder.",
        "",
        "The third plant was weak. That was plain.",
        "Its stem leaned like it was listening.",
        "But on Thursday a bud had opened anyway,",
        "white, no bigger than a fingernail paring.",
        "",
        "She deleted the alert. Then the schedule.",
        "Then she tied the stem to a chopstick",
        "with the green string from a rice sack,",
        "and watered it last, by hand, from a cup,",
        "the way you water something",
        "you have decided about yourself.",
        "",
        "In August it gave her four chilies.",
        "She put all four in one sambal",
        "and ate it without telling anyone why it burned so well.",
    ]
)


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    # The poem itself is 846 characters; the file adds one trailing newline.
    (out_dir / "entry.txt").write_text(POEM + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
