# Response to Reviewer (6/10, Weak Accept / Borderline Accept, confidence 4/5) — the construct-validity terminology round

Thank you for a careful, twenty-section report. We have made **four surgical edits** and **run no new
experiments**, in line with your §21's framing. Before the item-by-item response there is one thing you
need, because it changes which of your items are actionable.

---

## §0. Provenance: the build you read is ten revision rounds old

We say this first, as **information rather than rebuttal**. Your report names the file
`main(20260916-074428).pdf`.

- `20260916-074428` = **2026-09-16 07:44 UTC** = 13:14 IST.
- The commit whose build that is, is **`5229949`** (*"Table 1: report Family E's 1/5 in the roadmap, at net-zero page cost"*, 2026-09-16 13:10 IST — four minutes before the PDF was written).
- The current head is **`3d2805e`**, **23 commits and ten revision rounds later** (rounds 22–31).

**Two of your own quotations date the build independently, so you can check this without trusting us:**

| Your quote | Status at the build you read | Status now |
|---|---|---|
| §10: the abstract *"eliminates above-chance discrimination"* | present at `5229949` | **0 occurrences anywhere in `sections/`.** Removed in rounds 26/28 after an earlier reviewer made the same objection; a verifier check now *forbids* the string |
| §10: the 3B claim-pair-grouped accuracy as **46.0%** | `46.0%` at `5229949` | **36.0%** (`experiments.tex:57`). Corrected in round 26 when every figure was reprinted under a pinned scikit-learn 1.8.0 |

**This is also the same PDF that `RESPONSE_ROUND30.md` answered** — but it is a genuinely different pass
over it, not a re-send: that report was organized as priorities P1–P5 with a §15.2–15.5, and yours is
§1–§21 with a largely disjoint item set. We are treating it as a new review, and we are not asking you to
re-read anything on the strength of the date alone.

**What this costs, stated honestly.** When we audited all twenty of your sections against the live text,
**eleven items were already closed**, four were genuinely open (and are now done), two ask us to reverse a
change a *newer* reviewer required, and two are new experiments. Your report's own ceiling —
*"~7/10 after another focused revision"* — was therefore already partly priced in before you wrote it. We
are not claiming your score should move on provenance grounds; we are telling you which of your items a
reader of the current PDF would not have raised.

---

## §A. The eleven items already closed, with the site and the round

Spot-checkable: every string below is quoted verbatim from the current `sections/*.tex`.

| Your item | Where it is now | Closed in |
|---|---|---|
| §10 *"eliminates above-chance discrimination"* | 0 occurrences; the abstract now says the signal is *removed*, not the phenomenon eliminated | R26/R28 |
| §11 the bare phrase *"deception signal"* | Down to **two** sites in the main text, and both are statements that the paper does **not** establish one: `introduction.tex:84` (*"that equalization shows a deception signal to be absent rather than removed along with the confound"*, in the *what we do not establish* list) and Figure 2's **rung 5**, the rung labelled *no design audited here* | R26/R28 |
| §15 *"dominant paradigm"* | 0 occurrences | R28 |
| §8 / §21.4 **characterize the target dependence explicitly** | `introduction.tex:82`: *"once the instruction confound is removed, what remains is **neither stable across targets nor cleanly separable from surface behavior**"*; `experiments.tex:123`: *"**The standing count is one of five**"*; `methodology.tex:50` (Table 1, claim 5): *"**Weakest claim here, and target-dependent**"* | R31 |
| §12 don't oversell the ECCP as a new result | `methodology.tex:19`, **at the definition site**: *"The ECCP names a benchmark-design instance of standard pathway non-identifiability, not a new theoretical result… what is new is the audit it licenses, not the constraint"* | R31 |
| §13 *"what should a reader remember"* | `introduction.tex:77`: *"**Four objects carry the argument**"* — Figure 1 (why), Figure 2 (how far), Table 1 (every claim), Table 2 (what the audit found) | R31 |
| §14 tier the results by strength | `tab:claim_ledger` is now **Table 1 on p5**, six columns including pre-registration and replication status, with *"Nothing in the argument sits outside this table"* | R31 |
| §19 Q1 *why exactly five criteria* | `methodology.tex:78`, the A/B/C division paragraph, plus *"The five are not claimed to characterize every valid deception benchmark"* | R27, sharpened R32 (A3 below) |
| §19 Q3 *is it deception or a correlate* | `methodology.tex:83`, *Does not establish* (5): names uncertainty, refusal, conflict resolution, claim difficulty, length and style; EXP-AE gives them the battery's own estimator, **five of ten stay live** and **one positive is withdrawn** | R27/R31 |
| §21.1 novelty framed as evaluation methodology | `introduction.tex:54` carries your framing **verbatim**: *"The novelty is not the observation that confounding exists; it is turning a previously implicit causal-validity requirement into an auditor-executable protocol and showing that existing behavioral deception benchmarks fail it in empirically distinct ways."* | R31 |
| §7 / §21.2 robustness ≠ construct validity, in the criteria specification | `appendix.tex`, the criteria table's group C: *"**C. Robustness (5)** — *not a construct-validity test, and not equally fundamental*"* | R27 |

