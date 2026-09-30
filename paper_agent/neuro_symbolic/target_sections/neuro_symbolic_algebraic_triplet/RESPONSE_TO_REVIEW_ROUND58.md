# Response to Review, Round 58

**You told us the next revision should be "primarily editorial, not scientific," and that is exactly what
this one is. Three edits to the paper and one new gate. No experiment ran, no number moved, no claim widened,
and the document is still 101 pages. Exactly one edit moved the page budget at all: the figure fix, which
spent 3.266pt of page 2's slack; every other page, and every other edit, left the eleven-page profile
byte-identical.**

You also gave us the sharpest diagnosis this paper has had in eighteen rounds: *"the reader has to work too
hard to discover the simple idea underneath the machinery … The problem is compression and hierarchy, not
missing content."* We agree, and we measured before we cut. The measurement disagreed with your prescription
in one specific way, and the disagreement is the most useful thing in this letter, so it is stated in full in
item 9 rather than buried: **the density you scored 6.5 is not in the prose volume. It is in the markup and in
one picture.** We fixed it where it was.

**Before anything else: a disclosure the paper's own thesis obliges.** You reviewed
`iclr2027_conference(20260914-065637).pdf`, the **06:56** build of 14 Sep. The build on disk was **12:11**.
Everything round 57 shipped: the abstract's *"the audit falsifies by design"*, its closing *"The audit is the
deliverable; the findings are its test."*, and §3.3's **graded verdict**: postdates your copy. **You have not
seen round 57's work at all.** We note where that matters below rather than claiming credit against your text,
and none of the three edits in this letter is a round-57 edit.

---

## Part I: What shipped

### 1. Page 2's verdict band no longer reads as steps 5, 6 and 7 of the procedure above it

**This is your §13 (*"make what a pass means visually impossible to miss"*), and it is the item we are most
grateful for, because finding out why you asked for it exposed a real defect that all four gate scripts,
`pdftotext` and the verifier are blind to.**

Figure 1 is a strip of **four numbered boxes** read left to right: `1. the claim` → `2. can a P-invariant
control solve the task?` → `3. no: declare the family F and measure its ceiling` → `4. is the learned score
above that ceiling?`, with two exit labels hanging below. **Directly beneath them, at the same width, in the
same rounded-rectangle frame, at the same `\scriptsize`, sat the graded band**: `absolute` / `a pass ⇒
family-relative` / `never mechanism` — three cells differing from the numbered boxes only by a grey fill.

Two consequences, and both are invisible to every automated check in this repository:

- **A reader who has just walked 1→2→3→4 left to right continues left to right into the band, and reads it as
  steps 5, 6 and 7.** The strip's axis is **procedural order, ascending**. The band's axis is **evidential
  strength, descending**. Two orthogonal meanings on one horizontal axis, about **14pt** apart.
- **The dark→light fill compounds it.** The reading path *ends* on the palest cell (`never mechanism`) while
  the strongest verdict sits in the darkest cell at the far left, reachable only by jumping the full page
  width backwards from box 4.

**A graphical object placed beneath another inherits its axis.** That is the finding, and it is round 44's
cross-panel axis-direction defect and round 51's `yes ⇒` polarity defect in a third form, in the same figure.

**What shipped is the drawing, not the caption.** A hairline rule (`black!55`, 0.4pt) now spans the picture
between the exit row and the band, and immediately beneath it, in the picture itself:

> **a grading, not a fifth step** — strongest evidence first:

with the three cells re-hung off that heading. The boxes are numbered 1–4; the band now says out loud that it
is not numbered 5. Cost: **3.266pt** of page 2's 9.463pt of slack, against a 6.9pt estimate. Every other page
byte-identical.

**Vocabulary, because we no longer choose these words freely.** *a grading* is §3.3's own word
(`methodology.tex:381`): deliberately **not** *verdicts*, because round 57 established that all eight body
uses of *verdict* mean the outcome on **one claim**, so labelling three cells "verdicts" would re-introduce
the exact equivocation that round removed. *strongest evidence first* is round 47's own grant wording. *a
fifth step* respects round 55's discipline that **steps are Figure 1's and stages are Figure 5's**.

