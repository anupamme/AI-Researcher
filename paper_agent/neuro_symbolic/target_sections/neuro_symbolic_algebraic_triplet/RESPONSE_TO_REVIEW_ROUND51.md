# Response to Review: Round 51

Thank you. This is the eleventh review on an eleventh rubric, and the second running whose headline ask is
not an experiment. We took the instruction literally:

> *"I don't think you need more experiments. You need a stronger central intellectual compression."*

**Round 51 adds no run.** It changes one sentence of the conclusion, one clause in §4.2, one citation in §2,
four numbers in the Reproducibility Statement, and one gate.

**Four things stated before anything else. One is about your own copy of the paper, *two* are defects we found
in ourselves and are disclosing, and one is a correction to our own plan.** Both defects are in the same
file: the one you score 9/10, and the second was found by asking, after the round was finished and every
gate was green, whether the paper was ready. It was not.

**First, `verify_claims.py` does not move: 2486 assertions, exit 0, all three shipped copies byte-identical
(md5 `5fa64467ef226550c86145934245bc85`).** The standing rule in this correspondence is that the first
paragraph says whether the assertion count had to rise and why. It did not, and that is the right outcome for
a presentation round: a rise would have meant we had smuggled a result into it. What *did* rise is gate
coverage, and by more than we predicted: our plan said `check_protected_claims.py --control` would go
**16 → 17**; it goes **16 → 19**, because the first new check fires two controls (the cross-file comparison and
the arithmetic) rather than one, and a *second* new check was needed after the readiness pass below. We are
reporting the measured number, not the planned one.

**Second, the build you reviewed predates edits in six of our source files.** You name it:
`iclr2027_conference(20260912-060109).pdf`. That timestamp, `2026-09-12 06:01:09`, is earlier than both the
round-49 and round-50 edit passes:

| source | last edited | vs your build |
|---|---|---|
| `figure_framework.tex` | 2026-09-12 07:02:39 | **after** |
| `experiments.tex` | 2026-09-12 08:09:03 | **after** |
| `appendix_domain_guards.tex` | 2026-09-12 08:23:34 | **after** |
| `related_work.tex` | 2026-09-12 10:44:14 | **after** |
| `introduction.tex` | 2026-09-12 10:46:36 | **after** |
| `methodology.tex` | 2026-09-12 11:19:11 | **after** |

This is the third consecutive round in which this has happened, so we now date the build before reading the
review. It matters most for your **§15**, which lists six prior devices: *"adversarial baselines are old"*
among them, and asks us to *"emphasize that comparison table much more strongly."* **Round 50 did exactly
that, for exactly that reason, 4h43m after your build**: Table 1 gained an `adversarial baseline` row *and*
the `searches a class?` column without which that row is byte-identical to `shortcut baseline`, and the
caption was re-premised to lead on the novelty claim rather than the taxonomy. Your **§8**
(*"four primitives are not a library"*) is likewise already a measurement rather than a concession: round 49's
15-corpus census puts the usable rewrite ceiling at **6** and the repeatable one at **4**, with 9 of 13
shipped rewrites firing on **zero** poly8 anchors. Neither was in your PDF.

**Third, and this is ours, not yours: the Reproducibility Statement (the section you score 9/10 and
enumerate item by item) was describing the artifact wrongly, and had been for three revisions.** You quote
it as *"2,304 assertions; 43 indexed runs."* Neither number is ours; but what it actually said was **2398**
and **77**, and the truth is **2486** and **81**. `77` went stale in round 48 and again in round 49; `2398`
in rounds 48, 49 and 50.

Why nothing caught it is the part worth your attention, because it is a defect *class*, not a typo:
`LC_ALL=C grep -l statements.tex check_*.py` returned **nothing**. No gate script opened that file. The
verifier lives in a different tree and reads `REPRODUCE.md` and its own source, never this prose: the one
number in it the verifier does pin is *"six runs have no wall-clock time"*, via
`doc.count("runtime not recorded") == 6`, which was and is correct. **A gate's coverage is the set of files it
opens, not the set of claims it is about.** That is now closed by `check_artifact_counts()` (below), and the
statement's own numbers are the least-gated numbers in any paper: they are the ones no result depends on.

