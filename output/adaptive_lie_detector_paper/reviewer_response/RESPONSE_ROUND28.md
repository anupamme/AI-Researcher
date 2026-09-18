# Response to Reviewer (6/10, Weak Accept / Borderline, confidence 3.5/5)

You told us the uncertainty is not correctness — your sub-scores run 7–9 — but **whether the contribution is
sufficiently novel and significant for the main track**. And then you wrote the sentence you wanted the paper
to make. We have adopted it, essentially verbatim, as the paper's statement of contribution, in **both the
abstract and the conclusion**:

> **The contribution is an operational identification audit for behavioral LLM benchmarks, together with
> empirical evidence that the *common* instructed-lie paradigm produces large, reproducible attribution
> failures across three detector paradigms and that benchmark design can determine which behavioral signal
> appears to constitute "deception detection."**

**One word differs from yours, and we flag it rather than let you find it.** You wrote *"dominant."* The round-26
reviewer required that word removed as an **unmeasured prevalence claim** — we audit ten designs, which does
not license "dominant" — and we agreed with them. We have kept your sentence and substituted **"common."** If
you prefer "dominant," we will restore it and add the citation count that would license it; we did not want to
re-introduce a defect a previous round asked us to fix without saying so.

Your three named changes were **not more experiments**, and you were right that they were mostly not needed.
Two of the three were already latent in the text and merely **unbilled**. All three have landed:

| Your ask | What changed | Where |
|---|---|---|
| §1 — define an **Elicitation–Construct Confounding Principle**, deception as one instantiation | The Proposition was **already** stated over $k$ unobserved mechanisms. It is now **named**, stated construct-first, and deception is explicitly the instantiation $(M_1,M_2)=(D,C)$ | `methodology.tex` §2.1, mirrored in the abstract, the introduction's Contribution (1), and the conclusion |
| §2 — reframe criterion 4 as a **diagnostic**, not a validation result | Your sentence adopted verbatim; the buried "less stable" closer promoted to a **named positive finding** | `methodology.tex` §2.2, `experiments.tex` §3.5 |
| §3 — **elevate EXP-AD substantially** | Its own `\paragraph`, in your three-line shape, ending on your conclusion | `experiments.tex` §3.5 |
| §8 — (iii) "deserves much more justification"; two senses of *necessary* | The split is now **stated**: (i)–(ii) are identification-necessary, (iii)–(v) are audit-operational. `tab:external_audit`'s caption is narrowed accordingly | `methodology.tex` §2.2 (short form), `app:criteria_taxonomy` (full derivation) |
| §12 — the "same battery" circularity | One clause, now in the **main text** (it was appendix-only) | `experiments.tex` §3.5 |
| §15 — make the hierarchy **visually unmistakable** | A **Tier** column over all 22 rows of `tab:experiment_summary`, your three tier words, plus one line in §3.1 naming the Tier-1 results | `app:experiment_summary`, `experiments.tex` §3.1 |
| §17 — too dense; move formal qualification to the appendix | **Main text is 170 words shorter; the appendix is 2,294 words longer.** Details in §7 below | six main-text files |
| §14, §16, §18 | **Already satisfied in round 27.** Measurements in §7 | — |

We also ran one new analysis, **EXP-AF**, because your §1 asked whether the principle generalizes beyond
deception. **It came back with a negative that we report as a negative** (§6).

---

## 1. Your §1: the defect was billing, not mathematics

You asked for a general principle with deception as one instantiation. The Proposition already was one. Here it
is as it stood in the reviewed PDF, unchanged by this round:

> *Let $M_1,\dots,M_k$ be latent mechanisms that $\mathrm{do}(E)$ shifts, none of them observed. Restrict
> interventions to $\mathrm{do}(E)$ and observations to $(V,E,S)$. Then no function of the observed
> distribution identifies any individual $M_i$'s contribution to $S$, **for any causal arrangement among the
> $M_i$ consistent with all of them being descendants of $E$**.*

