# Response to Review: Round 50

Thank you. This is the tenth review on a tenth rubric, and the first in five rounds whose headline ask is
not an experiment. We took the instruction literally:

> *"The single biggest thing I would change now: **Do not add another major experiment. You have enough.**"*

**Round 50 adds no run.** It changes one table, one caption, one word in §1, and one gate.

**Three things stated before anything else, because one of them is about your own copy of the paper and one
is a correction to our own plan.**

**First, `verify_claims.py` does not move: 2486 assertions, exit 0, all three shipped copies byte-identical
(md5 `5fa64467ef226550c86145934245bc85`).** The standing rule in this correspondence is that the first
paragraph says whether the assertion count had to rise and why. It did not, and that is the correct
outcome here: this round adds no measured quantity, so a rise would have meant we had smuggled a result
into a presentation round. What *did* rise is gate coverage; see the last section: Table 1's grid had
**zero** coverage from any checker, and now has eight assertions and its own positive control.

**Second, the build you reviewed predates edits in six of our source files.** You name the file:
`iclr2027_conference(20260912-043054).pdf`, and say you reviewed *"the latest September 12 revision rather
than relying on the previous version."* The timestamp in that filename, `2026-09-12 04:30:54`, is earlier
than the round-49 edit pass:

| source | last edited | vs your build |
|---|---|---|
| `figure_framework.tex` | 2026-09-12 07:02:39 | **after** |
| `methodology.tex` | 2026-09-12 07:05:21 | **after** |
| `experiments.tex` | 2026-09-12 08:09:03 | **after** |
| `appendix_domain_guards.tex` | 2026-09-12 08:23:34 | **after** |
| `introduction.tex` | carries a round-49 design comment | **after** |
| `related_work.tex` | carries a round-49 design comment | **after** |
| `abstract.tex` | 2026-09-11 09:10:00 | before |
| `conclusion.tex` | 2026-09-11 08:50:14 | before |
| `statements.tex` | 2026-09-11 13:45:51 | before |
| `iclr2027_conference.tex` | 2026-09-10 18:25:16 | before |

A note on that table's method, because it is weaker than the one we planned and we would rather say so
than round it up. Our plan claimed *seven of nine* source files. We can no longer measure two of those
data points: `introduction.tex` and `related_work.tex` are the two files **this** round edits, so their
round-49 mtimes were overwritten by our own work before the response was written. For those two we cite
documentary evidence instead (each carries an in-source round-49 design comment), which is why the table
says "carries a round-49 design comment" rather than giving a time. **Four by timestamp, two by their own
comment blocks: six, not seven.** The mechanism for next time is to snapshot mtimes with `cp -p` before
editing; `cp` without it silently resets them, which is what happened here.

What that means for your review is concrete. Four of your nine sections are answered by a PDF you did not
have:

- **§4 and §5 (scope, and *"four primitives are not a library"*)**: the 15-corpus census. The largest
  *inventory-preserving* rewrite library anywhere in the survey is **five**, attained on `poly8`, the
  corpus the paper already uses, against the paper's four; no corpus anywhere exceeds **four** *repeatable*
  members, and two read three; **seven of the thirteen shipped poly-side schemas fire on zero of `poly8`'s
  1102 anchors**, each named in the appendix. `poly8`'s *usable* count is six, and the sixth
  (`_rw_power_to_explog`) is disqualified by the paper's own framework; it introduces `exp` and `log`,
  which occur nowhere in the corpus, so a held-out form carrying it is separable by an S1 cue. That is why
  the ceiling is five rather than six. It turns the concession you read as
  an apology into a measurement of the field's benchmark suite: there is no sixth admissible primitive to
  be had. Your §4 asks us to *"make the scope explicit and turn the limitation into a strength."* That is
  what the census is.
- **§7 (density)**: the depth-8 result is now a `\subsection` with its own argumentative title. Before
  round 49 it was a `\paragraph` inside a subsection named after a different result, which is exactly the
  routing complaint you raise. It landed 2h32m after your build.
