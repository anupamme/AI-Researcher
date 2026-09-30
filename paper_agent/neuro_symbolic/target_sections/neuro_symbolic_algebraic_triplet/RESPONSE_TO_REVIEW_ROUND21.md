# Response to review: round 21

**Summary: the score moved down, and your scorecard changed shape. Two axes you had never scored before
(Generality `5.5` and Theoretical novelty `6`) are now the two lowest, and they point in opposite
directions from the last two reviews.** Round 19 named its acceptance condition as making the
non-certifying result *forceful* (*"this moves from 7/10 to a realistic 8"*); round 20 asked for a
clarity fix and got a full round; you now say the theorem *"is essentially a consequence of the
definition of admissibility"* and should not be sold as a major theoretical result. **We are not
spending a third round on framing.** This round runs one experiment, ports the auditor out of symbolic
mathematics, and withdraws a number of our own.

Three things happened, in descending order of how much they cost us:

1. **You asked whether a stronger admissible structural statistic was missed, and proposed searching a
   constrained class to *estimate* the supremum. We do not have to estimate it: on this corpus the
   family provably saturates, and that was already computed.** It was in the appendix. It is now in the
   body.
2. **We ran the experiment this paper's own appendix admitted was missing**, and it did not confirm the
   explanation we had offered. It found that the thing being explained was **an aggregation artifact of
   ours**. `+0.250` is withdrawn.
3. **Generality is the one criticism no prior round addressed.** The auditor now runs outside symbolic
   mathematics, for zero GPU-hours, with the corpus's provenance labelled rather than glossed.

**`verify_claims.py` moves `1949 → 2056`, exit 0 in all three copies** (`--quick` is `2052`, as always
exactly four lower). **Main text is still 9 pages**, `E THICS S TATEMENT` first on page 10.

---

## Major Concern 2, the hand-designed family: you proposed a search; the supremum is computable

Your fix was to auto-search a constrained class of structural statistics and estimate
`sup 𝓕₃`. **A search estimates a supremum. Here it can be computed, and it was; we had buried it.**

- **The family saturates.** `poly8`'s maximum tree depth is `4`, so the `φ₈` row we already report **is**
  the complete order-blind fingerprint. This is asserted as **bag equality** (`bag_canon_blind ==
  bag_phi_d8`), not argued. Within the invariance class that admissibility defines, **there is no finer
  member to have missed.**
- **The limit is not the maximum, which is what makes a resolution search incoherent here.** The
  order-*sensitive* completion `φ_∞` falls **below** the coarsest member. The finest thing we can build
  is the *weakest* control, so "search harder for a stronger control" is not an instruction that can be
  followed.
- **Membership is a test that is run, and it rejects things.** A comparator enters `𝓕₃` only by scoring
  exactly `0.500` on the shape-matched twin, per instance. `φ_∞`, tree-edit distance and an untrained
  encoder **fail** it and are reported as extensions `𝓧` outside the criterion. A reviewer who suspects
  the family was hand-picked to be beatable should be able to see, in the body, that candidates get
  **thrown out** of it.
- **And it has already been widened by descriptors we did not choose**: the five a previous reviewer
  named. The supremum moves at `4` of `8` cells, always onto the same member, by at most `+0.038`, and
  **moves no verdict**. At the `K=500` `poly8` cell the body prints, it does not move at all.

All four of these are now in §4.2 under **"Why *these* descriptors: the family is not a selection"**, and
the membership-is-a-test sentence is in §3.3. **This is the sixth time a result you or a predecessor
asked for turned out to be sitting in our appendix.** We have accepted the rule that follows: a result
that exists only in the appendix does not exist.

## Theoretical novelty `6`: you are right, and it is rebilled; with the conflict named

You are correct that the impossibility result falls out of the definition of admissibility in a few
lines. **We kept the statement and the proof and changed the billing.** §3.4 now says, in the paper's
own voice: *"We bill it as **scoping**, not as a theoretical contribution: it falls out of
Definition 1 in a few lines, and earns its place by fixing what a passing audit **means**."* The
conclusion states it as what the method's output *is* (a falsification certificate relative to a
declared family), rather than as a theorem we are selling.

**We are telling you openly that this reverses round 19.** That review made the forceful version its
named condition for an 8. We think you are right and it was wrong, and we would rather say so than
quietly satisfy whichever reviewer reads the file next. The content is unchanged, so if you disagree
with each other the evidence is in the same place either way.

## Generality `5.5`: the auditor runs outside symbolic mathematics

