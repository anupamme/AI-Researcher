# Response to Reviewer (6/10, Weak Accept / Borderline, confidence 6/10)

*On `main(20260917-105819).pdf`. Sub-scores: problem importance 9, novelty 7, technical correctness 8.5,
experimental rigor 9, support for the central negative claim 9, support for the positive criterion-4 claim 6,
generalization 5, clarity 8, reproducibility 9.5, ICLR significance 7.5, overall 6.*

Thank you. Your §14 said the score moves on three things and **not** on more experiments: a blinded
independent audit of the criteria, the criterion-4 limitation reframed *as a finding*, and an unmissable
three-way causal display. We did all three. We also ran the one experiment you asked for — and **it came back
against us**, so we lead with that rather than bury it.

---

## 1. We ran your §14.1, and it narrowed one of our own claims (EXP-AA, pre-registered)

You asked for *"perhaps 10–20 benchmark/design cases, given to 2–3 independent researchers, blinded to your
verdicts, with agreement on criteria 1–5 reported."* We ran it on **18 cases** — the ten Apollo rollout sets
and the eight Liars' Bench configurations — with **three rater families** (`nova-pro-v1:0`,
`claude-haiku-4-5`, `palmyra-x5-v1:0`, all via Bedrock Converse at temperature 0), **54 ratings**, each rater
seeing one frozen packet of **release-authored text only** plus the criteria in the paper's own wording, and
nothing else: no paper text, no our verdicts, no other rater's answer. `UNDECIDABLE` was offered explicitly,
because forcing a choice would have inflated α and hidden the failure mode that actually matters. Everything
was fixed in `docs/PREREG_EXP_AA.md` **before any rater was called**, including the interpretation branches.

**The result, stated first because it is the bad one.** Every requirement falls **below** the pre-registered
α = 0.40 "partly decidable" floor:

| | (i) fixed elicitation | (ii) grade ≠ label | (iii) paired realizations | (iv) deployed channel | (v) construct ≠ input |
|---|---|---|---|---|---|
| Krippendorff's α | 0.234 | 0.116 | 0.130 | 0.257 | 0.026 |
| `UNDECIDABLE` | 3.7% | 16.7% | 31.5% | 5.6% | **59.3%** |

Pooled α = 0.309 on 90 units. Panel majority matched our recorded verdict in **21 of 42** judgements with a
recorded referent.

**So the pre-registration's §9 branch fired, and we took it.** Claim (2) no longer says the requirements are
*"decidable from a published description alone."* It now says they are decidable **from a design's
specification**, and that **these releases do not publish one at the resolution the requirements need**:

- `introduction.tex:50`, claim (2): *"…and **decidable from a design's specification**—we decide them on ten
  designs in five groups, four outside deception, **though a blinded panel re-deciding them from *release*
  text alone reproduces only (i)** (EXP-AA)."*
- `experiments.tex:124`, appended to "Stated exactly" (p8): *"**A blinded panel bounds how far that travels
  (EXP-AA, pre-registered)**: three rater families scoring all 18 audited cases from release text alone
  reproduce (i) wherever our packet is faithful (13/13, overturning four vacuous "$E$ fixed" labels) but
  agree weakly elsewhere (α = 0.03–0.26; (v) undecidable in 59% of ratings)—**the requirements are decidable
  from a specification, and these releases do not publish one**."*
- `related_work.tex:73` states it at length and **labels it a retraction of the stronger wording**, not a
  reword.
- New appendix §AB `app:audit_agreement` (pp. 69–71): the design, the packet manifest and md5s, the rater
  roster, the per-requirement α table, the `UNDECIDABLE` rates, **every** disagreement with us, and a defect
  of our own packet construction that we found and quantified rather than fixed silently.

**Two results ran our way, reported at equal prominence and no higher.** (a) The panel overturned, by
majority on all four, the Apollo sets whose published `elicitation_fixed` flag is **vacuous** — unanimously
on `goal_directed_lying`, 2/3 on the other three — reproducing from release text alone a correction we had
not published. (b) Requirement (i) concordance is 14/18 overall and **13/13** once the five
packet-granularity cases are excluded.

**What EXP-AA does not settle, in your terms.** These are **LLM auditors, not independent human experts**.
It tests whether (i)–(v) are decidable from release-authored text by raters blind to our verdicts — the
paper's actual claim — and it is **not** evidence that human domain experts would concur in either
direction. The appendix says exactly that in the same breath as the α table: *"A three-expert human study is
the version of this experiment we could not run, and it would be the right next one."*

## 2. Your §7 was right, and EXP-AA is the evidence for it

