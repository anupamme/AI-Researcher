# Response to the round-31 review

*Not part of the paper.*

**Summary: this review is of the draft as it stood *before* the previous revision, so part of it is
already answered, and the part that is not contains the single most useful finding we have had in
several rounds.** You asked us to give the composition result more visual prominence because it is
"buried under a huge amount of auditing machinery." **The depth ladder that *is* that result already
existed (as a table in the appendix), while the body printed only its endpoint.** It is now the
upper panel of Figure 2 in the body. You also asked for an external composition benchmark on the
grounds that this one is ours; **`poly8`'s expressions and equivalence classes are Allamanis et
al.'s released corpus, used unmodified and hash-pinned, and the paper never said so.** It does now.

No new experiments, datasets or statistical machinery. The assertion count is **unchanged at 2143**,
correctly: every value in the new figure was already asserted against run `r93`.

---

## 0. Which draft this review is of, and why it matters

The reviewed file is `iclr2027_conference(20260907-105203).pdf`. It is **the draft as it stood before
the previous revision**, which we can show three ways:

- You quote §3.4 as "the propositions *fall out of Definition 1 in a few lines*". That file reads
  **"The propositions here…"**; the current file reads **"The numbered results here, Theorem 1
  included…"**.
- Your §17A asks us to add prose next to Table 1 saying what admissibility auditing does that prior
  devices do not. **That sentence is already in the current file**, as the closing paragraph of §2.
- Your §11 list of overloading terms omits `identification` and `discrimination`: two terms the
  previous revision added to the glossary precisely because they were used in §4 and defined nowhere.

So this is a **second, independent opinion on the same draft**, not a score that moved. We mention it
only because three of your asks were already closed and we did not want to appear to ignore them:

| Your ask | Status before this round |
|---|---|
| §17A prose on what the framework makes answerable | already in §2; **sharpened** further this round |
| §5, §16.1 Theorem 1 is near-definitional and should not be sold | already done: the abstract and §1 carry a bare citation, and §3.4 says a reader who finds the theorem close to a restatement of what an admissible family means **is not disagreeing with us** |
| §11 cognitive load from undefined terms | `identification` and `discrimination` added to the glossary |

**One of your asks is factually mistaken about the paper, and we are not going to act on it.** §18
asks us to elevate the family stress test "rather than leaving it in the appendix." **It is in the
body**; §4.2, *"Family stress test: does a wider family change any verdict?"*, and the phrase *five
descriptors we did not choose* appears in the **abstract, §1 and §4.2**. Three body sites, and it
still read as appendix material. We have taken that as evidence about **framing**, not placement, and
added the framing you actually wanted: the family is ours to declare, **which is the researcher
degree of freedom to worry about**, so it was widened by descriptors we did not choose and no verdict
moved.

---

## 1. The change that matters: the ladder was in the appendix

You wrote that the paper's most interesting positive finding is buried, and asked for prominence for
*singles → depth 2 → depth 4 → depth 8 → unseen arrangement → unseen primitive*.

**That sequence existed as a table in Appendix AU and had never been in the body.** The body reported
one number from it: `0.736` at `d=8`. The full singles-only row is

```
d=1   d=2   d=3   d=4   d=5   d=6   d=7   d=8
.997  .983  .953  .905  .888  .841  .783  .736
```

**Figure 2 now has two panels.** The upper one plots that decay against the same encoder with depth-8
composites in its library (`.995 → .936`) and against `sup F₃`, the best admissible control, which
falls to chance. The lower panel is the three novelty-cost bars unchanged. The point the figure now
makes in one image (that identification decays *gracefully* rather than collapsing, while the entire
admissible family sits at the floor) was previously three paragraphs and an appendix table.

**This is the eleventh time in this review history that a reviewer's ask was answered by material the
paper already contained**, and the costliest, because it was the best positive result in the paper.

**It is also the second independent reader to make this complaint.** The previous reviewer called it
"Paper A dominates Paper B" and we answered with a measurement and no edit. Two independent readers
converging retired that answer.

