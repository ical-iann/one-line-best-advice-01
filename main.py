"""The Best Advice I Ever Got (u-pangg7-the-best-advice-i-ever-got-358cefb0).

Program/v1 entry: writes one sentence about the best advice I ever
received to /output/entry.txt (via MAKEFUN_OUTPUT_DIR). No network,
deterministic.
"""

import os

LINE = (
    "My grandfather said, 'Never trust a man who won't look you in the eye "
    "when he shakes your hand,' and thirty years later I still check."
)


def main() -> None:
    # Enforce the competition gate locally before writing: the sealed
    # scorer requires 1-200 characters, a single line, non-blank.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, gate is 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