The last one was **only half closed**, which is why it reappears below as A3: the *appendix* had the
three-way split since round 27, but the *main-text* paragraph still lumped criterion 5 in with 1–3. You
were reading the main text, so you were right.

---

## §B. The four edits made this round

All four are your items. None is an experiment; no number in the paper changed. The main text is nine
pages at **485/485 ruler lines — zero slack** — so each addition was funded by an equal-length
compression of a *restatement* elsewhere, never of a number, a caution, or a disclaimer.

### B1 — your §6: *"distinguishes predictive validity from attributional validity"* · `introduction.tex`

Both terms were **0 occurrences anywhere in `sections/`**. This is the one item on your list that could
plausibly move **novelty 6**, and the paper already had the structure for it: a
Generalization-vs-Identification comparison table on p3. We named the pair in both places.

**A fourth row, first in the table:**

| | **Generalization** (concurrent work) | **Identification** (this paper) |
|---|---|---|
| **Validity** | **Predictive** | **Attributional** |
| Asks | Does a detector fit in regime A still work in regime B? | Does accuracy in regime A measure deception *at all*? |
| Fails when | Accuracy drops out of distribution | One intervention moves two candidate causes |
| Fixed by | More regimes, more data, better detectors | **A different intervention** |

**And in the prose that contrasts the two literatures** (`introduction.tex:61`):

> Three concurrent evaluations find lie detectors fail to **generalize** beyond the regime they were fit
> in. **That is a question about predictive validity; ours is the prior one, about attributional
> validity:** instructed-lie accuracy is **not merely poorly generalizing but uninterpretable as evidence
> about deception**, because the intervention moves deception and compliance together — so
> generalization can be perfect while identification still fails.

The last clause is the payload: the two validities are not ordered by strength, and a paper that fixes
generalization has not touched ours. **The abstract is unchanged** — it is under a 403-word ratchet and we
did not spend the words there.

### B2 — your §16: *"construct validity and instrument validity are distinct"* · `methodology.tex`, `experiments.tex`

The substance was already the paper's own finding, in two places, and never named:
`experiments.tex:119` (*"the null is the instrument's, not the criterion's"*) and `methodology.tex:78`
(*"a verdict on a benchmark, not a detector"*). Now named at the second, as an extension of the existing
sentence rather than a replacement:

> The output is a verdict on a benchmark, not a detector: **construct validity and instrument validity
> are distinct**, and criterion 4 tests only the first — **the protocol falsifies validity claims rather
> than certifying them**.

And a length-neutral substitution at the §3.5 qualification, so the same distinction governs how a
criterion-4 null must be read (`experiments.tex:123`):

> because the contrast reuses *prior work's own* battery, a null is partly about **that instrument's
> portability**, ~~not only deception detectability~~ → **not the criterion's validity**

**The conceptual diagram you also asked for in §16 is declined**, on page budget: a seventh main-text
float at zero slack pushes the main text onto p10. See §C.

### B3 — your §7 / §21.2: separate identification from robustness, in the main text · `methodology.tex:78`

You objected to exactly the right sentence. It read:

> ~~**Criterion 4 is the one construct-validity requirement; 1, 2, 3 and 5 are diagnostic controls**~~

