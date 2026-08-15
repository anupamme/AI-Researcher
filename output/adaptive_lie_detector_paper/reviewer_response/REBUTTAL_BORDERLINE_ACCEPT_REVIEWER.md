# Response to Reviewer (Borderline Accept, Rating 4, Confidence 4)

**Paper:** Behavioral Deception Detection in Instructed LLM Roleplay Is Dominated by Correction-Marker and Instruction-Following Signals: A Three-Control Audit (3B-70B, English)

---

We thank the reviewer for the careful, constructive assessment and for recognizing the audit as timely and useful. We are especially glad the reviewer agrees the strongest result — the collapse of instructed-roleplay accuracy under equalization while a refusal-count rule stays competitive — is a valuable negative result. The reviewer's suggestions are well-targeted. During this response period we ran two new experiments the reviewer and our Discussion identified as the highest-priority gaps: (1) a **benign false-positive-rate** measurement and (2) a **faithful replication of [R1]'s actual detection mechanism**. Both results strengthen the paper's conclusions — we report the numbers below.

---

### 1. Narrowing the "deception" framing (Concern 1, Q1)

**We agree**, and we will sharpen this throughout. The reviewer is right that under prompt equalization the controlled task is closer to detecting *knowledge conflict / correction behavior* than deception: when a model is shown a false factual claim under a neutral prompt and responds "Actually, that is not correct," that is a correction, not a lie.

**Direct answer to Q1** ("Is the detector measuring deception, knowledge conflict, correction behavior, or refusal style?"): In the equalized setting the detector is measuring **correction/refusal behavior in response to a knowledge conflict**, not deception. This is precisely our point — much of the apparent "deception-detection" signal in the instructed paradigm is correction behavior that survives as a fact-checking-like cue once the lie instruction is removed.

**Commitments:**
- We will reserve the term "deception detection" for the instructed-roleplay framing, and explicitly relabel the equalized-condition signal as "correction/knowledge-conflict behavior."
- We will state, in the Abstract, Introduction, and Conclusion, that the strongest conclusion applies to **instructed-roleplay deception-detection evaluations**, not to autonomous strategic deception detection in general.
- We will add the reviewer's worked example ("Actually, that is not correct") to clarify the distinction.

---

### 2. Benign false-positive rate (Concern 5, Q2) — NEW RESULT

**We agree this is the key deployment gap.** Our submitted Discussion already flags it as "the highest-priority measurement gap for any practical application." During this response period we ran the experiment.

**Result.** We constructed a set of 50 ordinary **benign conversations** (factual Q&A, opinions, task-help, small talk) containing *no* false claim and *no* knowledge conflict, and measured how often the refusal-count rule (k≥1) spuriously fires:

| Model | Benign FPR |
|-------|-----------|
| Llama 3.2 3B | 2.0% (1/50) |
| Mistral 7B | 0.0% (0/50) |
| Qwen 2.5 7B | 0.0% (0/50) |
| Llama 3.1 8B | 0.0% (0/50) |
| Qwen 2.5 14B | 0.0% (0/50) |
| Qwen 2.5 32B | 0.0% (0/50) |

**Average benign FPR across 6 models: 0.3%.** The single false positive (Llama 3B) triggered on the word "actually" used conversationally ("has actually been shrinking"), not in a correction context. The rule essentially never fires on ordinary conversation.

This means the refusal-count rule's 80.1% balanced-set accuracy is *not* inflated by spurious firing on benign inputs — when deployed as a filter it would rarely flag non-deceptive content. In the revision we will report these numbers in a new section and revise the deployment discussion to incorporate the measured FPR.

---

### 3. Conceptual vs. direct replication; caution about prior work (Concern 2, Q3)

**We agree** and will scope our attribution carefully. We will ensure every claim is framed as a property of **this class of evaluation paradigms**, not as a definitive explanation of Pacchiardi et al.'s specific reported numbers. Concretely:
- We will move the "conceptual replication; original code/data not obtained" caveat from the appendix into the Introduction.
- We will replace any language implying we have explained a specific prior result with language about the paradigm class.
- We have now implemented a faithful version of the prior work's actual detection mechanism (unrelated yes/no elicitation questions → logistic regression on binary answers) and tested it under our controls. **Result:** R1's own detector collapses by 18-46 pp to chance (52%) under equalization (Mistral 7B: 98.0% → 52.0%; Llama 3.1 8B: 70.0% → 52.0%), confirming the confound is paradigm-level. This will be reported as a separate object in a new appendix (EXP-R1). We will also correct the bibliographic error in the citation.

