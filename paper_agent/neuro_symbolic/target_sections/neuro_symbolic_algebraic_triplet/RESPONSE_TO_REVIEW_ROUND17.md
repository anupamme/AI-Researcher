# Response to review: round 17

**Summary: the three claims you asked to be made unmistakable are now the paper's spine, and the one
objection you predicted a hostile reviewer would make is answered by measurement rather than by
argument.** You wrote that the gap is "significance and scope, not whether the experiments are
carefully done" (§2) and that "I don't think you need another 20 experiments — you need to make the
existing evidence land harder" (§21). So this round moves evidence rather than adding it, with one
exception: `r92`, which widens the control family with **your** list of descriptors and costs 72
seconds of CPU. No GPU, no training, no new corpus.

**The verifier count moves, 1805 → 1843, exit 0 in all three copies**, and `statements.tex` prints the
new number. **Main text is still exactly 9 pages**, `E THICS S TATEMENT` first on page 10.

Sections below follow your numbering.

---

## §4 / §20.3: "de-emphasize the formal propositions; make the empirical discovery the contribution." **Done in the sentence that describes them.**

§1's contributions now say it outright: *"The propositions of §3.3 are the language that makes this
measurable; the measurement is the contribution."* Nothing moved, no cross-reference broke: §3.3
already conceded the triviality in your terms last round, and what was missing was the framing at the
point where a reader decides what the paper is claiming.

## §5: "why *this* family? Why not subtree kernels, spectral features, graphlets, path kernels, tree automata, compressed subtree hashes?" **Answered twice: structurally, and by running it.**

**The structural half.** Admissibility *forces* order-blindness, which rules most of that list in or
out before any measurement: three of your seven names are already in the ladder under other names,
the unordered subtree kernel and the bottom-up tree automaton are both `bag_canon_blind`, the `φ_d`
family's own limit, and compressed subtree hashing is precisely WL's relabelling step. Appendix AT
says which, because a family assembled from the canonical order-blind constructions is a different
object from one sampled by taste.

**The measured half, `r92`.** The four genuinely new descriptors (WL at `h=4,5`, a graphlet census of
all connected 3- and 4-node subsets, a path kernel, a Laplacian spectrum) were added to `F_3` and the
supremum re-read on both algebras at all eight scales.

- **Admissibility is measured, not assumed.** Each candidate had to score **exactly `0.500` on every
  instance** of the published `K=500` swap twin (348 classes). All five passed. **The test ships with a
  control that must fail**: the order-sensitive token n-gram reaches `0.681`, reproducing r75's stored
  row exactly, in a different runner, and is refused admission. Without a control that fails, admitting
  five candidates would establish nothing.
- **The supremum moves at 4 of the 8 cells**, always to the path kernel, by at most **`+0.038`**
  (boolean8 `K=100`) and `+0.004` on poly8. **No verdict moves anywhere.**
- **At poly8's `K=500` (the cell §4.3 prints) it does not move at all**: tree-local stays `0.277` and
  every new member lands at or below `0.276`, so *"sweeping the family adds no stronger member"*
  survives the widening verbatim.
- **Two findings came free, and both cut against the intuition the objection rests on.** WL is
  **non-increasing in `h` in all eight cells**, strictly in seven, so Proposition 4 replicates on a
  resolution axis we did not choose. And the Laplacian spectrum, the most sophisticated member here, is
  the **weakest** control by an order of magnitude. Admitting more members cannot lower a supremum, and
  the family's *size* is not the audit statistic.

Your sentence went into the boxed contract almost verbatim: *"we do not propose S3 as the set of all
non-compositional explanations, but as an auditable, explicitly parameterized family whose adequacy is
itself stress-tested."* It is now true rather than defensive, because §4.3 points at the stress test.

## §12 / §20.2: "promote the GIN/twin result; put it front and centre." **It is now its own subsection.**

**§4.5, *One Encoder, Two Protocols, Opposite Verdicts*.** A GIN clears S3 on unseen `boolean8` classes
(`0.881 [0.850,0.909]` against a strongest non-learned bound of `0.596`) and sits at **chance** on the
shape-matched twin over the same corpus, the same partition and the same trained weights (`0.511`
against `0.500`). *A reader who accepted the unseen-class number alone would have credited that GIN
with structural identification.* The paper says so in the main text now, with the numbers, and states
in the sentence that the claim is the conjunction of two **intervals** over 3 seeds rather than either
point value: the same discipline §4.3 applies to its own GIN rows. `verify_claims.py` had already
asserted the conjunction; the appendix work was done, the promotion was not.

## §9: "reduce the prominence of the Lample–Charton audit." **Demoted, and it paid for §4.5.**

§4.5 was the external audit; it is now the closing paragraph of §4.3, keeping the S2 verdict in a
clause (`0.941` against `0.872`, correctly, since those labels are *defined* by operator content) and
keeping in full the part your §22 Claim 2 relies on: the external replication of the non-monotonicity.
The portability narrative moved to Appendix AR. `\label{sec:external_audit}` rides with the paragraph,
so all eight cross-references still resolve.

## §7 / §20.4: "the positive result is closer to compositional interpolation than to systematic reasoning." **Your phrase, adopted.**

The abstract's *What we do not claim* and the conclusion's *Not established* both now name it:
**compositional interpolation within a learned transformation basis**. Verified rather than asserted:
`compositional reasoning` occurs **5 times** in the main text and **all five are negations**.

## §8: "23 corpora is narrower than it sounds." **Already disclosed; sharpened where it is described.**

