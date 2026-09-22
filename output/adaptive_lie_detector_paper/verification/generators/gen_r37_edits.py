#!/usr/bin/env python3
"""Generate /tmp/r37_edits.json: the round-37 paragraph-level edit ledger.

Same coalescing opcode walk gen_r29..r35_edits.py used: a line-level difflib diff
of the round-36 commit (HEAD) against the working tree, with abutting opcodes and
opcodes separated only by blank lines coalesced, and non-unique blocks widened
backwards over preceding unchanged lines until they are unique.

ROUND-37 DIFFERENCE, and the reason it exists: **both sides are UN-CONVERTED
first**. Check 13g replays the round-23..35 ledgers onto the round-23 baseline,
which is in PRE-round-36 punctuation, and compares the result against
`UNCONVERT(live)`. A round-37 stage appended to that replay must therefore be
expressed in pre-round-36 punctuation too, or its `old` strings would not occur
in `rebuilt`. Diffing `UNCONVERT(HEAD)` against `UNCONVERT(tree)` puts the whole
ledger on that side of the conversion, and as a side effect it makes an
`old` string that overlaps a round-36 `new` string structurally impossible. That
is the round-36 `UNCONVERT` hazard the round-37 plan named, and it is asserted
below anyway rather than argued.

Emits lists [name, tag, old, new] so the verifier can json.load them into
tuples, exactly as r27..r35_edits.json do.
"""
import difflib
import io
import json
import os
import subprocess

PAPER = "output/adaptive_lie_detector_paper/"
REPO = "/Users/mediratta/code/paper_writing/AI-Researcher-align"
SEC = REPO + "/" + PAPER + "sections/"
DATA = REPO + "/" + PAPER + "verification/data/"
BOLDED = ["abstract", "introduction", "methodology", "experiments", "discussion",
          "conclusion"]
FILES = BOLDED + ["appendix", "related_work"]

# The round-36 ledger, read exactly as verify_r36.py reads it.
R36_EDITS = [tuple(x) for x in json.load(io.open("/tmp/r36_edits.json",
                                                 encoding="utf-8"))]
R36_BY_FILE = {}
for _r, _o, _n in R36_EDITS:
    R36_BY_FILE.setdefault(_r.replace("sections/", "").replace(".tex", ""),
                           []).append((_o, _n))


def UNCONVERT(text, name):
    """verify_r36.py's function, byte-for-byte, so both agree on the mapping."""
    for _o, _n in R36_BY_FILE.get(name, []):
        text = text.replace(_n, _o)
    return text


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


def invertibility_of_r36_against_the_live_tree():
    """The hazard check, stated in the strongest available form.

    verify_r36.py's check 36d inverts the round-36 ledger against the live tree,
    so a round-37 edit that deleted a round-36 `new` string (count 0) or
    reintroduced one (count 2) would break a RETAINED check. Assert both here,
    before any round-37 pair is emitted.
    """
    bad = []
    for rel, prs in sorted(
            {r: [(o, n) for rr, o, n in R36_EDITS if rr == r]
             for r, _, _ in R36_EDITS}.items()):
        live = io.open(os.path.join(REPO, PAPER, rel), encoding="utf-8").read()
        t = live
        for old, new in prs:
            c = t.count(new)
            if c != 1:
                bad.append((rel, c, new[:70]))
                continue
            t = t.replace(new, old)
    for rel, c, frag in bad:
        print(f"  R36 INVERT FAIL {rel}: post-image occurs {c}x: {frag!r}")
    if bad:
        raise SystemExit("round-37 edits broke the round-36 ledger's "
                         "invertibility; regenerate with gen_r36_edits.py "
                         "rather than hand-editing either file")
    print(f"round-36 ledger still inverts once per pair against the live tree "
          f"({len(R36_EDITS)} pairs)")


def main():
    invertibility_of_r36_against_the_live_tree()

    ledger = []
    # The replay target: the concatenation the verifier rebuilds, so uniqueness
    # must be judged against the whole main-text blob, not one file. Un-converted,
    # because that is the punctuation `rebuilt` is in at this point in 13g.
    blob = "\n".join(UNCONVERT(head(n), n) for n in BOLDED)
    for name in FILES:
        A = UNCONVERT(head(name), name)
        B = UNCONVERT(cur(name), name)
        a, b = A.split("\n"), B.split("\n")
        ops = coalesce(difflib.SequenceMatcher(None, a, b).get_opcodes(), a)
        for k, (_, i1, i2, j1, j2) in enumerate(ops, 1):
            lo = i1
            old = "\n".join(a[lo:i2])
            new = "\n".join(b[j1:j2])
            scope = blob if name in BOLDED else A
            while (not old.strip() or scope.count(old) != 1) and lo > 0:
                lo -= 1
                old = "\n".join(a[lo:i2])
                new = "\n".join(a[lo:i1] + b[j1:j2])
            if scope.count(old) != 1:
                raise SystemExit(f"{name} block {k}: pre-image not unique "
                                 f"({scope.count(old)}x): {old[:90]!r}")
            ledger.append([name, f"{name}-{k}", old, new])

    # THE ROUND-37 PLAN'S ASSERTION: no round-37 pre-image may occur inside any
    # round-36 post-image. Structurally guaranteed by the UNCONVERT above; checked
    # because "structurally guaranteed" is what a defect says about itself.
    clashes = [(tag, n36[:60]) for _nm, tag, old, _new in ledger
               for _r36, _o36, n36 in R36_EDITS
               if old in n36]
    for tag, frag in clashes:
        print(f"  CLASH {tag} lies inside a round-36 post-image: {frag!r}")
    if clashes:
        raise SystemExit("re-widen the round-36 pairs with gen_r36_edits.py; "
                         "never hand-edit data/r36_edits.json or the verifier")

    # Round-trip: applying the ledger to UNCONVERT(HEAD) must reproduce
    # UNCONVERT(tree) byte-for-byte, per file, or nothing is written.
    ok = True
    for name in FILES:
        s = UNCONVERT(head(name), name)
        for nm, tag, old, new in ledger:
            if nm != name:
                continue
            if s.count(old) != 1:
                print(f"  ROUND-TRIP FAIL {tag}: pre-image occurs "
                      f"{s.count(old)}x")
                ok = False
                break
            s = s.replace(old, new, 1)
        same = s == UNCONVERT(cur(name), name)
        ok &= same
        n = sum(1 for nm, _t, _o, _n in ledger if nm == name)
        print(f"  {name:<14} {n:3d} pairs   {'OK' if same else 'DIFF'}")
    if not ok:
        raise SystemExit("round-trip failed; nothing written")

    for path in ("/tmp/r37_edits.json", DATA + "r37_edits.json"):
        json.dump(ledger, io.open(path, "w", encoding="utf-8"), indent=1)
    print(f"\nwrote /tmp/r37_edits.json and data/r37_edits.json "
          f"({len(ledger)} entries)")
    for name, tag, old, new in ledger:
        print(f"  {tag:<18} -{len(old):<6} +{len(new):<6} {old[:60]!r}")


if __name__ == "__main__":
    main()
