#!/usr/bin/env python3
"""Build the round-36 em-dash conversion ledger: /tmp/r36_edits.json.

Round 36 replaced every prose em dash (`---`) in the paper with ordinary
punctuation. It was applied two ways:

  * main text (main.tex + 6 sections)  -- an explicit (old, new) string ledger,
    /tmp/r36_emdash_edits.json, 87 entries
  * appendix.tex + related_work.tex    -- offset-based ops, /tmp/appendix_ops.py,
    445 dash sites, because string matching is not unique at that scale

This script unifies both into ONE (relpath, old, new) ledger in the same shape
as /tmp/r3{1..5}_edits.json, so verify_r36.py can map any string a retained
check pins through the conversion instead of the string being hand-edited.

For the two offset-applied files the pairs are recovered by aligning the
pre-conversion snapshot against the live file and widening each changed span
until `old` occurs EXACTLY once in the pre-conversion text.

Round-trip assertion: applying the emitted ledger to every PRE snapshot must
reproduce the live file byte-for-byte, or this script writes nothing.
"""
import difflib
import hashlib
import io
import json
import os
import sys

D = "/Users/mediratta/code/paper_writing/AI-Researcher-align/output/adaptive_lie_detector_paper"
PRE = "/tmp/r36_snapshots/PRE"
OFFSET_FILES = ["sections/appendix.tex", "sections/related_work.tex"]


def pre_path(rel):
    return os.path.join(PRE, rel.replace("sections/", ""))


def char_opcodes(a, b):
    """Character-level opcodes for two large texts, computed line-block-wise.

    A whole-file character SequenceMatcher is O(n^2) and does not finish on a
    380 kB appendix. Align on LINES first (cheap), then refine only the changed
    blocks at character level. Offsets returned are absolute character offsets.
    """
    al, bl = a.splitlines(keepends=True), b.splitlines(keepends=True)
    aoff, off = [], 0
    for ln in al:
        aoff.append(off)
        off += len(ln)
    aoff.append(off)
    boff, off = [], 0
    for ln in bl:
        boff.append(off)
        off += len(ln)
    boff.append(off)

    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, al, bl,
                                                       autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        sa, ea, sb, eb = aoff[i1], aoff[i2], boff[j1], boff[j2]
        sub_a, sub_b = a[sa:ea], b[sb:eb]
        # refine inside the changed block only (a few lines at a time)
        for t2, x1, x2, y1, y2 in difflib.SequenceMatcher(None, sub_a, sub_b,
                                                          autojunk=False).get_opcodes():
            if t2 != "equal":
                out.append((t2, sa + x1, sa + x2, sb + y1, sb + y2))
    return out


def pairs_by_alignment(rel):
    """Recover (old, new) string pairs for an offset-applied file."""
    a = io.open(pre_path(rel), encoding="utf-8").read()
    b = io.open(os.path.join(D, rel), encoding="utf-8").read()
    # Each changed region is (pre_lo, pre_hi, post_lo, post_hi, pad). Widening
    # for uniqueness can make one span's context swallow its neighbour's, so
    # widening and merging alternate until every span is BOTH unique in the
    # pre-conversion text and disjoint from its neighbours. Only then can the
    # pairs be applied with str.replace in any order without interfering.
    spans = [[i1, i2, j1, j2, 0] for tag, i1, i2, j1, j2 in char_opcodes(a, b)]
    for _ in range(200):
        for sp in spans:
            while True:
                lo, hi = max(0, sp[0] - sp[4]), min(len(a), sp[1] + sp[4])
                # the matching span in b, widened by the same amounts (this is the
                # arithmetic `wide` below uses to carry the padding across)
                plo, phi = sp[2] - (sp[0] - lo), sp[3] + (hi - sp[1])
                # BOTH directions must be unique. `old` unique in the pre-conversion
                # text makes the ledger applicable; `new` unique in the LIVE text
                # makes it INVERTIBLE, which is what verify_r36's UNCONVERT needs.
                # Measured: without the second condition one appendix pair
                # ("ablishes---and what" -> "ablishes, and what") inverts onto a
                # second site that already carried the comma before round 36.
                if (a.count(a[lo:hi]) == 1 and len(a[lo:hi].strip()) > 3
                        and b.count(b[plo:phi]) == 1
                        and len(b[plo:phi].strip()) > 3):
                    break
                sp[4] += 8
                if sp[4] > 6000:
                    raise SystemExit("cannot make span unique in %s at %d" % (rel, sp[0]))
        wide = [(max(0, lo - p), min(len(a), hi + p),
                 plo - (lo - max(0, lo - p)), phi + (min(len(a), hi + p) - hi))
                for lo, hi, plo, phi, p in spans]
        merged, overlapped = [], False
        for w in wide:
            if merged and w[0] <= merged[-1][1]:
                m = merged[-1]
                merged[-1] = (m[0], max(m[1], w[1]), m[2], max(m[3], w[3]))
                overlapped = True
            else:
                merged.append(w)
        spans = [[lo, hi, plo, phi, 0] for lo, hi, plo, phi in merged]
        if not overlapped:
            break
    return [(rel, a[lo:hi], b[plo:phi]) for lo, hi, plo, phi, _ in spans]


ledger = []
# 1. the main text, already an explicit ledger
main_led = json.load(io.open("/tmp/r36_emdash_edits.json", encoding="utf-8"))
ledger.extend(tuple(x) for x in main_led)
print("main-text entries carried over: %d" % len(main_led))

# 2. the two offset-applied files
for rel in OFFSET_FILES:
    p = pairs_by_alignment(rel)
    ledger.extend(p)
    print("  %-28s %4d aligned spans" % (rel, len(p)))

# 3. round-trip: the ledger must reproduce every live file from its PRE snapshot
by = {}
for rel, old, new in ledger:
    by.setdefault(rel, []).append((old, new))

ok = True
for rel, prs in sorted(by.items()):
    s = io.open(pre_path(rel), encoding="utf-8").read()
    for old, new in prs:
        if s.count(old) != 1:
            print("  ROUND-TRIP FAIL %s: %r occurs %dx" % (rel, old[:60], s.count(old)))
            ok = False
            break
        s = s.replace(old, new)
    live = io.open(os.path.join(D, rel), encoding="utf-8").read()
    same = s == live
    ok &= same
    # and BACKWARDS: verify_r36's UNCONVERT replays this ledger in reverse to assert
    # every pre-round-36 pin, so the ledger must invert as exactly as it applies.
    t = live
    for old, new in prs:
        if t.count(new) != 1:
            print("  INVERSE FAIL %s: %r occurs %dx in the live file"
                  % (rel, new[:60], t.count(new)))
            ok = False
            break
        t = t.replace(new, old)
    inv = t == io.open(pre_path(rel), encoding="utf-8").read()
    ok &= inv
    print("  %-28s fwd %-4s inv %-4s %4d pairs"
          % (rel, "OK" if same else "DIFF", "OK" if inv else "DIFF", len(prs)))

if not ok:
    sys.exit("round-trip failed; nothing written")

json.dump([list(x) for x in ledger],
          io.open("/tmp/r36_edits.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("\nwrote /tmp/r36_edits.json (%d entries, %d files)" % (len(ledger), len(by)))
