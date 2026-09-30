# Response to the round-36 review

*Not part of the paper.*

**Summary: one experiment and one reframing, exactly as you asked, and the experiment found a defect
in our own instrument rather than a confirmation.** Your §17 was explicit (*"You need one experiment
and one reframing"*, *"rather than adding another 10–20 experiments"*), so we ran one: `r100`, a
**trained** $P$-invariant comparator. It showed that **every admissible ceiling in the reviewed paper
was measured with one fixed, unfitted nearest-centroid readout, while Definition 1's family is closed
under post-composition**, so the published ceilings were *lower bounds on the paper's own supremum*.
We now bound the supremum over **all** readouts at once, with nothing trained, and one of our own
appendix findings turns out to have been half an artifact of that readout. We report that.

Assertion count **2250 → 2304** (+54). One new run (`r100`), one new log, one new appendix (BA).
Body still **9 pages**; total 88 → 90 (the two extra pages are the new appendix, outside the limit).

---

## 1. Your binding question, answered as a consequence rather than an assertion

> *"Is 'admissibility auditing' genuinely a new methodological contribution, or is it a carefully
> formalized restatement of the obvious principle that a control must be invariant to the property
> under test? That is the question most likely to separate a 6 from an 8."*

The obvious principle says a control *should* be invariant. It does **not** say that you may admit an
arbitrarily strong **trained** model as a control, that you *must*, and that the statistic is that
family's ceiling rather than any member of it. That is a consequence with teeth, and it is the one
this round paid for:

**Admissibility is a property of the comparator's *input pipeline*, not of its strength.** If $g$ is
invariant to $P$, then $f \circ g$ is invariant to $P$ for **every** $f$: including a trained $f$,
since fitting changes $f$ and not what $g$ reads. So a learned readout over an order-blind feature map
is a family *member at any capacity*, the ceiling is a supremum over **readouts as well as feature
maps**, and "beat the strongest baseline" and "beat the ceiling" are different instructions.

Where it lives in the paper: one clause inside **Proposition 1** (not a new numbered result; three
consecutive reviewers have told us to demote, not re-sell, Theorem 1), the fifth row of §3.3's
*ingredient ⇒ what is measured* table, the eighth row of **Table 1** (`learned invariant control`, the
device your §6 names: ✓ on comparator invariance, **×** on family ceiling, because one learned control
is still one comparator), and claim (1) of §1.

**And it is the reason we had to re-measure.** Definition 1 declares $\mathcal{F}_t$ as *"a set of
representations each determined by the cues at levels $\leq t$ alone"*. Every $\mathcal{F}_3$ member we
had ever measured was a *bagger* scored by an unweighted nearest-centroid readout
(`benchmark_audit.py`), which is one member of the closure, not the closure. **Our own audit statistic
was under-measuring the family the paper had declared.** That is not a positioning problem, and we
would rather report it than have it found.

## 2. `r100`, the one experiment: prediction pre-registered, result reported either way

Assembly of parts already in the artifact: the published partition, the same triplet loss, the same
metric $M$, no new data, no new corpus, no new architecture. Inputs: the seven order-blind maps of
Definition 1 plus six admitted in `r92`/`r98`, each alone and concatenated. Readout: a fitted
`Linear → ReLU → Linear`, L2-normalised.

**Admissible by proof, which is the methodological point.** Every input map is order-blind, so a
held-out form and its twin have **identical** input vectors, so the comparator's twin score is exactly
$0.500$ *for any parameters*; not measured, forced. This is the family's first member whose
admissibility is **proved** rather than tested, and it is exactly why a *trained* comparator can be
admitted while a *stronger* one is rejected. The run asserts it as a positive control, and asserts that
the order-**sensitive** completion's twin inputs are *not* identical and that training *raises* its
twin score: the control that makes the check able to fail.

**What we pre-registered, and what happened.**

| Prediction | Outcome |
|---|---|
| The fitted readout **raises** the ceiling at every cell | **Held**: at every cell, and the fit helped all eight maps at every cell |
| It does **not** reach the encoder where the paper scopes its claim | **Held**, and now provably: from `poly8` $K{=}100$ up, no admissible readout over any admissible map can reach it *at any capacity* |
| On `boolean8` it may **close** the untrained-encoder gap, which would make our own appendix anomaly a readout artifact | **Held at $K{=}50$, and refuted at $K{=}100$ and $K{=}190$**: the anomaly splits in two |

**The strongest form of the result is readout-free.** A readout cannot separate what its input has
already merged, so the *collision partition* of the admissible maps bounds every readout at once: 12 of
the 13 maps induce the **same** partition and the 13th is strictly coarser, so one bound covers the
whole family with nothing trained. Eight cells across two corpora: **six are readout-proof**, and the
two that are not are exactly $K{=}50$ on both corpora.

**A correction to our own scoping, stated in the direction the measurement supports.** The bound
excludes every admissible readout from `poly8` $K{=}100$ up: one rung *below* the $K \geq 200$ the
paper already scopes its constructive claim to (that scoping comes from interval overlap, a different
criterion). So **the scoping the paper already declared is the stricter of the two, and the wider
statistic corroborates it rather than forcing it to be loosened.** We say it that way in §4.2, in
Appendix BA and in the verifier's own check name, because an earlier draft of this round had the
direction of derivation backwards.

## 3. §9: your "feature this as a major result" ask, and why the honest version is smaller

You were right that it was buried: *"the untrained encoder exceeds the $\mathcal{F}_3$ supremum at
every scale"* was in Appendix AO and **nowhere in the body**, the seventeenth appendix-only instance in
this project's history, and the one you named as the difference between 6 and 8.

`r100` splits it in two, and one half was ours:

- **$K{=}50$: a readout artifact.** Fitting the readout over the same order-blind maps raises the
  ceiling to $\mathbf{.838}$, which **overtakes** the untrained encoder's $.813$. Attributing that cell
  to the family was wrong, and Appendix AO now says so in its own text.
- **$K{=}100$ and $K{=}190$: a property of $\mathcal{F}_3$, and now *proved*.** $.769$ and $.698$ exceed
  $.652$ and $.640$, the supremum over **every** readout over **every** admissible map, so no member
  of the declared family reaches the untrained encoder there at any capacity.

The body carries the cost in §4.2: *"our $K{=}50$ pass is left unproved by $0.0027$, and Appendix AO's
untrained-encoder anomaly splits into a readout artifact there and a proved family property above it."*
Featuring the un-split version would have been featuring a defect of our instrument as a finding.

## 4. §6: your five alternatives, answered four ways

You asked why not *"a learned invariant kernel, graph spectral descriptor, optimal transport over tree
fragments, canonicalized tree kernels, or a sufficiently expressive permutation-invariant network."*
The answer is not one answer:

1. **Already admitted and already measured** (`r92`, `r98`; Appendix AT): the spectral one is
   `bag_laplacian_spectrum` (quantised Laplacian eigenvalues), the canonicalized tree kernel is the
   $\phi_d$ family's order-blind limit `bag_canon_blind`, plus a graphlet census and a root–leaf path
   bag. Each is admitted by the same per-instance twin test; the ceiling moves at 5 of 8 cells by at
   most $+0.038$, and **every cell the union passes is passed by all $8191$ of its sub-families**.
2. **Rejected by the test, and reported as extensions $\mathcal{X}$** (Proposition 1, §3.2): the
   order-*sensitive* completion $\phi_\infty$, tree-edit distance, a token $n$-gram, an untrained
   encoder. They are not $P$-invariant, so by Theorem 1(iii) they bound the ceiling at **no** value of
   $M$, which is a statement about what they can establish, not a claim that they are weak.
3. **Newly run** (`r100`): your *learned invariant kernel* and your *permutation-invariant network* are
   the same object under this criterion: a trained readout over an order-blind map. That is the
   experiment above, at 13 maps × 8 cells.
4. **Covered by proof rather than by run**: *optimal transport over tree fragments*. An OT cost between
   two order-blind fragment multisets is a function of those multisets, hence $f \circ g$ for an
   order-blind $g$: a member at any parameterisation (Proposition 1), and `r100`'s readout-free bound
   already covers **every** such $f$. Two forms with identical bags get identical OT distances to every
   reference, so it is pinned at $0.500$ on the twin by construction. No run can beat the bound, so we
   did not run one.

## 5. §13: your four contribution claims, adopted in structure, checked clause by clause

§1's contribution paragraph is now four numbered claims in your order, and the abstract matches. Two of
your clauses we did **not** paste, because they are not true of this paper; reviewer-supplied text has
been factually wrong about it for **six** consecutive rounds now, always in the direction of a stronger
claim than we can make:

- Your claim 2 (*"benchmark labels are separable by lower-level cues"* across 23 corpora) needs the
  body's own qualifier: **S1 is clean almost everywhere** and the exposure is at **S2, 66–100% of class
  pairs**. AI~Feynman is *"the severe case, not the typical one — a constructed counterexample, not
  evidence of prevalence."*
- Your framing of claim 4 drops the scoping that makes it defensible: *composition-of-known-*
  *transformations*, each rewrite trained alone, scoped to $K\geq200$ on `poly8` and to the polynomial
  setting for the coverage mechanism.

## 6. §5, §14: already the paper's own verdicts, reported rather than re-added

- **§5 Problem 2.** *"Composition of one known transformation onto one unseen primitive: still not
  compositional reasoning"* is §4.3 verbatim, and your requested relabel to *external validation of the
  methodology* is §4.3's *"portability, not general validation, never prevalence"*: gated at exactly
  one occurrence so a compression round cannot lose it.
- **§14 objection 4.** *"Type-2 clones show the audit's boundary, not structural learning"* is the
  body's verdict: *"every $\mathcal{F}_3$ member attains $0.990$: exactly the maximum this corpus
  admits. So no score here is evidence about structure above S3."*

## 7. §8, §11: measured, and already satisfied

- **§8 (drop `E3m` from the main paper).** `E3m` measures **0** across all six body files and all five
  body floats, and **0** in the rendered text layer of pages 1–9. The single hit in the tree is a TikZ
  **comment** in `figure_overview.tex:69`, an appendix figure. Measured with `shwordsplit`, a file-count
  assertion and a positive control (`the` = 35 in `methodology.tex`), because a silently word-split
  file list has read a false `0` in this project eight times.
- **§11 (~25% fewer new nouns).** The body's `Terms, once.` glossary is **six** entries: *cue*,
  $\mathcal{F}_t$, *twin*, *coverage*, *family-relative admissibility*, and $\sup\mathcal{F}_t$. Of the
  three terms we had planned to retire, **`skyline` and `identification` are already at 0 body
  occurrences**, and `discrimination` has 2, one of which is
  *composition-sensitive structural discrimination*: the Reviewer map's quoted claim for tag `r73`, so
  retiring it would break the map's body-quote check. Nothing to cut; the ask is met.

## 8. §10: declined, with the measurement and the third cross-round conflict disclosed

You ask for the forensic revision history to move to the supplementary. **Round 34's §17 and round 35's
§21 both explicitly asked us to keep it.** That is the third time two reviewers have asked for opposite
things on the same object, and the resolution here has always been measurement plus disclosure, never
arbitration: the developmental chronology already ships as `REVISION_HISTORY.md`; what remains in the
paper is three clauses, each gated at exactly one occurrence, plus the Ethics/Reproducibility
statements on page 10, which is outside the 9-page limit. Deleting them would reverse two prior rounds
to satisfy one.

## 9. §12, §3/§17, not done, and why

- **§12 (reorder §4 around five examples).** Declined on page mechanics, not on merit: Figure 2 sits at
  the top of page 8 and a float crossing a page boundary costs ~14 line slots at once, so moving prose
  across the p7–p9 float region cannot be done inside the page limit this round. The salience fix we
  *could* afford is in §4.2 and §4.4.
- **§3/§17 (do not sell Theorem 1).** Already done in round 35 at a previous reviewer's request: the
  theorem is retitled *Formal justification for the audit criterion*, its scoping concession sits next
  to it, and this round's closure property went **inside Proposition 1** rather than into a new numbered
  result. Changing it again would reverse three consecutive reviewers.

## 10. What our own gates caught this round, and what is now permanent

- **A protected claim deleted while making room.** `check_protected_claims.py` read
  `The audit falsifies; it certifies nothing`: **0 (want 1)**; we had cut it from the conclusion to buy
  a line. Restored, and the line was bought elsewhere.
- **A map row broken by shortening the body.** The Reviewer map's Claim cells are *verbatim body
  quotes*, checked to sit in the section each row names. Compressing two §4.3 sentences silently
  invalidated two rows; the gate caught both and the cells were re-quoted. New instance of the recurring
  class: a fact stated in two representations, corrected in one.
- **Three sentences nearly cut that a previous reviewer had asked for.** Grepping
  `RESPONSE_TO_REVIEW_ROUND35.md` before cutting showed that *"The chain is explicit…"*,
  *"The sharpest test of the whole procedure is one somebody else built"* and *"Failure is informative;
  passing is not certification"* were all added **last round at that reviewer's explicit request**. A
  compression round must diff its cut list against the previous round's grants.
- **An architecture sentence that was both needed and wrong.** Cut for space, then found to be the
  body's only support for the conclusion's *"no claim of architecture independence"*, and, on
  re-reading the appendix it cited, an **overclaim**: it said *"a Transformer neither"* where the
  Transformer's twin score is $0.606$ against chance $0.500$ and the appendix's own prose says it clears
  chance by $0.106$. It fails the *unseen* bound, not both. The body now says only what is measured:
  *"of the three, only the Tree-LSTM clears both"*, and the verifier's own explanatory note, which had
  carried the same wrong summary as unchecked prose, is corrected.
- **`statements.tex` had been printing `--quick`'s assertion count.** The Reproducibility Statement's
  figure was `2250`, which is what `verify_claims.py --quick` reports; the full run is four higher. It
  now prints the full-run count, `2304`.

## 11. Page mechanics, recorded because they are the binding constraint

The two new §4.2 paragraphs spilled the body onto page 10 by 8 lines. Every line was recovered without
losing a number, a disclosure or a refusal. What was measured:

- **Only cuts on page 9 itself move the p9/p10 boundary.** A 515-character consolidation package spread
  over pages 4–8 produced **zero** line movement; the glue on pages 7–8 absorbed all of it.
- **Cuts inside §3 propagate only when large and concentrated.** One 866-character whole-paragraph
  deletion moved the tail; eight ~50-character cuts across six paragraphs bought **nothing**, because a
  sub-line cut rounds to zero per paragraph.
- **Zone-1 cuts are chaotic, not helpful.** Deleting 525 characters from §1 made the spill jump from 6
  lines to **30**: a float repack, not a saving.
- **`\looseness=-1` bought nothing** on nine long paragraphs: TeX found no shorter acceptable setting.
- **Float shrink is absorbed once its page has slack.** After `\arraystretch{0.95}`, deleting a Table 2
  row bought **0** lines, where *adding* the row had cost 4.
- **A `\resizebox` width is a real one-line lever, and non-monotone**: Figure 2 at `0.97\textwidth` left
  the spill at 3, `0.92` at 3, **`0.88` at 2**, and `0.84` bought nothing further.
- **The single largest clean win was converting a `\subsection` on page 9 into a `\paragraph`**:
  ~2.5 slots for zero content loss. §4.5 is now a `\paragraph` inside §4.4, retitled *One Encoder, Two
  Protocols; and What the OOD Axis Names*, with all three of its labels preserved so every cross
  reference still resolves.

## Gate state

`pdflatex → bibtex → pdflatex ×2`. **0** errors, **0** undefined references, **0** `Float too large`,
**exactly 2** overfull boxes (`6.4211pt` vbox, `3.509pt` hbox: both pre-existing), **90** pages, body
ends **p9**, p10's first *body* line is `E THICS S TATEMENT`. All thirteen body headings and all four
body floats on their reviewed-version pages (Fig 1 p3 · Table 1 p4 · Table 2 p5 · Fig 2 p8); per-page
`yMax` identical to the pre-round baseline on all ten pages. Pages 4, 5, 6, 7, 8 and 9 read as rendered
images. `check_protected_claims.py` **PASS**: 19 claims, 4 body absences, 3 document-wide absences over
15 files, all controls firing. `check_reviewer_map.py` **PASS**: 16 rows, 272 checks, 43 `load_log()`
tags, 53 appendix letters. `verify_claims.py` **2304/2304, exit 0, in all three copies**
(2250 → 2304, +54).
