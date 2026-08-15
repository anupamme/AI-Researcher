# Response to Reviewer (Strong Reject, Rating 1, Confidence 5)

**Paper:** Behavioral Deception Detection in Instructed LLM Roleplay Is Dominated by Correction-Marker and Instruction-Following Signals: A Three-Control Audit (3B-70B, English)

---

We thank the reviewer for the direct feedback, and we want to address the most serious point without hedging: the reviewer is right that our citation of the paper we build on is wrong, and we take full responsibility for it. We correct it below, disclose a second error we found on our own audit, and then respond to the writing concerns with specific commitments.

---

### 1. Incorrect Pacchiardi et al. citation

**The reviewer is correct, and we apologize.** Our bibliography entry for Pacchiardi et al. — the very work our audit is built on — lists incorrect co-author names and an outdated venue. This should not have happened in a submitted paper, and we have no defense for the error itself. The correct citation is:

> Pacchiardi, Lorenzo, Alex Chan, Sören Mindermann, Ilan Moscovitz, Alexa Pan, Yarin Gal, Owain Evans, and Jan Brauner. "How to catch an AI liar: Lie detection in black-box LLMs by asking unrelated questions." In International Conference on Learning Representations (ICLR), 2024.

In the revision we will correct this entry and audit every other reference in the bibliography against its source of record. We note that no claim, analysis, or experimental comparison in the paper depends on the identity of the specific co-authors — the paper engages with [R1]'s *method* (unrelated yes/no elicitation questions + logistic regression on binary answers) and *reported results* (67-73% accuracy). The correction does not affect any substantive content.

We have also identified a second bibliographic error that we will correct: the `perez2022ignore` entry conflates two distinct papers (Schulhoff et al.'s "HackAPrompt" and Perez & Ribeiro's "Ignore Previous Prompt"). In the revision both will be cited correctly with accurate authors, titles, and venues.

---

### 2. Writing clarity: jargon, missing introduction, no related work section

We agree the paper in its submitted form is too difficult to follow. The reviewer identifies a real failure of exposition: technical terms are used before definition, and the paper lacks the structural scaffolding (clear problem statement, related work section, worked examples) that would make it accessible without first reading Pacchiardi et al.

**Commitments for revision:**

**(a) Clear problem statement and research questions.** We will add to the Introduction, in plain language:

- **Problem:** Prior work reports 67-100% accuracy at detecting when LLMs lie in instructed-roleplay settings. But does this accuracy reflect detection of *deception* or detection of *instruction-following artifacts*?
- **Research question:** How much of reported behavioral deception-detection accuracy survives when we control for instruction-following confounds?
- **Approach:** We apply three evaluation controls (prompt equalization, cross-family extraction, surface-lexical baselines) and measure the accuracy drop.
- **Finding:** Accuracy collapses 30-41 percentage points under these controls, and a one-line regex rule matches the full LLM pipeline, indicating the dominant signal is instruction-following, not deception.

**(b) Terminology defined before first use.** We will add a "Key Terms" block at the beginning of the Methodology section defining each technical term with a one-line plain-language gloss:

- *Prompt equalization* — giving both truth and lie conditions identical neutral prompts to remove instruction asymmetry
- *Correction-marker density* — how often the model produces correction/refusal language ("Actually," "That's not correct")
- *Refusal-count rule (k≥1)* — a zero-calibration regex baseline: any correction marker present → predict "truthful"
- *Pooled-LOO* — leave-one-out accuracy pooled across all models
- *Construct validity* — inter-annotator agreement (human vs. LLM raters) measuring whether features capture what they claim
- *L-indep / L-dep* — claims that are/aren't affected by features with poor construct validity
- *ADAGE* — our pipeline (Adaptive Deception Assessment via Generated Exchanges): asks follow-up questions, extracts 5 behavioral features, feeds them to logistic regression

**(c) Related Work moved into the main text.** The submitted draft placed Related Work in Appendix A. The revision will include it as Section 2 in the main body, covering: behavioral probing (Pacchiardi et al., Azaria & Mitchell), representation engineering (Zou et al., Burns et al.), sycophancy and strategic deception (Hubinger et al., Greenblatt et al., Scheurer et al.), and red-teaming (Ganguli et al., Perez et al.).

**(d) New Figure 1: worked pipeline example.** A schematic showing a concrete claim ("Water boils at 85°C"), the instructed vs. equalized system prompts side by side, an example model response, the extracted features, the refusal-marker check, and the classifier decision — with annotations showing where each control intervenes.

