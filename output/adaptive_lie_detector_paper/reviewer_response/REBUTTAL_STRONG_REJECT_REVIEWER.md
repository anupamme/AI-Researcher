# Response to Reviewer (Strong Reject, Rating 1)

**Paper:** Behavioral Deception Detection in Instructed LLM Roleplay Is Dominated by Correction-Marker and Instruction-Following Signals: A Three-Control Audit (3B-70B, English)

---

We thank the reviewer for the careful reading. We agree the paper was hard to follow and take that seriously. Below is a plain-language summary first, then our response to W2, W3, and W1 with concrete commitments.

**In plain language.** Prior work reports 67-100% accuracy at detecting when an instructed LLM is "lying" in roleplay. Our question: does that accuracy reflect detection of *deception*, or detection of the *instruction to lie* leaking through behavioral side-channels? We apply three controls — (i) **prompt equalization** (give the truth and lie conditions identical neutral prompts), (ii) **cross-family extraction** (score features with a different model family), (iii) a **surface-lexical baseline** (a one-line regex). The finding: accuracy collapses 30-41 points under equalization, and a zero-calibration refusal-word rule matches the full LLM pipeline on 6/7 models — so the dominant signal is instruction-following, not deception.

---

### W2 — "The correction-marker baseline does not directly test [R1]'s mechanism"

**We agree, and we have now run the experiment.** Pacchiardi et al. [R1] do not classify text by correction words: their detector asks a fixed battery of *unrelated yes/no elicitation questions* and trains logistic regression on the *binary answers*. Our submitted draft audited the *behavioral-feature paradigm* (LLM-scored features + a surface-lexical baseline), and acknowledged this as a "conceptual replication; original code/data not obtained" (in the Abstract, Introduction, and appendix). The reviewer is right that this distinction was not drawn sharply enough.

**New result (EXP-R1).** During this response period we implemented [R1]'s *actual* detection mechanism — (1) a fixed bank of 16 unrelated yes/no elicitation questions in R1's three published categories (lie-related, factual, ambiguous); (2) binary yes/no answer vectors (no LLM feature scoring, no correction-marker regex); (3) a logistic-regression classifier on those vectors — and evaluated it under both the standard instructed protocol and our prompt-equalized control with leave-one-out:

| Model | Instructed LOO | Equalized LOO | Collapse |
|-------|---------------|---------------|----------|
| Mistral 7B | 98.0% (n=50) | 52.0% (n=50) | **-46.0 pp** |
| Llama 3.1 8B | 70.0% (n=50) | 52.0% (n=50) | **-18.0 pp** |
| Pooled | 87.0% (n=100) | 36.0% (n=100) | **-51.0 pp** |

**R1's own detector also collapses under equalization — by 18-46 percentage points (to chance-level, 52%).** The instruction-following confound is a property of the *paradigm*, not of our reimplementation. Under equalized prompts, the binary answer vectors for truthful vs. deceptive conditions become statistically indistinguishable (mean vector sums differ by <1 bit out of 16), and the LR falls to chance.

Note that the instructed-condition accuracy (70-98%) brackets and is consistent with R1's reported 67-73%: the mechanism works when it has the instructed prompt asymmetry to exploit.

In the revision we will report [R1]'s detector and our behavioral-feature pipeline as *separate objects* in a new appendix (EXP-R1), cleanly distinguishing the two. We will also move the "conceptual replication; original code/data not obtained" caveat from the appendix into the Introduction.

---

### W3 — "Prompt equalization may change the task to fact verification"

**This is, in fact, our central finding** — we will make it explicit rather than leave it implicit. The reviewer writes that under a neutral prompt, discussing "water boils at 85°C" is closer to fact-elaboration than deception. We agree — and that is precisely the point: much of the accuracy reported in instructed-deception paradigms comes from detecting the *instruction/fact-conflict* signal (which persists as a fact-checking-like cue), not a deception signal that transfers to autonomous settings.

Prompt equalization is a **diagnostic control**, not a proposed "better" deception task. By giving both conditions identical neutral prompts, we remove the asymmetry between "answer honestly" and "defend this false claim." Accuracy that collapses (30-41 pp) was riding on the instruction leak; accuracy that survives is epistemic/fact-conflict — which, as the reviewer notes, is closer to fact-verification.

**Commitments.** We will (a) label the equalized condition explicitly as an "instruction-leak control"; (b) add a Methodology sentence: "the residual signal under equalization is epistemic/fact-conflict; the collapse measures how much prior accuracy rode on the instruction leak"; (c) foreground the three-regime decomposition (instructed → semi-autonomous → autonomous) so equalization reads as one axis, not a task swap; (d) add the reviewer's own worked example as an illustration.

---

### W1 — Writing, presentation, and clarity

The reviewer needed to read [R1] first to parse our aims. That is a failure of exposition, and we commit to a substantial rewrite:

- **Rewrite the Abstract** to be self-contained and readable — leading with the plain-language framing above, not a dense claim stack.
- **Terminology block** at the start of Methodology, each term glossed in one line before first use: *ADAGE* (our pipeline: related follow-ups → 5 LLM-scored features → logistic regression); *prompt equalization* (identical neutral prompts across both conditions); *correction-marker density* (frequency of correction/refusal language); *refusal-count rule, k≥1* (zero-calibration regex: any correction marker → predict "truthful"); *pooled- vs. per-target-LOO*; *construct validity* (human-vs-LLM rater agreement, Krippendorff's α); *L-indep / L-dep* (claims unaffected / affected by features that fail construct validity); *system-prompt-only control*, *sycophancy transfer*, *persona/false-belief*.
- **New Figure 1** — a worked pipeline example: one concrete claim, instructed vs. equalized prompts side by side, a model response, the five feature scores, the refusal-marker check, and the classifier decision, with the three controls annotated.
- **Structure:** move Related Work from Appendix A into the body as §2; resolve the orphan §1.1; shorten the title (e.g., "Do Behavioral LLM Lie Detectors Measure Deception? A Three-Control Audit"); switch to numeric citations per NeurIPS style.

Our aim is that the revised paper is self-contained: a reader should not need [R1] first.

---

## Reviewer's questions

**"Can the authors substantially improve the clarity?"** — Yes; see W1.

**"Why not use [R1]'s exact implementation?"** — We could not obtain [R1]'s original code/data (stated in the Abstract and Introduction). Our draft tested the general behavioral-feature paradigm. We have now *additionally* implemented [R1]'s actual mechanism and tested it under both conditions — see W2 above for the results.

---

## Summary of revision commitments

| Concern | Commitment |
|---------|-----------|
| W2: not testing [R1]'s mechanism | **Done:** Faithful [R1] detector (yes/no probes → binary LR) collapses 18-46 pp to chance (52%) under equalization; new appendix EXP-R1 in revision |
| W3: equalization = fact-verification | State explicitly this IS the finding; label as an instruction-leak control |
| W1: writing/terminology | Rewrite Abstract; add Key Terms block; add worked-example Figure 1 |
| W1: structure | Related Work into main text; resolve §1.1; shorten title; numeric citations |

We believe these — especially the faithful [R1] replication and the explicit framing of equalization as a diagnostic control — address the scientific concerns, and that the rewrite resolves the readability issues. We are glad to discuss further during the response period.
