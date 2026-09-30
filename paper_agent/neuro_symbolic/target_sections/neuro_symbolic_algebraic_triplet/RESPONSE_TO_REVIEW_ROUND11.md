# Response to the review (round 11)

*Not part of the paper. Text for the response form.*

The review scores the file **6; Weak Accept, confidence 0.80**, and is unusually
specific about why: the experimental core is judged strong (Experimental rigor
9/10, Reproducibility 9.5/10) while **Theoretical contribution sits at 6.5** and
**Clarity at 7**. The diagnosis we accept in full is this sentence:

> *"the paper sometimes presents a carefully scoped empirical methodology as if
> it were a more general epistemological/theoretical result."*

That is a claim about our billing, not about our evidence, and every one of the
three "surgical changes" the review asks for is a billing change. We made all
three, plus the one experiment §17 recommends, plus the smaller items. We did
**not** add breadth: the review's *"I don't think you need another 15
experiments"* is advice we followed.

---

## Change 1 (§16): the epistemic contract, made visually unavoidable

The review's point was not that the paper fails to state its scope; it grants
that we state it repeatedly, but that the statement is never **unmissable**.

A boxed statement now sits immediately after Definition 1, before any result:

> **What passing this audit establishes.** Not compositional reasoning. Only
> that the measured performance exceeds a **prespecified, explicitly
> enumerated** family of lower-tier controls under the stated protocol. We write
> **F₃-complete** for the tier-3 verdict so the family travels in the name; it
> never means exhaustive structural completeness.

The prose sentence that previously carried this was absorbed into the box rather
than duplicated, so the cost is the box, not the argument.

## Change 2 (§16): the theory is scoped, and re-billed on what is measured

This is the round's one genuine tension, and it is worth naming: **round 10's
reviewer asked us to elevate the control-family theory; this reviewer says do
not oversell Proposition 3.** Both are right, because they are about different
objects: a measurement and its explanation, and the paper had been conflating
them.

Three changes:

1. **Renamed** to *"Resolution–retrieval tradeoff for complete feature
   representations"*, the review's own wording. "Resolution is anti-correlated
   with retrieval" read as a general law; it is not one.
2. **Scoped, in the body and again at the proof.** Next to the proposition:
   *the proposition is a result about the class of feature-support similarity
   protocols defined here, not about structural representations or retrieval
   metrics in general.* Appendix AN adds a paragraph enumerating exactly what it
   inherits from that construction: the similarity, the uniform feature
   weighting, the completeness of `g`, and what "syntactically distant" means,
   and states plainly that **its role is to explain a measurement, not to
   license one**.
3. **Re-billed on the measurement.** The abstract no longer says "our main
   theoretical result"; it says the finding is *measured, not assumed*, and
   gives the scope of the measurement: `M(φ_d)` is non-monotone in `d` **on
   three corpora, two algebras and both protocols** (poly8 and boolean8 under
   `UnseenEqClass`, poly8 / oneVarPoly13 / boolean8 under the composition
   protocol). The intro's contribution (1) reads the same way, with Proposition 3
   demoted to the explanation and Corollary 2 carrying the citation.

The substantive claim is unchanged and, we think, stronger: **if the proposition
were dropped entirely, the non-monotonicity would still stand as a measured
finding about F₃.** That is now what the paper says.

## Change 3 (§16): the matched-schema intervention, promoted

We took the review's framing of *why* it matters, which is broader than symbolic
mathematics, and put it in the introduction:

> **And the paper's cleanest experiment says the OOD axis is not the one the
> protocol names**: holding the held-out tree *byte-identical* and varying only
> whether its generating rewrite schema was in the training library changes
> identification accuracy — a benchmark can be "out of distribution" because the
> held-out form is structurally distant, or merely because the transformation
> that produced it was absent from training, and those are different claims.

We did **not** reorder §4. The findings run in the order the framework produces
them, and coverage is Definition 1's tier-4 clause, which only bites after tiers
1–3 are cleared. The promotion is by billing and by weight (§4.4 now carries the
new experiment below), not by moving a section.

## §17: the wrong-schema control, run as a full transfer matrix

This is the one experiment the review asked for, and we ran it larger than asked.
The review's version trains an encoder on a library containing a *wrong*
out-of-library schema and tests it on the held-out form of a different one. We
ran that control **for every schema against every other**, because the cost of
the matrix is almost the cost of the single control: an encoder is defined by its
*library* and can be scored against every schema's held-out set, so a
5-library × 4-held-out-set matrix costs **5 trainings per seed, not 17**. At 25
seeds that is 125 encoders and **107.8 min** (tag `r88`, `REPRODUCE.md` R24, new
Appendix AP).