**The arithmetic is re-premised, not re-counted, and that distinction is the whole repair.** The naive fix (
`77 → 81`, `33 → 37`) ships a **false** claim, because the sentence asserted *"not one of the 33 it has
gained is a new run"*, and four of the new logs genuinely are new runs. `len(tags)` counts **log stems**, and
the gain of 37 decomposes as 32 (the self-check defect: fifteen `r82` seed logs, four `_rep2` replicates,
round 45's holdout arms) **+ the 77th** (`r31_hardened_recipe`, shipped since July; indexed is not asserted)
**= 33 that are not new runs**, plus **4 that are**: `r102_composition_lattice`, the two `r103_library_size`
invocations, and `r103_library_census`. So the statement now reads *"$33$ of the $37$ it has gained are not
new runs at all"*, and a new sentence names the other four as new runs rather than folding them into the
defect. Each of the four was checked against `check_reproduce_index()`'s own note, not against memory. Note
the sentence says *"invocations"* and *"indexed under one entry"* deliberately: those four **logs** occupy
only three `REPRODUCE.md` **entries**, and that is the one place where the two units diverge.

Two further staleness repairs in the same paragraph: *"two revisions ago"* is gone (a relative date decays
every round, and this paragraph's self-description has now drifted three rounds running), and *"it is this
revision's"* → *"it is our own"*, which keeps the self-attribution while dropping a claim that expired four
rounds ago.

---

## Your §20: the 7 → 8 lever. The paper's exit list did not contain its own best result.

Your condition is that a reader leave remembering exactly three things: strong baselines are not necessarily
valid controls; a control must be invariant to the claimed property; **and the right statistic is the best
admissible ceiling, of which the twin is the case where it is known exactly.** You score the twin 9/10,
*"the best part of the paper by a considerable margin."*

We measured before writing anything, and the measurement is the finding:

```
LC_ALL=C grep -ciE "twin|arrangement|0\.500|0\.994" conclusion.tex   →   0
```

**The result two consecutive reviewers call the paper's strongest asset appeared nowhere in the conclusion.**
§1's ladder (baseline / admissible control / family-relative ceiling, which is your triple) and §5's three
numbered findings therefore *ended on different statistics*, and the paper's exit list did not contain its own
killer experiment. Round 46's in-source note enumerates the three spans it removed from that file and the twin
is not among them: it was never there, so there was no predecessor's grant to undo.

Finding (1) now reads:

> **(1) The *direction* of comparison is forced; *which* family we declare is the choice — except at a twin:
> $0.500$ by proof** (Theorem 1, Prop. 4).

Folded into (1) rather than added as a fourth finding, because (1) is the finding about the *direction* of
comparison and the twin is the case where direction is all there is: the family choice stops mattering. The
three findings are not renumbered or reordered; they still mirror the abstract's four paragraphs in order.

**It shipped in its minimal form, and we are saying so rather than describing the version we drafted.** p9 is
the body's last page at 0.000pt of slack, so a tenth rendered line there is a ten-page body. The full clause
(*"except at a shape-matched twin: $0.500$ by proof against $0.994$"*) is 63 bold characters ≈ 258pt
against ~154pt of measured funding, and it **did** push two sentences onto p10 when built. Two things came out,
in this order, both recoverable one `\ref` away: **`against $0.994$`** (the contrast; (1) is about direction,
and *"by proof"* alone carries what the exit list must carry; that this ceiling is *known* rather than
searched) and **`shape-matched`** (the object's name, which `Prop.~\ref{prop:twin_exact}` in the citation slot
recovers). If a later round frees ~14 bold characters on p9, `"a twin" → "a shape-matched twin"` is the first
thing we buy back.

Self-funded, because it had to be: `methodological` deleted from the same clause (−15 rendered characters,
pinned by no gate, grepped, not assumed) plus 125.57pt of horizontal tail room on the paragraph's last
rendered line, measured with `pdftotext -bbox`. That deletion is also a **repair**: §5's clause now matches
`abstract.tex`'s wording *exactly*, which is the mirror round 46 wrote the file for, and `methodological` is
now absent from every body file.

**Cold reconstruction, reading only the conclusion:** all three of your items are recoverable; (2) is
*"'Strongest baseline' is not an evidential principle"*, (1) plus the recipe's *"name the property, declare the
invariant family"* is P-relative invariance, and *"except at a twin: 0.500 by proof"* plus *"estimate its
ceiling, report the margin"* is the third. Before this round the second half of your third item was absent
outright.

## Your §21: the first 1.5 pages. That is already the rendered order.

You ask for Problem → Counterexample → Principle → Method → Killer experiment → Scope. `introduction.tex`, in
rendered order: **Counterexample** (¶1, AI Feynman `1.000` vs `0.972`) → **Principle** (a bolded one-sentence
criterion, then the boxed display) → **Method** (the three-object ladder: baseline / admissible control /
ceiling) → the S1–S3 worked example → **Killer experiment** (`The sharpest form of the test: a ceiling that is
a theorem`, `0.500` by proof vs `0.994`) → prevalence → contributions and **Scope**.

The one deviation is deliberate and is a standing grant: the leading *Problem* sentence was deleted from §1 in
round 46 as the most visible page-1 redundancy, and the problem statement is the **abstract's first sentence,
bolded, on rendered page 1**. We are reporting the rendered page rather than the source line, because *"page
1"* is a claim about the document a reader holds. So we have not restructured §1, but your underlying
complaint was real, and it was §5, not §1: the object you want at the *end* was missing from the end.

## Your §12C: the search's status, at the search's own site

Granted, and it was a real gap rather than a stated one. The general rule existed (§4.4's *Scope of
inference*: *"inferential claims are restricted to the contrasts prespecified in §3.4, so every exploratory
appendix test is descriptive"*) and the mechanism existed at the site (§4.2: a hill-climb *"given the split we
report"*, holding *"with that winner frozen, re-scored on four partitions it never saw"*), but neither status
*word* occurred at the site, so a reader had to join them. §4.2 now says the `0.676` is **exploratory** and
names the frozen re-score **the *inferential* test**. Length-neutral by construction on a page at 0.000pt:
+3 rendered characters, funded inside the same sentence.

## Your §15's sixth device: contrast sets are in Table 1, under another name

All six devices you name are in Table 1, but the sixth is there as the `counterfactual eval.` row, whose
citation *is* Gardner et al., and `contrast set` occurred **0×** in the paper, so a reader scanning for your
term could not find it. §2 now reads *"counterfactual evaluation (contrast sets; Gardner et al., 2020)"*,
which costs one parenthetical rather than a gloss plus a citation because the name goes in natbib's own
pre-note slot. The **row name** is deliberately untouched: it is a pinned literal, and Table 1 is at full
`\textwidth` on a page with 0.000pt of slack, so renaming it is a width edit with no funding.

## Answered by measurement, not by edit

| your point | the answer |
|---|---|
| **§7, K≥200** | Verbatim in the body already, in the sentence carrying the numbers you quote: *"That threshold is instrument resolution, not the effect's onset: unseen accuracy moves 0.05 over a 10× K range (0.843→0.894) while the class-level interval narrows 0.333→0.066."* |
| **§12B, five partitions** | In the main paper twice: §4.2 (*"all five class partitions"*) and §1 (*"re-scoring that search's winner, frozen, on partitions it never saw"*). |
| **§6, "too defensive"** | Measured before conceding: 22 `certif*`/`falsif*` occurrences across the six body files (abstract 2 · §1 6 · §2 2 · §3 6 · §4 2 · §5 4). Several are pinned at exactly **one** occurrence *because earlier reviewers required them*. The voice conversion you ask for already exists: §3's *"That limitation is also the deliverable."* and Corollary 3's title, *"Which family we declared cannot manufacture a pass."* This is the ninth consecutive round in which a reviewer's proposed deletion would remove a predecessor's requirement, so we answer it by measurement and delete nothing. |
| **§5, "don't sell it as theory"** | Already done in round 49, by one word: `criterion` → **`protocol`** in §1. The abstract contains **zero** occurrences of theorem/proposition/corollary, §1 never cites `thm:necessity`, and §3 bills the numbered results *"as scoping, not as theoretical contributions"*, which your own §5 credits. Your lowest sub-score (6.5, theoretical depth) is on the axis the paper deliberately de-sells. |
| **§13, terminology load** | §3's `Terms, once.` block glosses the concepts in one place, on rendered p4. You are the third reviewer to raise density and this is the third time it is the answer, and a prior reviewer asked that the block be moved *earlier*, not deleted. |
| **§20, "no more experiments"** | Honoured, second round running. Round 50 added no run; round 49's authorized run was refused by **its own pre-registered stop rule** (paired depth-8 retention 175/1102 at ‖L‖=5: structural, not compute-bound). |

## The gate: `check_artifact_counts()`

Five assertions, cross-file, target **derived and never hard-coded**; a missing file or an unmatched pattern
**FAILs** rather than silently asserting nothing:

```
ok 81  ARTIFACT: 3 verifier copies agree the verifier asserts against that many logs
ok 81  ARTIFACT: indexed-run count matches the verifier
ok 37  ARTIFACT: 44 + 37 = 81
ok  4  ARTIFACT: 33 of 37 are not new runs, so 4 new runs are counted as such
ok 33  ARTIFACT: the digit agrees with the prose that decomposes it (32 + the thirty-third)
```

Two notes on what it deliberately does **not** do. **It does not pin the assertion total.** That number is
the length of a run; a static gate cannot derive it, and inventing a second hard-coded constant to make the
gate look complete would fake exactly the coverage this round is about. It is gated by `verify_claims.py`
exiting 0 after printing `2486/2486 assertions passed`, and the gate prints a line saying so. **And the
"not new runs" assertion is `not_new > gained`, not `>=`**; we caught our own first version failing on the
historically *correct* text, where all 33 genuinely were bookkeeping. The real protection is the re-premised
*pattern*, which stops matching if a future round re-labels the count instead of re-premising the sentence.

`statements.tex` is now in the gate's file list, which was the whole finding. The PASS-line denominators are
**unchanged** (*21 protected claims survive, 4 absences hold over 6+6 files, 3 hold over all 16*), because
the file was already covered by the absence checks; what it had never had was a *count* check.

## The second defect, found after the round was finished: the Ethics Statement was wrong about our own ledger

We ask ourselves at the end of every round whether the paper is ready. It has now found a real defect three
rounds running, and this one is the *same class* as the round's own finding, one paragraph over.

Part B closed `statements.tex` by *opening* it: for the Reproducibility Statement's counts. The **Ethics**
Statement, two paragraphs above, said:

> the four already-published numbers among them are the *Our…* rows of Table 10

That is an **identity claim, and Table 10 has six *Our…* rows.** Its own caption says which four:
*"Eight rows are already-published numbers, and four of those are systems and leaderboards built by other
people; **the last two** are claims of *ours* that only this revision's audit settled."* So the ledger
decomposes as 10 = 4 others' + 4 ours-already-published + 2 ours-settled-here, and the four that sentence
means are the **first four**. That word pair is the whole repair (+10 rendered characters, on p10, outside the
page limit), and it mirrors the caption's own *"the last two"*.

**Why eleven reviewers read past it, and this is the part worth your attention.** The sentence's own *six*
(four already-published + two protocol-level, and the protocol-level two are *not* table rows) and the table's
*six* `Our…` rows (four already-published + the caption's last two) are **different sets that share a count.**
A reader who counts the `Our…` rows gets six, matches the "six" in that clause, and concludes the rows *are*
the six claims, which the same clause then contradicts. Two sixes that coincide are worse than one wrong
number, because each of them checks out on its own.

**And the gate already held the right number.** `LEDGER_OURS = 6` has been a constant in
`check_protected_claims.py` for rounds, verified against this very table by `check_ledger_distribution()` 1100
lines above the check we added this round. Both facts sat in one process and nothing compared them. So the
lesson we wrote at the top of this letter needs its second half:

> A gate's coverage is not the set of files it opens. It is the set of **claims in them it compares.** Opening
> a file for one paragraph is not covering the file.

Closed by `check_ledger_pointer()`, which derives everything and types nothing:

```
ok 10  POINTER: caption closes -- 8 published (4 others', 4 ours) + 2 settled here
ok  2  POINTER: the last 2 rows really are ours
ok  4  POINTER: statements.tex names the first four of 6 `Our...' rows, and the caption agrees which they are
```

The second assertion grounds *"the last two"* (and therefore *"the first four"*) in the **rendered row
order**, which is what both phrases are claims about. Its control reverts exactly the defect we found and
reproduces our own error message; `--control` goes **18 → 19**. PASS-line denominators are unchanged.

## One near-miss, recorded because the method is the point

Reading the p9 render showed `$0.500$` rendering at **normal weight** inside its bold clause: `\textbf` does
not reach into math mode. We changed it to `\mathbf`, built it, and **reverted it**, because the first
measurement counted the wrong population. Counting `\mathbf` sites alone says *"15 bold numerals, all
`\mathbf`, so this one is the odd one out."* Counting the population the site actually belongs to (numerals
that sit **inside** a `\textbf` span) inverts it: there are **16**, across the abstract, §1, §3, §4 and the
statements, and every one is bare. The paper has a coherent two-convention system that eleven reviewers have
read: **`\textbf` marks the clause, `\mathbf` marks a numeral in normal prose, and the two are never
combined.** The edit would have made the conclusion the paper's only `\mathbf`-inside-`\textbf`. It was
width-neutral, and width-neutral is not the same as correct.

---

**Verified from a clean `.aux`:** 0 errors · 0 `(Reference|Citation).*undefined` · 0 `Float too large` ·
exactly **2** overfull boxes, both pre-existing at unchanged sizes *and unchanged log lines* (1192 `\vbox`
6.4211pt, 1325 `\hbox` 3.509pt) · **99 pages** · body ends p9 · `E THICS S TATEMENT` the first body line of
p10 · Fig 1 p2, Fig 2 p3, Fig 3 p8, Table 1 p4, Table 2 p5 · **the eleven-page slack profile printed, not
summarised, and identical to baseline at every page**: p1 `+0.561` · p2 `+0.001` · p3 `+6.624` · p4 `+0.000` ·
p5 `−0.695` · p6 `−1.927` · p7–p11 `+0.000` (p5 has zero headroom and did not move) · four gates PASS with
controls **19 / 9 inline / 1 / 2** · `verify_claims.py` **2486/2486 exit 0**, three copies still md5
`5fa64467ef226550c86145934245bc85` · p3, p8, p9 and p10 read at 300 dpi · content-loss diff against a `cp -p`
snapshot: **9 sentences rewritten, 10 written, and the only deleted content span in the round is the single
word `methodological`**.