The main text keeps *"broad corpus-level coverage, limited family-level diversity, so a per-family
reading is the honest one"* and now leads the audit paragraph with where the flaw actually lives: S1
clean almost everywhere, S2 exposure at `66`–`100%` across every family, AI Feynman the severe case
rather than the typical one.

## §10 / §20.5: "shrink the forensic history." **Consolidated, not deleted, and we say where it went.**

You also called the visible self-correction one of the paper's strongest aspects (§2), so the split we
made is: **outcomes stay, chronology ships.**

- **Stays in the paper**: the five-incident summary table, every corrected *number* in the table it
  belongs to, the superseded `score_5` reconstruction (Appendix T), the disclosure-vs-fix taxonomy
  (Appendix N: on reading it again it is methodology, not history, so it was left intact), and the
  verifier.
- **Moves to `REVISION_HISTORY.md`**, shipped with the supplement and cited from Appendix F: the
  per-incident narratives, and four narrative asides that had grown inside the *science* appendices:
  including ~15 lines of confession inside a table caption ("we first wrote that this was 'inside the
  seed spread'; it is not"). Each site keeps the corrected number, the one-sentence lesson, and a
  pointer.
- **The Ethics Statement was rewritten to match.** It claimed the corrections were "reported in the
  paper rather than removed from it"; after the move that sentence would have been false, so it now
  says where the chronology is.
- **An appendix reading guide** was added at the head: which letters are provenance and history, which
  are protocol specifications, which are the experiments the main text cites. That is also our answer
  to §17's "too many moving parts", at no cost to the 9 pages.

## §11: "the AI-use disclosure is rhetorically prominent." **Compressed from four paragraphs to two**, with every disclosed fact kept, since the disclosure is required. What went is the rhetoric about why the disclosure is checkable; the fact that the supplement ships an executable which asserts the prose against the logs survives as a clause.

## §17: density. **Placement, plus what the reading guide fixes.** Verified while planning: `E3`, `E3b`, `E3m`, `LOPO`, `leakage index` and `dual skyline` appear **0 times** in the main text; they are appendix vocabulary. §1 was rebuilt from four paragraphs to three and is ~13 rendered lines shorter, which is where most of the room for §4.5 came from.

## §22: "three claims must be unmistakable." **They are the abstract, §1 and the conclusion, in that order.**

The abstract's three bolded units are now your three claims, with the old Findings folded in as their
evidence; §1's contributions and the conclusion's first paragraph carry the same three-part spine. The
abstract opens on your own sentence: *a structural baseline is useful only if it is invariant to the
structure whose absence it is meant to rule out*, and Claim 3 arrives with its numbers rather than as
a caveat at the end.

## §18: the review you expect a hostile colleague to write. **This is what `r92` is for.**

That review's load-bearing sentence is "the authors demonstrate that their Tree-LSTM beats the
particular invariant family they selected." It is now answerable in one line: *we widened the family
with the descriptors a reviewer named, admitted them by a per-instance invariance test with a control
that fails, and the verdict did not move.*

---

## Verification of this round, in the paper's own terms

- **`verify_claims.py`: 1841/1841, exit 0, in all three copies** (working tree,
  `artifact/iclr-supplementary/`, `artifact/audit-sym/`), up from 1805. `statements.tex` prints 1843.
- **10 negative controls** against the new block, log restored byte-for-byte. **Two make the paper's
  claim stronger and must still fail** (making the n-gram look like a member; shrinking the widening's
  largest gain). **One is the inverse and must PASS**: corrupting r92's own copy of the trained lower
  bound changes nothing, because the verdict check re-reads that bound from `r70`/`r86`, a corrupted
  copy inside the new log cannot make it pass. **One found a blind spot rather than a defect**: the
  supremum checks carry a `1e-3` tolerance because two cells are exact half-way cases at three decimals
  (`0.4925`, `0.0375`), and the exact-value check written alongside them is what catches a mutation
  inside that band. Both are kept, and the comment in the verifier says why.
- **Two checks were added after a readiness pass**, not before it: §4.5 promotes the GIN interval
  `[0.850,0.909]` and the `0.596` bound into the main text, and neither was pinned to the digits the
  paper prints. They are now, which is why the count is 1843 rather than 1841.
- **One appendix was orphaned by this round's cuts and is not any more**: deleting §4.2's
  validates-rather-than-debunks sentence removed the only pointer to Appendix V, so Table 1's
  `score_5` row now carries it, and the reading guide names the five appendices that stand alone as
  full tables rather than being cited from the body.
- **`REPRODUCE.md` R28** carries the command (`python3 run_r92_family_stress.py`, 72 s, CPU), synced to
  both shipped copies with the absolute `log_dir` redacted, along with `REVISION_HISTORY.md`.
- **Page gate**: 9 pages of main text, Ethics first on page 10, `??` = 0, `0` LaTeX errors, `0 Float
  too large`, one pre-existing overfull hbox (3.509 pt), 71 pages total. Appendix AT's table was 27.6 pt
  overfull when first set and was re-set at `\scriptsize`; both new pages were rendered and inspected.
- **What paid for the additions**: §4.5's fold into §4.3 (−11 rendered lines), §1's rebuild (−13), the
  conclusion's `Scope:` clause, and three sentences that Table 1, Table 2 and Appendix AH already
  carried. Word-level trimming produced **zero** net lines until whole sentences went: the same lesson
  as last round.
- **`equivalence.py` is untouched**, and `structural_baselines.py` gained a separate `WIDER_BAGGERS`
  dict rather than an edit to the published ones, so no shipped row can move.
