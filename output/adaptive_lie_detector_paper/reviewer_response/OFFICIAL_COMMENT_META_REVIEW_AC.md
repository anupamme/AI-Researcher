# Official Comment — Response to Area Chair Meta-Review

We thank the AC for the meta-review. We acknowledge the submitted draft's real weaknesses — the citation error, the insufficient distinction from Pacchiardi et al.'s mechanism, and the accessibility problems. We address the three points directly, with new evidence produced during this response period.

## 1. "Implementation differs from Pacchiardi et al." (PHn9)

The most serious scientific concern — now resolved with evidence. PHn9 correctly noted that Pacchiardi et al. ask fixed unrelated yes/no questions and train logistic regression on the binary answers, which our behavioral-feature pipeline does not replicate. We therefore implemented their *actual* detector (16 fixed yes/no elicitation questions → binary vectors → logistic regression, leave-one-out) and ran it under both the standard instructed protocol and our prompt-equalized control:

| Model | Instructed | Equalized | Collapse |
|-------|-----------|-----------|----------|
| Mistral 7B | 98.0% | 52.0% | -46.0 pp |
| Llama 3.1 8B | 70.0% | 52.0% | -18.0 pp |
| Pooled | 87.0% | 36.0% | -51.0 pp |

Pacchiardi et al.'s own detector collapses to chance (52%) under equalization. Its instructed accuracy (70–98%) brackets their reported 67–73%, confirming correct function in its native setting. The instruction-following confound is thus a property of the *paradigm*, not of our reimplementation: two mechanistically distinct detectors — our pipeline (30–41 pp collapse) and their binary-probe mechanism (18–46 pp) — both lose discriminative power under the same control.

## 2. "The core paper is wrongly referenced" (XTps)

We take full responsibility. The entry listed wrong co-authors and venue. Correct citation: Pacchiardi, Chan, Mindermann, Moscovitz, Pan, Gal, Evans, Brauner, "How to catch an AI liar: Lie detection in black-box LLMs by asking unrelated questions," ICLR 2024. We will audit every reference (a second conflated entry is also fixed). Crucially, no claim depends on the co-author identities — the paper engages the method and reported accuracies, both correctly described — and the EXP-R1 result above shows that faithfully implementing the correct mechanism does not change the finding.

## 3. "Hard to follow, even the abstract"

Agreed; we commit to a substantial rewrite: an abstract led by a plain-language problem/finding; a terminology block defining each term before first use; a worked-example Figure 1; Related Work moved into the main body; and structural fixes (orphan §1.1, shorter title, numeric citations). The revision will be self-contained — no need to read Pacchiardi et al. first.

## On the negative-results bar

Two reviewers note the bar is high; we believe the paper now clears it on four converging lines: (1) prompt equalization collapses the behavioral pipeline 30–41 pp; (2) applied to Pacchiardi et al.'s own detector it collapses 18–46 pp to chance (NEW — rules out a reimplementation artifact); (3) a one-line refusal-count regex matches the full pipeline on 6/7 models (80.1%) at just 0.3% benign false-positive rate (NEW, 50 benign conversations × 6 models); (4) the only construct-valid feature yields 54.5%. When we submitted, line 2 and the FPR in line 3 were missing; both gaps are now closed with measured numbers. Two mechanistically distinct detectors collapsing under the same control is decisively stronger than the single-pipeline result in the draft.

We are grateful to answer with evidence rather than only commitments, and respectfully ask the AC and reviewers to reconsider in light of the faithful Pacchiardi replication and the concrete revision plan. We are available for discussion through August 3.
