#!/usr/bin/env python3
"""Generate /tmp/r39_edits.json: the round-39 paragraph-level edit ledger.

Same coalescing opcode walk gen_r29..r38_edits.py used: a line-level difflib diff
with abutting opcodes and opcodes separated only by blank lines coalesced, and
non-unique blocks widened backwards over preceding unchanged lines until they are
unique. Both sides are UN-CONVERTED first, exactly as rounds 37 and 38 did it, so
the ledger is expressed in PRE-round-36 punctuation. That is what lets 13g replay
it forward after the R38 stage, at which point `rebuilt` is in exactly that
punctuation.

TWO CORRECTIONS TO THE ROUND-38 RECIPE, both forced by the same fact: ROUND 38 IS
NOT COMMITTED. HEAD is 8f18687, the round-37 re-pin, and the working tree carries
rounds 38 AND 39 together. gen_r38_edits.py could diff HEAD against the tree
because round 37 WAS committed at that point; doing the same here would produce a
ledger of rounds 38+39 combined, double-counting every round-38 pair.

  1. THE BASELINE IS THE ROUND-38 TREE, NOT HEAD. It is reconstructed rather than
     assumed: replay the round-38 ledger forward onto UNCONVERT(HEAD), asserting
     each pre-image occurs exactly once. `r38_tree(name)` is that reconstruction,
     and the round-39 diff is taken against it.

  2. THE THREE RETAINED LEDGERS ARE CHECKED AS A CHAIN, NOT INDEPENDENTLY. Round
     39 renames \\paragraph{Relation to prior work.}, and that heading opens the
     1,605-character post-image of round 38's sole introduction.tex pair. Checked
     independently against the live tree -- gen_r38_edits.py's rule -- the
     round-38 ledger reports that post-image 0 times and the generator refuses to
     write, which is what the first run of this script did.

     That refusal was a false alarm, and the reason is the strip order. The
     verifier composes UNDO37(UNDO38(UNDO39(UNCONVERT(live)))): UNDO39 runs FIRST
     and restores the heading before UNDO38 ever looks for it. So the property
     the verifier actually needs is that each UNDO stage inverts THE TEXT IT IS
     HANDED, which is a chain:

         UNDO39(UNCONVERT(live))  ==  UNCONVERT(round-38 tree)   [asserted byte-
                                                                  for-byte]
         UNDO38(that)             ==  UNCONVERT(HEAD)
         UNDO37(that)             ==  UNCONVERT(ea6faf9)

     Each link is asserted below with a per-pair occurrence count of exactly one,
     so a round-39 edit that DELETED a post-image (0) or REINTRODUCED one (2)
     still fails loudly -- it just no longer fails for a legal overlap with the
     immediately preceding round. The independence claim in gen_r38_edits.py held
     only because rounds 37 and 38 happened not to touch the same paragraph; it
     was never the property the harness relies on.

WHAT ROUND 39 CHANGES, and therefore which files this ledger may name:

  appendix.tex      EXP-BF, the benign false-positive rate of the parameter-free
                    rule -- a new subsection after app:regex_patterns, plus its
                    \\ref in bucket 3 of the appendix roadmap.
  experiments.tex   three main-text clarity edits the NeurIPS 2026 main-track
                    reviewers named: prompt equalization defined operationally at
                    first use in the body, the reimplementation's bank-width
                    concession lifted out of the appendix, and the ADAGE acronym
                    REMOVED from the main text (it is defined once, in
                    app:adage_details).
  introduction.tex  \\paragraph{Relation to prior work.} -> \\paragraph{Related
                    work.}, the heading two reviewers searched for and did not
                    find. Character-negative, so it is free against the 9-page
                    budget.

Emits lists [name, tag, old, new] so the verifier can json.load them into
tuples, exactly as r27..r38_edits.json do.
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

# The round-36 ledger, read exactly as verify_r38.py reads it.
R36_EDITS = [tuple(x) for x in json.load(io.open("/tmp/r36_edits.json",
                                                 encoding="utf-8"))]
R36_BY_FILE = {}
for _r, _o, _n in R36_EDITS:
    R36_BY_FILE.setdefault(_r.replace("sections/", "").replace(".tex", ""),
                           []).append((_o, _n))

# The round-37 and round-38 ledgers, both in the four-field [name, tag, old, new]
# shape and both expressed in pre-round-36 punctuation.
R37_EDITS = [tuple(x) for x in json.load(io.open("/tmp/r37_edits.json",
                                                 encoding="utf-8"))]
R37_BY_FILE = {}
for _n37, _t37, _o37, _x37 in R37_EDITS:
    R37_BY_FILE.setdefault(_n37, []).append((_o37, _x37))

R38_EDITS = [tuple(x) for x in json.load(io.open("/tmp/r38_edits.json",
                                                 encoding="utf-8"))]
R38_BY_FILE = {}
for _n38, _t38, _o38, _x38 in R38_EDITS:
    R38_BY_FILE.setdefault(_n38, []).append((_o38, _x38))


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


def invert(rnd, text, name, pairs):
    """Strip one round's pairs from `text`, asserting each post-image occurs once.

    This is what an UNDO stage in the verifier does, with the occurrence count
    made explicit. 0 means a later round DELETED the post-image; 2 means a later
    round reintroduced it and `str.replace` would rewrite both copies. Either
    silently retires the historical pins that read through the stage.
    """
    for old, new in pairs:
        c = text.count(new)
        if c != 1:
            raise SystemExit(
                f"R{rnd} INVERT FAIL sections/{name}.tex: post-image occurs {c}x "
                f"in the text the UNDO{rnd} stage is handed: {new[:70]!r}\n"
                f"  regenerate with gen_r{rnd}_edits.py rather than hand-editing "
                f"either file")
        text = text.replace(new, old)
    return text


def r38_tree(name):
    """UNCONVERT(the working tree as round 38 left it), rebuilt not assumed.

    Round 38 is NOT committed, so HEAD is the round-37 re-pin and the diff that
    isolates round 39 has to be taken against this. Replaying the round-38 ledger
    forward onto UNCONVERT(HEAD) is also a re-verification of that ledger: every
    pre-image must occur exactly once, in order.
    """
    s = UNCONVERT(head(name), name)
    for old, new in R38_BY_FILE.get(name, []):
        if s.count(old) != 1:
            raise SystemExit(
                f"R38 FORWARD FAIL sections/{name}.tex: pre-image occurs "
                f"{s.count(old)}x in UNCONVERT(HEAD): {old[:70]!r}")
        s = s.replace(old, new, 1)
    return s


def main():
    # ---- the round-36 ledger inverts the LIVE tree, because UNCONVERT is the
    # first thing every historical pin applies and nothing strips round 39 first.
    for rel in sorted({r for r, _, _ in R36_EDITS}):
        nm = os.path.basename(rel)[:-4]
        invert(36, io.open(os.path.join(REPO, PAPER, rel),
                           encoding="utf-8").read(), nm,
               [(o, n) for r, o, n in R36_EDITS if r == rel])
    print(f"round-36 ledger still inverts once per pair against the live tree "
          f"({len(R36_EDITS)} pairs)")

    ledger = []
    # The replay target: the concatenation the verifier rebuilds, so uniqueness
    # must be judged against the whole main-text blob, not one file. Un-converted,
    # because that is the punctuation `rebuilt` is in at this point in 13g, and
    # taken at the ROUND-38 tree, which is the state the R39 stage is handed.
    blob = "\n".join(r38_tree(n) for n in BOLDED)
    for name in FILES:
        A = r38_tree(name)
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

    # THE OVERLAP REPORT, no longer a fatal assertion. gen_r38_edits.py refused to
    # write when a new pre-image lay inside an earlier post-image, on the reasoning
    # that 13g's stages must be independent. They are not independent and never
    # were: they are SEQUENTIAL. The R38 stage runs before the R39 stage going
    # forward, and UNDO39 runs before UNDO38 coming back, so a round-39 edit inside
    # a round-38 post-image is legal by construction -- which is exactly what
    # round 39's paragraph rename is, since that heading opens round 38's only
    # introduction.tex pair. The property that actually has to hold is the chain
    # asserted below, and it is asserted per pair with a count of one. Overlaps are
    # PRINTED so the round leaves a record of where it landed.
    for _nm, tag, old, _new in ledger:
        for rnd, pairs in ((36, [(o, n) for _r, o, n in R36_EDITS]),
                           (37, [(o, n) for _n, _t, o, n in R37_EDITS]),
                           (38, [(o, n) for _n, _t, o, n in R38_EDITS])):
            for o, n in pairs:
                if old in n:
                    print(f"  overlap: {tag} lies inside a round-{rnd} "
                          f"post-image (legal: stages are sequential, and "
                          f"UNDO{rnd} runs after UNDO39)")

    # Round 39 is an appendix round PLUS two main-text files. appendix.tex carries
    # EXP-BF and its roadmap reference; experiments.tex carries the three clarity
    # edits; introduction.tex carries the paragraph rename. Both main-text files
    # are BOLDED, so they replay into `rebuilt` and the word ledger stays balanced,
    # and related_work.tex is NOT touched this round -- which is the difference
    # from round 38 and the reason verify_r39's UNDO39 call sites are not a copy
    # of verify_r38's UNDO38 call sites.
    touched = sorted({nm for nm, _t, _o, _n in ledger})
    if touched != ["appendix", "experiments", "introduction"]:
        raise SystemExit(
            f"round 39 changed {touched}, not appendix/experiments/introduction; "
            f"verify_r39's UNDO39 call sites cover exactly those three and must "
            f"be re-checked before this ledger is written")

    # Round-trip: applying the ledger to the ROUND-38 tree must reproduce
    # UNCONVERT(live) byte-for-byte, per file, or nothing is written.
    ok = True
    for name in FILES:
        s = r38_tree(name)
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

    # ---- THE CHAIN, which is the property verify_r39.py's historical pins rest
    # on. Strip newest first and land on UNCONVERT(HEAD), per file, byte-for-byte:
    #
    #   UNDO39(UNCONVERT(live))  ==  UNCONVERT(round-38 tree)
    #   UNDO38(that)             ==  UNCONVERT(HEAD)
    #
    # UNDO39 is the ledger just built, read backwards, because a later pair's
    # pre-image can sit inside an earlier pair's post-image within one round too.
    # The third link, UNDO37(UNCONVERT(HEAD)) == UNCONVERT(ea6faf9), is round 37's
    # own invariant and holds at HEAD whatever this round does; it is asserted here
    # anyway, as a count, because that is cheap and the alternative is discovering
    # it as a failing rounds-30..35 pin.
    for name in FILES:
        t = invert(39, UNCONVERT(cur(name), name), name,
                   list(reversed([(o, n) for nm, _t, o, n in ledger
                                  if nm == name])))
        if t != r38_tree(name):
            raise SystemExit(
                f"CHAIN FAIL sections/{name}.tex: UNDO39(UNCONVERT(live)) is not "
                f"the round-38 tree byte-for-byte; nothing written")
        t = invert(38, t, name, R38_BY_FILE.get(name, []))
        if t != UNCONVERT(head(name), name):
            raise SystemExit(
                f"CHAIN FAIL sections/{name}.tex: UNDO38(UNDO39(...)) is not "
                f"UNCONVERT(HEAD) byte-for-byte; nothing written")
        invert(37, t, name, R37_BY_FILE.get(name, []))
    print(f"chain OK: UNDO37(UNDO38(UNDO39(UNCONVERT(live)))) strips to "
          f"UNCONVERT(ea6faf9) on all {len(FILES)} files")

    for path in ("/tmp/r39_edits.json", DATA + "r39_edits.json"):
        json.dump(ledger, io.open(path, "w", encoding="utf-8"), indent=1)
    print(f"\nwrote /tmp/r39_edits.json and data/r39_edits.json "
          f"({len(ledger)} entries)")
    for name, tag, old, new in ledger:
        print(f"  {tag:<18} -{len(old):<6} +{len(new):<6} {old[:60]!r}")


if __name__ == "__main__":
    main()
