# Response to review: round 16

**Summary: one new experiment, the one you asked for, and the positioning work you said the gap
actually is.** The review's own diagnosis sets the shape of this round: *"I don't think you need
another 20 experiments. You need to eliminate three reviewer doubts"* (§21) and *"The gap is primarily
positioning + novelty perception, not an experimental hole"* (§25). So there is exactly one run:
`r91`, §23's non-local transformation family, held out and tested in composition, and the rest of the
round moves the claim you identified as the paper's centerpiece into the parts of the paper people
read.

**The verifier count moves, 1742 → 1805, exit 0 in all three copies.** Last round it deliberately did
not: nothing was run, and `verify_claims.py` never reads the `.tex`, so a moving count would have meant
an unasserted number. This round a run happened, so a *frozen* count would have meant `r91`'s numbers
never entered the verifier. `+58` of the `+63` are `r91`'s.

**Main text is still exactly 9 pages**, spill `0`, `E THICS S TATEMENT` at index 6 of page 10.

Sections below are numbered by the review's own. Items that asked for no change, or that we found
already satisfied, are grouped at the end with the evidence.

---

## §10: "de-emphasize the formal proposition as a contribution and emphasize the empirical discovery." **Done, in place.**

Proposition 1 and Corollary 1 stay exactly where they are; nothing moved, no cross-reference broke,
and §3.3 now **concedes the triviality in your terms** rather than being caught by it: the invariance
observation is elementary once stated; what is not elementary is that the admissible family turns out
**non-monotone in resolution**, so the audit statistic cannot be any single baseline. The section's
emphasis is restructured so the *measurement* is the headline and both propositions read as what
licenses it.

We did not delete the propositions, for one reason worth stating: the non-monotonicity claim is an
empirical ordering over a family, and without the admissibility definition there is no family for it to
be an ordering over. The concession is that the definition is cheap, not that it is dispensable.

## §11: "I actually like §4.4 more than the paper currently emphasizes." **Elevated.**

§4.4 opened on bookkeeping and reached its own design three clauses later. It now leads with the
design and bills it: *"This is the cleanest intervention in the paper: the held-out tree is
**byte-identical** across the two arms, library membership is the only variable, and library sizes are
matched — so structural distance is held exactly fixed and nothing but exposure differs."* No new
evidence; the evidence was already there and was being undersold.

## §12: soften "causal." **Both main-text sites changed, to your own formulation.**

`abstract.tex`'s *"a causal result"* and the conclusion's *"causally changes"* are gone. The abstract
now reads *"a controlled intervention identifying the effect of exposure to the generating rewrite
family, since structural distance is held exactly fixed."* `experiments.tex` already said *controlled
intervention* (round 15). `causal` now appears **0 times** in the abstract and conclusion.

## §13: "compress §4.5 substantially and use the space for something more central." **Compressed, keeping the one part §25 made central.**

§4.5 lost the portability narrative and kept the external replication of the non-monotonicity, which
Part B of this round promotes to centerpiece evidence: `M(φ_d)` `0.752 → 0.726`, WL `0.818 → 0.776`,
`φ_∞` at the floor; **on a corpus we did not build**. Those four values were appendix-only and are now
printed in the main text, which is why four of the new assertions are theirs: a promoted number that
can drift is worse than a buried one.

## §16: p-values. **Verified rather than asserted: already satisfied, main text and appendix.**

`p<`, `p-value` and `p = 0.` occur **0 times** in the abstract, §1, §3, §4 and §5. We also checked the
complaint's harder version: that the *appendix* leads with significance where an effect size would do,
and all 15 appendix p-values appear as parentheticals **after** an effect size and its interval. No
change was needed and none was made.

## §17: density. **A placement fix, and one honest tension we chose to accept.**

Two of the terms in your list (`dual skyline`, `leakage index`) are **not in the main text at all**;
they are appendix vocabulary. The real main-text load is ~11 terms, all defined once in §3.3. So this
was placement, not vocabulary: the definition strip (*cue* / *skyline* / *twin* / *coverage*) was
buried at the tail of §3.3's longest paragraph and is now a one-line strip at the **head** of the
section, before any of them is used.

**The tension we accept, and how it resolved.** The page budget was also going to take §3.3's walked
example, which is the one place a fast reader sees what the levels concretely mean: your complaint. It
survives, **compressed from three levels to two** and folded into the strip itself: the class of `x+y`
against `y+x` and `(x+0)+y`, S2 reading the operator bag, S3 order-blind by construction, and what
*no* level can do (recognise that inserting `x+0` preserved the class). Figure 1 carries a worked
instance per rung as the second line of defence. That is the plan's own fallback rather than the cut,
and we think it is the right trade even though the lines had to come from elsewhere.

