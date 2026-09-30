# Response to the round-29 review

*Not part of the paper.*

**Summary: you asked for a conceptual theorem rather than another result, and said so twice. This
round adds one: Theorem 1, a *necessity* result, and adds no experiment. The theorem's job is the
direction of derivation: it derives the membership condition Definition 1 previously assumed, which
is the answer to "an elementary consequence of the definition." And your self-declared most
important technical criticism (that passing the twin admits a control operationally without proving
global invariance) was **already measured in `r74` and disowned by the paper in writing**. It is now
in §3.3 with its numbers: the twin is a nested ladder pinning 1, then 2, then all 3 of the same bags
at exactly `0.500`, and one rung looser an unpinned bag reaches `0.909` on the perturbation it would
have to be blind to.**

The assertion count moves **2129 → 2143**, which is the check that the residual actually entered the
paper rather than sitting beside it.

---

## 0. The scorecard, and the axis that left it

| Criterion | R26 | R27 | R28 | **R29** |
|---|---|---|---|---|
| Soundness / technical quality | 8 | 7.5 | 8 | **8** |
| Presentation / clarity | 7.5 | 7.5 | 7.5 | **8** |
| **Novelty** | 7 | 6.5–7 | 7 | **7 ← sole binding axis** |
| Significance | 7.5 | 7.5 | 7 | **8** |
| Empirical validation | 8.5 | 8 | 8 | **9** |
| Reproducibility | 9 | 9 | 9 | **9** |
| Scope / generalization | — | — | 6 ← binding | **gone from the scorecard** |
| Theoretical contribution | — | — | 6 | **folded into Novelty** |
| **Overall** | **7** | **7** | **7** | **7** (conf 0.75) |

**Round 28's experiment did what four rounds of reframing could not.** `Scope/generalization 6` was
the binding axis; after `r96` (the SCAN audit whose **pre-registered prediction failed**) it is off
the scorecard, Empirical validation moved `8 → 9`, Significance `7 → 8`, and you cite the negative
result as "excellent scientific practice." We are recording that as a lesson about this process, not
a compliment: *running something* retired an axis that arguing had not moved in four rounds.

Which is why this round adds **no experiment**. You said so twice: *"I would not add more
experiments indiscriminately"*, *"Not another empirical result"*, and both axes an experiment would
have served are gone.

---

## 1. §19: the theorem (the one thing that moves 7 → 8)

You wrote: *"Add a concise formal section showing that any evaluation of a representation-level
property necessarily requires an admissibility condition of this form. The current propositions are
too elementary to carry this burden. You need a stronger conceptual theorem, not more algebra."*

**Theorem 1 (Admissibility is necessary, and the ceiling is the only instrument)**: §3.3, proof in
Appendix AN. Fix a metric *M*, a protocol, and a property *P*. Let 𝒜_P be **every** representation
invariant to *P*, and *s* = sup{*M*(*g*) : *g* ∈ 𝒜_P}. If *M*(*h*) ≤ *s*, then two regimes (*h*'s
score produced by reading *P*, and produced by a *P*-blind cue) induce the **same** pair
(*M*(*h*), *M*(*g*)) for **every** comparator *g*, so no comparison of scores separates them. Hence
*M*(*h*) > *s* is necessary as well as sufficient to remove the ambiguity; and a comparator that is
*not* *P*-invariant bounds *s* at no value, so comparing against it decides nothing in either
direction.

Three things we want to be explicit about, because a false theorem would be worse than no theorem:

- **It is necessity only.** It certifies nothing, bounds nothing about non-comparator evidence
  (mechanistic, interventional, behavioural), and makes no family complete. Appendix AN states this
  in the theorem's own note, and states that a *declared* family gives only a **lower** bound on *s*,
so the theorem grants the paper nothing the paper does not already claim.
- **The derivation runs the other way, and that is the whole point.** Definition 1's membership
  condition used to be an assumption; it is now what the theorem forces, with a declared, testable
  family standing in for the invariant class nobody can enumerate. Your objection was that the
  propositions fall out of the definition in a few lines. They do. This does not.
- **It is not vacuous here, and its instance was already in the paper.** The AI~Feynman variable bag
  at `1.000` against the Tree-LSTM's `0.972` *is* a *P*-sensitive comparator winning and refuting
  nothing: the theorem's two-regime ambiguity, realised and asserted.

**The body's count of independent results went down, not up.** *Invariance falsification* is now
**Corollary 1**, the theorem's falsification half, and appendix `prop:nofinite` its other half. This
also serves §11.

### The stance reversal, stated plainly

Rounds 27–28 billed these propositions **down**, at a reviewer's explicit request: that reviewer
warned against selling this as a theoretical ML paper, endorsed the sentence billing the propositions
as scoping, and our round-28 response said in print *"we are not fighting this one."* Round 29 says
that billing is the novelty ceiling. **The two reviews directly oppose each other.**

