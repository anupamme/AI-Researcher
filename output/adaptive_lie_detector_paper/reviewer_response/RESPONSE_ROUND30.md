# Response to Reviewer (6/10, Weak Accept, confidence 4/5) — the generalizability round

> **DRAFT — not yet sendable.** Two things in it are not true yet, and are marked where they appear:
> three of the seven panel cells are still running (§2's table says *(running)*), and the five-site
> disclaimer retirement in §2 and row 4–5 of §6 is written but not yet applied to the manuscript. It is
> committed in this state so the letter and the edits are reviewable against each other. Remove this
> banner only when the panel table has seven scored rows and `verify_r30.py`'s five-site transaction
> guard passes.

**Read §0 first.** It is not a rebuttal; it is a dating exercise, and it changes what the rest of this
letter has to argue.

---

## §0. Provenance: which build you read, and what that means for your list

You told us exactly which file you read:

> *I reviewed the latest version I could find, `main(20260916-074428).pdf`, rather than the earlier
> September versions.*

That stamp is 2026-09-16 07:44 UTC = 13:14 IST, which is commit **`5229949`** (2026-09-16 13:10 IST,
*"Table 1: report Family E's 1/5 in the roadmap, at net-zero page cost"*). **HEAD is now `2d8b22e`,
19 commits later, spanning revision rounds 22–29.**

You were right that it was the latest version you could find. Three checks confirm which build it was,
each independent and each verifiable from the repository:

| # | Evidence | At `5229949` | At HEAD |
|---|---|---|---|
| 1 | You quote the title *"Lie Detection or Instruction Following? Identifying What LLM Deception Benchmarks Actually Measure"* | `main.tex:48`, verbatim | `main.tex:47` reads *"What Does Lie-Detection Accuracy Measure? An Identification Audit of Behavioral LLM Deception Benchmarks"* |
| 2 | Your **Priority 1** quotes the abstract string *"five criteria required before accuracy licenses a deception claim"* | present | **removed** (`01f01a2`, *"drop the 'all five criteria are necessary' overstatement"*) |
| 3 | You refer to the evidence ladder as **"Figure 3"** | Figure 3 | **Figure 2** |

**To be exact about the direction of this, because it matters: every item you raised was accurate about
the build you read, and none of it was already fixed at the time you wrote it.** Your read is 09-16
13:10; the commit that removed the sentence in Priority 1 is 09-18 10:01, two days *later*. The revisions
below happened **after** your review, not before it, in rounds prompted by your review and by other
reviewers converging on the same points.

So the purpose of this section is narrow, and it is not "you missed something." It is: **the build you
were given is 19 commits behind, so eleven of your items now read as open when they are closed.** If we
answered your list without dating it first, the closures would look like evasions.

### The eleven items addressed since your read

| Your item | Status at HEAD | Addressed in (all *after* your read) |
|---|---|---|
| **P1** Fix the "all five criteria are necessary" claim | **Done.** Current wording is materially your own recommendation | round 27 |
| **P2** Make the evidence ladder a central contribution | **Done in substance** — `fig:ladder`, its *"rung 4, not rung 5"* node, named as one of three spine objects | round 29 |
| **P3** Narrow the criterion-4 headline | **Done** — abstract says *target-dependent deception-associated signals* | round 26 |
| **P4** Promote the adverse surface finding | **Done, and stronger than asked** — EXP-AE *withdrew a positive* at p_Holm = 0.0005 | round 28 |
| **P5** Four experiments, ~15-minute read | **Largely done** — −151 words of main text, six Q-tagged subsections, roadmap demoted | round 29 |
| **§15.2** "dominant paradigm" overreach | **Done** — zero occurrences; changed to "common" | round 28 |
| **§15.3** "deception-associated at fixed elicitation" | **Done** throughout | round 26 |
| **§15.4** Criterion 4 is not one of five equals | **Done** — A/B/C groups, ■ vs □, *"different in kind"* | round 27 |
| **§15.5** Existence demonstration, not generality | **Done** — *"not an estimate of the prevalence or reliability of deception detection"* | round 26 |
| **§8** "none of the audited public materials" | **Done** — a verifier check now forbids the generalizing forms | round 29 |
| **§10** Novelty as operationalization | **Done** — near-verbatim in abstract and conclusion | round 28 |

Everything below is about what your review still asks for **after** that subtraction. There are three
things, and we did all three.

One further consequence worth stating: because eleven items were closed in the two days after your read,
the sub-scores that motivated them were assigned against a paper that no longer exists. The one axis that
is **not** in that position is **generalizability 5** — nothing in rounds 22–29 addressed it, your four
stated grounds for it were all true at HEAD as of yesterday, and it is therefore the axis this round
actually had to earn rather than merely re-present. That is why §2 is the longest section of this letter.

---

## §1. Your §12 framing, adopted as the paper's own thesis sentence

The most useful thing in your review is not in your priority list. It is in §12, where you propose the
headline:

> *instructed-lie benchmarks measure a heterogeneous mixture of instruction-following, surface
> behavioral markers, knowledge conflict, and sometimes deception-associated behavior; even after
> removing the instruction confound, the remaining signal is not stable across targets and is often
> itself explainable by simple surface behavior.*

**We had every clause and had never written the sentence.** Criteria 1/2/3 *are* instruction-following /
surface markers / knowledge conflict, and each is already measured. So this is a synthesis over evidence
already in the paper, adding no new claim — which is why we could adopt it verbatim in substance and at
zero page cost. It is now on p3 of the introduction, immediately before the *What we do not establish, in
plain terms* paragraph — so the reader gets the characterization, then its caveats, then the master
one-sentence summary, which we deliberately left as the last line of the introduction because your own
test for it was whether the argument can be stated from memory:

> **What the accuracy aggregates**: **a heterogeneous mixture** — instruction-following
> (equalization takes 97.0% to 43.3%), surface correction markers (a parameter-free 14-pattern rule
> reaches 69–80% with nothing fit), a component *consistent with* knowledge conflict (70.0% KNOWN vs.
> 57.6% UNKNOWN, p = 0.0045, stratified observational), and *sometimes* deception-associated behavior
> (one of five targets, at byte-identical elicitation) — **and once the instruction confound is removed,
> what remains is neither stable across targets nor cleanly separable from surface behavior.**
> Criteria 1–4 test these one at a time; **no one of them by itself is deception detection, and an
> accuracy figure does not say which it is measuring.**

One deliberate weakening of your wording: you wrote *"knowledge conflict"* flatly; we write *"consistent
with"* and mark it *stratified observational*, because that arm is not randomized and we do not want the
sentence to claim more than the design supports.

---

## §2. Generalizability 5 — the frontier-scale panel (EXP-FS)

This is the round's real work, and it exists because **the paper's own appendix asked for it.** Before
your review, `app:frontier_preliminary` carried two frontier cells, marked *"Preliminary observations,
not findings,"* excluded from every headline, with this limitation stated in the paper's own words:

> *the two targets differ on multiple confounded axes (closed/open weight, dense/MoE architecture, RLHF
> recipe); the panel is insufficient to attribute any observed pattern to a specific axis.* … *A third
> frontier model from a different organization (e.g., GPT-4o, DeepSeek-V3) would break at least one
> confound; this is a limitation of the current design.*

Your generalizability score rests on four grounds — mostly open-weight, English, instructed-roleplay, and
a target-dependent fixed-elicitation effect. A frontier panel attacks three of the four at once. So we
pre-registered one and ran it. **The ordering is checkable, not asserted:** `docs/PREREG_EXP_FS.md` was
committed at `4338fe7`, 2026-09-18 **18:24**; the earliest result file in the entire panel is
2026-09-18 **19:49**. Every cell postdates the frozen design by construction, and a verifier check now
asserts this from the commit graph rather than from our word. The design: **seven targets from seven organizations, n = 100 each, one byte-identical neutral system prompt in
both conditions, no target ever instructed to lie**, with Claude Haiku 4.5 held fixed as interrogator and
extractor so extractor family is a constant rather than a confound.

### Result

| Target | Organization | Weights | Arch. | Parameter-free rule | Transferred pipeline |
|---|---|---|---|---|---|
| Claude Sonnet 4.5 | Anthropic | closed | dense | **84.8%** | 50.5% |
| Amazon Nova Pro | Amazon | closed | undisc. | **80.0%** | 56.0% |
| Llama 4 Maverick | Meta | open | MoE | **83.0%** | 45.0% |
| DeepSeek-V3 | DeepSeek | open | MoE | **87.0%** | 40.0% |
| Mistral Large 3 | Mistral AI | open | MoE | *(running)* | *(running)* |
| Qwen3 235B-A22B | Qwen | open | MoE | *(running)* | *(running)* |
| GLM-5 | Z.AI | open | MoE | *(running)* | *(running)* |

At n = 100, 61/100 is the smallest count significantly above chance (p = 0.0352). **Every rule cell is far
above that floor; every pipeline cell is below it.** Three things follow, and none required us to shade a
number:

1. **The collapse generalizes to frontier scale.** The paper used to disclaim exactly this
   (`app:vintage`: *"We do not establish that the collapse reproduces on current-generation
   models"*). Across four organizations at 100B+–400B+, the transferred detector does not beat chance.
2. **The confound our own appendix named is broken.** Closed (Anthropic, Amazon) and open (Meta,
   DeepSeek) show the *same* pattern, as do dense and MoE. So the pattern is not attributable to weight
   availability or architecture — which is what a third organization was supposed to test, and it is a
   *null* on that contrast, reported as such.
3. **Criterion 2 gets stronger, not weaker.** The parameter-free 14-pattern rule reaches 80–87% at
   frontier scale, *above* the 69–80% we report for 3B–70B models. Frontier-scale accuracy on this task
   is **more** surface-accessible, not less. A detector can score in the 80s here with **zero learned
   parameters**, which is the whole point of criterion 2.

We pre-committed to what would count against us: *if the rule and pipeline both hold up at frontier scale,
the "collapse" is not general.* The pipeline did not hold up. We report that we won that bet only because
the bet was written down first.

### The disclaimers this retires, named explicitly

Promoting this material from "not load-bearing" to load-bearing **falsifies sentences the paper currently
asserts**, and we would rather list them than let you find them:

- §3.1's *"No claim below is a scaling, recency or effect-magnitude claim"* — narrowed.
- `app:vintage`'s *"We do not establish that the collapse reproduces on current-generation models"* —
  **removed**, because we now do.
- `app:frontier_preliminary`'s heading *"Exploratory: Not Load-Bearing for Any Claim"* — changed.
- The reader's-guide sentence *"No claim in §3.2–§3.5 depends on anything in bucket 4"* — updated.
- Both scope statements, *"open-weight models 3B–70B"* — widened.

All five move together as one edit, or none do.

---

## §3. A correction we owe you, which our own pre-registration caught

The EXP-FS pre-registration contains a gate (§8.3) requiring the analysis code to reproduce the two
*already-published* frontier cells before scoring any new one. **The gate fired. Nine published numbers in
our appendix did not reproduce from their committed result files.** We report this in full because you
scored reproducibility 9/10 and we would rather earn that than keep it quietly.

| Site | Published in the build you read | Recomputed from committed data |
|---|---|---|
| Sonnet 4.5 rule | 49.0% (5/50, 6/50) | **84.8% (47/49, 13/50)** |
| Sonnet Haiku pipeline | 83.0% | **50.5%** (degenerate) |
| Sonnet panel, Haiku / Llama-70B extractor | 50.5% / 50.5% | **92.9% / 78.8%** (LOO) |
| Sonnet extractor gap | −16.2 pp | **+12.1 pp** |
| Maverick rule | 77.0% (44/50, 17/50) | **83.0% (39/50, 6/50)** |
| Maverick RC means | 1.84 / 0.48 | **1.20 / 0.12** |
| Maverick feature means | 7.74 / 6.88 | **cons. 8.05/7.83, conf. 7.95/7.45** |

Where the bad numbers came from, where traceable: 49.0% is a *Maverick* value scored under a
non-canonical pattern list; 83.0% is *Maverick's rule* printed as *Sonnet's pipeline*; 1.84/0.48 are
*Llama 3.2 3B's* RC means; and the two 50.5% panel cells are transferred-pipeline accuracies sitting in
columns whose caption says leave-one-out refit. It is a bookkeeping failure across adjacent cells, not a
computation error.

**Two of the corrections cut against our own narrative, and we have let them.**

1. **A mechanism claim was contradicted, not merely unreproduced.** We had written that Sonnet 4.5
   *suppresses* the correction-marker channel. It does not: its lying trials characteristically open by
   correcting the false claim, and at least one of the 14 patterns fires on **47 of 49** of them. The
   channel is *preserved*. What fails on that cell is classifier *transfer* — and refitting on Sonnet's
   own conversations recovers the signal (LOO 92.9% / 82.8% / 78.8%), which locates the failure in
   transfer rather than in the features.
2. **An apparent double dissociation is withdrawn.** We had two frontier cells appearing to fail in
   *opposite* ways, which read as a mechanistic dissociation. Corrected, both fail the *same* way: rule
   succeeds, transferred classifier fails. The pair no longer separates marker suppression from
   classifier transfer, and the paragraph claiming an *"inverse pattern"* now says so.

Note the direction of the error. The **retracted** Sonnet pipeline figure of 83.0% was an apparent
counterexample to our own headline collapse; the true value, 50.5%, is not. **The correction makes the
paper's case easier, which is exactly why we are documenting its provenance rather than just changing the
digits.** Every corrected value comes from a stored metric or the canonical 14-pattern list documented in
the appendix.

**One column we did *not* touch.** The panel's refusal-only column, including Sonnet's 68.7%, is
unchanged. Our recomputation reproduces **0 of its 9 rows** — which is the signature of a methodology
mismatch on our side, not nine independent paper errors. Declaring nine numbers wrong on the strength of a
method that reproduces none of them would be the same class of mistake we are correcting. The reason is
recorded in the verifier so a later round does not "fix" the paper to match an unvalidated method.

**What we changed so this cannot recur.** Our verification suite had 1373 checks and **not one of them
recomputed a number from a result file** — every check compared paper text to paper text, which is
precisely why seven wrong values survived 29 rounds of review. There is now a data-provenance suite —
`experiments/verify_frontier_provenance.py`, **65 checks, committed and runnable**, not a scratch script
— that recomputes each frontier number from `data/results/*.json`, and that refuses to trust a verdict on
a disputed cell until the same estimator reproduces the *undisputed* cells in the same table. It also
pins each new panel cell **before** any of its numbers is written into the appendix, and fails on any
completed cell that has no registered expectation, so the path that produced these nine errors is closed
rather than patched.

---

## §4. Where the paper does not move, and why

- **Novelty stays at 6, and no edit we could make would change that.** Your §10 prescription — frame the
  novelty as *operationalization* rather than as the algebra — was implemented in round 28 and is
  near-verbatim in the abstract and conclusion. There is no further text edit available on this axis.
  What we have added this round is evidence, not framing.
- **Criterion 4 stays at rung 4 and at 1-of-5.** We are not widening it, and the reason is mechanical
  rather than editorial: the EXP-C4B roster is sealed by its own pre-registration's substitution rule,
  C4B already ran ten targets in seven families, and a new roster needs roughly 35 GB of weights that the
  disk cannot hold. We would rather say that than imply the scope was a judgment call.
- **English-only remains a real limitation, and it is the one ground of your generalizability score that
  this round does not touch.** The parameter-free rule is defined over *English* correction markers, so
  whether the 80–87% survives translation is a genuine open question and the most interesting thing we
  have not done. **It is not pre-registered and not run**, and we would rather say so than gesture at
  future work: doing it properly means localizing the claim set, the 16-probe battery, the 14 patterns and
  the yes/no parser, at which point translation quality becomes a new confound requiring back-translation
  and re-verification of the localized markers. That is a round of its own, not a paragraph in this one.

## §5. Two declines, with reasons

- **Ladder → Figure 1.** Declined. It renumbers every float and breaks the position pins for no reading
  gain, and we answered your P2 in prose instead (*"Three objects carry the argument…"*). `fig:dag` is
  Figure 1 because *why accuracy cannot attribute itself* is the paper's first claim; the ladder answers
  *how far the evidence reaches*, which is the second.
- **Title.** Declined, and this one is substantive. You asked us to narrow it toward *"Instructed"*. But
  the paper audits two public rollout corpora and builds criterion-4 materials in which **no target is
  ever instructed to deceive** — and the frontier panel above uses a byte-identical neutral prompt in both
  conditions. "Instructed" would under-scope exactly the parts of the paper that answer your Q3.
  *"Behavioral"* already scopes the detector class, which we take to be your actual concern.

---

## §6. Summary of changes in this round

| Change | Section | Page cost |
|---|---|---|
| Mixture thesis sentence (your §12) | `introduction.tex`, p3 | 0 |
| EXP-FS frontier panel, 7 targets / 7 organizations | new prereg + appendix | appendix |
| Nine corrected frontier numbers | `appendix.tex` | 0 |
| Retired recency/vintage disclaimers, five sites | main + appendix | net 0 |
| Widened scope statements | `abstract.tex`, `discussion.tex` | 0 |
| Data-provenance verification suite (65 checks) | tooling, committed | — |

Main text still ends on p9 at ruler 485 with the same 89-page total, zero overfull boxes, and all eight
float position pins unmoved.