## §19: the title. **Adopted verbatim.**

*Beyond the Strongest Baseline: Falsifying Structural Claims in Neuro-Symbolic Benchmarks.* A title is
a promise, so the abstract and §1 were rewritten to deliver it: `non-monotone` appeared **0 times** in
the abstract, `experiments.tex` and the conclusion before this round, which is a fair statement of how
badly the old framing buried the claim.

## §21: the three doubts.

**Doubt 1, "this is a careful application of known ideas."** Answered by moving the finding you named
into the paper's load-bearing positions, not by adding adjectives. The consolidated sentence now appears
in the abstract, in §4.3 (*"That inversion is the paper's centerpiece, and it is measured five times
over"*) and in the conclusion, carrying all the replications explicitly: three corpora, two algebras,
both protocols, all five independent class partitions (`φ_∞` `0.224±0.019` against tree-local
`0.266±0.023`, 5/5) and the external 80M-parameter model. Related Work now opens on your triad:
**shortcut baselines ask whether a benchmark is easy; control tasks ask whether a representation
contains a signal; we ask whether a baseline is logically *admissible* as evidence against a
representation-level claim, and find that admissibility is non-monotone in resolution.**

**Doubt 2, "the control family is hand-designed."** Conceded and turned into the claim, adopting §22's
wording nearly verbatim (below).

**Doubt 3, "composition over four primitives is thin."** The framework's own contrast is now billed as
a result rather than a caveat: `+0.079` for never having *composed* against `+0.535` for a primitive
held out of the library, an order of magnitude apart **under one design**, which is the framework
*separating* composition of known transformations from mere exposure to them. `r91` extends that
separation to a rewrite that duplicates a subtree.

## §22: scope the criterion instead of proposing a universal standard. **Adopted.**

The abstract now reads: *a held-out-form score supports a compositional interpretation only relative to
an explicitly specified family of invariant controls, here variable identity, operator/arity inventory
and bounded local structure, plus a separate coverage test.* The boxed contract already said *explicit,
not exhaustive*; it was buried and is now doing visible work.

## §23: a non-local transformation family, held out, tested in composition. **`r91`, and it is the round's only compute.**

**Design is a swap, not an addition.** Distributivity (`a·(b+c) → a·b + a·c`) replaces `mul_identity`
over the **same** class set, the **same** skeleton orders and the **same** library size, so the only
thing that varies is whether one primitive rewrites a bounded neighbourhood.

**Which non-local rewrite was measured, not chosen.** Over all `1102` `poly8` anchors, `_rw_distribute`
fires on `283`, `_rw_reassoc` on **`0`** (EQNET forms are already right-nested) and both removal schemas
on `0`. Distributivity is the only non-local rewrite the corpus admits, and it is non-local in the sense
your objection needs: the rewritten subtree appears **twice** in the output, so the edit is not confined
to a bounded neighbourhood and output size depends on the size of what was rewritten. **No rewrite
schema was written for this run: `equivalence.py` is untouched, and with it every published number.**

**Result, and this is the branch pre-committed in the module docstring before the run.** `N−L` on
identification is `+0.004 [-0.006,0.018]`, `+0.009 [-0.014,0.035]`, `−0.002 [-0.030,0.029]` and
**`−0.013 [-0.054,0.024]`** at depths 1–4: **every interval contains zero**. Never composing costs
`+0.077` in the non-local arm against `+0.056` in the local one. **Composition invariance is not
locality-specific**, so §4.3's named scope (*composition-of-known-transformations*) covers a primitive
set containing a subtree-duplicating rewrite. Had the sign gone the other way the paper would have
renamed the phenomenon *composition-of-known-**local**-transformations*; that branch was written down
first and was not renegotiated.

**What did move is coverage, in the direction nobody would have predicted.** Holding the **non-local**
primitive out of the library costs `+0.204 [0.161,0.250]` at `d=4`; holding the **local** one out costs
`+0.468 [0.391,0.540]`; the paired difference of differences is `−0.263 [-0.344,-0.184]`, excluding
zero at every depth `≥2`, both rows coming from the *same* encoder per seed. **A structurally bigger
rewrite is not a harder one**, which sharpens Finding 3's family reading rather than weakening it.

**Three disclosures the corpus forces, all in the log before they were in the prose.**

1. **`K = 133`, not the `200` targeted.** `840` anchors lack a site for some primitive, `121` cannot
   build the arm-N ladder at `Δ+4`, `8` fail the leader constraint.
2. **18 of the 24 orders.** `_rw_distribute` has ≥2 distinct sites on **`0`** of `1102` anchors, so one
   site cannot both stock the library and supply a held-out single application: the swapped primitive
   can never lead. **The same constraint is imposed on arm L**, so both arms run the same 18 orders over
   the same classes. Retained swap positions are logged as non-uniform (`54`/`47`/`32`).
3. **The token *multiset* is not matched**, because duplication is the point. A bag sees that, so the
   cue **raises** the non-learned rows rather than hiding beneath them: `0.263` in arm N against `0.173`
   in arm L at `d=4`, while the untrained encoder moves the *other* way (`0.134` against `0.174`). Read
   conservatively the cue inflates arm N's held-out row, so the coverage difference above is an **upper**
   bound; the primary contrast is unaffected, both arms' trained rows being equally exposed.

**Equivalence is verified, not inferred from the schema**; you asked for this explicitly. SymPy
confirmed all `532` ladder forms per arm equivalent to their anchors (`0` refuted, `0` unresolved), the
closure guard finds `0` test forms inside the library's searched closure at every depth, every depth-4
form is exactly `+16` tokens over its anchor, and the verifier **recomputes** all `1064` (class, depth,
arm) deltas from the log's own per-class counts against an independently written delta table rather than
reading the runner's boolean.

**And one number does not replicate. We flag it rather than absorb it.** `r91`'s alternate-order arm
costs ladder L `0.922 → 0.671` at `d=4`, where `r81`'s alternate-order row cost nothing (`0.937` against
`0.918`). The two are not the same object: `r91` restricts chains to `Δ+4` sites so the arms are
size-matched, on the `133` classes admitting a distributivity site, but on this class set a second
order of the same multiset is materially harder, so §4.3's order claim should be read as what it cites,
`r81`'s per-order minimum over all 24 orders, and not as a general claim that order is free. The effect
is **smaller** in the non-local arm (`0.908 → 0.816`), so it is not a locality effect either.

