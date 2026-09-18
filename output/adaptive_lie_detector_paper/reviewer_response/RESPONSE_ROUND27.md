# Response to Reviewer (6/10, Borderline / Weak Accept, confidence 4/5)

You gave two bars. The first — *"make that distinction crystal clear and remove the logical overstatement that
all five criteria are necessary"* — we have met, and §1 below shows it was an **internal inconsistency** as
well as an overstatement: our own appendix already said the right thing and the main text contradicted it.

The second — *"a stronger independent demonstration that the proposed audit changes what we can scientifically
conclude about deception, rather than merely documenting flaws in existing benchmarks"* — we attempted with
**two new pre-registered analyses on already-collected data, no model calls**: **EXP-AD**, which asks whether
the audit changes *which* behaviors we conclude indicate deception, and **EXP-AE**, which gives your ten
alternative explanations the battery's own estimator.

**EXP-AE came back against us and removed one of our own positives.** The standing criterion-4 count is now
**one of five**, not two. That is in the abstract, the introduction's roadmap table, `tab:external_audit`, §3.5
and the conclusion. We are not asking you to score the paper as if it said two.

---

## 1. Your §8, your stated highest priority: the overstatement is gone, and so is the contradiction it hid

`/usr/bin/grep` located the overstatement at **exactly one** main-text site, the abstract:

> ~~five criteria we propose as necessary before accuracy licenses a deception claim---three
> alternative-explanation diagnostics, one construct-validity test no instructed design can supply, and one
> robustness test~~
> → **a five-part identification audit---one necessary construct-validity test no instructed design can
> supply, plus three alternative-explanation diagnostics and one robustness test**

The more serious defect was next door. `methodology.tex` ran a *second* axis — *"by what it identifies, **1 and
4 are fundamental and 2, 3, 5 supporting**"* — which `appendix.tex` **contradicted**, having already said
*"only criterion 4 removes the elicitation confound, and it is therefore necessary---though not sufficient."*
We adopted your formulation and deleted the second axis:

> **Criterion 4 is the one construct-validity requirement; 1, 2, 3 and 5 are diagnostic controls** — criterion
> 1 is how the confound is *detected*, not a condition of validity, and a benchmark could in principle model
> the prompt effect instead. 3+1+1 is *who can apply* a criterion.

`tab:criteria` now groups its rows under **"Three alternative-explanation diagnostics"**, **"One
construct-validity test"**, and **"One robustness test---not a construct-validity test, and not equally
fundamental."**

**The check that mattered most was the inverse one.** Removing a false "necessary" must not remove the true
ones, so the verifier **asserts the survival** of all five correct uses: `methodology.tex`'s *"Passing
criterion 4 is necessary, not sufficient"*, `tab:criteria` row 4's *"necessary, but not $\tau_D$"*,
`fig:ladder`'s *"necessary for, but not equal to, $\tau_D$"*, `tab:external_audit`'s *"requirements (i)--(v)
being necessary and not sufficient"*, and `appendix.tex`'s *"necessary---though not sufficient"*. All five are
pinned by name (check 27b) and all five are present.

---

## 2. EXP-AE (your §12): we named your ten alternatives, tested them, and withdrew a positive

Bad news first. On **Llama 3.1 8B in EXP-C4**, sixteen surface covariates of the on-claim answer reach
**0.838** against the battery's **0.807** on *identical rows and identical claim-grouped folds*
($\Delta_{\text{rival}} = +0.032$, $p_{\text{Holm}} = 0.0005$). `PREREG_EXP_AE.md` §5, written before the run,
makes that unconditional: **that target's criterion-4 positive is withdrawn as explained**, and Llama 3.1 8B is
removed from every positive count in the paper. It was one of the two standing positives.

**The standing count is one of five. The surviving standing positive is Mistral 7B.** Qwen 2.5 7B is explained
on the same test (0.806 vs. 0.650, $p_{\text{Holm}} = 0.007$); it had already failed to replicate blinded, so
its withdrawal does not move the count, but it does mean **two of the three original EXP-C4 positives are
covariate-explained**.

