# Response to review: round 18

**Summary: you named exactly two things, and both are in the paper. §21B (the one experiment, if
there is compute for only one thing) is `r93`: depths 1–8, systematic leave-one-primitive-out, and the
leave-one-composition-family-out arm the earlier design could not express, 183.5 min of GPU, 5 seeds,
one paired class set. §21A (the formal subsection *Why This Is Not Merely a Control Task*) is
§3.4, in your own formulation.** The new experiment also **cost us a printed claim**: the abstract's
"an order of magnitude", inherited from the depth-4 numbers, does **not** survive at depth 8 and has
been withdrawn and corrected to `3.3×`. We report that here rather than let you find it.

**The verifier count moves, 1843 → 1928, exit 0 in all three copies**, and `statements.tex` prints the
new number. **Main text is still exactly 9 pages**, `E THICS S TATEMENT` first on page 10.

Sections below follow your numbering.

---

## §8: "the central theoretical claims follow almost directly from the definition of an admissible control; the methodological novelty over established control-task/shortcut-learning methodology is unclear." **Answered twice: a subsection that states the boundary, and a table that draws it.**

This is the sentence that would sink the paper, so it gets both halves of your §19/§21A ask.

**§3.4, *Why This Is Not Merely a Control Task*** carries your formulation nearly verbatim: a control
task establishes that a representation does or does not carry a signal beyond a randomized comparator;
**it does not establish that the comparator is invariant to the property whose presence is being
inferred, and it supplies no family-level supremum**. Then the three consequences that are ours, each
measured rather than argued:

- **(i) Admissibility is a *test*, not a judgement of strength.** A comparator enters `F_t` only by
  scoring **exactly `0.500` per instance** on the shape-matched twin. Five structural descriptors *you*
  named were admitted that way; three refinements failed the same test and were refused. `r92` runs it,
  and it ships with a control that must fail.
- **(ii) The audit statistic is a *supremum over the family*, never a baseline**: refinement either
  preserves invariance, in which case the refined control is inside the family and already dominated,
  or forfeits membership (Proposition 2).
- **(iii) Hence admissible strength can *fall* as resolution rises**, and it measurably does on every
  replication we ran. **A protocol that reported its strongest probe would report the wrong number**,
  which is precisely what a control task cannot tell you.

We accept the premise you are pressing on: the propositions *are* near-immediate given the definition.
§1 now says so in the sentence where a reader decides what the paper claims: *"the propositions of
§3.3 are the language that makes this measurable; the measurement is the contribution."* The novelty
claim rests on (iii) being **false-able and false-in-the-obvious-direction**: nothing in the prior
methodology predicts that a *more* refined structural probe is a *weaker* admissible control, and we
measure that inversion on three corpora, two algebras, both protocols, five independent class
partitions, and a published 80M-parameter model we did not train.

## §19: the comparison table. **Table 1, and it replaced prose rather than adding to it.**

| Prior device | Question it answers | What it leaves open |
|---|---|---|
| shortcut baseline | is the *benchmark* solvable without the model? | which alternative explanations of the model's score remain |
| control task | does the *representation* carry a signal? | whether the control is *invariant* to the property inferred |
| strongest baseline | can the model beat a sophisticated comparator? | whether that comparator is admissible as evidence at all |
| held-out split | does performance transfer? | what interpretation the transfer licenses |
| **this paper** | **is the comparator admissible, and what does clearing an explicit *family* license?** | |

It absorbed §2's *"What is new, given all of that"* paragraph, so it is paid for.

## §10, §21B: "the biggest weakness of the empirical story: four primitives, 200 classes, depths 1–4." **`r93`: depths 1–8, three held-out conditions, one paired class set.**

This is the third review to name the composition design. It is now the round's only compute.

**Depth 8 is the corpus's ceiling, not our budget, and we show the arithmetic.** `poly8` admits five
rewrite primitives and only four can repeat: `_rw_reassoc` and both removal schemas fire on `0/1102`
anchors, and `_rw_distribute` fires on `71` of `300` measured anchors but has two or more *distinct*
delta-matched sites on **`0`** of them. So depth 8 is bought by allowing each of the four locals **twice
at distinct sites**: a change to the chain builder, not to the corpus, and `equivalence.py` is
untouched, so no published number can move. `305` classes scanned, `200` kept, and the set is asserted
**identical across all four training depths, all four leave-one-primitive-out arms and all three
family arms**, so every comparison is paired.

**Size matching is order-invariant by construction**, which is what makes the new arm a contrast in
arrangement alone: the depth-8 delta is **`+32` tokens for every class in every arm**, all `1600`
class-depth pairs equal their own primitive sum, and the verifier **recomputes** this from the stored
per-class counts rather than reading the runner's flag. `2520` orders are possible; **`188` distinct
chains are realised over the `200` classes and at most `3` classes share one**: stated rather than
rounded up to "each one distinct".

**Result: the pre-committed branch that occurred is (1), written into the module docstring before the
run.** Trained on **single** applications only:

|  | d=1 | d=2 | d=4 | d=6 | d=8 |
|---|---|---|---|---|---|
| singles only (never composed) | .997 | .983 | .905 | .841 | **.736** |
| depth-8 composites in library | .995 | .989 | .979 | .961 | **.936** |
| twin, singles only | .998 | .984 | .959 | .921 | **.876** |
| strongest non-learned (bag) | .105 | .115 | .100 | .100 | .100 |