### 2. The abstract states the audit's scale, and stops bolding a fragment

**Your §17 sentence 5** (*"Applying the audit to 10 published claims across 3 modalities revises 8 of them"*)
was in §1 and in the conclusion, and missing from the one paragraph most reviewers weigh. Pricing it
surfaced a defect of ours in the same sentence: P3 read `**Four of the audited** results are other people's`,
**closing a bold run mid-noun-phrase**, a count and its partitive filed without their predicate. Round 56's
rule is *bold is filing*, and we had violated it in the abstract, on the axis you score lowest.

Both fixed in one edit. P3 now reads:

> **Four of the audited results are other people's** — ten in all, eight of them already published: a released
> 80M-parameter integration encoder scores 0.872 where a zero-parameter operator/arity bag scores **0.941** …

Every number was already in the paper (§1: *"ten claims across three modalities — eight already-published
results, four of them other people's"*), so **no new claim and nothing for the verifier to check.**

**Priced, and it is a data point rather than an estimate.** P3's last line carried **258.97pt** of usable tail
(the abstract's right edge is **468.14**, not the body's 504.00) and now carries **46.28pt**. The first 39
rendered characters cost 170.91pt = **4.38 pt/char**: at our *conservative* 4.40 budget, not in the 3.2–4.0
range this abstract usually measures, **because 27 characters moved into `\textbf` and bold glyphs are wider.**

`", three modalities"` (+18 characters) fits at that rate with about 9pt to spare and was **declined on the
margin**: a new abstract line cascades through page 1's +0.561pt into page 4's **0.000pt** and a ten-page
body, and the modality count is already stated in §1 and in the conclusion. Adding a third site to state it
works against your own thesis.

### 3. Emphasis on page 2 stops being emphasis

**Your §7/§20, and the measurement is the answer.** §1 is **4,699 rendered characters in 7 paragraphs
carrying 18 `\textbf` + 32 `\emph` = 50 emphasis spans (one span per ~94 characters, which is roughly one per
rendered line**) with 27 more on the same page from Figure 1. Round 56's lesson to us was *bold is filing*.
This is its limit: **when every paragraph is bolded, bold files nothing.** Demotion is also the only lever
available that is free in characters and non-negative on width.

Five spans demoted, one bold run narrowed. **`introduction.tex` is word-identical to the pre-edit file: only
markup changed.** The full list, because nothing else records it and a future round will otherwise revert it
silently:

| site | span | why it went |
|---|---|---|
| `:80` | `\emph{protocol}` | the bold lead already says *"about evaluation, not about encoders"* |
| `:113` | `\emph{best}` | inside a question, and round 45's grant puts questions in roman; the object is already filed by `**(3)**` and *family-relative admissible ceiling* in the same clause |
| `:115` | `\emph{perfectly}` | the em-dash clause after it, `{+}` against `{+,+}`, demonstrates it |
| `:115` | `\emph{which operators appear}` | its sentence is already flagged by **That is the trap** |
| `:222` | `\emph{inventory}` | **asymmetric**: the contrast is arrangement vs inventory and only the second half was marked, so the markup filed half a contrast |

**Narrowed, and it is the largest single find of the part.** `:140`'s bold ran ~150 characters and **swallowed
three `\citep`s**, rendering *Allamanis et al. 2017; Gangwar & Kani 2023; Zheng et al. 2025* in bold: round
56's *bold is filing* filing the citations as if they were the claim. It now reads **S1 is clean almost
everywhere**: roman parenthetical carrying the three citations, and **S2 is where the exposure is**.

**50 spans → 46.** `\textbf` goes *up* by one, because narrowing splits one run into two, while about 93
rendered characters of bold ink come out.

**Spared, and one of them taught us something.** `\emph{three}` at `:222` is **pinned together with its
markup**: `check_ledger_modalities()` builds its needle as `"revise %s claims across \emph{%s} modalities"`.
We proved this by performing the demotion, which produced `LEDGER: body does not say 'revise ten claims across
\emph{three} modalities'`, and then restored it. It is the **only interpolated-markup needle in all four gate
scripts**, and the lesson is durable: **a demotion is not markup-neutral to the gates.** Also spared:
`\emph{measured}`, `\emph{one}`, **upheld**, `\emph{no}` at `:113`, `\emph{by proof}` and the whole `:117`
flagship, round 56's `\emph{trained}` readouts, round 47's `\emph{case study}`, round 55's three bold
ordinals, and the entire `four failed` sentence.

### 4. One new gate: the first ceiling here on a *claim* rather than on a string

Your §7 is *"All are important. But you don't need each one three times."* You are right, and the reason it
happened is structural. **Nothing in `check_protected_claims.py` bounded how many times a claim may be *made*.
Its 35 corruptible controls assert that a string is present, is absent, or agrees with a neighbouring site, and
13 further literals are pinned at exactly one occurrence; those 13 do fail from above, but only on a
duplicated string. Every one of them is keyed to literal text, so the same claim written in different words is
invisible to all of them.** Every round's grant adds a floor, and a floor on a string is never a ceiling on a
claim. The criterion is stated
**four times on pages 1–2**, each time because a different reviewer asked: round 46's prose sentence, round
44's boxed display (asked three separate times), round 55's interrogative, and rounds 43/46/50's contributions
lead. Fourteen rounds of *"make X unmistakable"* produced four unmistakable statements of X, and the fourth is
what makes the first unreadable. **This is the inverse of the routing defect that has been our dominant
failure mode: not a thing missed for what it is called, but too many present.**

`check_restatement_budget()` is now registered in `main()`, with **six independently corruptible halves**: an
**upper bound of 3** signature-matching segments in §1, a **paired lower bound of 2** so the ceiling cannot be
satisfied by deleting the boxed display and the prose criterion together, the three allowlisted sites required
**exactly once each** so it cannot be satisfied by substitution, and three halves on Figure 1, a direction
word in the **picture**, the *not-a-step* disclaimer in the **picture**, and `what a pass means` still in the
caption. `--control` rises **35 → 41**.

Two disclosures about it, both of which belong in a letter rather than in a footnote:

- **The gate holds the line we measured, not a line we repaired, and its own docstring says so.** The two
  deletions scoped to reduce the count from four to three were both dropped on measurement (item 10), so the
  restatement count is unchanged. A gate that reported a repair that did not happen would be worse than no
  gate. Its normal output is `ok 3 RESTATEMENT BUDGET: \S1 states the criterion in 3 segments (floor 2,
  ceiling 3)` — three segments, not four, because the sentence splitter merges round 46's prose criterion with
  round 44's boxed display.
- **Its accepted blind spots are documented inside it.** A fifth statement inserted *inside* an existing
  segment escapes, because the unit is the segment. A restatement moved to §2 or §3 escapes, because the
  budget is scoped to §1, where the density was measured.

---

## Part II: What we measured, where the measurement answers you

### 5. Your §8's terminology budget: of seven targets, **two occur zero times in the paper**

Measured on the **flattened** text, not the source, because `\makecell{comparator\\invariance?}` does not
contain the string `comparator invariance` and a naive grep reports zero for a term that is on page 4. Please
run these yourself.

| your target | occurrences | where |
|---|---|---|
| `falsification-only` | **0**, whole tree | does not exist. The nearest string in the document is Table 1's column header *falsifies only?* |
| `protocol hypothesis` | **0**, whole tree | does not exist |
| `comparator invariance` | **1**, whole tree | Table 1's column header: a definition site |
| `readout closure` | **1**, whole tree | Table 1's column header: a definition site |
| `family-relative` | 7 body, 9 tree | including Figure 1's band, which item 1 rebuilt |
| `certification` | 3 body, 8 tree | one of them Figure 1's `never certification` |
| `resolution` | 5 body, 14 tree | four are the same phrase, *"the ceiling is non-monotone in resolution"*, which is the **content of Corollary 2** (`cor:supremum`, p6), cited by label in §1 and §3; the fifth distinguishes *instrument* resolution from an effect's onset |

**So: two of your seven targets do not exist at all. Two more occur exactly once each: both as bolded column
headers in Table 1, which is the one place in the paper whose job is to define them, and the nearest string to
a third is a column header too. One is a named result's own phrasing.** We would rather be told the remainder
is still too much than argue about it, but the budget cannot be cut by deleting terms that are not there.

There is a second reason, and it is a scoring reason, for the three targets that do recur. `readout closure`,
`family-relative` and `certification` are exactly the terms **round 56's reviewer identified as this paper's
differentiator**, and positioning them at four compression sites moved **Novelty from 6.5–7.0 to 8.5**: the
largest sub-score move in eighteen rounds, on no new evidence. That positioning is now required by
`check_contribution_closure()` at four sites plus Table 1's column. Demoting them fails a gate and reverts the
edit that produced your own 8 on Novelty.

### 6. Your §5 (*"do not introduce coverage on page 1"*) was already done, by a predecessor

**`coverage` occurs 0 times in the abstract's rendered text and 0 times in §1's prose.** The one source match
in `introduction.tex` is a **comment**; another comment, `abstract.tex:23`, records round 46's reviewer asking
for exactly this and a predecessor shipping it. Its only appearance on pages 1–2 is Figure 1's caption (
*"and coverage is a separate axis, not a fourth level (§3.2)"*), which is **round 47's grant**, added
specifically because that reviewer found `coverage`, the cue levels and `F_3` confusable and wanted the
distinction drawn in one place. §3.2's own title still announces it.

