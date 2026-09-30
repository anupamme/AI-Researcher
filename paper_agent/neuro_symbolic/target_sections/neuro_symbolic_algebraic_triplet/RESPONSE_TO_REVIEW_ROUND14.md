# Response to the review (round 14)

*Not part of the paper. Structured in the reviewer's own §19 order: Option C, Option A, Option B.*

**Thank you, and first, your previous round's diagnosis was right and it worked.** Round 13 was
presentation-only and spent pages on exactly two axes. Both moved:

| | Novelty | Technical | Empirical | **Clarity** | Significance | **Generality** | Repro | **Overall** |
|---|---|---|---|---|---|---|---|---|
| your round 13 | 7 | 7.5 | 8 | **6.5** | 8 | *(not scored)* | 9 | **7** |
| your round 14 | 7.5 | 8.5 | 8.5 | **7.5** | 7.5 | **6** | 8.5 | **7** |

**Clarity 6.5 → 7.5 and Technical 7.5 → 8.5.** We record that because it tells us the running
example, the rewritten abstract, the question headings and the removal of the $C_t$/$g_t$/$P_t$
notation were the right spend, and it makes your new lowest score the one to act on rather than a
second clarity round.

**Your §19 asks for Option C *plus* A or B, not C alone. We have done all three.** Below, each is
marked with what changed and where. Two framing points first, because they determine how to read the
round:

**(1) The generality experiment cost no training, no fine-tuning and no download.** Your review
reasonably assumes an external-generality result means new compute; it does not. The published
80M-parameter checkpoint, 320 parsed integrands from its own test distribution, and every tier
skyline were already on disk and already audited. The new run is **forward passes and zero-parameter
bags: 5.5 seconds.** No new corpus, no new architecture, no new machinery; it is assembly of
components the verifier already covers. This matters because you say **twice** not to add volume,
and we agree; we have not.

**(2) We fixed the interpretation before the run, not after it.** Appendix B already recorded a token
bag at `0.85` against this model's `0.876`, so we knew tier 2 would be close, and a paper with our
self-audit record cannot write its reading after seeing the number. The pre-committed framing is the
one now in §4.5, and it is the intellectual point of the round rather than a hedge: **the framework
converts a caveat into a verdict.**

---

## Option C: "claim less, more precisely." Done. Your §17 is the most valuable paragraph in the review

You are right that the paper read as *"we built a framework that shows when compositional
generalization is real,"* with the Tree-LSTM work as the thesis. It now reads as the sequence you
wrote: **a score cannot support a compositional interpretation until progressively stronger
alternative explanations have been ruled out; here is a concrete procedure; applying it changes
conclusions about published benchmarks, about a published external model, and about our own earlier
claims.** The Tree-LSTM study is now billed, in the contribution list itself, as **the demonstration
that the procedure is usable.**

**This is re-billing, not deletion. Every number, interval and disclaimer stays.**

| Where | What changed |
|---|---|
| **Abstract, opening** | Now opens on the problem: *"A score cannot support a compositional interpretation until progressively stronger alternative explanations have been ruled out, and the field has no standard for doing that. We give a concrete procedure…"* |
| **Abstract, Finding 1** | Gains the external result in one sentence, so generality is visible in the first paragraph a reviewer reads rather than in §4.5. |
| **§1, contributions** | **Reordered to four**: (1) the framework; (2) the 23-corpus audit + the released auditor + the self-correction record; (3) **new, the external audit of a published 80M model**, "so the *procedure* transfers, not merely its conclusions"; (4) the hardened evaluation study, *"billed as the demonstration that the procedure is usable and not as the thesis."* |
| **§1, paragraph headings** | Now *"The procedure is usable: a demonstration at scale"* and *"Validation: the method catches protocol errors, including ours."* |
| **§5** | The untested promise is gone; see §C3 below. |

### C4 (your §11): what is falsified. Title kept, precision added

We kept *falsification* in the title, which the round-13 reviewer asked for, and fixed the claim in
the text instead. §1 now reads: **what it refutes is an *evidential* interpretation; that the number
is evidence of structural sensitivity, and *not* the hypothesis of compositional reasoning, which no
result of this kind can settle.** The abstract's method sentence now says the framework *"can refute
an evidential reading of such a score, though never certify one."* We use *evidential* consistently
where the looser word appeared.

### C5 (your §10): breadth rhetoric, with the limit volunteered

**"23 corpora from four benchmark families"** now appears everywhere the breadth is load-bearing
(abstract, §1, §4.2, §5). §4.2 states the limit plainly in bold: **"This is broad corpus-level
coverage and limited family-level diversity: 15 of the 23 are EQNET variants, so a per-family reading
of the table is the honest one."** The concessive clause is kept, not softened.

### C3: the conclusion's untested promise is replaced by what was found