which groups criterion 5 with 1–3 and so blurs the line you asked us to draw — and contradicted our own
appendix, which has carried the three-way split since round 27. Replaced with the split itself:

> **The three groups differ in kind**: **1–3 diagnose the confound**, **criterion 4 is the one
> *identification* requirement**, and **criterion 5 is *robustness*, not a construct-validity test** —
> criterion 1 is how the confound is *detected*, not a condition of validity.

The paragraph's existing *who can apply* argument is untouched (A and C are checkable on someone else's
released artifact; B must be designed in), and `robustness` now appears in the main text, where it
previously had **0 occurrences**. The word "necessary" is still not applied to all five.

### B4 — your §9: the multiplicity / nesting ladder · new **Appendix Table 30** + one main-text clause

Your ask — that a reader never mistake the trial count for the sample size — was answerable only from
prose scattered across three appendix subsections. It is now one table. **Every figure is transcribed
from a cell that already printed it; nothing is recomputed**, and the verifier asserts each number occurs
at least twice in `appendix.tex` so that the table cannot drift from its source.

| Level | *n* | Note |
|---|---|---|
| Graded trials | 1,760 (R); 1,440 (E) | 1,419 of Family E analysed, 21 evasive exclusions |
| Resamples per claim | 8 | not independent observations |
| Claims per target | 30–50 | after the pre-registered top-up rule |
| **Paired claims/target** | **12–23** (R); **12–15** (E) | **the inferential unit**: both *D* values realized |
| Targets per family | 5 | Holm correction applied within the five |
| **Standing positives** | **1 of 5** | exact 95% CI [0.005, 0.716] |

The caption states the point directly: the thousands of graded trials are **not** thousands of independent
samples; multiplicity is controlled by Holm–Bonferroni *within each family of five*; and the exact
interval on 1 of 5 — **[0.005, 0.716]** — *"spans almost the whole unit interval: five targets cannot
distinguish a rare property from a common one."* That is the strongest statement of your §9 concern we
can make, and it is against our own result.

In the main text, appended to the existing *Inferential unit: target × claim-pair* sentence
(`methodology.tex:81`, inside the caution box):

> individual trial counts are not treated as independent evidence of a population-level effect — **the
> thousands of graded trials reduce to 12–23 paired claims per target** (Appendix Table 30).

---

## §C. What we declined, and why — nothing silent

### C1 — §21.3, *"put the C4 result front and center"*: declined, because a newer reviewer required the opposite

This is the one place your report and a newer one conflict, so we show the conflict rather than resolve it
quietly. A reviewer reading `149da0d` — two days after your build — raised as their §21.2 the item we
recorded verbatim at `RESPONSE_ROUND31.md:72`:

> **§21.2 — "Stop over-weighting the criterion-4 result"**

Round 31 implemented that, at `conclusion.tex:4`:

> **We establish — (1)–(3) structurally or by replication, (4)–(5) as a weaker, target-dependent
> secondary finding:**

Reversing it now would re-open an objection on a build you have not seen, and the user's decision was to
keep the down-weighting. **What we could adopt from your §21.3, we did:** your reading of C4 as *the
constructive resolution rather than a footnote* is already in the text at `introduction.tex:56`
(*"**A construct-valid benchmark: the critique does not imply undetectability.**"*) and in the §3.5
conclusion (*"**The standing 1-of-5 is itself a positive finding rather than a disappointment**"*). What
we will not do is promote it above the identification result.

### C2 — §21.2, restructure and promote the criteria table: declined as a float move, answered as text

`tab:criteria` was **demoted to Appendix A in round 31 on the user's instruction**, with its operational
column folded into Figure 2's *"Reached by"* column so the main text keeps the content without the float.
Promoting it back costs p10. B3 answers the substance — the identification/robustness split — in the main
text at zero float cost, and every main-text citation of the table names it as an *Appendix* table so no
reader hunts for it on p5.

### C3 — §21.5, cut 15–20% of the main narrative: declined as specified, with the real number reported

The main text is **9 pages at 485/485 rulers, slack 0**. Round 29 already cut 151 words and round 31
added Table 1 at net-zero ruler cost. At this density a 15–20% cut is not compression — it is deleting one
of: the three structured caution boxes, the five-item *Does not establish* list, or §3's numbers. **Each
of those has been named as the paper's principal strength by a previous reviewer**, including the
*Does not establish* list by two.

