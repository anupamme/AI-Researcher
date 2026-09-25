#!/usr/bin/env python3
"""Round-21 budget arbiter. Run FROM the paper dir.

/tmp/measure.py's anchor is a whole sentence and breaks whenever a reflow puts a
ruler number in the middle of it, so it reports "anchor not found" for a paper
that is merely one line longer. This uses a short anchor that cannot straddle a
line, and additionally prints, for each marker, the ruler drift against a
reference PDF -- which is how a float re-pack is told apart from a text change.

usage: pos.py [reference.pdf]
"""
import re
import subprocess
import sys

CEILING = 485          # last ruler on p9
LAST_PAGE = 9
END = "magnitude we measure only"   # last words of the main text (r26: the
                              # phrase now straddles a line break, so anchor the tail)

MARKERS = [
    "Three questions, kept apart", "Contribution: four claims",
    "Related work", "The design that would settle",
    "An instructed-lie benchmark changes two things", "Proposition (",
    "How the criteria divide", "What is proven, what is shown", "We evaluate seven LLMs",
    "The most discriminative question", "A hand-written regex",
    "The same confound inside a white-box", "The $2\\times2$ factorial",
    "Our rule is null where", "So we built one", "We establish:", END,
]


def positions(pdf):
    out = subprocess.run(["pdftotext", "-layout", pdf, "-"],
                         capture_output=True, text=True, check=True).stdout
    d, cur = {}, None
    for i, page in enumerate(out.split("\f"), 1):
        for line in page.split("\n"):
            m = re.match(r"^\s*(\d{1,4})(\s|$)", line)
            if m:
                cur = int(m.group(1))
            for k in MARKERS:
                if k in line and k not in d:
                    d[k] = (i, cur)
    return d


def main():
    now = positions("main.pdf")
    ref = positions(sys.argv[1]) if len(sys.argv) > 1 else {}
    if ref:
        print(f"{'marker':42} {'ref':11} {'now':11} drift")
        for k in MARKERS:
            x, y = ref.get(k), now.get(k)
            dr = (y[1] - x[1]) if (x and y and x[1] and y[1]) else None
            tail = f" {dr:+d}" if dr is not None else ""
            print(f"{k[:40]:42} {str(x):11} {str(y):11}{tail}")
    if END not in now:
        print(f"!! end anchor {END!r} not found")
        return 1
    page, ruler = now[END]
    slack = CEILING - ruler
    print(f"\n  main text ends on    : p{page}  (ruler {ruler})")
    print(f"  SLACK                : {slack}"
          f"   {'OK' if slack >= 0 and page <= LAST_PAGE else 'OVER BUDGET'}")
    return 0 if (slack >= 0 and page <= LAST_PAGE) else 1


if __name__ == "__main__":
    sys.exit(main())