The mapping is the one our related work already named, and it is exact: **S1 variable identity →
identifier names**, **S2 operator/arity inventory → AST node type with arity**, equivalence class →
clone class. **No new measurement code**: `benchmark_audit.separability_from_trees` is called on trees
built by Python's own `ast`, so the statistic is byte-for-byte the one the 23-corpus survey reports.

- **Corpus, labelled and not glossed.** `300` Type-2 clone classes × `4` members, α-renamed from `995`
  **real** Python `3.14.6` standard-library functions of `40`–`400` AST nodes. **It is a constructed
  clone corpus over real code, not a published clone-detection benchmark**, and the survey caption says
  so in those words. It shows the auditor **ports** and what it reports there, **not** the prevalence
  of the flaw in that literature. We would rather score `5.5` again than claim the second thing.
- **Two guards make the mapping a measurement rather than an assertion.** The AST node bag is verified
  renaming-invariant in **`300/300`** classes, so the S2 cue really is blind to the renaming; and the
  identifier set is verified to **vary** within **`300/300`**, so the S1 probe has something to read. A
  corpus failing the second guard would report a clean S1 for free.
- **Result: both failure modes appear, and T1 fires more sharply here than in any symbolic corpus**,
  `96%` of classes have an identifier set no other class shares, against AI Feynman's `84%`, with
  pairwise separability `100%` on identifiers, node types and full tokens over a `1454`-symbol
  identifier pool. As everywhere in that table the T1 column measures **representatives**, so the
  shortcut can only transfer through the identifiers a renaming leaves shared: **measured, and
  reported, at `0.308` overlap** rather than left for a reader to worry about.

**Cost: training-free, seconds, CPU** (tag `r95`, R31). **It lands as rows in the existing survey table
plus one sentence in §4.1 and one clause in the abstract, no new float**, because there is no page for
one.

## Figure 2's arrangement bar: you found a real exposure, and it was ours

You were right that Figure 2's first bar (*arrangement `+0.012`, CI covers `0`, **supported***) sat
beside an appendix recording an alternate-order arm costing **`+0.250`**, and that the appendix's own
words were *"we have not run the experiment that would separate diversity from the other differences."*
**We ran it.**

**Three conditions, not two, on the same class set**: singles alone (the published condition), a
**control** library of `2` composites all following the *forward* permutation, and a **diverse** library
of `2` composites following *distinct* permutations of the same multiset. Class set (`133`), site filter
(Δ+4), depth (`4`), anchors, skeletons and scored forms held **fixed**; only order-span varies. The
manipulation is checked, not asserted: distinct composites per class is exactly `1` in the control arm
and `2` in the diverse arm, token delta `+16` identical in both. Both ladders, `5` seeds, paired within
encoder (tag `r94`, R30, `49.6` min).

**Diversity is not the mechanism.** It removes `-0.0075 [-0.0331,0.018]` of the cost on the local ladder
and `+0.0075 [-0.0135,0.0256]` on the non-local one: **the two ladders disagree in sign and both
intervals cover zero**. So the explanation we had offered is withdrawn.

**And then the validity check became the finding.** The singles arm reproduces the *published*
condition, so it should have shown `+0.250`. It shows `+0.0286`. A discrepancy in the **delta** and in
**neither operand** localises the fault to the aggregation, and it did:

> `r91` accumulates alternate-order scores into a per-**ladder** list from inside a loop over training
> **libraries**, so the alternate-order cell averaged the full library together with the
> leave-one-primitive-out library, while the forward cell it was subtracted from was the full library
> alone. **The published quantity was a contrast between two training libraries, not between two
> orders.**

**The signature is exact rather than argued.** In all six cells the published delta equals full-library
forward minus the pooled alternate mean (`d=4` L: `0.9218 - 0.6714 = +0.2504`), and the ten per-seed
values split cleanly `5`/`5` by library. **Corrected, no order cost anywhere exceeds `0.035` in
magnitude and six of the twelve library-by-ladder cells are negative**, so all six of that run's stored
*"interval excludes zero"* flags are **spurious**. `r94`'s singles arm reproduces the corrected cell to
**four decimals** (`+0.0286`) from a different RNG stream in a different runner, which is what makes
this a measurement rather than a re-reading.

**The consequence for Figure 2 is the opposite of the one you were braced for: the arrangement bar is
now *corroborated* on a second class set rather than contradicted by it.** The caption says that, and
names the withdrawal in the same breath.

Three further things we are stating rather than letting you find:

- **We deviated from a pre-registered rule, and we say which.** The run was specified to be **discarded**
  if the singles arm failed to reproduce the published number. We diagnosed instead of discarding.
  Appendix AV states the rule, the deviation, the reason, and the counterfactual: *had the arithmetic
  not closed, the run would have been discarded as specified*.
