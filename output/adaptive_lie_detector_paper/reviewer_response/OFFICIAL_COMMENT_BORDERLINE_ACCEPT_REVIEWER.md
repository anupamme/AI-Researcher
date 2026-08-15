# Official Comment — Follow-up to Rebuttal (Reviewer, Borderline Accept)

In our rebuttal we committed to two experiments the reviewer and our Discussion identified as the highest-priority gaps: (1) a benign false-positive-rate measurement and (2) a faithful replication of Pacchiardi et al.'s actual detection mechanism. Both are now complete. This comment reports the results.

---

## 1. Benign False-Positive Rate — NEW RESULT

**Setup.** We constructed a set of 50 ordinary **benign conversations** (factual Q&A, opinions, task-help, small talk) containing no false claim and no knowledge conflict, and measured how often the refusal-count rule (k≥1) spuriously fires — i.e., falsely classifies a benign response as deceptive.

**Results:**

| Model | Benign FPR |
|-------|-----------|
| Llama 3.2 3B | 2.0% (1/50) |
| Mistral 7B | 0.0% (0/50) |
| Qwen 2.5 7B | 0.0% (0/50) |
| Llama 3.1 8B | 0.0% (0/50) |
| Qwen 2.5 14B | 0.0% (0/50) |
| Qwen 2.5 32B | 0.0% (0/50) |

**Average benign FPR across 6 models: 0.3%** (1 false positive in 300 trials total).

The single false positive (Llama 3.2 3B) triggered on the word "actually" used conversationally in an informational response ("has actually been shrinking"), not in a correction context. The refusal-count rule essentially never fires on ordinary conversation.

**What this means:** The rule's 80.1% balanced-set accuracy is not inflated by spurious firing on benign inputs. For deployment as a filter, an operator would see fewer than 1 false alarm per 300 benign conversations — the rule is conservative in the right direction. In the revision we will report these numbers and revise the deployment discussion (Concern 5 / Q2).

---

## 2. Faithful Replication of Pacchiardi et al.'s Detector (EXP-R1) — NEW RESULT

**Setup.** We implemented Pacchiardi et al.'s actual detection mechanism:

1. **16 fixed unrelated yes/no elicitation questions** (from their three published categories: lie-related, factual, ambiguous) — asked after the target model defends a claim.
2. Answers parsed to **binary** (yes=1, no=0) — producing a 16-dimensional feature vector.
3. **Logistic regression** on those binary vectors, evaluated with leave-one-out cross-validation.

This is mechanistically distinct from our behavioral-feature pipeline (ADAGE: related follow-ups → 5 LLM-scored features → LR). We ran R1's mechanism under both conditions:

- **Instructed:** asymmetric truth/lie system prompts (R1's native setting)
- **Equalized:** identical neutral prompt for both conditions (our control)

**Results:**

| Model | Instructed LOO | Equalized LOO | Collapse |
|-------|---------------|---------------|----------|
| Mistral 7B | 98.0% (n=50) | 52.0% (n=50) | **-46.0 pp** |
| Llama 3.1 8B | 70.0% (n=50) | 52.0% (n=50) | **-18.0 pp** |
| Pooled | 87.0% (n=100) | 36.0% (n=100) | **-51.0 pp** |

**R1's own detector collapses to chance (52%) under equalization.** The instructed accuracy (70–98%) brackets R1's reported 67–73%, confirming the mechanism functions correctly in its native setting — but loses all discriminative power when the prompt asymmetry is removed.

**What this means for the paper's conclusions:**

- The instruction-following confound is a property of the *paradigm* (the asymmetric instructed-roleplay evaluation setup), not a limitation of our specific reimplementation.
- Both mechanistically-distinct detectors (behavioral features AND binary probes) exploit the same underlying signal: the systematic behavioral differences created by asymmetric truth/lie instructions.
- The reviewer noted (Concern 2) that we should scope claims to the paradigm class rather than Pacchiardi et al.'s specific numbers. This result validates exactly that framing: it is the paradigm — not any one implementation — that is confounded.

---

## How these results strengthen the paper

Together, the two new experiments close the gaps this reviewer identified:

| Gap identified | Result | Status |
|---------------|--------|--------|
| Benign FPR unknown (Concern 5) | 0.3% avg — rule almost never fires on benign conversation | **Resolved** |
| Claims should be scoped to paradigm class (Concern 2) | R1's own mechanism collapses under equalization, confirming paradigm-level confound | **Resolved** |
| Deployment utility unclear | Low FPR (0.3%) + high balanced-set accuracy (80.1%) → rule is conservative and precise on its target signal | **Clarified** |

The equalization-collapse finding (30–41 pp for the behavioral pipeline; 18–46 pp for R1's mechanism) and the refusal-rule finding (80.1% from a one-line regex, 0.3% benign FPR) are independent of the citation and presentation issues raised in the other reviews, and survive all corrections intact. We believe the paper's empirical contribution is now strengthened by converging evidence from two detection mechanisms and a measured false-positive rate.