`0.736 [0.693,0.777]` at depth 8 is `147×` chance and `7.4×` the strongest zero-parameter method.

**Three kinds of novelty, and they cost in that order.** An unseen **arrangement** (an ordered
adjacent pair of primitives occurring in *no* training chain, every primitive still trained
individually *and* in composition) costs `+0.012`, and **all three intervals cover zero**. Never
having **composed** costs `+0.200 [0.163,0.237]`. A primitive held **out of the library** costs
`+0.664`. Training buys invariance to *arrangement*, much of it to *depth*, **none** to the primitive
inventory.

**What this cost us, stated plainly.** The gap between depth and inventory is only **`3.3×`** at depth
8, not the *"order of magnitude"* the abstract claimed from the depth-4 numbers. **That sentence is
withdrawn.** The order-of-magnitude gap turns out to belong to *arrangement* (`54×`), which is a
sharper claim and a different one, and it is the one now in print. Two further results cut against our
earlier reading and are printed anyway: holding out `commute` is the **cheapest** of the four, so the
primitives are not interchangeable in difficulty; and the depth cost's interval **excludes zero**, so
§4.2 now says training buys *much* of the invariance to depth rather than invariance outright.

**The length reading is ruled out rather than argued away.** A depth-8 form is ~3.5× its anchor, so we
added a **per-depth shape-matched twin** (evaluation-only, no extra training): the true composition
against a non-equivalent partner matched on token multiset, operator multiset **and** tree-local shape.
It holds `0.876` at depth 8. Every order-*blind* bagger is pinned at exactly `0.500` at every depth,
and (the part that makes the pin interpretable) the two order-*sensitive* extensions are strictly
above it (`0.610`, `0.560`), so `0.500` is a passed test rather than a task nothing can score on.

**Three disclosures the prose does not lean on**, all in Appendix AU: past radius 3 the closure
certificate is **4 applications, not the declared depth**, and **all `40`** sampled searches hit the
frontier cap, so beyond `d=4` it is the search-free token bound that carries the certificate; we
claim the independently certified floor at `d>4` is four rewrites, and the verifier asserts the
sequence `1,2,3,4,4,4,4,4` so it cannot be quietly upgraded. The `0.100` non-learned row is a **tie
floor**, not a structural cue, and we quote it against ourselves anyway; the strongest *structural* bag
is tree-local at `0.035`. And the arrangement result rests on **three** bigrams, not twelve, chosen by
frequency so each has >100 member classes.

## §11: "the composition result is entangled with the Tree-LSTM's inductive bias." **Conceded in print, and now quantified at depth 8.**

We claim no architecture independence and **treat that as a finding**: the conclusion says the curve is
the Tree-LSTM's, the abstract reports a GIN and a Transformer decaying `3.3×` and `6×` further, and
§4.5 is a GIN that clears the unseen-class criterion and sits at **chance** on the twin. What `r93`
adds is that the *shape* of the entanglement is now measured over eight depths rather than four. We do
not claim the depth curve generalizes across architectures, and we say so where the curve is printed.

## §13: "make the scope limitation prominent." **Moved to where the claim is made, not where it is qualified.**

§4.2, in the sentence that states the constructive result: *"the constructive claim is scoped to
`K≥200` on this corpus and design"*, intervals **overlap** at `K=50` and `K=100`, explicitly *not*
partition-independent, and separate cleanly from `K=200` on.

## §14: the external audit's prominence. **Verified, not changed.**

Round 17 folded it into §4.3 as a closing paragraph; it is still there, still a paragraph, and the
eight cross-references still resolve (the label rides in that subsection). We did not re-promote it.

## §16: reorder the contributions. **Done: methodological → empirical → practical → demonstration.**

The paragraph now opens with the ordering by name, and (4) is billed explicitly as *"evidence the
procedure is usable, not the thesis"*. It is a rewrite, not an addition.

## §17: Figure 1 as the visual centerpiece. **One forward pointer, in §1's opening sentence.**

*"Figure 1 is that framework in one picture and is the place to start."* The figure is unchanged.

## §22: the causal sentence. **Both sites.**

Abstract and conclusion now read: *"the controlled intervention — the held-out tree **byte-identical**,
library membership the only variable — identifies training-library coverage, not composition depth, as
the dominant axis governing the observed transfer."*

## §12, §5, §18: the baseline-weakness thread. **Nothing re-run.**

You wrote *"I would not worry about baseline weakness anymore"*; we took that at face value and spent
the round's compute on §21B instead.

---

## Reproducibility

`r93` ships with **13 negative controls** (`negctl_r93.py`, included), each required to exit non-zero on
the *intended* assertion, with the log restored **byte-for-byte** and `filecmp`-compared afterwards.
**Three flatter the paper and must still fail**: lifting the depth-8 identification to `0.980`, zeroing
the arrangement cost, and lifting the depth-8 twin to `0.990`. **One is the inverse and must pass**:
corrupting the runner's own stored `2520` changes nothing, because the verifier recomputes the
multinomial. **One had to be redesigned rather than accepted**: relabelling a member class's chain by
*sorting* it removed the held-out bigram but also broke the prefix deltas, so the size-matching guard
fired instead of the arrangement guard and the control would have passed for the wrong reason; it now
exchanges two primitives of equal token cost, leaving the multiset and every prefix delta untouched.

`REPRODUCE.md` **R29** gives the command, the runtime and the expected output. The verifier makes
**1928** assertions, exit 0 in the working tree and both shipped copies.
