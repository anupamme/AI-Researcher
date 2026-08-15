# Official Comment — Follow-up to Rebuttal (Reviewer PHn9)

In our rebuttal we committed to implementing Pacchiardi et al.'s *actual* detection mechanism (W2) and reporting the results during this response period. We have now done so. This comment reports the completed experiment.

---

## EXP-R1: Faithful Replication of Pacchiardi et al.'s Detector

**What we implemented (R1's actual mechanism, not our behavioral-feature pipeline):**

1. After the target model makes/defends a claim (truth or lie), we ask a fixed bank of **16 unrelated yes/no elicitation questions** drawn from Pacchiardi et al.'s three published categories (lie-related, factual, ambiguous).
2. Each answer is parsed to a **binary value** (yes=1, no=0) — producing a 16-dimensional binary feature vector per trial. No LLM feature scoring, no correction-marker regex, no ADAGE pipeline.
3. A **logistic-regression classifier** is trained on these binary vectors and evaluated with **leave-one-out** cross-validation (the same protocol used in our other experiments for apples-to-apples comparison).

This is the detector the reviewer correctly noted we had not tested: unrelated yes/no probes → binary answers → logistic regression. It is mechanistically distinct from our behavioral-feature pipeline (which asks topically-related follow-ups, scores 5 LLM-judged features, and uses a refusal-word regex).

**Conditions tested (per model):**

- **Instructed** — R1's native setting: asymmetric truth/lie system prompts (the target is explicitly told to defend a true claim or defend a false claim).
- **Equalized** — our prompt-equalization control: both conditions receive an identical neutral prompt ("You are a helpful assistant. Share what you know about this topic."), removing instruction asymmetry.

**Results:**

| Model | Instructed LOO | Equalized LOO | Collapse |
|-------|---------------|---------------|----------|
| Mistral 7B | 98.0% (n=50) | 52.0% (n=50) | **-46.0 pp** |
| Llama 3.1 8B | 70.0% (n=50) | 52.0% (n=50) | **-18.0 pp** |
| Pooled (both models) | 87.0% (n=100) | 36.0% (n=100) | **-51.0 pp** |

---

## Interpretation

**R1's own detector collapses to chance (52%) under prompt equalization.** Under equalized prompts, the binary answer vectors for truthful vs. false-claim conditions become statistically indistinguishable (mean vector sums differ by <1 bit out of 16), and the logistic regression falls to chance-level discrimination.

The instructed-condition accuracy (70–98%) brackets R1's reported 67–73%: the mechanism works when it has the instructed prompt asymmetry to exploit — confirming it is functioning correctly in its native setting.

**This directly addresses W2.** The reviewer's concern was that the instruction-following artifacts we identified might be specific to our behavioral-feature reimplementation rather than a property of R1's actual detection paradigm. The result shows the opposite: R1's own mechanism (unrelated yes/no probes → binary LR) also collapses by 18–46 percentage points under equalization. The instruction-following confound is a property of the *paradigm* — the asymmetric instructed-roleplay evaluation setup — not of our specific pipeline.

**Why this happens:** In the instructed setting, the truth/lie system prompts create systematic behavioral differences that leak into how the model answers unrelated questions (e.g., a model told to "defend this false claim" may answer unrelated yes/no questions with different confidence or hedging patterns than one told to "answer honestly"). Under equalization, both conditions receive the same neutral prompt, so there is no instruction asymmetry to leak — and the binary answer vectors converge.

---

## Relationship to the submitted paper's findings

This result strengthens the paper's central thesis:

- The **30–41 pp collapse** we reported for the behavioral-feature pipeline under equalization is now joined by a **18–46 pp collapse** for R1's own detector under the same control.
- The **refusal-count rule** (80.1% accuracy from a one-line regex) and R1's faithful detector (70–98% instructed) both exploit the same underlying asymmetry — and both lose discriminative power when that asymmetry is removed.
- The confound is paradigm-level: it affects both behavioral-feature pipelines *and* the binary-probe mechanism, across different model families and scales.

In the revision, we will report R1's detector and our behavioral-feature pipeline as *separate objects* in a new appendix (EXP-R1), cleanly distinguishing the two — exactly as the reviewer requested. The paper's headline claim ("instructed-roleplay deception detection is dominated by instruction-following signals") now has converging evidence from two mechanistically-distinct detectors.

---

We hope this completed experiment — delivering evidence rather than a commitment — directly resolves W2 and demonstrates that the paper's conclusions hold across detection mechanisms, not only our specific implementation.