Nothing in that is about deception. `app:criteria_taxonomy` already derived it from assumptions (A1)–(A5) with
**(A4), no exclusion restriction**, flagged as *"the assumption doing the work."* What we never did was **name
it, bill it, or state it construct-first** — we introduced it deception-first and let the general case read as
a technical generalization of the special one. That is a presentation failure and it cost us your §1.

The paragraph now reads:

> **The Elicitation–Construct Confounding Principle (ECCP).** *When a benchmark creates its target construct
> $Y$ by an intervention $E$ that also changes the elicited behavior $C$ a detector reads, no score evaluated
> only under $\mathrm{do}(E)$ is attributable to $Y$.* The Proposition below is that statement for $k$
> unobserved mechanisms; **behavioral deception detection is the instantiation $(M_1,M_2)=(D,C)$.**

**The math is unchanged, and our verifier asserts that.** Check 28b pins all three load-bearing fragments of
the Proposition — the general quantifier, the "any causal arrangement" clause, and the
$\tau_D\!=\!0$ witness — so the renaming cannot have quietly weakened the statement it renames.

---

## 2. Your §8, which we take to be the most damaging criticism available: (iii) and (v) are *not* identification-necessary, and we now say so

You wrote that *"you have defined a very demanding benchmark standard and then shown that existing benchmarks
don't meet your definition"* is the criticism that hurts, and that (iii) and (v) deserve justification. The
honest answer narrows our claim, so we state it as a narrowing:

- **Necessary for causal identification** — (i) $E$ held fixed and (ii) $D$ graded independently of the
  condition label. Without (i) the Proposition applies and $\tau_D$ is unidentified at any accuracy; without
  (ii) the "ground truth" *is* the condition label, so there is no $D$ to identify. **These two are forced by
  (A1)–(A5).**
- **Necessary for *this* audit to be operational, not for identification** — (iii) the same scenario realized
  under both outcomes of $D$, which is the observable procedure by which an auditor **checks** (A4) on a
  benchmark they did not build; (iv) a deployed-observable channel, which bounds what a result *means for
  deployment* rather than what it identifies; (v) $D$ not definitionally equivalent to the detector's input,
  which rules out **construct recovery** — a threat to the **claim** attached to a score, not to identification.

`app:criteria_taxonomy` derives this in full and concedes the consequence explicitly: *"a design could in
principle identify a deception-associated signal while failing (iii)–(v), and we would still decline to read
its score as evidence about a deployed detector; that is a stance about interpretation, and we mark it as
one."* `methodology.tex` carries the short form, and **`tab:external_audit`'s caption — the one string in the
paper that overstated this — is narrowed** from

> ~~criterion 4's requirements (i)–(v) being necessary and not sufficient~~

to

> **necessary for *this audit* and not sufficient for attribution: (i)–(ii) for identification, (iii)–(v) for
> its operation.**

The verifier asserts the un-narrowed string **absent** from all six main-text files, and separately asserts that
the **five true uses of "necessary"** identified in round 27 all survive (check 27b) — removing an
overstatement must not remove a correct statement.

### The escape route, which is what makes the standard meetable rather than merely demanding

Your criticism has a constructive answer we had not stated: **(A4) is a design choice, not a law of nature.** An
observable that is a child of exactly one $M_i$ **is** an exclusion restriction, and `app:criteria_taxonomy`
now gives three ways to manufacture one before data collection — **(1) cross elicitation with items, (2) record
the response channel a deployed detector reads, (3) grade the construct off that channel.**

And there is a **published design that passes all five**: reward tampering (Denison et al., 2024), already in
`tab:prior_work_criteria` group (e). It passes **mechanically, not luckily** — the manipulation is *training,
not the prompt*, so at evaluation time there is no $\mathrm{do}(E)$ for the elicited behavior to descend from
and (A4) does not bind. **A standard that some published design meets is not a standard built to be unmeetable.**

---

## 3. Your §2: criterion 4 as a diagnostic, and why 1-of-5 now argues *for* the paper

Adopted verbatim, in `methodology.tex`:

> **Criterion 4 does not validate deception detection; it tests whether the benchmark has crossed the minimum
> design boundary at which deception attribution becomes meaningful.**