---

## 2. `poly8` is not our benchmark

Your §17C is the ask we weighed hardest, because **the previous reviewer forbade exactly what you
recommend**, twice: *"Importantly, I would not add another 10 experiments. The paper is already
empirically overloaded"* and *"add no datasets."* We are disclosing that conflict rather than
silently picking a side.

We resolved it with a fact that was already true and never stated. **`poly8` is loaded from
Allamanis et al.'s released archive** (`semvec-data.zip`, fetched by `fetch_data.sh`, SHA-256 pinned,
not redistributed, used unmodified). **The expressions and the equivalence classes are theirs.** What
is ours is the composition protocol layered on top, which chains to build and which to hold out.
§4.2 now says exactly that, and draws the line exactly there rather than claiming more.

That does not fully answer you, and we say so **in the paper**: *"An independently designed
composition benchmark would test this further; we do not run one, and the claim is scoped
accordingly."* We would rather scope the claim in print than run a benchmark the other reviewer
explicitly ruled out.

---

## 3. The entitlement ladder (§12)

You asked for the hierarchy "immediately after the abstract", ending with the row that says
compositional reasoning is unreachable. The §1 box (which is already in that position) now contains
it as a table rather than a run of prose questions:

| clear | and the score is |
|---|---|
| **S1** variable identity | not explained by *which variables appear* |
| **S2** operator/arity inventory | … nor by *which operators appear* |
| **S3** bounded local structure | … nor by *order-blind local statistics* |
| and **gate C** coverage | generalization *outside the training rewrite library* |
| **no level, at any width** | *compositional reasoning*: unreachable by this method |

It is a `tabular` inside the existing box rather than a float, because a float cannot be pinned to a
page and you asked for this specific position.

---

## 4. Title and related work

- **Title** is now *"Beyond the Strongest Baseline: Admissibility Auditing for Structural Claims in
  Neuro-Symbolic Benchmarks"*: your preferred form, so the method is discoverable.
- **§14.** Added Lippl & Stachenfeld (ICLR 2025), which derives shortcut bias and memorization leak
  from training-data structure, with the distinction stated in your words: **the question that
  becomes answerable is not whether a model exploits a shortcut, but whether the experiment could
  have told.** That line of work asks what models do; this paper asks what a comparison is *capable*
  of establishing.

---

## 5. What we did not do

- **No new experiments, datasets or corpora**, per the previous reviewer's explicit instruction.
- **We did not move the family stress test**, because it is already in the body (§0 above).
- **We did not restructure §4.** Every addition was funded by compressing passages the abstract,
  Table 2 or the new figure already carry, never by dropping a claim.

---

## 6. Verification

- **0 errors, 0 undefined references or citations, 0 `Float too large`, exactly 2 overfull boxes**:
  the same pre-existing `6.4211pt` vbox and `3.509pt` hbox. 83 pages. `bibtex` clean with the one new
  entry.
- **Abstract still ends page 1**, **body still ends page 9**, **page 10 still opens `ETHICS
  STATEMENT`**, and Figure 2 sits on page 8.
- **Every region netted ≤ 0, proved by placement rather than arithmetic: all thirteen section
  headings land on exactly the same page as before this round.** Zero float repacking.
- **The figure's data was verified by decoding it back out of the plot.** The 24 plotted coordinates
  were inverted through the axis transform and compared against Appendix AU's table: all 24 match
  exactly, and the endpoints appear in `r93_deep_composition.json`. A mistyped coordinate would have
  been invisible to every text-based gate.
- **`verify_claims.py`: 2143/2143, exit 0, in all three code copies**, unchanged, the ladder values
  were already asserted (`verify_claims.py:5554`), which is why the count correctly did not move.
- `check_tex_numbers.py` over every rewritten paragraph; the two residuals were the known
  `{,}`-separator false positive (`37{,}758`) and a block-boundary artifact, both traced to their
  logs.
- **Figure 2 inspected as a rendered image**, and pages 1, 2, 3, 8 and 9 read as rendered text.