We resolved it by **adding rather than retracting**: §3.4's scoping sentence stays verbatim, now
scoped to *the propositions*, with one clause added; Theorem 1 is not one of them, because it runs
the other way. Nothing an earlier round endorsed was withdrawn.

---

## 2. §8: your most important technical criticism, already measured

You wrote: *"a control could be blind to your twin and sensitive to another perturbation."* Correct,
and it is measured: `logs/r74_probe_matrix.json`, **17 cells over six corpora**, `n_pass` 17.

| rung | matched on | bags pinned at exactly `0.500` | **max score of an *unpinned* bag** | trained−untrained gap |
|---|---|---|---|---|
| `rotate` | inventory | **1 of 3** | **`0.909`** (tree-local, poly5) | `+0.060 … +0.414` |
| `swap` ← the twin the body reports | inventory + local shape | **2 of 3** | **`0.769`** (token n-gram, oneVarPoly13) | `+0.103 … +0.252` |
| `relocate` | inventory + local shape + **order** | **3 of 3**, zero violations | — | `+0.142 … +0.383` |

So the residual is **not hypothetical and not conceded; it is bounded**. Weakening the test one rung
would have admitted a control scoring `0.909` on the very perturbation it was meant to be blind to,
and the verdict **survives at the strictly most-matched rung**, with the encoder gap positive in all
14 cells that carry one. §3.3 now says this with the numbers; the matrix is a numbered table.

**We have to report how this was sitting in the paper, because it is the worst version of a failure
mode we have now hit twelve times.** Appendix AB already said it in prose, un-numbered, with no body
pointer. Appendix AA said *"We do **not** treat it as part of the central argument."* And the
appendix reading map listed AA among the sections that *"stand alone … rather than being cited from
the body."* **The paper argued itself out of its own best answer to your criticism, in writing**:
the first self-inflicted instance of "a result that exists only in the appendix does not exist."

The re-billing does not contradict AA's caveat, which is kept verbatim: AA disowns `relocate` as
*positive evidence for a composition claim* (variable-to-position binding sits close to variable
identity, so it is not cleanly gate C). That is a different job from using the same matrix to measure
**the coverage of the admissibility test itself**. Two jobs, one matrix, both stated in AA. §3.3's
pointer is the **body's first `\ref` to Appendix AA**.

---

## 3. §11, §21, §13: the contributions and the central sentence

- **§11, four contributions → three**, in one order across the abstract, §1 and the conclusion:
  **method → finding → what survives**. **Round 28's stated reason for declining this was wrong.** It
  cited cross-reference risk; `grep` shows the contributions are cited by number **nowhere** in the
  paper. The collapse was free the first time you asked. We are recording that as a process lesson: a
  decline should be re-tested against measurement, not carried forward.
- **§13, protocol sensitivity elevated**; it is now *inside* the finding, beside the non-monotone
  ceiling, because both say the same thing: what a number is evidence *of* is not a property of the
  number. You called it *"arguably more broadly useful than the particular symbolic-math
  experiments"*, and this is the billing that acts on that.
- **§21, the central sentence is now the theorem in words.** The abstract and §1 both open with *a
  baseline is evidence against an alternative explanation only if it is invariant to the property
  being claimed*, with *"a stronger baseline is not necessarily a stronger control"* as its trailing
  corollary. Zero lines: a swap, and it makes the paper's first sentence and its main theorem the
  same statement. Figure 1's caption keeps the slogan, where it is a figure's takeaway.

---

## 4. §7 and §19's second half: positioning against the existing paradigms

Table 1 previously named shortcut baselines, control tasks, invariance tests, "strongest baseline"
and held-out splits. **The two devices it did not name are the two closest to us**, and both are now
rows with new citations: a **matched control** (Elazar et al., *Amnesic Probing*, TACL 2021) and
**counterfactual evaluation** (Gardner et al., Findings of EMNLP 2020).

**We gave `matched control` `partly`, not `×`, in the comparator-invariance column.** A matched
control *is* invariance by construction along the one dimension it matches; it is simply not
invariance over a *declared family*, and it carries no ceiling. Conceding that the nearest prior
device earns partial credit, and naming the two columns it still lacks, is a stronger answer to
"isn't this repackaging?" than a clean sweep would be. The caption changed accordingly, from *"the
columns that are ours"* to *"the two columns no prior device clears"*: the old wording became
imprecise the moment a `partly` appeared in one of them.

---

## 5. §20, §12, §10, §15, §14, §17

- **§20, the failure taxonomy** is the level table's rewritten fourth column: *if the control wins,
  the result is explained by* **notational identity** / **the operator inventory** / **local
  structural statistics**, plus the two **off-ladder** rows you named: gate C (a split that set no
  novel transformation) and protocol disagreement (the metric, not the representation). No fifth
  column: five prose columns overflow the line width by `97.1pt` at `\footnotesize` here.