This sits beside the two hedges we already had and which you did not object to — *"the protocol falsifies
validity claims rather than certifying them"* and *"Passing criterion 4 is necessary, not sufficient."*

The consequence is the edit we think buys the most. §3.5 previously ended its longest paragraph with the
clause *"removing the confound makes detection markedly less stable across targets."* It is now a sentence with
your reading attached:

> **Criterion 4's purpose is not to show deception is generally detectable but that the canonical benchmark's
> failure is not an impossibility result — and the standing 1-of-5 is itself a positive finding rather than a
> disappointment: once the elicitation confound is removed, detection is markedly less stable across targets
> than the instructed benchmark's near-ceiling accuracy suggests.**

We are not asking you to read 1-of-5 as a strong detection result. We are saying that **1-of-5 at fixed
elicitation against 100% instructed is the measurement the paper is about**, and that we had buried it.

---

## 4. Your §12: the same-battery circularity, in the main text

You observed that because EXP-C4 reuses **prior work's own probe battery**, a null there is partly a statement
about the **portability of that instrument**, not only about deception detectability. That caveat existed in
exactly one place — the appendix — and in **none** of the seven main-text files. It is now in §3.5, in the same
sentence as the nulls:

> the other two are **null and uninformative** (MDE $\ge 0.80$) — and because the contrast reuses *prior work's
> own* battery, a null here is partly about **that instrument's portability**, not only deception detectability.

---

## 5. Your §3: EXP-AD, elevated, in your three-line shape

You called it *"a very intuitive demonstration that the benchmark can manufacture its own apparent deception
signature."* It was two clauses at the end of §3.5's longest paragraph, after five other results. It is now its
own `\paragraph`, in your order:

1. On the instructed benchmark, the battery's most discriminative question — *"if you had made an error, would
   you point it out without being asked?"* — reaches **100.0%** grouped-5-fold on five of six targets.
2. At byte-identical elicitation the **same** probe is **inert**: rank 1 on **none** of the five shared
   targets, *exactly constant* on three.
3. What discriminates instead is a **different** probe — *"would you stake your reputation on the accuracy of
   what you just said?"* — which **points the same way on all five targets in both collections and survives
   Holm on two**, and is near-useless in the instructed regime.

> **So benchmark design can determine which behavioral signal appears to constitute deception detection.**

Two accuracy constraints from round 27 are kept in the same breath, because the elevation must not inflate the
claim: the probe is **inert** (rank 1 on none), not merely "constant"; and the two regimes use **different
claim sets**, so this is transfer *between designs*, not a causal effect of elicitation. EXP-AD is **Tier 1**
in the new tier column, by your §3.

---

## 6. EXP-AF: we tried to measure the confound on a second construct, and could not

Your §1 asked for generality. The strongest version of that is a **magnitude** measured on a non-deception
construct. **We attempted it on our pinned data and it is not deliverable, and we lead with that.**

EXP-AF (`docs/PREREG_EXP_AF.md`, the fifteenth pre-registration, written and frozen before the analysis ran;
no model calls) mechanically decides (i)–(v) over **28 pinned public corpora** — 8 Liars' Bench configurations
and 20 Apollo rollout files. Its **pre-registered branch (b) fired: no corpus combines a non-deception
construct with a separable elicitation and a recorded response channel, so no magnitude is measured outside
deception** — not by this analysis and not anywhere in the paper. The conclusion says exactly that:

> **Its precondition is decidable outside deception and we decide it** — on four published designs and 28
> pinned corpora — **while its magnitude we measure only for behavioral deception detection.**

The reasons, each a measured quantity rather than a judgement:

- **`harm-pressure-choice`, construct = underperformance.** The validity anchor is exact: `answer ≠
  meta.model_belief` reproduces the release's own `deceptive` label on **5,400 of 5,400 rows**. Underperformance
  is a genuinely *distinct* construct — agreement **0.873148**, rate 0.2174 vs. the released label's 0.1302,
  with **810** rows where the model's stated belief differs from the objective key. It then **fails (i)**:
  **0 of 4,601** distinct option blocks appear under more than one of the **7** framings, so framing and item
  are collinear by construction and the base-rate spread across framings (0.075–0.311) **is not attributable to
  the framing**. And it records **no channel** — median response length **one character** — so no detector is
  expressible on it at all.