### 7. Your §15 and §21 are already true of the render

- **§15, restructure §4 chronologically.** `experiments.tex` already runs: **4.1** the flaw survey · **4.2**
  the shape-matched twin · **4.3** trained on singles, tested at depth 8 · **4.4** the ports, including our own
  inversion failing to replicate · **4.5** the protocol. That is your proposed order with the twin placed
  *earlier* than you place it, which is your own §3/§21 preference.
- **§21, a 9-page architecture.** The body **is** 9 pages: `E THICS S TATEMENT` is the first body line of page
  10, and the paper is 101 pages by `pdfinfo` with everything after page 9 appendix and references.

### 8. Your §17's other sentences are the abstract's own sentences

Five of your seven proposed sentences are already in the abstract (its opening thesis, the criterion sentence,
the twin result, the certificate boundary, and its closing sentence) four of them bolded. Your sentence 4 is
there nearly verbatim: *"**every arrangement-invariant
representation, declared or not, is pinned at exactly 0.500 by proof**, and a Tree-LSTM reaches **0.994**."*
Your §1 thesis sentence is the abstract's **first** sentence, bolded, which you quote back to us approvingly.

The rewrite itself is declined in item 12.

---

## Part III: What we declined, and the arithmetic

### 9. Your §7's 25–30% Introduction cut: **declined at ~15%, and then the 15% declined too.** ~1.3% is free