The diagonal is §4.4's IN arm, every off-diagonal cell is the review's
wrong-schema control, and the schema-free row is the OUT arm, not a new baseline
but **`r59`'s own OUT arm**, same seeds and same code path, and the verifier
asserts its first ten seeds equal the shipped `r59` log *exactly* in both arms.
That anchors a new 25-seed matrix to the published 10-seed experiment instead of
inviting a cross-run comparison. Population is the **four universal** schemas,
measured at start-up rather than assumed, so every cell has the same `K=10`;
held-out trees are built once outside the seed loop, so a column's test items are
byte-identical across all five libraries; and every library holds the same number
of forms, so a contrast isolates *which* schema, never how much data.

**We pre-registered the reading of all four possible outcomes before the run**,
including the one that would have cost us a sentence: if a wrong schema helped
as much as the right one, §4.4's claim survives only as a *coverage* claim and the
abstract has to say so. The runner picks the verdict from its own pooled
contrasts before any prose exists, and the verifier pins it, so a rerun landing
elsewhere **fails** rather than leaving §4.4 describing an outcome the log no
longer shows. We also pre-registered the near/far pair: `scale_and_divide`
(*a → 2a/2*) and `triple_of_third` (*a → 3a/3*) are the same rewrite at a
different constant, `add_subtract` (*a → (a+a) − a*) is unlike all three.

**The result is `schema_specific`.** Pooled IN−WRONG is **+0.070 [0.021, 0.115]**
plain and **+0.033 [0.019, 0.046]** renamed, positive on its own interval in each
of the three columns with headroom, and IN−OUT is +0.094 [0.031, 0.139]:
replicating `r59`'s +0.061 at 2.5× the seeds. The pooled figure is conservative:
`add_subtract` is identified perfectly in every library and contributes an exact
zero. So the gain is not from having seen *one more* out-of-library
transformation; it is from having seen *that kind* of transformation.

**Two findings qualify it, and both ship, each pinned by an assertion so it
cannot quietly be dropped.** First, a wrong schema does help slightly on average
(WRONG−OUT +0.024 [0.006, 0.041]) but **that effect does not survive variable
renaming** (+0.009 [−0.016, 0.023]) where the schema-specific one does, and an
`add_subtract` library sits **at or below the schema-free row in every column**
(−0.096 / −0.036 / −0.036 / 0.000). Out-of-library *volume* is therefore not the
mechanism. Second, the specificity is at the level of the rewrite **family**, not
the schema: each constant-scaling schema transfers to the other almost completely
(near 0.452 / 0.364 against far means 0.290 / 0.276, themselves *below* the OUT
arms 0.296 / 0.284), and on the renamed `half_of_double` column **the diagonal is
not the maximum**; two same-family libraries read 0.464 and 0.456 against the
generating schema's 0.412. That last number is quoted *against* our own diagonal
story and asserted as an exact set for that reason. The wider three-versus-one
grouping is **post hoc**, "family" is our own descriptive grouping rather than a
formal equivalence, and Appendix AP says both.

So the sentence §4.4 makes is now stronger and narrower at once: **a training
library must contain a member of the held-out form's rewrite family, not the
rewrite itself.** The abstract carries that grain too (it had been billing the
result at the schema level, which the matrix has now shown is the wrong grain)
paid for inside the abstract, since page 1 has no slack either.

**Verification.** The construction is checked by **recomputation, not by flag**:
the verifier rebuilds all 40 held-out serialisations with an independent
pre-order traversal (deliberately not the runner's imported
`_apply_schema_at_root`) recomputes which schemas are universal from the corpus,
and re-checks every logged forced training form against the recomputed sets. That
last check is what the design's one new hazard needs: `r59` only had to stop a
forced form reproducing *its own* held-out form, but here each encoder faces
**four** held-out sets, so the guard must avoid their union or a wrong-schema cell
trains on its own test item. Clean: 0 collisions, 0 excluded cells, over all 40
library-equation pairs. `verify_claims.py` goes **1599 → 1663** assertions, exit 0
in all three copies, and **9 negative controls** were run against the new block,
each exiting non-zero on the *intended* assertion. The sharpest plants a
collision between a wrong library's training form and another schema's held-out
form **while leaving the runner's own `guard_violations` list empty**: only the
recomputation catches it, which is why the recomputation is there.