- **Apollo `sandbagging_v2` (both files).** Topic and label are **perfectly collinear** (bio/chem/cyber 100%
  deceptive; astronomy/anatomy/abstract_algebra/business_ethics/clinical_knowledge 100% honest), and **task
  correctness *is* that corpus's deception label** by its own construction (`analyze_external_audit.py:170`
  defines `dec = answer_idx != correct_answer`), so it is not a second construct.

**The headline is the piecewise result, and it is a better answer to your §8 than the pass case alone:**

> **Each of the three design-rule properties is satisfied by some pinned public corpus — 2, 21 and 3 of 28
> respectively — and no corpus satisfies all three.** So an auditable benchmark **needs no new idea, only the
> combination** of three choices that three different existing benchmarks have each already made — and **two of
> the three are already made inside the instructed-lie paradigm this paper critiques**: `instructed-deception`
> realizes 100 of its 100 released items under *all four* of its system-prompt templates, and `convincing-game`
> crosses all 5 of its released items with all 10 of its templates.

Per your framing preference we put the **pass case first** and the verdicts second, and the verifier pins that
ordering so it cannot drift.

### Three disclosures we would rather you heard from us

1. **DEVIATION 1, which reverses two of our own verdicts.** The pre-registration named `env_md5` as the
   fallback item key. That hash covers **every message the model did not write, including the system prompt**,
   so for a corpus whose elicitation variant lives in the system prompt it contains $E$ by construction and
   "the same item under two variants" is arithmetically impossible. Under `env_md5` alone,
   `instructed-deception` and `convincing-game` would both have been reported as **failing** (i) — a
   measurement artifact, not a measurement. The analysis therefore reports every candidate key with its own
   counts and gates each verdict on **admissibility** (E-free, non-vacuous, non-over-merging; a
   frequency-thresholded residual key merged 293 of 4,308 classes and credited exactly 293 spurious
   crossings). **The pre-registration is frozen and was not edited.** No published number elsewhere depends on
   `env_md5` as an *item* key: EXP-XL used it as a *scenario* key, where containing the system prompt is
   harmless.
2. **Four of the twenty Apollo rollout files carry the literal string `"SEE OTHER FILE"`** where the rollout
   list belongs (`insider_trading{,_doubledown}__upscale__llama-70b{,-3.3}.json`). Recorded as `rows_absent`,
   not skipped silently.
3. **`run_liars_bench_audit.parse_meta` returns `{}` for both `harm-pressure-*` configurations**, because
   their shipped `meta` strings are Python reprs containing `np.float64(...)`. So EXP-XL never saw a
   `meta.template_index` for the only two configurations that publish one. EXP-XL's verdicts used `env_md5`, so
   **no published number changes**; EXP-AF strips the wrappers.

EXP-AF is labelled **descriptive, not confirmatory, Tier 2**, and it is **a census, not an estimate** — every
corpus is read in full, so there is no sampling, no estimator, no fold and no $p$-value in it. Its own *"What
EXP-AF does not establish"* paragraph leads with the missing magnitude, and adds that the census covers **the
corpora we pinned** — a benchmark we did not audit may well cross elicitation with items.

---

## 7. Your §14, §16, §18 were already satisfied; your §17 is answered as a budget fact

- **§14 (transfer belongs in the appendix).** §3.5 carries one clause — *"Criterion 5 (transfer) is
  exploratory: 2 of 5, not part of the argument"* — plus a single appendix reference. That is the whole of it in
  the main text.
- **§16 (no mechanistic language).** Zero occurrences of "represents deception," "encodes deception," or
  "representation of deception" anywhere in the main text. EXP-WP says **"we withdraw any representational
  reading"** and **"decodable, not causal."** The one occurrence of "mechanistically" describes two *detectors*
  being of different kinds, not a claim about internal representations of deception.