- **§2/§4 (the adversarial search you call *"an excellent addition"*)**: Figure 2's `best of 706` label
  and the four-optima asymptote clause, which are the provenance of that search.
- **your instruction not to add another experiment**: round 49's authorized run was pre-registered, and
  **its own stop rule refused to let it train** (depth-8 delta-matched retention `175/1102` at `|L|=5`,
  structural rather than compute-bound). The paper already contains our instance of the discipline you are
  recommending.

**Third, the correction we owe you on our own scoring.** Our plan intended to score `strongest baseline` as
a ✓ on the new column. We scored it **×**, and the reason is substantive, not cosmetic: selecting the
strongest known comparator is not *searching a declared class*. That is the whole distinction the new
column exists to draw, and it keeps the caption's lead claim (round 47's stated 7→8 condition, *"× in all
eight columns"*) literally true, so only the numeral moved.

---

## §2, your biggest criticism, and the 7 → 8 lever

You wrote:

> *"You already have most of this in Table 1, but it is currently presented as a taxonomy. It needs to be
> presented as the novelty argument."*

We measured what was actually missing before touching it, and it was not a column. You name four prior
devices: matched controls, invariance tests, shortcut baselines, and **adversarial evaluation**. Table 1
had rows for the first three. **`adversarial` occurred 8× in the body and 0× in `related_work.tex`**: the
paper runs an adversarial family search and calls it a contribution while never once placing adversarial
evaluation as a *prior device*. The one comparison you say would answer your biggest criticism was the one
comparison §2 did not make.

Three changes, and they are a set:

**1. A row: `adversarial baseline`**, directly under `strongest baseline` so the two search rows read as a
block.

**2. A column: `searches a class?`**, without which that row would be **byte-identical to `shortcut
baseline`** — a name with no discrimination, which in the table you call the novelty argument is worse than
nothing. The two rows now differ in exactly one cell, and it is that one. This is asserted by a gate, not
trusted (below).

**3. A caption that states the claim instead of describing the grid.** The old caption diagnosed one row
and pointed at three bold headers without ever saying what the conjunction *was*. It now reads:

> **Takeaway: "strongest baseline" clears *nothing*** — × in all eight columns: strength is not blindness,
> which is what the three **bold** columns test, and **no prior row attains any of them**: that conjunction
> is what is new. **The last column is × on every row, ours included** (§3.3).

One word there is load-bearing and was chosen against the stronger alternative. **`attains`**, not *tests*:
three prior rows read `partly` in two of the three bold columns (four cells in all), those cells are
visible in the grid, and *"no prior row tests any of them"* would have been false. A reviewer who checks
the grid against the caption finds them consistent. This is also §1's own vocabulary: §1 already calls
Table 1 *"the axes no prior device **attains**"*, so the caption borrows the paper's word rather than
introducing a new one.

**And the prose, so the argument is not only in a float.** §2's paragraph titled *"What is new, given all
of that"* now reads *"Prior devices test one comparator, one perturbation, or an **adversarial** search in
isolation; **none estimates** $\sup_{g\in\mathcal{F}}M(g)$…"*. `in isolation` deliberately governs all
three items: it is what the new row's × under `family ceiling?` says in prose.

**Your predicted R2** (*"your most dangerous reviewer,"* 6/10, whose objection is repackaging) is who
this is aimed at. The device R2 would name is the one that now has a row.

## §6, the hierarchy

You asked that primary (admissibility auditing) versus secondary (protocol-dependence) be *"unmistakable."*
Measured, §1's contribution list was:

- **(i) An audit of published claims**
- **(ii) A finding: an evaluation protocol is itself a hypothesis about what generalization means**
- **(iii) A demonstration, and its exact scope**

So the secondary result was enumerated as a **co-equal finding**, and admissibility auditing was not an
enumerated item at all: a reader counting contributions found protocol-dependence at (ii) and the
framework nowhere in the list. The **conclusion's** list is correctly framework-first. §1 and §5 disagreed
about what the paper's primary contribution is, and §1's is the one on page 2.