**(e) Rewrite the Abstract.** We will rewrite the Abstract to be self-contained and readable — leading with a plain-language statement of the problem, the question, and the single headline finding, rather than the dense stack of results it currently opens with.

**(f) Structural fixes:**
- Shorten the title (e.g., "Do Behavioral LLM Lie Detectors Measure Deception? A Three-Control Audit")
- Add a proper §1.2 or flatten the orphan §1.1 into Introduction prose
- Switch to numeric citations per NeurIPS formatting

---

### 3. "Without clearly articulating the problem statement, research hypotheses, and goal of the audit"

Beyond the structural fixes above, we will explicitly state in the Introduction:

**Hypothesis:** The high detection accuracies (93.9-100%) reported in instructed-roleplay deception evaluations are primarily driven by instruction-following artifacts (asymmetric system prompts that leak the truth/lie label through behavioral side-channels) rather than genuine deception signals.

**Audit protocol:** We test this by applying three controls that each isolate a different artifact source:
1. *Prompt equalization* — removes instruction asymmetry; any accuracy drop is attributable to instruction-following.
2. *Cross-family feature extraction* — removes same-model bias; any accuracy drop is attributable to self-preference.
3. *Surface-lexical baseline* — bounds the contribution of LLM feature extraction; if a regex matches the pipeline, the signal is lexical, not latent-behavioral.

**Goal:** Determine whether behavioral deception-detection accuracy survives these controls, and if so, in which regime (instructed roleplay, semi-autonomous sycophancy, or fully-autonomous deception).

---

### 4. On the paper's contribution type

We agree with the reviewer's classification: this is a negative-result / methodological-audit paper, and the significance bar is high. Our contribution is not a new detection method but a three-control evaluation protocol that:

1. Identifies instruction-following as the dominant signal (30-41 pp accuracy collapse under equalization)
2. Shows a one-line regex matches or exceeds the full LLM pipeline (80.1% vs. pipeline on 6/7 models)
3. Demonstrates that the only construct-validated feature yields 54.5% (barely above chance)
4. Provides preliminary evidence that the signal does not transfer to autonomous settings (null results on persona/false-belief scenarios)

**Additional evidence produced during this response period.** Another reviewer raised the concern that our audit tested a behavioral-feature pipeline, not Pacchiardi et al.'s actual detector mechanism (unrelated yes/no probes → binary logistic regression). We implemented R1's faithful mechanism and ran it under both conditions:

| Model | R1-faithful instructed | R1-faithful equalized | Collapse |
|-------|----------------------|---------------------|----------|
| Mistral 7B | 98.0% | 52.0% | -46.0 pp |
| Llama 3.1 8B | 70.0% | 52.0% | -18.0 pp |
| Pooled | 87.0% | 36.0% | -51.0 pp |

R1's own detector also collapses under equalization (by 18-46 pp to chance), confirming the confound is a property of the detection *paradigm*, not our reimplementation. This strengthens the audit's scientific content.

We believe this is a valuable contribution precisely because it challenges a growing body of work that reports high detection accuracies without controlling for instruction-following artifacts. We will make this contribution statement more prominent and explicit in the revision.

---

### Summary of revision commitments

| Issue | Action |
|-------|--------|
| Hallucinated reference | Correct Pacchiardi et al. entry; audit full bibliography |
| No problem statement | Adding explicit problem/hypothesis/goal to Introduction |
| Jargon without definition | Adding Key Terms block before first use of all technical terms |
| No Related Work | Moving from Appendix A into main text §2 |
| No illustrative figure | Adding Figure 1 with worked pipeline example |
| Hard-to-follow abstract | Rewriting the Abstract to lead with a plain-language problem/finding |
| Too-long title | Shortening to ≤15 words |
| Orphan §1.1 | Restructuring Introduction |
| Citation format | Switching to numeric |
| R1's actual mechanism | **Done:** Faithful R1 detector collapses 18-46 pp to chance (52%) under equalization (new appendix EXP-R1) |

We acknowledge that the submitted draft failed to make itself accessible, and we are committed to a substantial rewrite. We hope the reviewer will consider whether the *scientific content* — particularly the three-control collapse result, the regex-vs-pipeline finding, and now the faithful-R1 replication confirming the paradigm-level confound — merits publication once the presentation is brought to standard.