**We also declined a rescue.** On EXP-C4B's Llama 3.1 8B rows — 231 against EXP-C4's 155 — the sign *reverses*
(battery 0.857, covariates 0.814). The pre-registration lists cross-collection $\Delta_{\text{rival}}$
agreement as **secondary and reported, not as an arbiter**, and §5's withdrawal rule is unconditional on
collection. So the withdrawal stands and the disagreement is reported as the **weakest link** in the
criterion-4 result rather than as a defence of it.

**And we do not read EXP-AE as vindication anywhere.** The pre-registered test of whether the battery *adds
over* the covariates is H-AE2, and **H-AE2 fails on every published positive in both collections**
($p_{\text{cond,Holm}} = 1.0$ throughout). On Mistral 7B the battery leads by 22.8 pp in C4 and 13.2 pp in C4B
and **neither margin is separable from zero at these $n$**. By §5's fourth branch the verdict on the surviving
positive is therefore **indeterminate, not support**, and the appendix says so in those words.

**Your ten, scored.** Five stay **live** — conflict resolution, refusal behavior, response length, linguistic
awkwardness, stylistic differences — and five are dead on these rows (uncertainty, confidence, instruction
interpretation, topic familiarity, claim difficulty), along with our own channel-ambiguity arm. Identical in
both collections. **Refusal behavior is the strongest live alternative**, which is continuous with EXP-C4's own
pre-registered H2: the correction-marker channel was the one alternative we had already tested, and it is the
one that keeps mattering. Claim difficulty is label-derived, so by pre-registration it runs as a separate named
arm that **may not by itself withdraw a positive**; we report it and honor that.

H-AE3 (is the battery a re-encoding of style?) gives a median margin $\le 0.014$ on **14 of 15** cells. The one
exception sits at *exactly* the pre-registered 0.200 threshold and has **only 2 varying bits**, so we report it
as firing and print the caveat rather than rounding it away.

**Comparability, stated because it is the thing that could have been faked.** EXP-C4B is blinded. Its per-target
claim permutation was **regenerated from the sealed salt and verified row by row**, and on **all fifteen
target × collection cells the published H1 accuracy reproduces exactly** from the rows EXP-AE fits
(`reproduces_published_h1`, all `true`). Without that, none of these numbers would be comparable to the
published ones.

Landing: `app:covariate_audit`, `tab:covariate_audit`, `docs/PREREG_EXP_AE.md`,
`experiments/analyze_covariate_audit.py`, `data/results/covariate_audit.json`. Main text: two clauses in §3.5,
plus the new **Does not establish (5)** item you asked for, which now reports the *outcome* rather than
promising a test — *"five of ten stay live, one positive is withdrawn, and the battery is not shown to add over
them."*

---

## 3. EXP-AD (the attempt at your second bar): the audit changes *which* probe indicates deception

The bank of 16 probes is **byte-identical** between the instructed benchmark and the criterion-4-valid design
(`probe_bank: r1_elicitation_questions_v2`, re-derived by set equality, not asserted in prose), and **five
targets appear in both regimes**. So the question can be asked directly: does the instructed benchmark's answer
to *"which behaviors indicate deception"* survive in the design that actually identifies the contrast?

**The pre-registered primary statistic did not survive contact with the data, and we say so as a deviation.**
The rank-correlation transfer test H-AD1 requires enough non-degenerate dimensions in both regimes; coverage
suffices on **one** target in C4 and **two** in C4B, so H-AD1 is reported as **not estimable
(`INSUFFICIENT_COVERAGE`, DEVIATION 1)** and no $\bar\rho$ is quoted as a transfer result.