**(ii) now reads "A consequence."** We did not re-order or renumber: a gate compares §1's counted
parenthetical to the appendix's reading-path list, the conclusion's list is already framework-first, and
the paragraph's own heading (*"Applying the criterion changes conclusions, in three places"*) already
subordinates all three items to the criterion. The defect was the label, so the label is what changed.

Two mechanical notes, because they are the reason this was a four-character edit and not a paragraph:

- That paragraph's last rendered line ends on page 3 at a **full 98 characters**: zero tail room, and
  page 3 carries 6.624pt of slack, which is 0.57 of a line. One new line there overflows into a page 4
  that carries **0.000pt**, and the body becomes 10 pages.
- So the +4 characters are **self-funded from the same paragraph**: *"the declared family's ceiling rather
  than any member"* → *"…ceiling, not any member"*, −6 characters, meaning identical, for a net −2. The
  obvious funding source was the *next* sentence, and it is frozen: our own checker pins *"four failed, and
  all four are printed"* verbatim at exactly one occurrence.

## §3, §5, §8, §1: answered by measurement rather than edit

| your point | the answer |
|---|---|
| **§3**: *"family-relativity is the most important conceptual objection; your answer should be that it is not a flaw but the point of the method"* | Already the paper's answer, in the paper's own words, bolded, in two places: `methodology.tex`: **"That limitation is also the deliverable"**, and the named corollary **"Which family we declared cannot manufacture a pass"**, with *"leaving a descriptor out is strictly against our own interest."* Worth recording how nearly we missed this: our first grep used **your** phrasings (*"not a flaw"*, *"is the point"*) and returned **zero hits**, which would have led us to concede a gap that does not exist. Never grep a reviewer's wording to test whether their point is answered. |
| **§5**: *"the title/abstract still repeatedly foregrounds compositional generalization"*; prefer *composition-of-known-transformations* | Measured, and this one we think is simply mistaken. The **title contains no form of *composition* at all**. The abstract's only `compositional` is a **denial**: *"That is not compositional reasoning: four primitives are not a library."* `compositional generalization` appears **3×** body-wide, every one scare-quoted and immediately narrowed. And *composition-of-known-transformations* **is already in the abstract**, in the exact form you prescribe. No edit. |
| **§1**: *"the paper takes too long to make this feel inevitable"*, with a sentence you supply | Your sentence is bolded in the abstract's second paragraph, which renders on **page 1**, and again in §2's paragraph literally titled *"What is new, given all of that."* Your objection is about position and inevitability rather than presence, which is why this round's answer is the caption and §1's label, both routing changes, rather than new prose. Your prescribed five-statement opening (problem / solution / limitation / escape hatch / validation) **is** the abstract's four paragraphs in order; page 1 carries the escape hatch as a *proof* (*"every arrangement-invariant representation, declared or not, is pinned at exactly 0.500"*). |
| **§7**: 13 concepts, no one-sentence mental model | The depth-8 subsection above, plus `methodology.tex`'s **"Terms, once."** glossary, which renders on **page 4**: the same page as Table 1, and glosses the concepts in one place. We flag it by page because it was the mechanically ideal place to find the space this round needed, and we did not spend it: a previous reviewer asked that it be moved *earlier*, i.e. made more prominent. Deleting it would have answered your §7 backwards. |
| **§8**: the 9-page limit | You verified it independently; you are the second reviewer to do so. Body ends on page 9, `ETHICS STATEMENT` is the first body line of page 10. |

## Page mechanics, since a column and a row both had to be paid for

Table 1 already occupied the full `\textwidth` and page 4 carried **0.000pt** of vertical slack, feeding a
page 5 at **−0.695pt** with no headroom. A column is a width edit; a row is a height edit. Both were paid
for **inside the float's own spacing**, so no prose was cut:

- `\tabcolsep` 4pt → **1.5pt**. Over a nine-column spec that is 16 gaps, so ~16pt of width per point.
- booktabs rule separation → **0.5pt/0.5pt** (from defaults of 0.4ex above and 0.65ex below, ~4.1pt per
  rule at `\footnotesize`) over **four** rules: ~12pt of height, almost exactly the new row's cost. The
  precedent is this paper's own page-9 modality table, which already sets the same three lengths.

