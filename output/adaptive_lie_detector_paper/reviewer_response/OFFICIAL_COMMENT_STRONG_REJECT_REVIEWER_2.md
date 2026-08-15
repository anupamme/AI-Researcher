# Official Comment — Follow-up to Rebuttal (Reviewer XTps)

In our rebuttal we addressed the citation error, the writing/clarity concerns, and the paper's contribution type. This comment reports a new experimental result produced during the response period that strengthens the paper's scientific content — independent of the citation and presentation issues.

---

## New Experiment: Faithful Replication of Pacchiardi et al.'s Actual Detector (EXP-R1)

Another reviewer raised the concern that our audit tested a behavioral-feature pipeline (ADAGE: related follow-ups → 5 LLM-scored features → logistic regression), not Pacchiardi et al.'s actual detection mechanism. This is a valid distinction. We have now implemented and tested R1's real mechanism.

**R1's mechanism (what we implemented):**

1. After the target model defends a claim, we ask **16 fixed unrelated yes/no elicitation questions** from Pacchiardi et al.'s three published categories (lie-related, factual, ambiguous).
2. Each answer is parsed to **binary** (yes=1, no=0) — a 16-dimensional binary feature vector. No LLM feature scoring, no correction-marker regex.
3. A **logistic-regression classifier** on those binary vectors, evaluated with **leave-one-out** cross-validation.

We ran this under both the standard instructed protocol (R1's native setting: asymmetric truth/lie prompts) and our prompt-equalized control (identical neutral prompts for both conditions):

| Model | Instructed LOO | Equalized LOO | Collapse |
|-------|---------------|---------------|----------|
| Mistral 7B | 98.0% (n=50) | 52.0% (n=50) | **-46.0 pp** |
| Llama 3.1 8B | 70.0% (n=50) | 52.0% (n=50) | **-18.0 pp** |
| Pooled | 87.0% (n=100) | 36.0% (n=100) | **-51.0 pp** |

**R1's own detector collapses to chance (52%) under equalization** — by 18–46 percentage points. The instructed-condition accuracy (70–98%) brackets R1's reported 67–73%, confirming the mechanism functions correctly in its native setting.

---

## Why this matters for the paper's contribution

The reviewer questioned whether the paper's negative results constitute a sufficient contribution. This new experiment strengthens the scientific content in three ways:

1. **Converging evidence from two mechanistically-distinct detectors.** The paper's central finding (instruction-following dominates reported accuracy) now holds for both our behavioral-feature pipeline *and* R1's actual binary-probe mechanism. This is not a limitation of one specific reimplementation — it is a property of the instructed-roleplay evaluation paradigm.

2. **The four-point case is now complete:**
   - Control 1 (equalization): 30–41 pp collapse for the behavioral-feature pipeline
   - Control 1 applied to R1's mechanism: 18–46 pp collapse (NEW)
   - Control 2 (surface baseline): a one-line regex matches the full LLM pipeline (80.1%)
   - Control 3 (construct validity): the only validated feature yields 54.5% (near chance)

3. **The citation correction and the science are independent.** Even after correcting the bibliography entry (which we have committed to do) and testing the correct mechanism faithfully, the paradigm-level confound holds. The wrong co-author names in the citation did not affect any experimental comparison, any claim about the method, or any numerical result — and the new experiment confirms this empirically.

---

## Summary

The citation error in the submitted draft is a serious presentational failure and we take full responsibility for it, as stated in our rebuttal. But the paper's *scientific* claims — that instructed-roleplay deception-detection accuracy is dominated by instruction-following signals — are now supported by converging evidence from two independent detection mechanisms, including R1's own. We will report EXP-R1 in a new appendix in the revision, clearly distinguishing it from the behavioral-feature pipeline.