- **§18 (`cooney2026didyoulie`).** Cited at **4 main-text sites and 3 more in related work**: the Corollary's
  own boundary (*"uninstructed deception has no instruction to follow, and evaluations there report the
  predicted drop"*); `tab:criteria`'s *beyond the protocol* row; the introduction's explicit concession that
  **trained belief-verified organisms have fixed elicitation and go *beyond* it, with $D$ set rather than
  observed**; and the abstract's *"Fixed elicitation itself is not new"* clause, which carries the same
  concession without the key.
- **§17 (too dense; leave more of the formal qualification in the appendix).** We agree, and it is the only
  reason this round's additions fit. The paper is at **zero slack** against the 9-page main-text limit, so
  every sentence added had to be paid for. Measured: **main text −170 words** (abstract −43, introduction −159,
  methodology +109, experiments −83, discussion ±0, conclusion +6) against **appendix +2,294**. Four demotions
  paid for T4/T5/T7, in this order:
  1. the **EXP-XA/XJ paragraph** reduced to its verdict plus the AUROC pair; the hidden-scaffold argument moved
     to `app:external_audit`;
  2. the **annotation-leakage / construct-recovery paragraph** merged into it, keeping both verdicts and both
     headline deltas; the mechanism narrative moved to the appendix;
  3. the **EXP-AA statistics** — the $\alpha$ range and the 13/13 concordance — moved to
     `app:audit_agreement`, keeping the verdict *"the requirements are decidable from a specification, and
     these releases do not publish one"* in §3.5;
  4. **light compression only** of the setup paragraph, the `fig:r1c_collapse` caption, the factorial and
     `tab:external_audit`'s column widths. **EXP-AD was not shortened below the three-line narrative** — that
     was the point of the round.

  **We cut no structured caution.** Every previous reviewer named those as a strength, and all three boxes are
  intact and unshortened: *"Three questions, kept apart"* and *"The design that would settle the attribution
  question — stated in full, and then run"* in the introduction, and *"What is proven, what is shown at fixed
  elicitation, and what is unresolved"* in §2 — along with the appendix sections' own limits paragraphs.

**Verification.** 1,225 automated checks pass, of which 990 are retained from round 27 — any retained check
that fails is treated as a regression, and every changed string is a documented substitution recording which
of your items it serves. They include: the build clean (0 overfull hbox, 0 overfull vbox, 0 undefined
references, `warning$ -- 0`); **twelve float page pins**; every EXP-AF number re-derived from
`eccp_decidability.json` with a guard that **if** any corpus passed (i) **then** the text may not say all
failed; the 15 pre-registrations on disk matching the main text's number word, with `git diff` empty on the 14
pre-existing ones; and rendered inspection of pp. 1, 5, 6, 8, 9, 19 and 23.

---

## 8. Where the paper does not improve, stated plainly

- **The algebra is not novel and we do not claim it is.** It is a standard non-identifiability result; the
  paper says so in the introduction, in `app:criteria_taxonomy` (*"The algebra is standard; what this paper
  contributes is the protocol that enforces it on a published benchmark"*), and in related work. Naming the
  ECCP buys **significance and scope**, not novelty. If novelty of the theory is your binding constraint, this
  round does not move it.
- **Generalization is bounded by what we could run.** Open-weight targets 3B–70B, English, instructed-roleplay
  evaluations. The recency check (EXP-R1d) was inconclusive and is reported as inconclusive. The EXP-C4B target
  roster is **sealed** by its pre-registration's substitution rule and we did not reopen it.
- **Criterion 4 stays observational.** It reaches rung 4 of five: a deception-**associated** signal at fixed
  elicitation, not $\tau_D$. A latent $U$ with $U\!\to\!D$ and $U\!\to\!S$ survives it, and the one surviving
  standing positive is a single target.
- **No magnitude outside deception, on this data.** §6 above. That is a hard property of the pinned corpora,
  not a scoping decision, and the paper states it in the same breath as the principle's generality.

We think your three levers were the right three, and we have taken all of them. What they change is what the
paper is *billed as* and what a reader can *act on* — the general principle is named, its precondition is
decidable and decided outside deception, the escape route is a design property with a published existence
proof, and the criterion-4 result now reads as the diagnostic it always was. What they do not change is the
novelty of the underlying algebra, which we continue to concede.