- **§12, S2**: operator identity is *legitimate* information, and still cannot support a claim about
  **composition** on its own: reading a multiset is not parsing. A corpus separable at S2 is
  **mis-described, not broken**, and the paper now says no cue here is a cheat.
- **§10**: *"the family is generated, not hand-picked"* is gone, replaced by your formulation:
  **membership is tested rather than assumed, while the candidate family stays an explicit
  researcher-specified scope.** You are right that the procedure is systematic only after step 1.
- **§15**; the audit is about evidence **validity**, not benchmark difficulty: an easy positive that
  a *P*-blind control also solves is exactly the case the audit is *for*, and the depth-8 ladder is
  where difficulty is tested. Stated where the ≈3-member disclosure is made, not elsewhere.
- **§14**: SCAN and NeSymReS are billed as **portability and a boundary condition**, never as
  general validation. SCAN appears as the corpus where the inversion **does not hold**.
- **§17**: the sentence you quoted no longer exists. The contributions rewrite split it, and its
  second half now lives only inside Proposition 1's formal statement, which is where that precision
  belongs. We also measured the rest of the prose before touching it: §3 runs `4.4` bolds per 1k
  characters against the abstract's `5.6`, §1's `6.1` and the conclusion's `6.2`; §3 is not the
  bold-dense part of the paper, so we did not do the §3-wide de-bolding we had planned. What was
  true is that two §3 paragraphs sat at **26%** and **37%** bolded *characters*, where bold stops
  discriminating; three spans that restated an already-bolded claim or marked a secondary list are
  now plain. No words removed.

---

## 6. Two defects this round found in our own file

**Nine bare appendix labels.** This round's new `Appendix~\ref{app:relocate}` rendered as **"Appendix
Z"** with **0 undefined references**: a bare `\label` after a `\subsection*` silently inherits the
previously pinned letter. Round 26 saw this once and treated it as a one-off; auditing for it found
**nine live instances**, and the tenth would have been this round's own new pointer. All nine are now
pinned. **No automated gate here can catch this**; it took reading a rendered page.

**The cold reconstruction gate caught a real misalignment.** Reading the abstract, §1, the box,
Theorem 1, Figure 1 and the conclusion out of the *PDF* with the source closed, item (3) turned out
to be a **different item** in §1 than in the abstract and the conclusion: §1 said "the
demonstration" and never said *narrower than "compositional generalization"*, the phrase the other
two both headline, and which appeared **zero times** in `introduction.tex`. Fixed net-negative,
funded by (3)'s own verbatim restatement of a claim §1 had already made in bold two paragraphs
above, with the same `\ref`.

**A third defect, found after this document was drafted, by reading page 7.** §3.4 cites
**`Theorem 1(iii)`**, and the theorem's printed statement carried **no clause labels**. The clause
existed only in the Appendix AN proof, 60 pages away. No gate could catch it: `(iii)` is literal
text, not a `\ref`. The statement's three clauses are now labelled **(i)/(ii)/(iii)**, which also
breaks a dense five-line sentence into three. We are noting the general form because it is new to us:
**a literal clause number is an unchecked cross-reference.**

---

## 7. What this round did not target, and what happens if Novelty holds

**Soundness 8** and **Reproducibility 9** were left alone deliberately; nothing in the review asks
for either. This round targeted **Novelty** and §8's technical criticism, and nothing else.

If Novelty holds at 7 after a necessity theorem, we will treat the conceptual argument as exhausted.
The honest next lever is then the one that worked at round 25: **declining the axis in the paper's
own text**, which retired two axes outright, and not a third reframing. With round 28's
qualification: that play works only while there is no cheap way to answer the axis instead.

---

## 8. Gate state

0 LaTeX errors · 0 unresolved references or citations · 0 `Float too large` · exactly 2 overfull
boxes, both pre-existing (`6.4211pt` vbox, `3.509pt` hbox) · **83 pages**, appendix exempt · abstract
ends page 1 on *"four primitives are not a library"*, body ends page 9 on the conclusion's last
sentence, page 10 opens with the Ethics Statement · every section heading on pages 4–10 at its
pre-round slot · `bibtex` clean with the two new entries · `verify_claims.py` exit `0` at
**2143/2143 in all three copies**, `statements.tex` printing the full-run count ·
`check_tex_numbers.py` over Theorem 1's paragraph, the residual sentence and the new ladder table,
every unmatched literal given an **assertion** rather than adjudicated away: including the probe
ladder's own rung sizes, which had been unchecked prose · Table 1 and the level table inspected as
**rendered images** (`\checkmark` drops silently from `pdftotext`) · pages 3, 4, 5, 6, 7, 8, 49, 65 and 66
read as rendered text, and every `\ref` to a numbered result audited for the correct type word.