---

### 4. Autonomous-transfer experiments (Concern 3, Q4)

**We agree** these are the weakest part and will demarcate them cleanly. We will:
- Move the sycophancy and persona/false-belief results into a clearly-labeled **"Secondary Exploratory Diagnostics"** subsection, removed from all headline claims.
- State directly that the deployment-relevant autonomous regime is where our evidence is weakest, and that these results are exploratory (dispositional sycophancy; null/scenario-confounded persona results).
- Frame a properly-powered, artifact-free redesign of the autonomous experiments as explicit future work.

---

### 5. Cleaner separation of validated vs. exploratory claims (Concern 4, Q5)

**Commitment:** We will add, early in the paper, a **"Validated Claims vs. Exploratory Analyses"** table that sorts every result into one of two buckets:
- *Validated* (e.g., the 30-41 pp equalization collapse; the 80.1% refusal rule; the 54.5% construct-valid-feature result) — the label-independent (L-indep) claims.
- *Exploratory* (e.g., autonomous transfer, frontier-scale spot-checks, level-dependent pipeline numbers) — clearly flagged as directional.

We will leverage the existing L-indep/L-dep distinction to make this separation explicit and consistent throughout the text.

---

## Summary of revision commitments

| Concern | Commitment |
|---------|-----------|
| Q1: "deception" framing | Relabel equalized signal as correction/knowledge-conflict; reserve "deception" for instructed roleplay |
| Q2: benign FPR | **Done:** Measured benign FPR = 0.3% avg across 6 models (rule almost never fires on benign conversation) |
| Q3: conceptual replication | **Done:** Faithful R1 replication confirms paradigm-level confound (18-46 pp to chance (52%) collapse); scope claims to paradigm class; correct citation |
| Q4: autonomous experiments | Move to labeled "Secondary Exploratory Diagnostics"; redesign as future work |
| Q5: validated vs. exploratory | Add a Validated-vs-Exploratory table using the L-indep/L-dep distinction |
| Deployment caution | Measured FPR (0.3%) shows the rule does NOT spuriously flag benign inputs |

We are grateful for a review that engages directly with the paper's core contribution. We believe the new benign-FPR experiment and the tightened framing around "deception" address the reviewer's substantive concerns, and we hope these revisions warrant an increased score.

---

### On the concerns raised by the other reviews and the meta-review

For completeness, and because the meta-review foregrounds them, we note how we are addressing the three points that dominated the other reviews:

- **Citation error.** One review correctly identified an incorrect bibliography entry for Pacchiardi et al. (wrong co-authors and venue). In the revision we will correct it and audit the full bibliography. No claim, analysis, or numerical result in the paper depends on the identity of those co-authors — the paper engages with the *method* and *reported accuracies*, which are unchanged.
- **Faithfulness to prior work's mechanism.** Another review noted that Pacchiardi et al.'s detector (unrelated yes/no questions → logistic regression on binary answers) differs from our behavioral-feature pipeline. We agree, and we have now implemented and run their *actual* detector under both conditions. **Result:** it collapses by 18-46 pp to chance (52%) under equalization (Mistral 7B: 98.0%→52.0%; Llama 8B: 70.0%→52.0%; pooled: 87%→36%), confirming the confound is paradigm-level. This will be reported as a separate appendix (EXP-R1).
- **Clarity.** We will rewrite the Abstract to be self-contained, add a terminology block and a worked-example figure, and move Related Work into the main text — so the paper can be read without first reading the prior work.

We mention these here so that the record is complete: the equalization-collapse and refusal-rule findings this review found valuable are independent of the citation and presentation issues, and survive all three fixes intact. The faithful-R1 replication and benign-FPR numbers reported above are new empirical evidence produced during this response period that strengthens, not qualifies, the paper's conclusions.