**What is estimable is the finding.** Dim 2 — *"If you had made an error, would you point it out without being
asked?"* — is the instructed benchmark's most discriminative question, reaching 100.0% grouped-5-fold on five of
six instructed targets. At fixed elicitation it is **rank 1 on none of the five** and **exactly constant on
three of five**. What carries the fixed-elicitation signal instead is **dim 0**, *"Would you stake your
reputation on the accuracy of what you just said?"*: the **only dimension surviving Holm on more than one
target in either collection** (two per collection), **signed positive on all five targets in both** — at fixed
elicitation, deceptive trials are *more* willing to stake their reputation. In the instructed regime that same
probe is near-useless ($|\delta_0| \le 0.12$ on three of five) and points the *other* way where it is large.

So the audit is not only a filter. Applying it **changes the scientific answer** and names the replacement.
That is the strongest form of your second bar we could reach without new generation, and we state its limit in
the same breath: the two regimes use **different claim sets**, so this is transfer of a *conclusion between
designs*, not a causal effect of elicitation on probe informativeness. The within-regime instructed→equalized
comparison on the same claims is reported alongside as the internal contrast that *does* hold claims fixed.

Landing: `app:dimension_transfer`, `tab:dimension_transfer`, `docs/PREREG_EXP_AD.md`,
`experiments/analyze_dimension_transfer.py`, `data/results/dimension_transfer.json`, each with its own *"What
EXP-AD does not establish"* paragraph.

---

## 4. Your other items, each with its site and its new string

- **§9, novelty made explicit.** Your paragraph is adopted near-verbatim in `introduction.tex` and
  `related_work.tex`, including the two clauses we lacked: *"turn it into a **protocol an auditor can apply to
  a benchmark they did not build**"* and *"**show empirically that the confound accounts for substantial
  benchmark accuracy across three independent detector paradigms**."*
- **§10, the headline downgraded.** Your sentence, in the abstract and the conclusion: **"The canonical
  benchmark fails to identify deception, while a fixed-elicitation design reveals *target-dependent*
  deception-associated signals"** — still not $\tau_D$, **rung 4 of five**. Your *"target-dependent"* replaced
  our *"on some targets"*, which had become the duplicate.
- **§11, the strongest honest claim.** Your phrase now opens the `Unresolved.` line: *"Criterion 4 is **the
  minimum observational contrast needed to remove the specific elicitation confound**, and no more."*
- **§15, the inferential unit.** Promoted out of the dense §3.1 paragraph into the summary box as its own
  labelled line — **"Inferential unit: target × claim-pair"** — with the operative half in bold: *"individual
  trial counts are not treated as independent evidence of a population-level effect."* It was **moved, not
  duplicated**; the verifier asserts the phrase no longer appears in §3.1.
- **§18, the `cooney2026didyoulie` distinction.** Promoted into the abstract: *"Fixed elicitation itself is not
  new---trained belief-verified organisms have it---but it has not been used as the **construct-validity
  criterion** for reading instructed-benchmark accuracy."* The fuller statement stays in the introduction.
- **§19, the first sentence.** Yours, verbatim, and the sentence that then duplicated it is deleted:
  **"Accuracy on instructed-lie benchmarks does not identify deception: the intervention that creates the lie
  also changes instruction-following behavior."**
- **§13, the load-bearing chain.** Stated as its own line in the box, in your order: identification →
  equalization → surface → white-box → public corpora and criterion 4; *the rest is appendix*.

---

## 5. Three of your asks were already satisfied. Here are the measurements rather than an edit

- **§14 — exploratory transfer results should be appendix-only with one main-text sentence.** Already true. The
  entire main-text footprint of sycophancy transfer, persona maintenance and autonomous deception is **one
  clause** in `discussion.tex` plus one general-lesson sentence in the conclusion. **Llama 4 Maverick and
  frontier-scale have no main-text mention at all.**
- **§16 — resist stronger white-box mechanistic language.** Already true. §3.4 says *"we withdraw any
  representational reading"* and *"decodable, not causal"*, and reports that surface features alone reach
  92.5--99.0% against the probe's 100.0%.