**The free half of §23, which was already in the repo and never said out loud.** `boolean8`'s De Morgan
primitive is a non-local rewrite that rebuilds a node and both children: the paper had been composing
a non-local primitive on a second algebra for three rounds without saying so. §4.3 now says it. It does
**not** replace `r91`: a skeptic can call De Morgan bounded-depth, which is exactly why distributivity (
subtree duplication) is the arm that answers you.

## §25: "make that the intellectual center of the entire paper." **This is the round.**

Everything above serves it: the title, the abstract's centerpiece sentence, §4.3's *"measured five times
over"*, Related Work's triad, and §4.5 compressed **around** its external replication rather than out of
it. One correction we owe you in the other direction: `r91` gives the non-monotonicity a **sixth**
replication, and the appendix reports it as a **sign, not an effect size**; chance on `133` classes is
`0.0075` and the entire `F₃` ladder there lives between `0.000` and `0.038`. The load-bearing versions
remain §4.3's `poly8` ladder, the five partitions and §4.5's external one. We also fixed a label we had
wrong: that ladder row was labelled *tree-local `φ₁`*, and the arg max is in fact a Weisfeiler–Leman
member in all eight cells. The verifier now pins the arg-max member set as an exact set.

---

## Verification of this round, in the paper's own terms

- **`verify_claims.py`: 1805/1805, exit 0, in all three copies** (working tree,
  `artifact/iclr-supplementary/`, `artifact/audit-sym/`), up from 1742.
- **10 negative controls** against the new block, each exiting non-zero on the *intended* assertion, log
  restored byte-for-byte. **Two make the paper's claim stronger and must still fail** (arm N lifted to
  `0.950`; the size confound erased from arm N's bag row). **One found a hole in the verifier rather
  than in the log**: the `+16` recomputation read arm L alone while its note claimed both arms. It now
  recomputes both.
- **`REPRODUCE.md` R27** carries the real command:
  `python3 run_r91_nonlocal_composition.py --K 140 --num_seeds 5 --verify_classes 200` (**43.9 min**,
  one Apple M-series GPU), synced to both shipped copies with the absolute `log_dir` redacted.
- **Page gate**: 9 pages of main text, spill `0`, Ethics at index 6, `??` = 0, `0` LaTeX errors, `0
  Float too large`, one pre-existing overfull hbox (3.509 pt), 71 pages total.
- **What closed the page budget was structural, not verbal**: main Table 3 was deleted outright, its
  content already existing as Appendix AH's full matrix (a strict superset), with all seven
  cross-references repointed. Three partial-sentence cuts attempted first produced **zero** net rendered
  lines, because they did not cross a line boundary.
