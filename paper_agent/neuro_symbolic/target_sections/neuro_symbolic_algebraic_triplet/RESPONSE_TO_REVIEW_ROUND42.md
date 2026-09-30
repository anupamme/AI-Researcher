# Response to the round-42 review

**No new experiments, no new sentences of consequence, and not one number changed. What changed is the
markup: 206 bolded clauses in the body are now 98, of which ~48 are table headers and row labels, so
prose emphasis fell from ~156 marks to ~50, across ~50 body paragraphs. 93 pages, body still ends on
page 9, `verify_claims.py` at `2337/2337`: the one added assertion is described in §6.**

You wrote that we *"don't need another major experiment"* and that the blocker is weakness 5: the paper
*"reads like an audit dossier rather than a research paper."* We agree, and we took that literally rather
than rhetorically: we measured the dossier.

---

## 0. This is a different reviewer on the same draft, and every ask is answered as current

Round 41 scored this text **7/10** on a **twelve**-axis scorecard; you score it **6/10** on a **seven**-axis
one. That is not a regression on any shared axis; it is a different rubric. Three internal markers confirm
you read the post-round-41 build: you cite the `0.676` adversarially-searched composite (added in round 41),
the 93-page length (round 41 added 3 pages), the withdrawn NeSymReS claim, and the five-margin novelty chain.

**We spent the staleness card two rounds ago and are not spending it again.** Every ask below is answered
against the current text. Where an ask was already satisfied, we say which page it is on and what we changed
about its *form*.

---

## 1. The measurement that is itself the answer

Before editing anything we counted, because "too defensive" and "too long" are the two complaints most often
answered by deleting the wrong thing. Every ★★★★★ and ★★★★☆ item in your prescription turned out to be
**already present in substance and defeated by presentation**:

| your ask | what was already there | why it still read badly |
|---|---|---|
| rewrite the conclusion as 3 takeaways | `conclusion.tex` was **already** `(1)/(2)/(3)` | one 115-word paragraph carrying **10** bolded clauses |
| give §1 a numbered contribution list | §1's last paragraph **already** had `(i)/(ii)/(iii)` | inline inside ~350 words |
| headline the protocol disagreement (`.881` vs `.511`) | a bold `Takeaway:` lead in §4.4, **and** in the abstract, **and** in §1: three separate statements | last subsection of the last body page |
| stop overselling Theorem 1 | its paragraph title **is** a previous reviewer's own de-sell sentence | buried in a run-on paragraph |
| make Table 1 less triumphalist | its caption **already** says *"the last column is × on every row, ours included"* | a 9×7 grid of ✓/× reads as a scorecard before the caption is reached |
| turn S1/S2/S3 into an intuitive table | a 4-row tabular existed | its third column was abstract prose (*"anything structural"*), not forms |
| show `x+y` vs `y+x` vs `(x+0)+y` | §1 had all three | as prose, mid-paragraph, on page 1 |

Two numbers made the diagnosis concrete. The body carried **206 `\textbf` and 229 `\emph` in 6,541 words**:
one emphasis mark per ~15 words, with **nine bolded clauses in a single paragraph** of §4.2 and **19 in a
416-word abstract**. And Table 2's Verdict column bolded **17 of its 18 cells**, under a column header that
already said "Verdict".

**A page on which everything is shouted has no emphasis on it at all.** That is the audit-dossier effect in
its measurable form, and it is what this round removed.

---

## 2. What changed, ask by ask

### ★★★★★ #1: the abstract, rewritten around one story (p1)

Rewritten in place, same four paragraphs, **19 → 6 bolded clauses**, 421 words. The order is now: the
principle and the AI Feynman inversion → what admissibility auditing estimates and what passing does *not*
buy → **the twin first**, `0.994` against `0.500` *by proof* → **`0.894` against `0.676`, a margin of
`+0.22`** → the protocol disagreement, `.881` and `.511` → what survives, and what it is not.

**`0.894`, `0.676` and the margin now appear on page 1 for the first time.** Your pre-submission change #1 was
to make `0.676` the main baseline and lead with the margin rather than the ratio; the abstract now prints
*"a margin of $+0.22$, as a ratio $1.3\times$ and not the flattering $6.1\times$ against a variable-blind
bag"*: the de-sell kept, deliberately, because the flattering ratio is the one a reader would otherwise
compute.

### ★★★★★ #2: the twin as the centrepiece (p1, p2)

Textual elevation, in three places: the twin is now the abstract's **first** result; §1's twin paragraph is
retitled **"The sharpest form of the test: a ceiling that is a theorem"**, which names its result in its
title; and its closing sentence became *"No other rung's ceiling is a theorem rather than the result of
exhausting baselines."* Figure 1 is unchanged; see §3 below for why.

