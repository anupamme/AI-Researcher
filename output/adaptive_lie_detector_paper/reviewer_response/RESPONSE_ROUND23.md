# Response to Reviewer (6/10, Weak Accept / Borderline, confidence 4/5)

*On `main(20260916-123547).pdf`. Sub-scores: correctness 7.5, rigor 8.5, novelty 6.5, clarity 7.5,
significance 8, reproducibility 9.*

Thank you — this is the most useful of the three reports we have received, because it separates what the
paper establishes from how the paper presents it, and its three priorities are ordered the way we would
order them ourselves. We have implemented all three, added the one experiment you asked for, and declined
two items with reasons stated below rather than quietly.

**One thing worth saying up front:** two of your three priorities turned out to be presentation problems
rather than substance problems, and in one case (P2) the paper already contained your preferred framing —
in `§2.1`, under the heading `Proposition (pathway non-separability)` — while the *abstract* still led with
the estimand language you asked us to de-emphasize. Your read was right and our ordering was wrong.

---

## P1 — Make the novelty unmistakable and early

**What you observed.** Claims (1)–(3) are on p2, but the contrast with prior work — that generalization is
not identification, and that fixed elicitation is not ours to introduce — sat on p3, and §1's first
paragraph *ended* on a disclaimer (`Our contribution is not a new causal-identification theorem`) exactly
where the claim belonged.

**What we did.** §1 ¶1 now carries the positive statement, and the honest bound is folded into it rather
than replacing it:

> **What is new**, given prior work that already reports poor generalization and already builds
> fixed-elicitation, belief-verified settings: not a causal-identification theorem, but that the standard
> instructed benchmark is *structurally non-identifying*, that this is operationalizable as an audit
> protocol applicable to a benchmark one did not build, and that the failure is *empirically active*
> across three detector paradigms and both public releases.

It lands on **p2**. The detailed prior-work contrast stays where it was, as the expanded version.

**What we will not claim.** This is a relabeling, not new evidence. The novelty of the *contribution* is
the protocol and the audit, and we say so in the same paragraph (`the protocol and the audit, not the
algebra, are what is new`). If the 6.5 novelty sub-score reflects a judgment that an identification audit
of an existing benchmark is a smaller contribution than a new method, that is a defensible position and
this revision does not answer it — it only ensures the reader is judging the actual claim.

## P2 — Reframe as pathway non-separability; de-emphasize τ_D as a formal estimand

`§2.1` already states the result as pathway non-separability, already says `Nothing below requires
do(D) to be well defined`, and already glosses it in plain words. The **abstract** was the problem. It now
reads:

> **We show the conflation is *active*, not hypothetical.** The reason is structural: **no experiment that
> intervenes only on the instruction can separate a detector response mediated by deception from one
> mediated by instruction-following** — both are descendants of that instruction, and neither pathway is
> independently manipulated or observed. A deception-attribution reading therefore needs τ_D, the effect
> of *deception*, which the identified τ_E — the *instruction*'s effect — neither bounds nor signs, so no
> gain in accuracy, scale, or detector sophistication resolves it.

τ_D is now introduced as the quantity a *reading* of the benchmark requires, not as something we estimate.
`§2.1` needed no change. The edit is net shorter than what it replaced.

## P3 — A compact main-text criterion-4 table, and an explicit non-impossibility sentence

**The table.** Table 1 (p3) already had your four settings as rows with the numbers you wanted
(81.7% / 97.0→43.3% / 3-of-5 / 1-of-5); what it lacked were your two diagnostic columns. We added them to
the **existing** float rather than adding a new one: `E?` (elicitation held byte-identical) and `D?`
(deception graded independently of the condition label, with `†` marking *observational* grading, so not
τ_D). Reducing `\tabcolsep` from 4pt to 2pt freed the width; measured cost was **exactly zero** lines, and
the table is still on p3.

If what you wanted was a *standalone* compact table, that is a page-budget refusal and we would rather say
so than pretend otherwise: the main text is nine dense pages at zero slack.

**The sentence.** §3.5 now ends:

