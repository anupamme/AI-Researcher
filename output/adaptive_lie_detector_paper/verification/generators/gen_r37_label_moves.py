#!/usr/bin/env python3
"""Generate /tmp/r37_label_moves.json: every \\newlabel that moved since c9718cf.

Check 35g pins all 223 `\\newlabel` entries of the document against their page at
c9718cf (round 34's commit) and lists the exceptions explicitly. Round 36 had four
exceptions and wrote them as a literal dict in the verifier. Round 37 adds ~17.3k
characters of appendix text (EXP-XP's subsection and Parts A/C/D's paragraphs), so
the tail of the appendix repaginates and the exception list is ~100 labels long --
too long to hand-write without becoming the near-miss substitution the read-back
rule exists to prevent. So it is DATA, generated here and loaded from /tmp by the
verifier, exactly as the round-23..37 edit ledgers are.

The file records, per moved label, its (float number, page) at c9718cf and now. It
is a record of the round's PRICE, not a licence: the verifier asserts the moved set
is exactly this one, that each move is exactly this delta, that no label with a
c9718cf page inside the 9-page main text appears in it at all, and that the delta
histogram matches -- so a main-text pin sliding, or a 104th label moving, still
fires.
"""
import io
import json
import re
import subprocess

REPO = "/Users/mediratta/code/paper_writing/AI-Researcher-align"
PAPER = REPO + "/output/adaptive_lie_detector_paper"
DATA = PAPER + "/verification/data/"
PIN = re.compile(r"newlabel\{([^}]*)\}\{\{([^}]*)\}\{(\d+)\}")
ADDED = {"app:pacchiardi_census", "tab:pacchiardi_census"}


def pins(aux):
    return {m.group(1): (m.group(2), m.group(3)) for m in PIN.finditer(aux)}


def main():
    was = subprocess.run(["git", "show", "c9718cf:output/adaptive_lie_detector_paper/"
                          "main.aux"], cwd=REPO, capture_output=True, text=True)
    was.check_returncode()
    a = pins(was.stdout)
    b = pins(io.open(PAPER + "/main.aux", encoding="utf-8").read())
    print("c9718cf: %d labels    now: %d labels" % (len(a), len(b)))

    added, removed = set(b) - set(a), set(a) - set(b)
    print("added: %s    removed: %s" % (sorted(added), sorted(removed)))
    if added != ADDED or removed:
        raise SystemExit("the label set changed by something other than EXP-XP's "
                         "two labels; re-read the round-37 plan before proceeding")

    moved = {k: [list(a[k]), list(b[k])] for k in sorted(set(a) & set(b))
             if a[k] != b[k]}
    unmoved = len(set(a) & set(b)) - len(moved)

    hist = {}
    for k, (x, y) in moved.items():
        hist[int(y[1]) - int(x[1])] = hist.get(int(y[1]) - int(x[1]), 0) + 1
    print("moved: %d    unmoved: %d    page-delta histogram: %s"
          % (len(moved), unmoved, dict(sorted(hist.items()))))

    # the property the round is costed on: nothing inside the 9-page main text moved
    inside = sorted(k for k in moved if int(moved[k][0][1]) <= 9)
    print("moved labels whose c9718cf page was in the main text: %s" % inside)
    if inside:
        raise SystemExit("a main-text page pin moved; round 37 is costed at zero "
                         "main-text rulers and this contradicts it")

    for path in ("/tmp/r37_label_moves.json", DATA + "r37_label_moves.json"):
        json.dump(moved, io.open(path, "w", encoding="utf-8"), indent=1,
                  sort_keys=True)
    print("\nwrote /tmp/r37_label_moves.json and data/r37_label_moves.json "
          "(%d entries)" % len(moved))


if __name__ == "__main__":
    main()