### ★★★★★ #3: 30–40% of the Introduction's conceptual load removed (p2)

**32 → 13 bolded clauses**, and the symbol `$\mathcal{X}$` is **retired from the body entirely**; it
appeared exactly once in nine pages against 21 times in the appendix, a symbol introduced for a single use.
It is now the words *"extensions outside the criterion"*; the appendix defines it in place. `$\mathcal{A}_P$`
(3 uses) and `axis C` (2) were each classified occurrence by occurrence and kept: every one is referenced by
a later sentence or a theorem statement.

The meta-language changed register rather than content, per your §14: *"the result we would put first"* and
*"What we claim, exactly, is Table 2"* are gone; the latter is now *"Table 2 is the ledger."*

### ★★★★☆ #5: S1/S2/S3 now shows the forms (p4)

The third column was retitled **"It cannot tell apart"** and its three cells replaced with your own examples:

| Level | The control reads | It cannot tell apart | If it wins, the result is explained by |
|---|---|---|---|
| **S1** variable identity | *which* symbols appear: purely notational | $x{+}y$ from $x{\cdot}y$ | **notational identity** alone |
| **S2** operator/arity inventory | *which* operators, over how many variables | $(x{+}y){\cdot}z$ from $x{\cdot}(y{+}z)$ | the **operator inventory** |
| **S3** order, depth, local shape | adjacency, depth profile, parent–child statistics, subtree sizes | $x{+}y$ from $y{+}x$ | **local structural statistics** |

No new column, no width change, and provably height-neutral: every row's height is set by column 2, and the
new cells are shorter than the prose they replaced.

### ★★★★☆ #4, #16 and #11: §4 reads as findings; Table 2 stops shouting (p5, pp7–9)

The margin is now printed in §4.2 beside the ratio clause, derived from the logs rather than from the paper's
own three decimals. **Table 2's Verdict column: 17 bolds removed, no word, number or row height changed.**
The §4.2 paragraph that carried nine bolded clauses now carries one: *"the verdict still holds, `0.181`
clear"*, and the other eight sentences are unchanged text.

Table 1's geometry and caption are untouched; see §3.

### ★★★☆☆ #13: the run tags are out of the narrative, and cost us nothing

**All 22 inline `(tag \texttt{r100})` citations are gone from the body; every `\ref` stayed.** This was the
round's funding: ~440 characters, ~4 body lines. Nothing reproducible was lost, because the appendix already
tags every run and `statements.tex` already scopes the promise there: *"each EQNET run is tagged in the
appendix subsection that reports it."*

### ★★★☆☆ #18: the conclusion (p9)

**10 → 3 bolded clauses**, one per takeaway, each starting its own sentence at a line's head. The theory
takeaways `(1)` and `(2)` share a paragraph; `(3)`, the empirical scope, has its own. See §4 for why it is
two paragraphs and not three.

### weakness 5 / §21.5: the appendix front matter is a reading path, not a wall (p15)

The ~750-word *"How to read this appendix"* paragraph became a lead sentence plus **two four-item
description lists**: the four objects on the critical path, then the four bands (A–K provenance, L–Z
protocols, AA–BB the experiments behind the main text, Proofs). Its duplicated description of its own
organisation collapsed into one list, which is what funded the vertical space. Every pointer kept; ~30 bolds
became ~10; the appendix is not shorter and the paper is still 93 pages.

---

## 3. What we declined, and why

**§17's nine-page restructure.** Declined. Your own §19 keep-list and the restructure disagree: the
restructure moves the family-relative ceiling analysis and the coverage/S1–S3 distinction into a
"Framework" section that would separate each from the result that motivates it. The current order is also
the order 17 frozen reviewer-map rows quote against; moving a section moves a claim out of the section its
`\ref` names. In-place reformatting delivered the same clarity gain at zero risk to that machinery.

**§21.5's appendix compression.** Declined, on your own grounds. Everything your §19 says to keep lives
there: the family-relative ceiling, the trained-readout closure, the 28-descriptor adversarial search, the
corrected nulls, the NeSymReS withdrawal, the explicit `F_3`-incompleteness statement, and the
reproducibility infrastructure that earned the 9/10. Cutting it would orphan 21+ body→appendix `\ref`s, and
ICLR sets no appendix limit. We answered the fatigue complaint with the reading path instead.

**The proposed abstract text.** We used your structure and none of your sentences. Your draft deletes all
three of the abstract's pinned literals (*"no admissible family can turn it into a certificate"*, *"Four of
the audited"*, and *"four primitives are not a library"*) each of which is a scoping clause a **previous**
reviewer required, and each pinned at exactly one occurrence by a gate script. This is the seventh
consecutive round in which a reviewer-supplied sentence about this paper is lossier than the sentence it
would replace, which is why the gate exists.