> **The purpose of criterion 4 is not to establish that deception is generally detectable; it is to
> establish that the canonical benchmark's failure is not an impossibility result.**

You were right that this was the sentence that would settle the misreading — `impossibility` appeared
nowhere in the paper before this round.

---

## Item 11 — Criterion 4 is conditional on the operational belief criterion

Genuinely absent, now stated at the point where the latent-*U* caveat already lives (§2.2): criterion 4
`removes the elicitation confound and no other, and what passing it establishes is deception-associated
behavior **conditional on the operational belief criterion**, not deception in a philosophically or
causally privileged sense`.

## Item 12 — Separate objective findings from framework-dependent judgments

Also genuinely absent — `framework-dependent`, `circular` and `operational belief` returned zero hits
across the paper. Addressed in two places:

- **Main text** (§3.5, `Stated exactly`): `the channel facts are measurements, the verdict that they
  violate (iv) or (v) is our criterion's, and a reader who rejects the criterion keeps the measurement`.
- **Appendix** (`Which findings are measurements and which are our framework's judgments`): an
  item-by-item split. On the measurement side: 371/371/54 hashes, 0.0% firing, +4.1/+7.7 pp against AUROC
  0.71/0.94, +84.3 pp, 91.5% vs 10.8%, 9 of 22 cells, every rollout Llama-70B. On the judgment side: the
  (iv)/(v) disqualifications, the inexpressible-vs-failed distinction, the 5–95% inapplicability range,
  and the aggregate verdict. It closes: *these are design judgments, not derivations from anything more
  primitive*, and a reader who sets a different bar for (iv) or (v) reaches a different verdict on the
  same measurements.

We think this is the right resolution of your concern, and we note what it does *not* do: it does not
derive the criteria from anything more primitive. They embed design judgments and now say so.

## Item 13 — Promote the +84.3 pp annotation-channel leakage

It was already in the abstract, Table 3, §3.5 and the Conclusion — missing only from §1's claim (3), which
now names all three failure modes: `an instrument-specific null, **annotation-channel leakage** (+84.3 pp,
the model echoing its own instruction), and **construct recovery**`. The wording is taken from the
Conclusion's existing enumeration, so no new claim is introduced.

## Item 14 — Modern frontier-model checks

**We ran it, and we are reporting it as inconclusive.** EXP-R1d (new Appendix `app:r1d`) was
pre-registered at `docs/PREREG_EXP_R1D.md` and committed before any target was pulled. It re-collects
EXP-R1c's identical v2 contrast on four current-generation ≤ 14B open-weight targets. **Three of the four
are void on the pre-registration's own admissibility gate**, and the reason is our instrument rather than
the models:

| Target | Pilot per-probe ambiguity | §4 verdict and failure mode |
|---|---|---|
| `olmo-3:7b` | **100.0%** | VOID — zero response tokens; the whole 40-token budget goes to a reasoning channel |
| `ministral-3:8b` | **0.0%** | ADMISSIBLE |
| `granite4.2:8b` | **35.0%** | VOID — answers, but inside an unrequested dialogue continuation a yes/no parser cannot read |
| `qwen3.5:9b` | **100.0%** | VOID — as `olmo-3`; the one permitted substitution, spent on `granite4.2`'s failure |

The one admissible target behaves as §3.2 predicts — `ministral-3:8b` is informative instructed (100.0%,
*p* = 0.001) and falls to 54.0% (*p* = 0.327) under equalization, −46.0 pp, with a non-degenerate equalized
channel (6 of 16 probe dimensions still vary; 10 distinct 16-bit vectors across 50 trials). **We are not
reporting that as a recency result.** §7 of the pre-registration fixes, before any target was pulled, what
to do with fewer than two admissible informative targets: report inconclusive, make no recency claim, and
leave `app:vintage`'s "we do not establish that the collapse reproduces on current-generation models"
exactly as written. One target consistent with the prediction is not a panel, and reporting it as one after
three of four targets failed an instrument check would be the move this paper spends its length criticising.

Two consequences you should see stated rather than inferred:

- **We dropped the §3.1 edit we had planned for this item (R7 in our own plan).** It would have promoted
  `app:vintage`'s nine-model list into the main text alongside a clause licensing a recency reading. Under
  branch 5 there is no recency claim to license, and the main text's scope sentence — *no claim below is a
  scaling, recency or effect-magnitude claim* — is true only if we leave it alone. So the concern is
  answered in the appendix and the main text is unchanged.
- **We corrected one of our own errors in the process.** `app:future_directions` item (7) called this the
  cheapest open test in the paper and listed five candidates "each requiring thinking verifiably off",
  flagging only `granite4.2:8b` and `gemma4:12b` for thinking behaviour. `olmo-3:7b` and `qwen3.5:9b` also
  advertise a `thinking` capability, and both voided for that reason. Item (7) now says so, and says the
  test is no longer cheap: the binding constraint is a 40-token probe channel, not model availability.

**We then tried to repair the instrument, declared it as a deviation, and report what it returned.** The
pre-registration's §9 permits one deviation; it was written *after* we saw the voids, so we fenced it off
instead of trusting it not to matter — the deviated cells are archived outside the pre-registered analyzer's
file glob, and their ledger keys are suffixed `[think:false]` so no reader or script can pool the two arms.
Re-invoking the runner with `"think": false` clears both empty-channel voids at the gate (`qwen3.5:9b`
100.0 → **0.0%** pilot ambiguity, `granite4.2:8b` 35.0 → **25.0%**), so both become admissible — and then:

| `[think:false]` | cond | 5-fold | grp-5f | LOO | perm *p* | amb |
|---|---|---|---|---|---|---|
| `qwen3.5:9b` | instructed | **92.0%** | 92.0% | 92.0% | **0.001** | 0.0% |
| | equalized | 54.0% | 54.0% | 4.0% | 0.387 | 0.0% |
| `granite4.2:8b` | instructed | 54.0% | 54.0% | 50.0% | 0.385 | 31.0% |
| | equalized | 44.0% | 50.0% | 44.0% | 0.774 | 39.5% |

**The deviation repaired the instrument and did not rescue the experiment**, and we would rather you read
that from us than find it:

- **Only one of the two admissible targets is informative instructed**, which is the criterion §7 branches
  on — so **the exploratory arm independently reaches the same fewer-than-two condition branch 5 was written
  for**. Whether a deviation *could* have overturned the pre-registered verdict is counterfactual: it did not
  produce a panel either. The sequencing argument holds regardless and we state it too — an instrument changed
  after seeing which targets failed may not then select the reporting branch, which is the exact ordering
  criterion 4 exists to detect.
- **`qwen3.5:9b`'s −38.0 pp looks like the collapse and is weaker than it looks.** Its equalized cell is
  near-degenerate: 1 of 16 probe dimensions varies, 50 trials give 2 distinct vectors, LOO 4.0%. This paper
  reads that configuration elsewhere as *absence of a usable signal* rather than as an accuracy estimate, and
  we read it the same way here. `granite4.2:8b` fails the opposite way — 16 of 16 dimensions vary and 47 of 50
  trials are distinct, yet the instructed cell is at chance and null, so there was no signal for equalization
  to remove and its −10.0 pp says nothing about H1.
- **Our own gate has a defect, and we found it by running the arm.** `granite4.2:8b` passed a 26.0% pilot
  gate at 25.0%, then ran 31.0% and 39.5% ambiguous on its confirmatory cells — *above* the threshold it was
  admitted under. We keep the admissible verdict, because §4 fixes the gate as a *pilot* measurement and
  re-reading a rule after seeing what it admits is the move this paper exists to criticise. But a 160-probe
  pilot estimates a 25% rate to ±3.4 pp (wider, since probes cluster within claims), so **the gate's
  resolution is coarser than the 1.0 pp margin granite passed by** and 31.0% sits inside the pilot estimate's
  own interval. `app:r1d` says so, and says what a future version should do instead.

What holds independent of the outcome:

- The paper's audit machinery already runs against 2025–2026 models — `app:vintage` names nine (Claude
  Haiku 4.5, Sonnet 4.5, Llama 4 Maverick, Mistral Large 3, Qwen3-4B, Gemma 3 4B, Kimi-K2, Palmyra X5,
  Llama 3.3 70B). Your concern was correct about the *criterion-4 roster*, which is pre-2025 **by design**
  and sealed by `PREREG_EXP_C4B.md`'s substitution rule.
- EXP-R1d therefore does **not** add criterion-4 targets. It re-runs EXP-R1c's identical v2 equalization
  contrast — same claims, same probe bank, same estimator, same n = 50 — on current-generation targets, so
  it bounds *recency for that contrast* and nothing else. Four targets, all ≤ 14B, all open-weight, none
  frontier, none closed. `app:r1d` states that limit itself, so the run cannot read as a frontier check —
  and in the event it bounds nothing, because the roster closed at one admissible target.
- Identification is vintage-independent either way: §2.1 is structural, so no outcome of this run can
  repair or worsen it. What EXP-R1d bounds is the *empirical* claim of §3.2.
- The pre-registration fixes an admissibility gate derived from data already in the paper rather than
  chosen for the run: a target is admissible iff its pilot per-probe ambiguity rate is ≤ 26.0%, which is
  the worst cell (`mistral:7b` equalized) the paper already reports. A target failing it is reported as
  **void with its measured rate**, not dropped.

## Item 16 — Title

Adopted verbatim: **What Does Lie-Detection Accuracy Measure? An Identification Audit of Behavioral LLM
Deception Benchmarks.** Beyond your reason, there is a substantive one worth recording: our own
disclaimer (1) denies claiming that detectors measure *only* instruction-following, so the previous title
(`Lie Detection or Instruction Following?`) mildly contradicted the paper's own scope statement.

---

## Not asked for, found while checking EXP-R1d: a reproducibility defect, now fixed

You scored reproducibility 9, so we should say what the integrity checks around the new experiment turned
up about the old ones. `requirements.txt` specified `scikit-learn>=1.3.0` — a lower bound, not a pin — and
under the version we now have installed (1.8.0) the **grouped-5-fold** column did not reproduce the digits
the paper printed. `GroupKFold`'s fold composition changed between versions; nothing else did.

Everything primary reproduces exactly, and we checked rather than assumed: all six targets' instructed and
equalized stratified-5-fold and LOO cells in **both** panels, every permutation *p* at 1000 draws, and the
pooled 97.0% → 43.3% / −53.7 pp at *n* = 300. Four **grouped** cells moved by 2–10 pp:

| Site | Cell | Was | Now |
|---|---|---|---|
| `tab:r1c_v2` | Llama 3.2 3B equalized | 46.0% | **36.0%** |
| `tab:r1c_v2`, `tab:r1_variants` | Mistral 7B equalized (v2) | 54.0% | **58.0%** |
| `tab:r1c_v2` | Pooled equalized | 47.7% | **48.3%** |
| `tab:r1_variants` | Mistral 7B equalized (v1) | 62.0% | **60.0%** |

The paper now prints the 1.8.0 values, `requirements.txt` pins `scikit-learn==1.8.0` with the reason, and
the appendix states the version and which column is version-sensitive. Grouped 5-fold is a secondary
leakage check throughout and no claim rests on it; all four cells stay near or below chance.

**One of these required rewriting an argument, not just a digit.** EXP-R1c's caveat (ii) explained Llama 3.2
3B's below-chance equalized 24.0% partly by noting that grouped folds on the same cell gave 46.0%, i.e. near
chance. At 36.0% that support is gone, so the caveat now rests on what actually carries it — both estimators
below chance, seven sparse and partly claim-aligned dimensions, and the permutation null at *p* = 0.998.
Changing the number and keeping the sentence would have left an argument its own data no longer supported.

## Declined, with reasons

