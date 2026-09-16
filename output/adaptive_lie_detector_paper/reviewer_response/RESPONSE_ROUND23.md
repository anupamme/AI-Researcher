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

*(Pending — to be completed before submission. EXP-R1d is pre-registered at
`docs/PREREG_EXP_R1D.md`, committed before any target was pulled, and is in flight as of 2026-09-16.
This section will report its outcome under whichever branch of the pre-registration's §7 the data
selects, including a void or inconclusive outcome.)*

What can be said now, independent of the outcome:

- The paper's audit machinery already runs against 2025–2026 models — `app:vintage` names nine (Claude
  Haiku 4.5, Sonnet 4.5, Llama 4 Maverick, Mistral Large 3, Qwen3-4B, Gemma 3 4B, Kimi-K2, Palmyra X5,
  Llama 3.3 70B). Your concern was correct about the *criterion-4 roster*, which is pre-2025 **by design**
  and sealed by `PREREG_EXP_C4B.md`'s substitution rule.
- EXP-R1d therefore does **not** add criterion-4 targets. It re-runs EXP-R1c's identical v2 equalization
  contrast — same claims, same probe bank, same estimator, same n = 50 — on current-generation targets, so
  it bounds *recency for that contrast* and nothing else. Three targets, all ≤ 14B, all open-weight, none
  frontier, none closed, none a reasoning model. We will state that limit in the paper rather than let the
  run read as a frontier check.
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
- **EXP-R1d is three targets at n = 50**, one generation, ≤ 14B, no frontier or closed model.

## What was dropped to fit

Five restatements were cut, each of whose content survives at its canonical site: `tab:external_audit`'s
caption clause on design-vs-effort independence (kept in full at `app:external_audit`, *Materials and
independence*); two of five appendix pointers in §3.4 (`tab:appendix_roadmap` routes the reader); the
21–30× instruction-to-truth-value coefficient ratio (the betas it summarizes are kept: β_E = 1.95–2.03 vs
|β_V| ≤ 0.10, p = 0.0005); one of three trailing appendix pointers in §3.3; and the Discussion's sentence
distinguishing the structural from the survey result (Table 1's caption now carries it, on p3 rather than
p9). No disclaimer, null, MDE, scope statement or `NOT ESTABLISHED` row was cut.

## Build state

75 pages; 0 overfull hbox, 0 overfull vbox; no undefined references or citations; no bibliography
warnings; main text ends on the last line of p9. A 422-check verification script confirms every protected
phrase from earlier rounds is still present, that the funding cuts moved no word out of the paper without
a named surviving site, and that the retitle added no line to the title block.