Both regressions this caused, and how each was closed, because the second one was not visible in any
number we normally print:

1. **A third overfull box** (8.59596pt) when the column went in at `tabcolsep=2pt`. Closed in stages:
   `learned invariant control` → `learned inv.\ control`, header `controls?` → `a class?`, then
   `tabcolsep` to 1.5pt. **Exactly 2 overfull boxes remain, both pre-existing, at unchanged sizes.**
2. **The body spilled to 10 pages**: the new row pushed the glossary's last line off page 4, and §5, which
   had been ending on page 9's *very last line*, was displaced as a block. Diagnosed against the ICLR
   `lineno` numbers rather than `pdftotext` line counts: `pdftotext` regroups table rows and reported a
   spurious −5/−3 on pages 6 and 9. The rule separation fixed it at source. §5 is back on page 9, ending
   on *"Table 2 is the ledger."*

**The full eleven-page slack profile is byte-identical to the pre-round baseline** (p1 `+0.561` · p2
`+0.001` · p3 `+6.624` · p4 `+0.000` · p5 `−0.695` · p6 `−1.927` · p7–p11 `+0.000`) with every float on
its baseline page (Fig 1 p2 · Fig 2 p3 · Fig 3 p8 · Table 1 p4 · Table 2 p5). We print the profile rather
than calling it unchanged, because last round we called it unchanged while page 5 had in fact moved.

One funding source we did *not* use, recorded because we tried: the `(Figure 3).` orphan in §4.4. Its own
source comment says a previous round already attempted that compression, that it *moved the break without
removing the line*, so the orphan is not slack, and that the sentence is a frozen verbatim quote pinned
to its section in `check_reviewer_map.py`, which the attempt failed twice.

## The gate this round adds, because the table you call the novelty argument had no coverage

`tab:novelty` is a grid of `\checkmark` / `$\times$` / `partly` with **no decimals anywhere**, and our
caption checker matches exactly-three-decimal literals. It therefore saw **zero cells** in this table. The
caption could have claimed "eight columns" over a seven-column grid, or claimed a row clears nothing while
it ticked one, and nothing would have fired. A gate with zero coverage asserts nothing.

`check_novelty_grid()` now adjudicates the **caption's prose against the grid's cells**: the direction
that can go stale silently, since a round that edits the grid edits it deliberately while the count word in
the caption is what everyone forgets. Eight assertions: the caption's count word read out of the caption
(not hard-coded) against the actual column count; exactly three bold headers, pinned by name; ten rows,
nine prior devices with ours last; `strongest baseline` × in all eight; no prior row attaining a bold column
(reporting the four `partly` cells); our row attaining all three, so the conjunction claim is not vacuous;
the last column × on every row including ours; and the new row differing from `shortcut baseline` at
`searches a class?`. Its positive control corrupts the caption's count word to `seven` and fires one line.

One assertion we deliberately did **not** write: *"no two prior rows are identical."* It is the obvious
generalisation of the discriminating-row rule and it is **false here**: `strongest baseline` and
`held-out split` legitimately have identical all-× vectors, because two devices that establish nothing
establish the same nothing. A false positive in a new gate costs more than the coverage it buys.

## Verification

- **Build**: 0 errors · 0 `(Reference|Citation).*undefined` · 0 `Float too large` · **exactly 2** overfull
  boxes, both pre-existing (`\vbox` 6.4211pt, `\hbox` 3.509pt) · 99 pages · body ends page 9 · page 10's
  first body line is `ETHICS STATEMENT`.
- **Slack**: the full eleven-page profile above, identical to baseline at every page.
- **Render read at 300 dpi**, pages 4 and 2: Table 1 fits inside the right margin, the eighth column is
  intact, every row's cells align with their header, the three bold headers are the intended three,
  `searches a class?` is correctly not bold, the caption still occupies three lines, and the
  `Terms, once.` glossary is back on page 4.