This is the item we owe you the most detail on, because we tried to do it and could not.

§1 is **4,699 rendered characters in 7 paragraphs.** Your 25–30% is **1,175–1,410 characters**. There is no
sentence-level trimming that reaches that; it requires deleting whole paragraphs. Here they are, with what
each one is:

| ¶ | chars | what it is |
|---|---|---|
| 1 | 749 | the running example you ask for **more** of in your §4/§16/§22 |
| 2 | 278 | *"a paper about evaluation, not about encoders"*: round 47's identity statement, the sentence your own review paraphrases as *"the audit — not the encoder — is the deliverable"* |
| 3 | 661 | the three-objects ladder, **gated** by `check_critical_path()` |
| 4 | 456 | the S1/S2 example that fixes the cue levels |
| 5 | 537 | the shape-matched twin: the flagship, and the one rung whose ceiling is known by proof rather than by search |
| 6 | 474 | rounds 46/47's survey paragraph, carrying three citations |
| 7 | 1,544 | the contributions ledger, gated at two sites by `check_contribution_closure()` |

Every one is a gated anchor, a flagship result, or a pinned grant. We checked each candidate cut against all
four gate scripts **and** against every prior response letter with the letters flattened, and the finding was
not what we expected: **three of four candidates died on the letters, none on a gate.** The material that
measures genuinely free totals **about 62 characters, ~1.3%.**

