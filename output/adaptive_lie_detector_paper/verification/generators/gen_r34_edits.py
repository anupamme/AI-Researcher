#!/usr/bin/env python3
"""Generate /tmp/r34_edits.json: the round-34 paragraph-level edit ledger.

Same opcode walk /tmp/gen_r29_edits.py used: a line-level difflib diff of the
round-33 commit (HEAD) against the working tree, with abutting opcodes and
opcodes separated only by blank lines coalesced, and non-unique blocks widened
backwards over preceding unchanged lines until they are unique.

Emits lists [name, tag, old, new] so the verifier can json.load them into
tuples, exactly as r27/r28/r29/r30_edits.json do.
"""
import difflib
import io
import json
import subprocess

PAPER = "output/adaptive_lie_detector_paper/"
SEC = "/Users/mediratta/code/paper_writing/AI-Researcher-align/" + PAPER + "sections/"
REPO = "/Users/mediratta/code/paper_writing/AI-Researcher-align"
BOLDED = ["abstract", "introduction", "methodology", "experiments", "discussion",
          "conclusion"]
FILES = BOLDED + ["appendix", "related_work"]


def head(name):
    r = subprocess.run(["git", "show", f"HEAD:{PAPER}sections/{name}.tex"],
                       cwd=REPO, capture_output=True, text=True)
    r.check_returncode()
    return r.stdout


def cur(name):
    return io.open(SEC + name + ".tex", encoding="utf-8").read()


def coalesce(ops, a):
    """Merge opcodes that abut or are separated only by blank lines."""
    out = []
    for op in ops:
        tag, i1, i2, j1, j2 = op
        if tag == "equal":
            continue
        if out:
            ptag, pi1, pi2, pj1, pj2 = out[-1]
            gap = a[pi2:i1]
            if i1 - pi2 == 0 or all(not ln.strip() for ln in gap):
                out[-1] = ("replace", pi1, i2, pj1, j2)
                continue
        out.append(("replace", i1, i2, j1, j2))
    return out


def main():
    ledger = []
    # The replay target: the concatenation the verifier rebuilds, so uniqueness
    # must be judged against the whole main-text blob, not one file.
    blob = "\n".join(head(n) for n in BOLDED)
    for name in FILES:
        a = head(name).split("\n")
        b = cur(name).split("\n")
        ops = coalesce(difflib.SequenceMatcher(None, a, b).get_opcodes(), a)
        for k, (_, i1, i2, j1, j2) in enumerate(ops, 1):
            lo = i1
            old = "\n".join(a[lo:i2])
            new = "\n".join(b[j1:j2])
            scope = blob if name in BOLDED else head(name)
            # widen backwards until the pre-image is unique and non-empty
            while (not old.strip() or scope.count(old) != 1) and lo > 0:
                lo -= 1
                old = "\n".join(a[lo:i2])
                new = "\n".join(a[lo:i1] + b[j1:j2])
            if scope.count(old) != 1:
                raise SystemExit(f"{name} block {k}: pre-image not unique "
                                 f"({scope.count(old)}x): {old[:90]!r}")
            ledger.append([name, f"{name}-{k}", old, new])
    json.dump(ledger, io.open("/tmp/r34_edits.json", "w", encoding="utf-8"),
              indent=1)
    print(f"{len(ledger)} entries")
    for name, tag, old, new in ledger:
        print(f"  {tag:<18} -{len(old):<6} +{len(new):<6} {old[:60]!r}")


if __name__ == "__main__":
    main()
