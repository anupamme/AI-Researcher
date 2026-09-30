# Response to the round-44 review

**No new experiments, per your instruction: `verify_claims.py` reads `2353/2353` in all three copies, exactly
as it did on the draft you read, which is the mechanical proof that no run was added. We adopted your boxed
principle and had to reverse its connective. And taking your "14–15 pages" complaint literally led to a
mechanical routing bug: two full-page figures, one of them cited nowhere in 93 pages, were rendering *behind
the bibliography*. Body still ends on page 9. 93 pages, unchanged.**

You wrote that *"the biggest uncertainty is novelty, not correctness"*, that you *"would submit this version"*,
and (twice) that you *"would not add more experiments indiscriminately"*. So this round is positioning,
compression and routing only. Nothing below is a new run; every number here was already in the paper or already
in a log the verifier reads.

---

## 1. Your boxed principle: adopted, with the arrow reversed

You asked three separate times for the criterion as a display: §21 (*"that distinction should be the central
equation of the paper"*), §23 (*"elevate it visually — perhaps a boxed principle"*), §31.1 (*"a short boxed
statement"*). **We measured before writing it: the six body files contained zero display equations in nine
pages.** No `equation`, no `align`, no `\[`, no `$$`. The object you call the paper's centre existed only as
inline prose. You were right, and it was worse than you could see from the PDF.

It now ships as the body's first and only display, in §1 ¶1, immediately under the thesis sentence you called
memorable:

> **The criterion, in one sentence: a learned representation *h* is evidence for a property *P* only if it
> outperforms the *best* representation that is invariant to *P* — the family ℱ — under the same protocol
> and score *M*.**
>
> ┌──────────────────────────────────────────────────────────────────────┐
> │  evidence about *P* **requires** *M(h) >* sup_{g∈ℱ} *M(g)* — not merely *M(h) > M(g)*.  │
> └──────────────────────────────────────────────────────────────────────┘

**Two deliberate departures from the box as you wrote it, and the first is the most important thing in this
response.** You proposed

> Evidence for *P* ⟺ *M(h) > sup_{g∈F_P} M(g)*

A **biconditional asserts that clearing the ceiling is evidence *for* P.** That is precisely the certification
this paper spends nine pages refusing: it contradicts Corollary `prop:falsification`, Figure 1's terminus
(*"yes ⇒ evidence against the alternatives the family declared, and nothing more"*), and a literal that is
pinned at exactly one occurrence in our own gate script because an earlier reviewer required it (*"no
admissible family can turn it into a certificate"*). Theorem 1(ii)–(iii) gives the shape the paper can defend:
the inequality is **necessary, never sufficient**. So the box reads `requires`, the sentence above it reads
`only if`, and a comment in `introduction.tex` records why, so a later round cannot "improve" it back to `⟺`.

We think the flip is a point in the paper's favour rather than a concession: your formalism was *stronger* than
our claim, and the criterion is worth stating precisely because the strong version is the one people reach for.

**Second departure, purely typographic:** `\sup\nolimits`. In display style `\sup_{g∈ℱ}` sets its subscript
*below* the operator, which makes the box two lines tall and repacks pages 1→2→3 into the paper's bistable §4.3
page boundary. No text gate in this repo can see that. We read the rendered page as an image and confirm: one
line, subscript beside the operator, frame inside the text block.

**Third departure, found by re-reading the box cold.** Promoting a display to page 2 means it can no longer
borrow notation from page 6. `M` and `h` are first *defined* in Theorem 1, four pages later, so the sentence
above the box now binds both (*"a learned representation $h$ …under the same protocol and score $M$"*), while
`ℱ` was already bound there and `g` is bound by the `sup`'s own quantifier. Fourteen rendered characters; the
per-page slack profile is unchanged.

**Honest note on placement.** You suggested page 1, and we chose page 1, but page 1 is entirely title and
abstract: §1 begins in its last three lines. The box therefore renders at the **top of page 2, the first page
of body text**, directly under the thesis sentence. That is the earliest position it can occupy without cutting
abstract content.

---

## 2. "About 14–15 pages before the enormous appendix"; you were reading a routing bug

This was not a misreading of the page limit; it is what the PDF looked like, and the cause was mechanical.

`iclr2027_conference.tex` `\input`-ed `figure_overview.tex` (Figure 3) and `figure_procedure.tex` (Figure 4)
**before** `\section*{Appendix}`. The `placeins` package with `[section]` raises a `\FloatBarrier` at that
heading, so both floats were flushed *ahead* of it, and behind the references. Measured, before and after:

| | before | after |
|---|---|---|
| body | pp. 1–9 | pp. 1–9 |
| statements | pp. 10–11 | pp. 10–11 |
| references | pp. 11–12 | pp. 11–13 |
| **Figure 3** | **p. 13** | p. 15 |
| **Figure 4** | **p. 14** | p. 16 |
| **APPENDIX heading** | **p. 15** | **p. 14** |

So the front of the document read as 9 + 2 + 2 + two full-page figures = **14 pages before anything announced
itself as an appendix**. Now nothing stands between the bibliography and the APPENDIX heading. **Cost: zero
body lines.** Total page count is unchanged at 93, figure numbers are unchanged (they follow `\input` order,
which we preserved), and every `\ref` still resolves: checked against the `.aux`.

There is a second consequence you flagged without knowing it. **Figure 4 is the seven-stage procedure that
round 43 promoted into the conclusion as the paper's "what to do on Monday" object**, and it was rendering
five pages past the end of the body, behind the bibliography. It is now the first thing after Appendix A's
front matter.

---

## 3. Figure 3 was cited nowhere in 93 pages, and reading it then found a defect no gate could

`fig:overview` (Figure 3) appeared exactly once in the entire source tree: **its own `\label`.** A full-page,
three-panel figure that no sentence in the paper sent a reader to. It is now cited from the appendix subsection
that owns its panels, as *"three views of the same leakage"*, beside `tab:diversity_sweep`.

Citing it meant reading it against the text for the first time, which surfaced a real defect:

- **Panels B and C both label their vertical axis `accuracy`, and they ran in opposite directions.** Panel C
  put 0 at the top with the bars hanging downward. Every tick was labelled consistently *with its own panel*,
  so no numeric, caption or provenance check could see it, but the reading the caption states (*"in
  distribution, bag and untrained encoder track each other; under out-of-library shift they diverge 7×"*) was
  visually inverted for anyone comparing the two panels.
- **Panel A plotted the leakage index ℓ′ downward**, which rendered a *rising* ℓ′ against tree-edit distance as
  a *falling* curve: the visual opposite of the caption's claim.
- Three label collisions (`accuracy` overprinting the first x-tick label in B and C; the legend overprinting
  the group labels in C; the two annotation columns overprinting each other in A).

All three panels now read upward, all collisions are gone, and **no data value changed**: the fix is
coordinate arithmetic plus label placement. The figure lives in the appendix, so this cost nothing in body
pagination: the per-page slack profile is byte-identical to the draft you read.

We are reporting this rather than quietly fixing it because it is the honest version of your Weakness #16: an
uncited float is invisible to every automated check we have, and *that* is what let a mislabelled axis survive
44 rounds.

---

## 4. The novelty argument (your §20, §31.2, and Weakness #13)

Your §20 is written as the rejection paragraph we most need to answer: *"largely a principled synthesis of
existing ideas."* Two changes, both routing and wording, no new claims.

**§2's "What is new, given all of that" paragraph now names the statistic.** It reads: *"Prior devices test one
comparator or one perturbation in isolation; **none estimates sup_{g∈ℱ} M(g), the ceiling of a declared
family**, which is the statistic a learned score is read against here, and §3.3 sets out the rest device by
device (Table 1)."* Your §31.1 contrast (*"existing work typically provides a comparator; we ask whether that
comparator is admissible evidence and whether it approximates the ceiling of the admissible family"*) is the
paper's own §1 ¶2 sentence, already bolded on page 2: *"A baseline comparison estimates relative performance;
this estimates the best score the declared alternatives can reach — a different inferential object, and no
published evaluation reports it."* We did not paste your sentence (ninth consecutive round we have declined
to), because a reviewer's phrasing in the paper's voice is how the next reviewer's objection gets manufactured.

**§3.3 is now reachable by name from page 3.** Your §13 reconstructs its seven ingredients, so you found it,
but its own source comment records that **round 40's reviewer asked for exactly that table and missed it**,
crediting Table 1 instead. It is an uncaptioned tabular with no float number and no list-of-tables entry, and
the reason is page mechanics, not preference: see the decline in §7 below.

---

## 5. Family incompleteness as the deliverable (your Weakness #14, §31.3)

§3.3 already conceded *"the family is incomplete by construction: the audit falsifies within ℱ₃, never outside
it — the standing limitation of the method."* Your §31.3 is right that this is also the product. The caveat
stands verbatim, and the positive form now stands beside it in the same breath:

> **That limitation is also the deliverable**: what the audit reports is *which* alternative explanations are
> ruled out, and Table 2 is that list.

This is round 43's instrument (voice conversion, zero caveats removed) applied to the one caveat that is the
paper's philosophy. **Nothing was thinned:** all three certification literals are still pinned at exactly one
occurrence each by `check_protected_claims.py`, which passes.

One caveat *was* removed this round, and only one: a trailing clause in §1 ¶4 that restated the
falsification-not-certification stance a seventh time. The stance is stated six further times in the body and
all three of its pinned forms are elsewhere. It funded §2's supremum sentence one page later. The census went
7 → 6; nothing became less hedged.

---

## 6. A drift we found while answering you, and the two gates that now prevent it

While adding the audit ledger to §1's critical path we found that **§1 said "four objects are the critical
path" and listed four, while the appendix front matter said "five objects carry the argument" and listed
five**: round 43 promoted the ledger in the appendix only. Two counted lists of the same objects, in two
files, differing by one, both individually well-formed, invisible to every literal check.

Both now say five and name the same five. And because "we fixed it in one representation and left it standing
in the other" is this project's most-repeated failure mode, two new checks ship in
`check_protected_claims.py`, beside round 43's `check_ledger_distribution()`:

- **`check_critical_path()`** parses the appendix's `\item[…]` list and §1's parenthetical, and asserts the
  count words *and the sets of `\ref` targets* match. It prints `ok 5 CRITICAL PATH: §1 and the appendix name
  the same five objects`.
- **`check_float_routing()`** asserts that Figures 3 and 4 are each `\ref`'d somewhere, that no figure is
  `\input` between `\appendix` and the appendix file (the placeins trap above), and that the set of uncited
  floats **equals** a pinned list of eight appendix tables that *are* the sections reporting them. A new
  uncited float is now a hard failure rather than something nobody notices for 44 rounds.

`--control` mode now fires **5** deliberate failures (was 2); all five fire.

---

## 7. Already in the paper: answered by line number, not by edit

| your point | where it already is |
|---|---|
| §25: *move "one encoder + two protocols → different conclusions" closer to the beginning* | `abstract.tex:6`, **page 1**: *"one set of GIN weights clears the unseen-class criterion at .881 and sits at chance, .511, on that twin."* It is also §1 item (ii) and §4's own subsection. It is already as early as the document has text. |
| Weakness #18: *the 0.994 twin measures structural sensitivity, not semantics* | `experiments.tex:27`, in the paper's words: *"Twin members are **not** algebraically equivalent, so a high score measures composition-sensitive structural discrimination, not algebraic-equivalence generalization."* A frozen reviewer-map quote; also in the abstract. |
| Weakness #17 (*the theory is formal clarification, novelty ~6.5* | Pre-conceded at `methodology.tex:102`: the numbered results are *"billed as **scoping**, not as theoretical contributions — they fall out of the definition below"*) a literal pinned at exactly 1; with what is *not* definitional named in the same sentence (closure putting a trained readout inside the family; the ceiling measured non-monotone). |
| Weakness #13: *the seven ingredients* | Table 1 (the device-by-device scorecard, page 4) plus §3.3, both on §1 ¶2's critical path, and §2 now names §3.3 explicitly. |
| §24 (*prefer "generalization to unseen compositions of transformations observed individually during training"* | The gloss already **precedes** the compact term at both first uses) abstract ¶4 and §4.2. The compact term itself is a pinned literal and a frozen reviewer-map quote, so it cannot be replaced without breaking the 17-row claim↔run↔script map; it is glossed, not unexplained. |

---

## 8. Declines, each with its reason

- **§31.4, "compress the appendix bookkeeping."** Declined. Round 43 promoted the audit ledger *out* of the
  bookkeeping band at the previous reviewer's insistence, on exactly the axis you score 7; that reviewer's
  complaint was that the paper filed its own significance evidence under *Reproducibility* and then told the
  reader to skip that band. Compressing it now would re-create the defect one round after fixing it. The
  developmental chronology already ships separately as `REVISION_HISTORY.md`; what is in the paper is the
  corrections' outcomes and the checks that prevent them.
- **A caption and float number on §3.3's tabular.** Declined, for page mechanics rather than preference: ~3
  lines there land on the paper's bistable §4.3 page boundary, which flips ~14 lines of downstream content.
  Answered by routing instead (§4 above).
- **Weakness #15, `poly8` is small and specialized with easy positives.** The disclosure this rests on is ours
  (`methodology.tex`), and it bounds our own positives in the same sentence. Answering it properly needs a
  larger benchmark: a new run, which your §31 explicitly rules out for this round. Noted as future work, not
  argued away.

---

## 9. What did *not* change, and how to check

- **`verify_claims.py`: `2353/2353`, exit 0, in all three copies** (`artifact/audit-sym`,
  `artifact/iclr-supplementary`, the workspace copy). `statements.tex` is untouched. The count did not rise,
  which is the mechanical proof that this round added no experiment.
- **Body ends page 9.** Every heading and every body float on its original page: Figure 1 p3, Table 1 p4,
  Table 2 p5, Figure 2 p8; the ethics statement is still the first body line of p10. Per-page slack is
  identical to the draft you read except p2, which improved from −0.695pt to 0.000.
- **Build:** 0 errors, 0 undefined references or citations, 0 `Float too large`, exactly the 2 pre-existing
  overfull boxes, 0 bibtex warnings, 93 pages.
- **All five gate scripts pass**, and every one that has a `--control` mode fires its deliberate failures:
  protected claims 21 claims / 4 absences / 3 document-wide (control 5 FAILs), reviewer map 17 rows / 285
  checks / 44 run tags / 54 appendix letters, figure provenance 10 values (control 2), caption rows 34 literals
  over 35 floats (control 1).

Four things we would most like you to check: that the box's connective is the one the paper can defend, that
the APPENDIX heading now precedes both figures, that §2 answers §20 well enough to move the novelty axis, and
that Figure 3's three panels now say what its caption says.