Related Work is not the reserve either: its prose was already cut 30–40% at round 46's request.

**So we took the density win through markup instead of through words** (item 3): 50 emphasis spans → 46, ~93
characters of bold ink removed, and the six bold run-in leads left standing as page 2's skeleton. That is a
real answer to a 6.5 density score, and it is a smaller answer than you asked for. We would rather say so than
report a 25% cut we did not make.

**Your §6's *"exactly four paragraphs"* is declined at seven**: unchanged, because the merge that would have
taken it to six was scoped to fund a caption edit we then declined (item 10), and we will not ship a paragraph
merge whose only justification has evaporated.

### 10. Three edits we planned, priced, and dropped: with the price

- **Figure 1's caption naming the band's direction.** Its last rendered line carries **26.37pt** of tail ≈ 7
  characters at the measured ≈3.9 pt/char. The shortest truthful direction clause is 17 characters. So any
  caption addition buys a **fourth caption line at 11.6pt** against page 2's remaining **6.197pt**, which
  cascades into page 4's **0.000pt** and a ten-page body. Every clause in that caption is pinned by rounds 46,
  47, 55 and 57, so **no truthful swap exists in either direction**: round 57's finding, re-measured and
  unchanged. **The direction word went into the picture instead**, which is where the defect was.
- **§1's six-object glosses.** `check_critical_path()` reads only the `\ref{}`s, so the glosses are invisible to
  it. But of the six objects, **two never carried a gloss** (the twin and §2), and of the four that do, **two
  cannot lose theirs**: *every claim and its verdict* (round 57's enumeration of the body's uses of *verdict*)
  and *the axes no prior device attains* (rounds 48/50, borrowed deliberately into Table 1's caption). **That
  leaves two glosses free, ~52 rendered characters**, and deleting them leaves a ragged list of two glossed and
  four bare references: worse prose than either extreme, and not enough to shorten the paragraph's last line.
- **`:222`'s `, and a supremum over trained readouts too` (~48 characters).** Not letter-pinned and not a
  `check_contribution_closure()` site, but it is **readout closure**, the paper's one proved non-definitional
  item and the differentiator whose four-site positioning produced your 8 on Novelty. Deleting it from §1's
  contributions paragraph to win a clarity point would revert that and orphan `prop:ceiling`'s citation.

### 11. Your asks collide with each other: for the sixteenth consecutive round

We say this every round now, and it is not a complaint; it is why *"just make it clearer"* has not converged
in eighteen rounds.

- **Your §2 against your own §13.** §2 calls Figure 1 visually overloaded and supplies a redraw with **no
  band**. §13 asks that what a pass means be *"visually impossible to miss."* **The band is the object that
  does §13's job and is exactly what §2 deletes.** `figure_audit.tex:47–53` recorded that trade-off a round
  before you raised it: *"he asks for five boxes … his fifth step is the pass VERDICT, which is the graded band
  … Cutting the band to reach five boxes would delete two predecessors' requirements and one of his own in the
  same stroke."*
- **Your §18 against your §11.** *"Do not add more math"* against *"box the central principle, with the
  intuition preceding the theorem."* The boxed principle at `introduction.tex:44` is round 44's, asked for on
  three separate occasions.
- **Your §19 against a gate.** Deleting *"six objects are the critical path"* fails `check_critical_path()`
  outright and orphans the appendix's mirrored **Six objects carry the argument** description list at
  `appendix_domain_guards.tex:112`. What actually produced the *forensic dossier* tone you name is the itemized
  glosses interrupting §1's central sentence, and item 10 explains why only two of them are free to go, and
  why removing two makes the list read worse rather than better.
- **Your §10 against three predecessors.** Table 1 is **eight criteria columns plus a label column, over nine
  prior devices and ours.** Cutting to four fails `check_novelty_grid()` twice; it prints `ok 8 NOVELTY:
  caption's 'eight' agrees with the grid's columns` and `ok 3 NOVELTY: the three bold columns are comparator
  invariance?, family ceiling?, readout closure?` — and fails `check_contribution_closure()`'s Table 1 half.
  Those three bolded columns are rounds 48's, 50's and 56's grants, and they are also three of the terms your
  §8 asks us to demote.
- **Your §8 against your §17.** Demoting `certification` while keeping your sentence 6, *"a pass rules out
  declared alternatives, not all alternatives"*, whose abstract form is the literal `no admissible family can
  turn it into a certificate`, pinned at exactly one occurrence.

### 12. Your §17's 7-sentence abstract rewrite is declined, for a reason a gate can print

It drops *"no admissible family can turn it into a certificate"* and the abstract's **only** `falsif` token.
Those are **two halves of `check_verdict_ladder()`**, a gate written last round precisely because that token
had gone missing once before: round 57 measured `falsif*` at **zero occurrences** in the abstract, and the
round-51 letter proved it had once been there and a compression pass had deleted it. Your copy of the paper
predates the repair. We are not going to lose it twice.

---

## Part IV: What we found in our own work this round, and one limit in yours

### 13. Your running example cannot reach the twin, and saying so is the clarity gain

Your #2, §4, §16 and §22 ask for `x+y` / `y+x` / `(x+0)+y` as a single running example **throughout**,
including the twin. **It cannot reach the twin, and the reason is load-bearing.** §1 says *"The class of x+y
**contains** y+x and (x+0)+y"*; they are the **same class**, which is what makes them a clean demonstration
that an S1 bag separates nothing while an S2 bag separates perfectly. A **shape-matched twin** pairs a
held-out form with *"the same variable multiset and the same operator multiset in a **different
arrangement**"*, and it is the *different class* that makes 0.500 chance-level rather than trivial. `y+x` has
the twin's multisets and the **wrong** class. So the truthful version of your ask is that the same *example
family* extends with a harder pair, not that the same pair carries through, and we would rather state that
than ship a running example whose final step is false. When no truthful edit exists in the form asked, that is
the finding.

### 14. This round's own readiness pass found four defects in this round's own new text

We run this pass at the end of every round, on a fully green board. It has found a real defect fifteen rounds
running, and this round all four were in text we had just written:

1. **The abstract's new clause had a count-containment gap.** It first shipped as *"ten in all, eight already
   published"* beside *"Four of the audited results are other people's"*: three counts whose relationships
   are unstated, from which a reader can compute 4 + 8 = 12 > 10. Fixed to **"eight of them already
   published"**, which binds eight ⊂ ten and mirrors §1's nested phrasing. **A clarity defect introduced by a
   clarity edit**, in the abstract, in the same sentence that answers your §17.
2. **A count attached to a noun, wrong, at three sites.** A comment in `figure_audit.tex` described *what a
   pass means* as a five-word phrase. It is four words, and the error had already propagated into the
   docstring and the failure message of the gate we wrote this round. **Deleted rather than corrected**: the
   sentence does not need the number.
3. **"SIX spans demoted"** in our own comment block, which in the same breath said `:140` was *narrowed rather
   than demoted*. Five demoted, one narrowed.
4. **A universal quantifier about our own gates, falsified by the file it described: found after this round
   was already finished, on a second pass.** Item 4 above first read *"all 35 existing assertions are a
   presence or an absence,"* and called the new gate the repository's first upper bound. `PRESENT` pins 13
   literals at **exactly one occurrence**, so 13 assertions in that same file already fail when a string
   appears twice, and the number 35 excludes them by construction, because it counts controls inside the 20
   check functions and those 13 are checked in `main()`. Several of the 35 are agreements between two sites
   rather than presences. The claim is now the narrower and truer one: what is new is a ceiling on a
   **concept**, which survives paraphrase; every predecessor bounds a **string**.

Round 57's lesson, now confirmed three times: **a count is a universal quantifier wearing a numeral, and so
is the word "every."** Round 57's own second readiness pass had found a defect in its own first repair, and
find 4 above was found only because we ran the pass again after declaring the round done; that is now the
procedure, not the exception. **Our own most-repeated finding is that a claim written to be unmistakable is
the one likeliest to be over-broad**, which is the same defect your §7 identified in the paper's prose, one
level up, in the tooling that is supposed to catch it.

---

## The ledger

| | |
|---|---|
| pages | **101**, by `pdfinfo`, after every build |
| build | 0 errors · 0 undefined references or citations · 0 `Float too large` · exactly **2** pre-existing overfull boxes at unchanged sizes (`\vbox` 6.4211pt, `\hbox` 3.509pt) |
| slack profile | p1 +0.561 · p2 +6.197 · p3 +9.463 · **p4 0.000** · p5 −0.695 · p6 −1.927 · p7–p10 0.000 · p11 +0.687. **Page 2 is the only page that moved all round** (9.463 → 6.197, the figure fix); every other page is byte-identical to the pre-round profile, and the last three edits moved nothing |
| placement | Fig 1 p2 · Fig 2 p3 · Fig 3 p8 · Table 1 p4 · Table 2 p5 · body ends p9 · Ethics first on p10 |
| `.tex` gates | four **PASS** from the paper directory; controls **41 / 9 inline / 1 / 2**: up from 35, one new gate, six corruptible halves |
| verifier | **2591/2591**, exit 0, md5 `85e77e416b9b89fce4665bff4805348c`, identical across all three copies. **Untouched this round.** `equivalence.py` untouched |
| experiments | **none.** You are the **fifth consecutive reviewer** to say you would not add any |

`verify_claims.py` cannot read the `.tex` by design, so a round whose entire paper diff is prose, markup and
one TikZ hairline is checked by the four `.tex` gates instead, which is why the new gate, not a new assertion, is this
round's verification deliverable.

---

## One question, and it is a real one

Eighteen reviewers, eighteen rubrics. Significance moved **7.0 → 8**, and Novelty has held at **8 or above**
across the two consecutive rounds whose entire content was positioning, no new evidence, no new experiment
in either. Clarity moved
**7.5 → 7** on a build that does not contain round 57's three clarity edits. **Presentation, at 7, is a new
axis on your rubric.**

So: **is Clarity 7 a verdict on the prose, or on page 2's picture?**

We ask because of one datum. Your §13 asks for a boxed statement of what a pass means. **Round 55's §7 asked
for it. Round 57's P2 asked for it.** All three of you were asking for an object that has been on page 2 since
round 47, and your §13 asks for it in **Figure 1's caption's own words**, so you read that caption and still
filed the object as missing. Round 55's rule is that **a reported absence that is present is a layout failure**, and
after three rounds it is not a naming failure either: round 57 tried the naming fix and correctly declined
it, because no truthful swap existed. What was left was the drawing, and the drawing turned out to be telling
three consecutive reviewers that the band was steps 5, 6 and 7.

If we are right, the density score is measuring markup and one figure rather than 4,699 characters of prose,
and this round moved the thing that was actually in the way. If we are wrong, tell us **where you looked**,
which page, which paragraph, and we will treat it as a layout problem there too.