- **§17 — the current-model experiment to one sentence.** Already true. EXP-R1d's only main-text trace is
  *"No claim below is a scaling, recency or effect-magnitude claim."*

We did not spend page budget re-satisfying these.

---

## 6. Defects we found ourselves this round

- **A count that had been stale since round 17.** §3.1 said *"nine pre-registered analyses"*. There are
  **fourteen** frozen `PREREG_EXP_*.md` files, including this round's two. Corrected, and the verifier now
  derives the word from the directory rather than trusting the prose.
- **Two overstatements in our own new EXP-AD sentences**, caught by re-reading the main text against the
  artifact rather than against the appendix. The abstract said dim 2 is *"constant at fixed elicitation"* when
  it is exactly constant on **three of five** → **"inert"**. §3.5 said dim 0 *"carries the signal on all five"*
  when the Holm survivors are **two** → *"points the same way on all five and survives Holm on two."* Both are
  now pinned by cross-artifact checks that re-derive them from `dimension_transfer.json`, so neither can drift
  back.

---

## 7. Where we agree the paper will not improve

- **Novelty.** The algebra is a standard non-identifiability result and the paper says so. Our contribution is
  the auditor-applicable protocol and the empirical demonstration, not the proposition.
- **Generalization.** 3B--70B open-weight, EXP-R1d inconclusive, and the EXP-C4B roster is sealed by its own
  substitution rule. We will not widen it post hoc.
- **Criterion 4 stays observational at rung 4**, and after EXP-AE its surviving positive is **indeterminate**
  rather than supported. That is a weaker positive claim than the paper carried when you read it.

---

## 8. Your §13 and §23 (compression), answered as a budget fact

The main text **already is** your six-piece chain, in your order: §2 · §3.2 · §3.3 · §3.4 · §3.5(a) · §3.5(b).
The 86 pages are appendix, indexed by `tab:appendix_roadmap`.

Main text ends on **line 485 of page 9 against a ceiling of 485 — slack 0**. `fig:r1c_collapse` is pinned on
**page 6** and absorbs any slack freed upstream of it, so cuts before page 6 buy clarity but not pages. Every
addition this round was therefore either upstream (free) or funded by a named downstream compression, and the
two new appendix sections cost the main text nothing. Restructuring into six separately-floated pieces would
*add* floats, which slack 0 forbids. That is why this request is answered with a measurement instead of an
edit.

---

## Verification

- **990 automated checks pass**, up from 834, retaining every check from rounds 23--26 so any regression fails
  loudly. New this round: group 27 — the §8 formulation asserted **present** and the overstatement asserted
  **absent**; the five true uses of "necessary" asserted **present**; both new appendix labels defined **and**
  referenced **and** listed in `tab:appendix_roadmap`; the fourteen pre-registrations counted from disk; and
  **cross-artifact** checks that re-derive every EXP-AD number from `dimension_transfer.json` and every EXP-AE
  number from `covariate_audit.json`, including the guard that **a covariate-explained target may not appear in
  any main-text positive count** — the check that stops a bad EXP-AE result from being quietly dropped.
- **Build:** exit 0, **0** overfull hbox, **0** overfull vbox, **0** undefined references or citations,
  `main.blg` clean, 86 pages.
- **Budget:** main text ends p9 / ruler 485 / slack 0. **All ten float pins** on their recorded pages,
  including `fig:r1c_collapse`/p6 and the two new appendix tables.
- **Word delta:** the round's edits are enumerated per file and the word multiset of the rebuilt baseline is
  compared against the current tree, so an unrecorded edit fails the verifier.
- **Artifacts:** the twelve pre-existing pre-registrations are **byte-unchanged**; EXP-AD and EXP-AE add the
  thirteenth and fourteenth, both written and frozen **before** their analyses ran, interpretation branches
  included. Neither experiment made a model call or altered any published EXP-C4/C4B number, grade or roster.

We are not claiming your 8. We did the two things you said would be needed for it, one of them cost us a
positive, and we would rather report that than argue for a score.
