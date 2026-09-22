# Verification harness

`verify_r37.py` asserts **2,765** properties of this paper: every load-bearing number, every
claim-to-experiment mapping, every pinned sentence, the page budget, the float pagination, the
bibliography, and the punctuation. It is the artifact the response letters' "Verification" tables refer to.

```
python3 verification/run.py          # the current harness (round 37)
python3 verification/run.py r36      # the previous round, for comparison
```

`run.py` exits non-zero on the first failure and prints which check failed and why.

## The one rule

**Retain all checks.** A retained check that fails is a regression. The only exception is a check the
current round *deliberately* changes: those are **updated in place, with the round's reason recorded in a
comment, never deleted**. Several have been *strengthened* this way — round 36 replaced "no float pin
moved" with "exactly these four labels moved, by exactly these deltas", and round 37 replaced round 36's
"the code repo has no uncommitted tracked changes" with an explicit seven-path allow-set, which fails on a
stray file the old form accepted.

## Why the verifier is generated, not written

Each round's verifier is produced from the previous round's by `generators/mk_verify_rNN.py`, which
performs string substitutions and **asserts that each `old` string occurs exactly once** before rewriting
it. That assertion is the point: it makes it impossible to "update" a pinned literal by pattern-matching
something adjacent to it. A near-miss substitution is how a real defect (a 3/5 figure written where 2/5
belonged) once got in, and this is the mechanism that stops it recurring.

The consequence is that `verify_r37.py` **must not be hand-edited** — including to change its file paths.
It loads its ledgers from `/tmp` exactly as it did when it was generated, and `run.py` seeds `/tmp` from
`data/` and `snapshots/` before running it from the paper directory (the verifier opens `sections/*.tex`
relatively).

## Layout

| Path | What it is |
|---|---|
| `verify_r37.py` | the current harness, 2,765 checks. Generated; do not edit |
| `verify_r36.py` | its immediate predecessor, 2,464 checks. Kept so round 37's generation step is auditable end to end |
| `verify_r35.py` | round 35's, 2,230 checks |
| `generators/mk_verify_r33..37.py` | the generators. **These are the audit trail** — each substitution carries a comment saying which round changed what, and why |
| `generators/gen_r3*_edits.py` | build each round's `(old, new)` prose-edit ledger and assert it round-trips a snapshot to the live tree |
| `generators/emdash_edits.py`, `gen_appendix_props.py`, `appendix_ops.py` | round 36's punctuation pass: the main-text ledger, the appendix proposal generator, and the reviewed per-site verdicts |
| `generators/measure36.py`, `show_props.py` | measurement and inspection helpers used while reviewing that pass |
| `data/r2*_edits.json`, `data/r3*_edits.json` | the per-round edit ledgers the verifier replays |
| `data/r37_label_moves.json` | round 37's float-pin price: the 103 appendix labels that repaginated, each with its exact page delta |
| `data/r23_base/`, `data/pos28.py` | the round-23 baseline tree and the offset helper the replay needs |
| `data/appendix_props.json`, `data/r36_appendix_ops.json` | the 329 appendix punctuation proposals and the ops actually applied |
| `data/r36_verify_literal_updates.json` | which pinned literals round 36 re-derived by span alignment, and from what |
| `snapshots/PRE/` | the nine `.tex` files as they stood **before** round 36's punctuation pass |
| `snapshots/*.BASE.tex` | the two offset-applied files' inputs, so `appendix_ops.py` is re-runnable from a clean base |

Rounds 23–34's intermediate verifiers are not preserved here; each is a strict subset of its successor's
checks, so `verify_r37.py` contains all of them, and `generators/` records how each round got there.

## The `UNDO37` mechanism (round 37)

Round 37 rewrote ten paragraphs across `methodology.tex`, `appendix.tex` and `related_work.tex`, several of
them inside literals that rounds 30–35 pin byte-exactly. `UNDO37` is the same device as `UNCONVERT`, one
layer out: those checks now assert against `UNDO37(UNCONVERT(live, f), f)`, which by ledger round-trip is
exactly `UNCONVERT(ea6faf9:f, f)` — so each historical assertion still holds at the byte string it was
written for, rather than being loosened.

The round-37 ledger (`data/r37_edits.json`) is generated from `UNCONVERT(parent)` against `UNCONVERT(tree)`,
i.e. in **pre-round-36 punctuation**. Two consequences, and both are why it was built that way: check 13g
can replay it **forward** as a stage after round 35's, and a round-37 pre-image lying inside a round-36
post-image is structurally impossible. Check 37b asserts the second one anyway.

## The `UNCONVERT` mechanism (round 36)

Round 36 replaced 560 em dashes with ordinary punctuation, which threatened every pinned literal in the
file. Rather than rewrite ~2,000 assertions, the verifier carries `UNCONVERT` and the round-36 ledger
(`data/r36_edits.json`, 538 widened pairs) as data: any check that pins pre-conversion prose asserts it
against the un-converted text. So every historical assertion is still the **byte-exact** string it was.

Its soundness is a checked property, not an assumption. Each ledger pair is widened with surrounding
context until it is **two-way unique** — `old` occurs exactly once in the pre-conversion text (so the
ledger applies) *and* `new` occurs exactly once in the live text (so it inverts).
`generators/gen_r36_edits.py` asserts both directions round-trip byte-exactly, and check 36d re-asserts
apply-once / invert-once against the live tree alone, so it holds even with this directory as the only
surviving copy.

This is also why check 13g un-converts instead of replaying a forward round-36 stage after round 35's: the
earlier ledgers are disjoint paragraph rewrites and compose in any order, whereas round 36's widened
context frequently overlaps text a later round-23..35 replacement also edits. `generators/mk_verify_r36.py`
records that reasoning at the substitution site.

## Environment

- `python3` needs no third-party packages. `pdftotext` and `pdftoppm` (poppler) are required for the
  rendered-page and page-budget checks.
- Run against a **fresh build**: `touch main.tex && latexmk -pdf -g -interaction=nonstopmode main.tex`.
  Several checks read `main.aux`, `main.log`, `main.blg` and `main.pdf`, so a stale build reports stale
  results.
- `verify_bib.py` in the paper directory is separate and complementary: it re-resolves every
  `references.bib` entry against DOI/arXiv/publisher records.