While adding this we found that **`r59` itself had no `REPRODUCE.md` row**, though
§4.4 has quoted it for three rounds. R24 now covers both runs, and records that
`r59`'s `--num_seeds` default is 25 while the shipped log is 10.

## §5: "control-complete through tier 3" is now qualified by construction

The review asks for the qualification "every time". Rather than repeat a clause,
we made the **term** carry it: Definition 1 introduces **F₃-complete**, and every
use site in the paper (the conclusion, Table 1's verdict row, the introduction,
and four sites in the appendix) now uses it. The definition says in the same
breath that it never means exhaustive structural completeness.

Measured: the built PDF contains **zero** unqualified uses. "Control-complete"
survives only inside the statements of Definition 1 and Proposition 2, where it
is the defined term and the family is named in the same sentence.

## §6: one causal formulation, and it is the review's

Three sites disagreed again (this drifted back after round 8 fixed it once), and
a fourth (the conclusion) asserted the causal direction with no intervention
named at all. All four now read as the review proposes: *under our
leave-one-schema-out intervention, including the generating schema in the
training library causally changes identification accuracy.* "Causal determinant"
appears **zero** times in the built PDF, appendix included.

## §7: the `UnseenEqClass` concession, made harder

The review is right that the metric measures clustering, not transformation
generalization, and that we only half-said so. §4.3 now says it outright, *the
encoder never identifies a class, only places its members together*, and, more
usefully, **Table 2 gains a row for the paper's own headline metric**, which it
had been omitting from the very instrument built to make this distinction:

| Result | Establishes | Does *not* establish |
|---|---|---|
| Unseen-class k-NN precision | clustering of unseen classes | generalization of transformations |

We also adopted the review's judgement about which experiment carries the weight:
the sentence now points forward to the composition test as the thing that speaks
to transformations.

## §13: the novelty defence, stated in the terms the objection is made in

Related Work's "What is new" paragraph now opens with the formulation the review
supplies, because it is harder to dismiss than ours was:

> **The contribution is not that controls detect shortcuts — that is established
> — but a criterion fixing what a held-out-form score can and cannot establish, a
> treatment of structural controls at the level of a *family* rather than a
> statistic, and a demonstration that applying it changes published
> conclusions.**

The (i)–(iv) list below it was compressed, since the new lead sentence had made
half of it a restatement.

## §15: the AI-use statement is shorter

The "why the disclosure is checkable" paragraph went from five sentences to two,
keeping the verifier argument and dropping the meta-commentary. The disclosure
itself is unchanged; the review asked for proportion, not for less transparency.

## §10, §11, §12: what we did *not* change, and why

- **§10 (don't oversell generality).** Already done in round 10: the abstract's
  first sentence scopes the framework to *"symbolic-expression representation
  benchmarks, not reasoning benchmarks at large."*
- **§12 (the five-finding narrative).** §4 already runs in that order. The
  review's Findings 3 and 4 are our §4.3's two paragraphs; we billed them as such
  rather than restructuring a section three rounds of reviewers have now read.
- **§11 (the paper does too many things).** We agree, and spent this round's page
  budget accordingly; see below. What we did not do is delete results earlier
  reviewers asked for.

## The page budget, since every addition had to be paid for

The main text was at **exactly 9 pages** with no slack, and it still is: the
Ethics heading is the first line of page 10, as before. The additions above cost
about 13 lines and the new experiment's four sentences another five. Every line
was paid for by removing **duplication**, and in each case the removed statement
is still checkable somewhere it is load-bearing:

- the introduction restated the abstract's standard **verbatim** (−3 lines);
- Related Work's (i)–(iv) list restated its own new lead sentence (−3);
- the composition construction detail and the boolean primitive enumeration are
  both already in the appendix and in `REPRODUCE.md` (−5);
- the φ_d paragraph justified the tier-3/tier-4 boundary twice (−1);
- §4.3's closure guard and its `+16`-token clause: both stated in Appendix AH, in
  `REPRODUCE.md` R16 and in the verifier, and its alternate-order clause, which
  is a **row of Table 3** two inches above the sentence;
- §4.2's two metric-audit figures, which the Ethics statement and both ceiling
  tables carry (the concession itself stays in the main text);
- the conclusion's `Scope.` clause, which stated the paper's thesis a **third**
  time, and §3.1's AI Feynman clause, which §4.1 states where it does work.

**Appendix pointer sites in the main text: 22 → 19**, including the new appendix,
against round 10's ≤20 target. Nothing that a previous round's reviewer asked for
was removed: Table 1, Table 2, the S-versus-F₃ split and the composition table's
stress-test rows all survive intact.