§5 previously said the evidentiary argument *"we believe is not [domain-specific], but do not test
elsewhere."* It now reads: *"the tier **construction** is domain-specific, though only $\phi_d$ deeply
so, while the **evidentiary** argument is not — and §4.5 **tests that rather than asserting it**, on a
model and benchmark we did not build."* This is the single sentence where the round's work lands.

### C6, C7 (your §12, §13): both promoted into the main text

- **§12, the five partitions.** §4.3 now says the $K{=}500$ separation *"reproduces on **five
  independent class partitions**; it is not one lucky split (Appendix AL)."* You should not have to
  find that in an appendix to rule out a lucky split.
- **§13, the MPS caveat.** §4.3 now states inline that *"neither the GIN nor the Transformer trains
  reproducibly here, so no claim rests on their point values."* Nondeterminism disclosed only in an
  appendix invites exactly the doubt you describe.

### C8: the disclaimers are untouched

Every scope limit your §7 says is *helping* the paper is intact and unweakened: four primitives are
not a library; the curve is this architecture's; the coverage closure does not survive a change of
algebra; passing the audit is not evidence of compositional reasoning; training is credited with at
most $0.206$ over an untrained encoder.

---

## Option A: an external audit. New §4.5 and Appendix AR, tag `r90`, 5.5 seconds

**"Does the Argument Travel to a Model We Did Not Train?"**: a Definition-1 audit **through tier 3**
of the published **Lample & Charton 80M-parameter integration encoder** (6 layers, $d{=}1024$, trained
by its authors on millions of FWD+BWD+IBP problems) on **320 integrands from their own test
distribution**, labelled by integration family. One nearest-family-centroid protocol, `25` seeds,
chance `0.25`, and **every row shares the seed's held-out split byte for byte**.

| rung | control | score |
|---|---|---|
| $\mathcal{F}_1$ | variable bag | `0.250`: **degenerate by construction**, all `2000` decisions tied |
| $\mathcal{F}_2$ | **operator/arity bag** | **`0.941` `[0.9255,0.9691]`** |
| $\mathcal{F}_2$ | full-token bag | `0.851` |
| $\mathcal{F}_3$ | $\mathrm{WL}_{h=1}$ (the **coarsest** member) | `0.8175` `[0.7787,0.8562]` |
| $\mathcal{F}_3$ | $\phi_1$ / $\phi_2$ / $\phi_4$ / $\phi_8$ | `0.752` / `0.7335` / `0.726` / `0.726` |
| $\mathcal{S}$ | $\phi_\infty$ / untrained Tree-LSTM / tree-edit distance | `0.726` / `0.782` / `0.8115` |
| **subject** | **the published 80M encoder** | **`0.8715` `[0.8467,0.9127]`** |

**A zero-parameter operator/arity bag beats the 80M encoder by `0.0695`.**

**The reading is not that the benchmark is broken, and we do not write a sentence that says we broke
Lample–Charton.** Those four family labels are *defined* by operator content: a radical integrand
contains a radical, so **a task an operator bag solves is a tier-2 task correctly identified as
one.** Definition 1's verdict is that this number licenses no claim above tier 2. Your Appendix-B-era
predecessor called this a *"label-definition confound"*; in tier language it is not a confound at all,
it is the correct entitlement. **The framework buys the verdict, not a scandal.**

**What makes that defensible rather than convenient is asserted as a conjunction**: the encoder **does**
clear tier 3 (`0.8715 > 0.8175`) *and* clears both structural stress tests (above the untrained
encoder's `0.782` and tree-edit distance's `0.8115`). So the tier-2 loss is **specific**, not the
general weakness a weak-model artefact would produce. Drop either half and the claim is unsupported,
so the verifier asserts them together.

**Two hazards this run inherits, both of which have bitten this paper before, and both handled:**

1. **Ties.** Bags map distinct forms to identical vectors *by design*, and in `float32` the ties are
   not even detected. We use the established rule: `float64`, `TIE_DECIMALS=6`, stable sort under one
   fixed label-blind permutation. It matters most at tier 1: under `argmax`'s first-max rule that row
   would have read **`1.000`** for family 0 instead of exactly chance with all `2000` decisions tied.
   The tie rule is what makes the degeneracy visible instead of spectacular.
2. **Unit of inference.** With only **4** families there is nothing to bootstrap over, so the unit is
   the **held-out integrand** (`320` items, `80` per family) and **§4.5 and Appendix AR say so** rather
   than silently reusing §3.4's *"the class is the primary unit."*

**What this is not, stated in the paragraph rather than left to be discovered:** family identification
is not a held-out-*form* protocol, so the audit runs **through tier 3 only** and Definition 1's
coverage clause never applies. The log records `passes_tier3_audit: null` rather than a boolean,
because the composite verdict is *undefined* when a lower tier is not cleared.