- **A null needs its sensitivity shown, and the honest anchor was not the in-run one.** Changing the
  training library moves the forward column by `+0.048` and `+0.078`: more than any cost here, but only
  `1.7×` on the local ladder. So the load-bearing anchor is that the **same** paired estimator on these
  **same** `133` classes resolves coverage effects of `+0.204` and `+0.468` with intervals **excluding**
  zero. Our first draft of that caption said *"several times more"*; the assertion we wrote to check it
  **failed**, and we fixed the paper rather than the tolerance.
- **Three negative controls, and the third exists because the second does not test what it looks like.**
  `--nc_leak` injects the held-out form *after* the leak guard has counted, showing the measurement
  responds to leakage; `--nc_leak_pre` injects it **before**, so the **guard itself** must fire. A
  passing `leak == 0` proves no leak was present, never that one would be seen.

**This is the fifth correction to a claim of our own and the sixth revision incident**, and it is one of
the two that corrected something in our **favour**. The verifier now recomputes the whole decomposition:
the pooled mean, the `5`/`5` split by clustering, both per-library corrected costs, and the corrected
cell **as printed**, so the artifact cannot reappear silently.

## Length: the body carries no archaeology, and here is the measurement

For the third review running, the length complaint is about the bound PDF rather than the paper.
Measured across `abstract`, `introduction`, `related_work`, `methodology`, `experiments`, `conclusion`
and the two figure files:

| | count |
|---|---|
| occurrences of *superseded*, *retracted*, *revision history*, *archaeology* | **0** |
| run tags mentioned (`r90`–`r95`) | **7** |
| appendix pointers | **22** |
| body source words | **6165** |

The hard separation you ask for: *"Main paper: 1–7. Supplement: everything else"*; **already exists
exactly as described.** The body ends on **page 9** with `E THICS S TATEMENT` the first line of page 10.
The other 67 pages are the appendix and the material the verifier recomputes against; cutting the body
would remove evidence, not archaeology.

**On shipping the appendix as a separate file: the CFP allows either, and encourages a single one, and
splitting this file would ship a broken one.** `21` body→appendix `\ref`s (methodology `2`, experiments
`15`, conclusion `1`, Figure 2's caption `3`) would print `??` in a split build, and rewriting them into
prose pointers is a change we are not willing to make blind at this stage. **So we keep the single file
and answer the perception with the measurement above** rather than with a format change that could cost
`21` cross-references.

---

## Verification

- **Build:** `pdflatex → bibtex → pdflatex ×2`. `0` errors, `0` `??`, `0` *Float too large*, `2` overfull
  boxes: both **pre-existing** (`6.4211pt` vbox, `3.509pt` hbox). The one *undefined* is the standing
  `TS1/ptm/m/sc` font warning. `76` pages.
- **Page gate:** body ends page 9; `E THICS S TATEMENT` is the first non-folio line of page 10. The new
  appendix table needed `\tabcolsep` surgery to clear a `21.2pt` overfull, and Figure 2's caption
  addition was funded by deleting a *third* restatement of a name that survives in the abstract and in
  adjacent body prose.
- **Reconstruction gate re-run** (round 20's, and it was mandatory this round because the abstract and
  Figure 2 both changed): abstract, §1, Figure 1, Figure 2 and the conclusion extracted from the built
  PDF and read cold. The argument reconstructs from those five alone, now including the generality
  result and the withdrawal.
- **Figure 2 re-rendered and looked at.** `\resizebox`'d TikZ collisions are invisible to every
  text-based gate.
- **`verify_claims.py` `2056/2056`, exit 0** in the working tree and both artifact copies. The new
  assertions pin `r91`'s defect **and its correction** (the decomposition, the `5`/`5` library split by
  clustering, every within-library cost, the printed cells), every cell of `r94`'s table, the
  cross-log agreement between the two, and `r95`'s guards and separability values.
- **A verifier gap this round's own checking surfaced:** one assertion used `.get()` with `continue`, so
  a mistyped key **silently skipped** the load-bearing sensitivity check. It now indexes directly: a
  missing key must FAIL, not skip.
- **A stale number this round's own checking surfaced:** the appendix said *four* of the twelve corrected
  order-cost cells were negative. It is **six**: exactly half, which is the stronger statement. Both
  the prose and the assertion's label are corrected.
- **`REPRODUCE.md`** gains rows **R30** (`r94`) and **R31** (`r95`) in all three copies, with which
  values are recomputed and which are read from the log stated per row.