**Figure 1's row reorder.** Declined on mechanics, not on merit. The twin already occupies rung 4 with the
caption's opening sentence (*"The twin is the one rung whose ceiling is known by proof"*) and a verdict cell
widened last round. Reordering the four evidence rows means re-fitting four absolute-y TikZ blocks against
rendered anchors: the exact operation that produced three invisible collisions in one rebuild here,
undetectable by `pdftotext` and by every gate in this repo. The remaining gain is cosmetic; the downside is
a silent overprint on the paper's entry-point figure.

**A one-clause reading instruction in Table 2's caption.** Declined **on measurement, not preference.** After
this round the per-page slack against a full page of `732.014pt` is: p1 `+0.000`, p3 `+0.000`, **p4 `+0.736`**
(0.07 of a line), p6 `+0.070`, **p7–p11 `+0.000`**. There is no page with room for a caption line, and Table
2's caption growing 3→7 lines once repacked five pages of floats. Nothing was added.

**A literal Question / Test / Result / Interpretation template per experiment (§16).** Declined on line cost:
four labels across ~8 paragraphs is ~8 body lines the paper does not have, and the `\paragraph` titles
already function as the question. Instead, each paragraph's **first** sentence now carries its number.

**And one framing we cannot adopt.** Your §10 treats the untrained encoder (`0.788`) and tree-edit distance
(`0.723`) as *controls*. Both are **extensions**; they fail the membership test at the twin, which is why
the paper reports them as evidence *outside* the criterion rather than inside the family. If they were
controls, the twin's ceiling would not be `0.500` by proof, and Proposition 4 would be false.

---

## 4. Two deviations from our own plan, reported because they are deviations

**§1's paragraphs 3 and 4 were not reordered.** The plan was to move the twin paragraph ahead of the
S1/S2/S3 example. We stopped when we read the seam: the twin paragraph opens *"Hold every lower-level cue
fixed"*, and "lower-level" is undefined until the example fixes the three levels, and the example ends by
motivating the twin (*"$x{+}y$ and $y{+}x$ are identical to every $\phi_d$"*). Moving it creates a forward
reference in the paper's first page. We took the elevation from the title and from the abstract instead, at
zero cost.

**The conclusion is two paragraphs, not three.** Three spilled ~1.5 lines onto page 10 and page 9 has
`+0.000pt` of slack. Merging the two theory takeaways and tightening the third fits it, and each takeaway
still opens with its own bolded label.

---

## 5. What did **not** change, deliberately

Nothing on your §19 keep-list. Also nothing from round 41's grants: the four-object critical path in §1,
Theorem 1's de-sell title, the rung-indexed concessions, Proposition 4, and the `+0.1584` adversarial search
result that **beat our strongest published control** and is printed in the body anyway. No result, no number,
no scoping clause was removed as "defensive prose": a sentence whose content is a refusal is not surplus.

`\emph` was held at ~236 by decision, not oversight: it marks technical terms at first use and contrasts
doing logical work (*not*, *declared*, *differs*), where deletion changes the reading rather than the tone.
The bolding was the measurable problem.

---

## 6. Verification

- **Build** `pdflatex → bibtex → pdflatex ×2`: **0 errors · 0 undefined references or citations · 0 "Float
  too large" · exactly 2 overfull boxes** (`6.4211pt` vbox, `3.509pt` hbox: both pre-existing) **· 0 bibtex
  warnings**.
- **93 pages · abstract ends p1 · body ends p9 · References p11.** Page 10's first body line is the Ethics
  heading. All four floats on their prior pages (Fig 1 p3 · Tab 1 p4 · Tab 2 p5 · Fig 2 p8); all 13 body
  headings on their prior pages. The bistable §4.3 boundary held its canonical state.
- **All four gate scripts PASS**: 19 protected claims (8 pinned at ==1) · reviewer map 17 rows / 285 checks /
  44 run tags / 54 appendix letters · 10 figure values against their source rows · 34 caption literals across
  35 floats. Both `--control` modes still fire, so the guards are live and not vacuous.
- **`verify_claims.py` exit 0 at `2337/2337` in all three code copies**: `artifact/audit-sym`,
  `artifact/iclr-supplementary` (the redacted copy that ships), and the workplace copy. **The count is
  unchanged, which is the point**: this round touched no computation, so any change would have meant a prose
  edit broke an assertion.
- **Pages 1, 2, 4, 9, 15 and 16 read as rendered images**, not as `pdftotext`. This caught two real defects
  this round that no text gate can see: `description` with `style=nextline` wasted a line per item in the
  appendix list, and the second list's long labels collided with their own body text.
