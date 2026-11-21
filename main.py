"""One-line joke about working beside an AI coding agent.

Writes exactly one joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
when set, for local testing). No network, no input files.
"""

import os
from pathlib import Path

JOKE = (
    "My coding agent reviewed my PR, fixed every nitpick it left, "
    "approved it, and then asked me to review its review."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