What we can report honestly is the shape you may have been reacting to: **of the 91-page artifact, 9
pages are main text and the rest is appendix.** If the length is what read as bloated, the main text is
not where
that lives, and rounds 29/31 built the four-object spine precisely so a reader can stop at p9.

### C4 — §16's conceptual diagram: declined on budget

Five main-text floats plus the p3 comparison table, at slack 0. One more costs page 10. The distinction
the diagram would draw is now named in prose (B2) at a cost of eleven words.

### C5 — §19 Q2, sensitivity to target construction / claim difficulty / screening: answered, not run

This is already measured, by **EXP-AE**, the pre-registered covariate audit: sixteen surface covariates
including claim difficulty, response length and style are given *the battery's own estimator*, and the
result is reported against us — **five of ten stay live, the battery is not shown to add over them, and
one criterion-4 positive is withdrawn** (`methodology.tex:83`, *Does not establish* (5)). A dedicated
sensitivity study would strengthen this; it is not what carries the claim, and we are not running new
experiments this round.

### C6 — §19 Q4, a joint / additive decomposition of instruction-following + surface + knowledge conflict: identified, scoped, unrun

A new experiment, and the paper already disclaims the decomposition explicitly rather than implying it:
*"a rule **reaching** benchmark accuracy shows what is surface-reachable **without decomposing** the
detector's signal"*, and *"surface-accessible accuracy, **not a decomposition of the rest**."* We name
this as the natural next study and leave it unrun.

---

## §D. Carried-forward disclosures — restated, not dropped

These are live limitations that earlier rounds disclosed. None is closed by this round.

1. **Generalization stays at 6.** We are not claiming this round moves it. It sits at 6 on two specific
   grounds — **English-only materials**, and **instructed roleplay everywhere outside criterion 4** — and
   the item that addresses it is what the paper calls the **Non-English pilot**: a scoped *n* = 50
   Spanish-or-Mandarin arm with localized claim pairs and a language-appropriate refusal-lexeme
   inventory, specified at `appendix.tex:770` and **identified, scoped and unrun**.
2. **The EXP-C4B surface-rule deltas remain appendix-only**, at slack 0 — and they run against us: at
   12–23 paired claims instead of 6–11, the parameter-free rule *does* separate *D* on the detector's own
   input on **both** replicated positives (Llama 3.1 8B **−30.3 pp**, *p* = 0.0010; Mistral 7B
   **−28.7 pp**, *p* = 0.0057), which retires the EXP-C4 reading that *"the battery's separation is not
   the surface rule's."* So do the per-target paired-claim counts behind the two replications —
   **12 and 17**. We would print all of this in the main text if there were a line for it.
3. **`tab:frontier_panel`'s Anthropic pipeline cell prints 50.5%**, which is the *same-family*
   sensitivity value; the **cross-family primary is 49.5%**, disambiguated in the adjacent paragraph
   rather than in the cell.
4. **This paper reaches rung 4, not rung 5.** The criterion-4 result is *deception-associated at fixed
   elicitation*, not τ<sub>D</sub>: any latent *U* with *U* → *D* and *U* → *S* survives it, and no design
   audited here — ours included — manipulates *D*.

---

## §E. Standing declines from earlier rounds

- **The title stays.** A user decision, reaffirmed: the paper's subject is the audit, and the current
  title names it.
- **The evidence ladder stays Figure 2, not Figure 1.** Figure 1 is the DAG, which is what a reader needs
  before the ladder means anything.

---

## What we think this round is worth, stated plainly

**Your report cannot be fully answered by a revision, because eleven of its twenty items were closed
before it was written.** The four edits are real: B1 is the only move available on **novelty 6**, and
B3/B4 the only moves on **clarity 7**. But they are worth about the one point your own report already
priced in — *"~7/10 after another focused revision"* — not more.

**The remaining gap is an evidence round, not a presentation one.** Generalization sits at 6 for two
concrete reasons, and the cross-lingual arm is the named, scoped, unrun study that addresses one of them.
We would rather tell you that than imply this round closes it.