You wrote that our classifications are *"defensible judgments, but not mathematical facts."* We are not
arguing. α = 0.03–0.26 across three blinded rater families **is** the quantitative form of your objection,
and it is now in the paper with our name on it. The distinction the paper draws — measurements a reader keeps
even if they reject our criteria, versus verdicts our protocol issues — is unchanged (`experiments.tex:124`,
`appendix.tex:1747`), but the second half is now bounded by a number instead of asserted.

**A correction this surfaced, and we chose to report rather than repair.** Gate 1 of the ten-set audit hashed
the concatenated **system** messages and called $E$ fixed if one distinct hash occurred. That test is
satisfied *vacuously* when a set has no system messages to hash, and **four of the ten sets are in exactly
that position**: both AI-audit sets and the paired-fact set carry the scenario in the *user* turn (8/8, 16/16
and 11/40 distinct user prompts) and goal-directed lying has no message list at all (per-item
`deceive_instruction`/`normal_instruction`, 27 distinct values each). Hashing the whole prompt flips all four
from ✓ to ×. **Three of the ten demonstrably do hold one non-empty elicitation fixed** — both sandbagging
tags and on-policy insider trading — and those three are the only sets any reported contrast is estimated
from, so **no estimated number moves and no *Status* cell moves**: each of the four was already inapplicable
on an independent ground. `appendix.tex:1745` states this as a labelled correction; `tab:external_eligibility`
now shows `0` distinct system prompts and a dagger on those Gate-1 cells, with the dagger defined in the
caption. Our verifier re-derives the counts 4 and 3 from the pinned corpus, so text and corpus cannot drift
apart again.

## 3. Your §14.2 — the criterion-4 limitation, reframed as a finding

`experiments.tex:126` (p9), added before the closing sentence you praised, which stays verbatim:

> **Three stages, and the trend is the result.** Instructed elicitation is high and stable (81.7%, 97.0%
> pooled), equalizing it collapses accuracy to chance (53.7%, 43.3%), and at fixed $E$ the signal returns on
> *a subset* of targets — **removing the confound makes detection markedly less stable across targets**, so
> instructed headline accuracy overstates how much of detection is invariant.

## 4. Your §14.3 — the unmissable three-way display

`methodology.tex:85–89` (p6). The box is **retitled** and gains a **labelled third line**; the Establishes
and Does-not-establish lines and last round's asymmetry sentence are untouched, and the old trailing *"Nor
causal identification of $D\to S$"* clause is **absorbed** into the new line rather than duplicated:

> **What is proven, what is shown at fixed elicitation, and what is unresolved.**
> …
> **Unresolved.** Whether $D$ *causes* $S$. Criterion 4 delivers $D_{\mathrm{operational}} \leftrightarrow S$
> at fixed $E$ — an association at byte-identical elicitation — so any latent $U$ with $U\to D$ and $U\to S$
> survives it. $D\to S$ requires $D$ *manipulated*, which is rung 5, and **no design audited here, ours
> included, reaches it**.

## 5. The remaining items, each with its site and its new string

| Your item | Site | Now reads |
|---|---|---|
| **§4/§15** — *"realized deception" sounds stronger than the evidence* | `abstract.tex:4`, `introduction.tex:50`, `experiments.tex:99`/`:120`/`:122`/`:126`, `conclusion.tex:4`, `appendix.tex` ×4 | **operationally verified deception**, at all 11 sites, one vocabulary rather than two. `:99` is a `tab:external_audit` cell; the p8 pin was re-checked after the substitution and holds |
| **§15** — the abstract clause you wrote out | `abstract.tex:4` | *"with **deception operationalized independently of the detector's input**, prior work's battery separates operationally verified deception on three of five targets"* |
| **§9** — soften *"dominant LLM deception paradigm"* | `abstract.tex:2` | *"and show that the **common instructed-lie paradigm** fails it."* Conceded: `cooney2026didyoulie`'s belief-verified organisms make "dominant" an unnecessary fight |
| **§8** — sharpen the novelty claim | `introduction.tex:87`; `related_work.tex:71` | *"instructed-lie accuracy is **not merely poorly generalizing but uninterpretable as evidence about deception**, because the intervention moves deception and compliance together."* The related-work form adds: *"a detector that generalized perfectly across every lie type would still leave the attribution question open"* |
| **§6** — de-emphasize criterion 5 | `experiments.tex:126` | *"**Criterion 5 (transfer) is exploratory**: 2 of 5, cross-model only, **not part of the argument**."* −14 words, and that cut funded §14.2 above |
| **§11** — promote the 2×2 factorial | `experiments.tex:113` | Its own lead paragraph, **The $2\times2$ factorial: the score tracks the instruction, not the label**, with both numbers you singled out: standardized instruction effect **+1.27–+1.56 SD** on every target ($p<0.001$), truth-value effect smaller and sign-changing, and the true-claim/deceive-instruction cell scoring **below chance (39.0–44.0%)** — both verified against `app:factorial_txd` before printing. ADAGE and EXP-G demoted to one clause |
| **§10** — cut ~10–15% of defensive prose | `introduction.tex:50`; `experiments.tex:113` | Deleted the ~45-word *"Stated plainly: we do not show that LLM deception cannot be detected…"*, which restated `introduction.tex:3` almost verbatim, and the second half of the ADAGE disclaimer, which the appendix roadmap already carries. The verifier asserts *"Stated plainly"* is now **absent** |

