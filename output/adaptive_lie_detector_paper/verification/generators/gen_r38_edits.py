#!/usr/bin/env python3
"""Generate /tmp/r38_edits.json: the round-38 paragraph-level edit ledger.

Same coalescing opcode walk gen_r29..r37_edits.py used: a line-level difflib diff
of the round-37 commit (HEAD) against the working tree, with abutting opcodes and
opcodes separated only by blank lines coalesced, and non-unique blocks widened
backwards over preceding unchanged lines until they are unique.

Both sides are UN-CONVERTED first, exactly as round 37 did it, so the ledger is
expressed in PRE-round-36 punctuation. That is what lets 13g replay it forward
after the R37 stage (at which point `rebuilt` is in pre-round-36 punctuation),
and it makes an `old` string that overlaps a round-36 post-image structurally
impossible. Asserted below anyway, because "structurally impossible" is what a
defect says about itself.

ROUND-38 ADDITION: the round-37 ledger is now load-bearing the same way the
round-36 one is. verify_r37.py routes eight historical pins through
UNDO37(UNCONVERT(live)), so a round-38 edit that DELETED a round-37 post-image
(count 0) or REINTRODUCED one (count 2) would break a retained check by making
UNDO37 misfire. Both the round-36 and the round-37 ledgers are therefore
invertibility-checked against the live tree before any round-38 pair is emitted.

Emits lists [name, tag, old, new] so the verifier can json.load them into
tuples, exactly as r27..r37_edits.json do.
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

# The round-36 and round-37 ledgers, read exactly as verify_r37.py reads them.
R36_EDITS = [tuple(x) for x in json.load(io.open("/tmp/r36_edits.json",
                                                 encoding="utf-8"))]
R36_BY_FILE = {}
for _r, _o, _n in R36_EDITS:
    R36_BY_FILE.setdefault(_r.replace("sections/", "").replace(".tex", ""),
                           []).append((_o, _n))

R37_EDITS = [tuple(x) for x in json.load(io.open("/tmp/r37_edits.json",
                                                 encoding="utf-8"))]
R37_BY_FILE = {}
for _n37, _t37, _o37, _x37 in R37_EDITS:
    R37_BY_FILE.setdefault(_n37, []).append((_o37, _x37))


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


def invertibility_against_the_live_tree(rnd, pairs_by_rel, on_unconverted):
    """A retained UNDO stage must still invert once per pair against the tree.

    verify_r37.py's 36d inverts the round-36 ledger against the live tree, and its
    rounds-30..35 pins invert the round-37 ledger against it. Either breaks if a
    round-38 edit removed a post-image or created a second copy of one, so both
    are asserted here rather than discovered as a failing retained check.

    `on_unconverted` is True for the round-37 ledger, which lives in pre-round-36
    punctuation and therefore inverts UNCONVERT(live), not live.
    """
    bad = []
    for rel, prs in sorted(pairs_by_rel.items()):
        path = rel if rel.endswith(".tex") else "sections/%s.tex" % rel
        name = os.path.basename(path)[:-4]
        t = io.open(os.path.join(REPO, PAPER, path), encoding="utf-8").read()
        if on_unconverted:
            t = UNCONVERT(t, name)
        for old, new in prs:
            c = t.count(new)
            if c != 1:
                bad.append((path, c, new[:70]))
                continue
            t = t.replace(new, old)
    for path, c, frag in bad:
        print(f"  R{rnd} INVERT FAIL {path}: post-image occurs {c}x: {frag!r}")
    if bad:
        raise SystemExit(
            f"round-38 edits broke the round-{rnd} ledger's invertibility; "
            f"regenerate with gen_r{rnd}_edits.py rather than hand-editing "
            f"either file")
    n = sum(len(v) for v in pairs_by_rel.values())
    print(f"round-{rnd} ledger still inverts once per pair against the live "
          f"tree ({n} pairs)")


def main():
    invertibility_against_the_live_tree(
        36, {r: [(o, n) for rr, o, n in R36_EDITS if rr == r]
             for r, _, _ in R36_EDITS}, on_unconverted=False)
    invertibility_against_the_live_tree(
        37, {k: list(v) for k, v in R37_BY_FILE.items()}, on_unconverted=True)

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

    # THE PLAN'S ASSERTION: no round-38 pre-image may occur inside any round-36
    # post-image. Extended to the round-37 ledger for the same reason -- a
    # round-38 `old` that lay inside a round-37 post-image would mean the two
    # stages of 13g's replay are not independent.
    clashes = [(tag, rnd, n[:60]) for _nm, tag, old, _new in ledger
               for rnd, pairs in ((36, [(o, n) for _r, o, n in R36_EDITS]),
                                  (37, [(o, n) for _n, _t, o, n in R37_EDITS]))
               for o, n in pairs if old in n]
    for tag, rnd, frag in clashes:
        print(f"  CLASH {tag} lies inside a round-{rnd} post-image: {frag!r}")
    if clashes:
        raise SystemExit("re-widen the earlier round's pairs with its own "
                         "generator; never hand-edit data/r3*_edits.json or the "
                         "verifier")

    # Round 38 began as an appendix-only round. The clibib re-audit (24 Sep 2026)
    # added the two ICLR venue promotions -- burns2022discovering -> 2023 and
    # goodfellow2014explaining -> 2015 -- and a citation key lives wherever it is
    # cited, so the round now also touches introduction.tex (a BOLDED file, so it
    # replays into `rebuilt` and the word ledger stays balanced) and
    # related_work.tex (not BOLDED, so verify_r38's r38_side must carry it).
    # UNDO38 is keyed by file name and inverts whatever the ledger names, so the
    # widening is in the CALL SITES, not the function: every place that un-does
    # round 38 on related_work.tex had been left un-wrapped on the old
    # appendix-only ground and is now wrapped.
    touched = sorted({nm for nm, _t, _o, _n in ledger})
    if touched != ["appendix", "introduction", "related_work"]:
        raise SystemExit(
            f"round 38 changed {touched}, not appendix/introduction/related_work; "
            f"verify_r38's UNDO38 call sites cover exactly those three and must "
            f"be re-checked before this ledger is written")

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

    for path in ("/tmp/r38_edits.json", DATA + "r38_edits.json"):
        json.dump(ledger, io.open(path, "w", encoding="utf-8"), indent=1)
    print(f"\nwrote /tmp/r38_edits.json and data/r38_edits.json "
          f"({len(ledger)} entries)")
    for name, tag, old, new in ledger:
        print(f"  {tag:<18} -{len(old):<6} +{len(new):<6} {old[:60]!r}")


if __name__ == "__main__":
    main()