**Item 15 — restructure §3 into Claim 1 / Exp 1–2 / Claim 2 / Exp 3 / Claim 3 / Exp 4.** Declined.
Table 1 *is* that mapping — question, evidence, result, what it licenses, grouped by kind of warrant —
and this round's two new columns sharpen it at roughly 1/20 the page cost. A section restructure needs
page budget the paper does not have: the main text ends on the last available line of p9. We would rather
decline this openly than implement it by cutting a disclaimer or a null result.

**Item 21 — additional detector architectures.** Not done, per your explicit instruction not to. We agree
with the reasoning: the identification claim does not turn on architecture count, and §2.1's corollary
says no detector sophistication resolves it.

**Additional criterion-4 targets.** Not added. `PREREG_EXP_C4B.md`'s substitution rule closes the roster
once a target's trials are graded; all ten are graded, and re-drawing targets after seeing counts is
exactly what that rule exists to prevent. `app:vintage` argues this at length.

---

## Objections that survive this round, stated rather than papered over

- **Novelty remains the exposed flank.** P1 relabels; it does not add evidence. The only thing in this
  round that adds evidence is EXP-R1d, and it speaks to *recency*, not novelty.
- **EXP-C4 is still 3/5 → 2 of 3 replicated → 1/5 on new targets**, and the roster is correctly sealed.
- **The criteria still embed design judgments.** Item 12's revision says so explicitly; it does not make
  them less judgment-laden.
- **The main text is still nine dense pages.** Item 15 is declined for that reason.
- **EXP-R1d is inconclusive, and its roster closed at one admissible target of four.** Three targets void
  on a probe-channel gate is a limit on what we could measure, not a finding about the collapse, and the
  appendix says so in its first sentence.

## What was dropped to fit

Five restatements were cut, each of whose content survives at its canonical site: `tab:external_audit`'s
caption clause on design-vs-effort independence (kept in full at `app:external_audit`, *Materials and
independence*); two of five appendix pointers in §3.4 (`tab:appendix_roadmap` routes the reader); the
21–30× instruction-to-truth-value coefficient ratio (the betas it summarizes are kept: β_E = 1.95–2.03 vs
|β_V| ≤ 0.10, p = 0.0005); one of three trailing appendix pointers in §3.3; and the Discussion's sentence
distinguishing the structural from the survey result (Table 1's caption now carries it, on p3 rather than
p9). No disclaimer, null, MDE, scope statement or `NOT ESTABLISHED` row was cut.

One planned *addition* was also dropped, and for a reason rather than for space: **R7**, the §3.1 sentence
that would have promoted `app:vintage`'s model list into the main text. See Item 14 — under the
pre-registration's inconclusive branch there is no recency claim for it to license, and dropping it is what
keeps §3.1's *no claim below is a scaling, recency or effect-magnitude claim* true.

## Build state

78 pages — 75 plus the three appendix pages of `app:r1d` and its `think:false` arm, all after p9; 0 overfull
hbox, 0 overfull vbox; no undefined references or citations; no bibliography warnings; **main text still ends
on the last line of p9**, so EXP-R1d and its exploratory arm cost zero main-text lines. A 554-check
verification script confirms every protected phrase
from earlier rounds is still present, that the funding cuts moved no word out of the paper without a named
surviving site, that the retitle added no line to the title block, and — new this round — that the
pre-registration was committed before the first result file was written, that every number printed in
`app:r1d` appears in the collected result files, that no pilot cell is discoverable by the analyzer, that
all 26 pre-existing result files are byte-identical to their pre-collection hashes, and that the reporting
branch the appendix claims is the one the ledger's verdicts actually select, and that `fig:r1c_collapse`
differs from its pre-round baseline by exactly the two reprinted digits. The exploratory arm is held to the
same standard: every accuracy and *p* it prints is traced to its own summary artifact, no deviated checkpoint
is left anywhere the pre-registered analyzer's glob would reach it, any confirmatory cell above the 26.0% gate
must be disclosed with its rate, and **how many exploratory targets are informative is derived from the data
rather than asserted** — so if that count ever reached two, the check would start demanding the sequencing
argument be load-bearing and explicit instead of letting the appendix rest on the count.