- **Gates**: all five pass. Controls fire **16 / inline / 1 / 2**: `check_protected_claims.py` rises from
  14 to 16, one line for each of the two new checks' controls (see the addendum for the second). (Two of
  those scripts invert their exit code in control mode and print `CONTROL: expected at least one FAIL
  above`; a `grep -c FAIL` over their output counts that line too, and over-reports by one. It did, before
  we read the output.)
- **`verify_claims.py`**: 2486/2486, exit 0, in all three copies, md5 `5fa64467ef226550c86145934245bc85`.
- **Content-loss proof**: comment- and markup-stripped sentence diff of all six body files against a
  pre-round snapshot enumerates **−6 / +7** spans, every one of them an intended edit;
  `abstract.tex`, `methodology.tex`, `experiments.tex` and `conclusion.tex` are unchanged at 0/0. The net
  +1 is the caption's new sentence.

## What we did not do

No new experiment, on your instruction, and for the first time in five rounds. No modality was added
(your §4 asked us not to). No terminology sweep (§5 is already satisfied). No caveat was deleted to answer
*"takes too long to feel inevitable"*: several of those caveats are pinned by earlier reviewers'
requirements, and this would have been the eleventh consecutive round in which one reviewer's edit deletes
a predecessor's condition.

---

## Addendum: a stale count this round introduced, found in the readiness pass and fixed

We report it because it is the exact defect class this round's own new gate was written to close, and the
gate did not see it.

**§3.2's prose said Table 1 runs across "eight prior devices". After this round's new row it is nine.**
The sentence is `Table~\ref{tab:novelty} runs the first five across eight prior devices; the nearest is a
learned invariant control…`, and it renders on **page 7** — two pages after the table, in a **different
source file**. Adding `adversarial baseline` made it stale the moment it landed, and nothing could see it:
every one of `check_novelty_grid()`'s eight assertions reads `related_work.tex`, so **the gate written for
that table had a blind spot inside its own defect class**, the same shape of miss as the 24th mis-routed
reference we reported last round, one round later. It was found by grepping the whole tree for countable
claims about the table, not by any check.

Fixed, and the fix is **length-negative** (`eight` → `nine`, −1 rendered character), so it was free on a
page 7 carrying `0.000pt`.

**Assertion (7) now closes it**: the count is read out of `methodology.tex`, compared against the grid's
actual prior-row count, and **a missing phrase FAILs** rather than silently asserting nothing. Its control
reproduces the real defect verbatim: `NOVELTY: methodology.tex says 'eight' prior devices, the grid has 9`.
`check_protected_claims.py --control` therefore now fires **16** legible lines, not 15.

**Two things we checked and did not change.** *"The nearest is a learned invariant control"* survives the new
row: on raw cell agreement `adversarial baseline` and `learned inv.\ control` now tie at 4 of 8, but the tie
is broken by exactly the three bold columns; `learned inv.\ control` reads `partly` in two of them and
`adversarial baseline` in none, so the claim holds on the axes the paper says discriminate, which is also
the criterion the sentence itself gives. And *"the first five"* is still correct: the practice table above it
has six rows, and the sixth (`"out-of-distribution"`) deliberately has no column in Table 1.

**Re-verified after the fix**, from a clean `.aux`: 0 errors · 0 `(Reference|Citation).*undefined` · 0
`Float too large` · exactly **2** overfull boxes, both pre-existing at unchanged sizes and log lines · 99
pages · body ends page 9 · every float on its page (Fig 1 p2 · Fig 2 p3 · Fig 3 p8 · Table 1 p4 · Table 2
p5) · the eleven-page slack profile unchanged to the last decimal · four gates PASS, controls
**16 / inline / 1 / 2** · `verify_claims.py` **2486/2486 exit 0**, three copies still md5-identical
(`5fa64467ef226550c86145934245bc85`) · page 7 read at 300 dpi, the corrected sentence still setting on
three lines with §3.4 unmoved.