**What we did not cut, deliberately.** Your §13 named the establishes/does-not-establish box, the A1–A5
assumption list, the paraphrase probe, the surface-feature caution, the white-box restraint, the honest
nulls and the 2/5 count as strengths; the previous round's reviewer asked that the box *"absolutely remain."*
So §10 was satisfied by deleting **scattered restatements** of the structured cautions, not the structured
cautions themselves.

## 6. Where we agree the paper will not improve

**Novelty 7 stands.** The paper says it itself — *"the protocol and the audit, not the algebra, are what is
new"* — and the related-work appendix concedes the constraint is a standard non-identifiability result. Your
framing that the outcome *"depends on whether the community views the identification/audit framework as
sufficiently novel and consequential"* is not something an edit closes, and we have not tried to edit around
it.

**Generalization 5 stands.** The criterion-4 evidence is on 3B–14B open-weight targets, EXP-R1d is reported
as inconclusive, and the EXP-C4B roster is sealed by `PREREG_EXP_C4B.md`'s substitution rule — re-drawing
targets after seeing counts is precisely what that rule exists to prevent. No new experiment and no new
criterion-4 targets this round.

**Criterion 4 stays observational, at rung 4.** Three of five in EXP-C4, two of those replicating blinded,
one of five *new* targets positive; stratified at fixed $E$, so a latent $U$ with $U\to D$ and $U\to S$
survives it. Your diagnosis of the 6 — *"an observational association between judge-defined deception and
detector behavior, not a causal demonstration"* — is accepted as stated, and §4 above now says so in a
labelled line instead of a trailing clause. This round makes the positive result look **weaker** on purpose.

**And the honest ceiling.** Your own estimate for these three recommendations was 6 → 7–8. We think that is
about right, and we would rather say so than claim more.

## 7. The budget, stated once

The main text ends on **line 485 of page 9 against a ceiling of 485 — zero slack**, so every addition above
was paid for by a named cut, all of them downstream of the page-6 figure pin that would otherwise absorb the
saving: criterion 5 to a pointer (−14 w, your §6), ADAGE and EXP-G to an appendix clause (−10 w, your §11),
and the *"Stated plainly"* restatement (−45 w, your §10). Nothing was funded from §4 Discussion, which is one
paragraph with twelve stacked labels and already maximally compressed. Every future restructure request gets
this same answer as a budget fact rather than a preference.

## Verification

`latexmk` exit 0; **81 pages** (9 of main text, unchanged); 0 overfull hbox, 0 overfull vbox, 0 undefined
references or citations; bibtex 0 warnings; main text ends p9 at ruler 485 with **slack 0**; all eight float
pins on their recorded pages (Figure 1/p2, Table 1/p3, Table 2/p5, Figure 2/p5, Figure 3/p6, Table 3/p8,
Table 4/p14, Table 6/p18). Pages 1, 5, 6, 8, 9, 18, 62–63 and 69–71 were inspected as rendered images, not
as extracted text, because a grown table row is invisible to extraction.

An automated checker of **834 assertions** passes, up from 688, with 146 new for this round. Every changed
string is recorded as a **documented substitution** (old → new, commented with the reviewer item it serves),
and a word-multiset check over the 46 substitutions proves no token entered or left the main text without
being accounted for by a named item. The checks that matter most are the **cross-artifact** ones, which
compare text against data files rather than against other text:

- every α printed in the appendix equals `data/results/audit_agreement.json` to three decimals; the
  `UNDECIDABLE` rate, the 21-of-42 concordance, the 13/13 and the four vacuous cases likewise;
- **if** any requirement's α < 0.40, **then** the unqualified *"decidable from a published description
  alone"* must be absent from every section file and `related_work.tex` must carry the narrowing **and** the
  word *"retraction"* — this is the check that stops a bad EXP-AA result from being quietly dropped;
- no section file may claim the panel overturned all four vacuous cases *unanimously*, because the artifact
  records 3/3 on one and 2/3 on the other three (this caught an overstatement of ours in draft);
- the Gate-1 counts 4 and 3 are re-derived from the pinned Apollo corpus, not read from our prose;
- `realized deception` absent everywhere, `dominant` absent from the abstract, `Stated plainly` absent from
  the introduction;
- the eleven pre-existing pre-registrations are byte-identical (`git diff` empty); EXP-AA is a **twelfth**
  file, not an edit to any of them.