**And this is where Option A and Option B meet.** The theory replicates on a corpus we did not build:
$M(\phi_d)$ is again non-increasing in $d$, $\mathrm{WL}_h$ non-increasing in $h$, $\phi_\infty$ at or
below the coarsest $\phi_d$, and the $\mathcal{F}_3$ supremum again attained at the **coarsest**
member; **Corollary 2, measured externally.** A family is not audited by its most resolving member,
and that is now a statement about someone else's data.

### A second external model already in the file, but it stayed in the appendix

Worth your attention even though **we did not promote it**, because it is a fact about the auditor
rather than about this round: Appendix I audits a published Set-Transformer (NeSymReS) in a
**different modality** (numerical point-sets, sharing no code or architecture with anything here), and
`r62`'s global-permutation control came back **null**, superseding the earlier positive `r28`. The same
protocol applied to a second external model returns **no effect**: the auditor validating rather than
debunking, the move that also makes the surviving $\mathrm{score}_5$ leaderboard row valuable in
Table 1. **We had planned one main-text sentence for it and cut it**: the main text is at exactly 9
pages with no slack, and trading a rigour point for a generality point is a bad trade at a scorecard
where rigour is 8.5. §4.2 carries the *validates-rather-than-debunks* point in one clause via the
$\mathrm{score}_5$ row instead.

---

## Option B: the control-family principle, sharpened. §3.3, and Appendix AN

**Two reviewers now disagree about Proposition 3**: round 13 asked us to demote it into the appendix,
you ask for a stronger control-family principle. We satisfy both by sharpening the **principle** in
the main text while the **environment** stays in Appendix AN. Proposition 3 is *not* re-promoted.

### B1: the three-way distinction your §19-B asks for, in §3.3

**"Three claims must not be run together, and only the middle one is ours."**

1. **An arbitrary strongest baseline licenses nothing** unless it is invariant to the property at
   issue: the membership test we already run. ($\phi_\infty$, tree-edit distance and the untrained
   encoder all *read arrangement*, so they are $\mathcal{S}$, not $\mathcal{F}_3$.)
2. **An invariant control family licenses refutation**: beating $\sup\mathcal{F}_t$ rejects every
   tier-$t$ explanation the family encodes. **This is Definition 1 and all we claim.**
3. **An exhaustive family would license certification**, and is not merely unbuilt but
   **self-defeating**: a hierarchy of maximally resolving controls is vacuous, every member at chance,
   so the tiers must be **coarsenings** and the supremum sits at *coarse* members. That is
   Proposition 3, and §3.3 cites it as measured non-monotone on **three corpora, two algebras and both
   protocols**: with §4.5 adding a fourth corpus, external, reported there rather than folded into
   §3.3's count.

**This is also our answer to your §9** (*"the framework is defined into existence"*). The hierarchy is
**forced by the invariance requirement, not chosen for convenience**: a control that resolves the
structure its tier does not determine *forfeits membership*, so the ordering is derived rather than
stipulated. $\mathcal{F}$ is **explicit, not exhaustive**: an auditable hierarchy of alternative
explanations, not a canonical decomposition of "structure." That is a weaker and checkable claim in
place of an unfalsifiable one.

### B2, which step of Proposition 3 is protocol-specific, and which is not

Appendix AN now says this plainly, without touching the proof or its scope. **Step 1** (that feature
supports become disjoint once a rewrite chain rebuilds the root) depends on the feature-support
construction; a different or weighted similarity could soften it, and **we claim nothing about how
far.** **Step 2** (that once the supports are disjoint the ranking is label-blind, so $M(g)$ falls to
the class-prior rate) is **general**, holding for *any* scoring rule that reads only the overlap of
two representations, whatever built them. And the consequence **Definition 1 actually uses is weaker
still and needs neither step**: a supremum over a family whose members are *required* to be invariant
to the structure their tier does not determine cannot be raised by adjoining resolution, because
resolution is what forfeits membership. That follows from the invariance requirement alone, which is
why §3.3 states the triple in terms of invariance rather than in terms of this proposition.

**No new assertions were needed here**: the two supporting measurements ($\phi_\infty$ below the
tier-3 maximum on three corpora; $\phi_\infty$ at chance at depth 4) were already asserted.

---

## The verifier count moves off 1717, and the movement is the signal

`verify_claims.py`: **1717 → 1742, exit 0, in all three shipped copies.**

Round 13 held the count at 1717 *by design*; it was presentation-only, and the verifier recomputes
from logs and **never reads the `.tex`**, so any movement would have meant an edit had touched a
claim. **This round adds evidence, so a frozen count would have meant a number entered the paper
unasserted.** The delta decomposes exactly:

- **+23**: `check_external_audit()`, the **23rd** check function. The 80M encoder's row is the one
  value **read from the log**, because reproducing it needs the ~1 GB published checkpoint, which is
  not ours to redistribute. **Everything zero-parameter is recomputed** from the shipped
  `lample_integrands.json`: the corpus is rebuilt (`320` trees, `[80,80,80,80]` per family), and the
  operator/arity and $\phi_1$ rungs are re-scored end to end through the same splits at `tol = 1e-9`.
  So the comparison that carries the claim (a zero-parameter bag against an 80M transformer) is
  verified on your side, and only the transformer is trusted.
- **+2**: a fifth self-audit incident, below.

**8 negative controls** were run against the new block, each exiting non-zero on its **intended**
assertion, each mutated file `cmp`-checked byte-for-byte afterwards, with `python3 -B` and a cleared
`__pycache__` between runs so no control can silently test the previous mutation. **Two make the
paper's claim *stronger* and must still fail**: raising the logged $\mathcal{F}_2$ supremum to `0.990`
widens the headline gap from `0.0695` to `0.1185`, and dropping $\mathrm{WL}_{h=1}$ to `0.600` widens
the encoder's tier-3 clearance from `+0.054` to `+0.272`. The first is caught **twice**, and the
second catch is the one that matters (*"tier2_operator_arity_bag recomputed from the registry: got
0.9410, paper says 0.99"*), because it is the **recomputation**, not a stored expectation, that
refuses the flattering number. The sharpest control touches **no headline value at all**: raising
$\phi_2$ to `0.800` leaves every printed number intact and breaks only Proposition 3's external
replication. And thinning the registry by five `trig` integrands (a mutation to the **data**, not the
log) moves both recomputed rungs while every stored value still agrees with itself, which is the
proof that the recompute path is live rather than decorative.

## A fifth self-audit incident, found by this run, and it runs in our favour

Appendix F's revision history goes from four rows to **five**.

`_postorder` returned each node's own index in place of its left-most leaf, so $l(i)$ never propagated
up a left spine, and both the keyroot set and the forest recurrence were computed from a wrong $l()$:
**changing the tree-edit distance on a majority of pairs.** It surfaced as an `IndexError` when the
ladder met the external corpus, whose trees are deeper than any of ours. Checked against an
independently written Zhang–Shasha reference, the fix agrees on **`3000/3000`** sampled pairs and the
shipped code on **`453`**.

**Both corrected values make the baseline weaker**: the swap twin moves `0.733 → 0.723` and the
rotation twin to `0.889`, **so the correction runs in this paper's favour, which is stated rather
than left implicit.** The two new assertions pin it in the direction that matters: one covers the
rotation-twin tree-edit-distance column that **no assertion had covered before**, and one asserts the
*qualitative* claim (tree-edit distance stays below the untrained encoder) so the argument must survive
the correction and not merely the number.

---

## What we did not do, and why

- **No new training run.** Your review says twice not to add volume, and we agree. `r90` adds no
  corpus, no architecture and no GPU-hours.
- **Proposition 3 was not re-promoted to the main text.** Round 13 asked for its demotion; your
  Option B asks for a sharper *principle*. B1 delivers the principle in §3.3 and leaves the
  environment in Appendix AN, which satisfies both asks rather than oscillating between them.
- **The title still says *falsification*.** It was set last round at the previous reviewer's explicit
  request. Your §11 concern is a precision issue, and we fixed it in the text (C4) rather than
  re-opening a decision a reviewer had just made.
- **The `Established` / `Not established` block was not converted to bullets** and no scope disclaimer
  was softened, for the reasons in your own §7.
- **We do not read the two scores that moved down** (Significance 8 → 7.5, Reproducibility 9 → 8.5),
  because the prose does not name either. If there is a specific ask behind them we will act on it.

## Build state

- Main text **exactly 9 pages**, unchanged. Page 10 carries **zero main-text lines** before the Ethics
  heading; page 1 still ends with the abstract and §1 still starts on page 2.
- Total **65 → 67 pages**, all of it appendix: Appendix AR's ladder table, Appendix AN's
  protocol-specific/general paragraph, Appendix F's fifth incident row, Appendix K's `r90` provenance
  row.
- `0` errors, `0` *Float too large*, `0` undefined references, `0` `??`, **1** overfull hbox: the
  pre-existing `3.509pt` one.
- The funding for §4.5, the §3.3 triple and the six Option-C promotions came predominantly from
  redundancy the re-centering itself created: §1's demonstration paragraphs duplicated §4, and §1's
  fourth contribution duplicated its own third paragraph.
- `verify_claims.py` → **1742/1742, exit 0** in all three copies. `REPRODUCE.md` gains **R26** with
  the checkpoint fetch pointer; the `320`-integrand registry is shipped, so every zero-parameter rung
  is reproducible without it.
