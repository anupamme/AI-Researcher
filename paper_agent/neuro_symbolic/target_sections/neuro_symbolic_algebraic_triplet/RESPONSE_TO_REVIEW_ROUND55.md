# Response to Review, Round 55

**TL;DR; you asked for this as a paragraph in the paper (§16). It costs seven rendered lines the body
does not have, so here it is where a reviewer actually reads first.** A baseline is evidence against an
alternative explanation only if it is *invariant* to the claimed property. So the statistic is not a
comparator's score but a *declared family's ceiling*, and as of this revision the abstract says that in
symbols, $M(h) > \sup\nolimits_{g\in\mathcal{F}}M(g)$, the same string as the boxed display on page 1.
Everything else in the paper is evidence for that one sentence: a proof that at a shape-matched twin the
ceiling is *exact* at $0.500$ for every invariant map (so the family is not a stand-in there), ten
audited claims across three modalities, eight of them already published and four of them other people's,
and a released auditor that reproduces all of it. What it never buys is certification: of mechanism, of
completeness, or of compositional reasoning.

**Assertion count: unchanged at 2591.** No experiment ran, no number moved, `equivalence.py` was
untouched. `verify_claims.py` cannot read the `.tex` by design (its own note, line 6337), so a round whose
diff is entirely source structure is checked by the `.tex` gates instead: **one new gate,
`check_criterion_form`, and `check_protected_claims.py --control` rises 23 → 25**, two, not one, because
the new check has two independently corruptible halves (the `\nolimits` form, and the agreement of the
abstract's string with the boxed display's), and its control fires on each. md5
`85e77e416b9b89fce4665bff4805348c`, identical across all three copies.

You wrote that we do not need more experiments; that 7 → 9 on clarity comes from *"simplifying the
argument, not adding more explanation."* Taken literally, and it decided the whole round: **nothing was
added to the body. Three things were reformatted, one sentence was extended by three words inside its own
line, and the page budget went up.**

---

## 1. Your top three, shipped, with the page and the measured cost

| your ask | your weight | what shipped | page | cost |
|---|---|---|---|---|
| **#1** abstract built on one criterion | +0.5 | the criterion is now **math** in P2: *"That direction of comparison is forced --- $M(h)>\sup\nolimits_{g\in\mathcal{F}}M(g)$; **which** family we declare is the choice."* | **p1** | **0 rendered lines, 0 pages** |
| **#2** Figure 1 as the *n*-step audit | +0.4 | the four decision boxes are **numbered 1–4**, and the caption's count is now checkable against the picture: *"steps~2 and~4 end the inference, and only step~2 before any learned score is read"* | **p2** | **−1 caption line; +3.475pt** of p2's slack on its own, before #5 supplied the rest |
| **#5** the prose "three objects" becomes a table | +0.2 | one bold ordinal and one $\Rightarrow$ per object, the mapping grammar of the table, in prose flow: *"**(1)** a *baseline* $\Rightarrow$ did the model score higher? **(2)** an *admissible control* $\Rightarrow$ could something blind to $P$ have scored that? **(3)** the *family-relative admissible ceiling* $\sup\mathcal{F}$ $\Rightarrow$ could the *best* such control have…"* | **p2** | **8 → 7 rendered lines** |

**On #5 I owe you the measurement, because I tried your version first and it lost.** This paper already
contains the device you are asking for: the `\footnotesize` `r@{$\Rightarrow$}p{}` mapping tabular at
`methodology.tex:337–338`, six rows, rendered on p6, so the comparison was against a real render, not an
estimate.
Three rows there cost the lead-in line (11.6pt) + four table lines at `\arraystretch 0.95` (37.6pt) + two
paragraph breaks (~10pt) + the closing sentence and its gate-pinned parenthetical, which cannot live in a
cell (46.4pt) ≈ **105.6pt**, against the prose's 8 rendered lines = **92.8pt**. That is **+12.8pt on a page
that carried +0.001pt**. The ordinal form delivers the same one-question-per-object mapping and comes out
**110 rendered characters shorter**, because each object's question stops being a subordinate clause.
If you still want ruled rows, the honest price is one body line, and it has to come from somewhere.

**What I did not do on #2, and it is deliberate: I did not cut the graded band to reach five boxes.** Your
fifth step is the pass verdict, and that *is* the band. It is round 47's §8 requirement and round 51's
graded-entitlement work, **and it is your own §7 ask for a boxed statement of what a pass means.** Cutting
it would delete two predecessors' requirements and one of your own in a single stroke. The four boxes are
four rather than five because *"declare the family"* and *"measure its ceiling"* were folded into one box:
at five, `\scriptsize` text does not set legibly at the strip's ~0.85 `\resizebox` factor. Numbering makes
the procedure readable without adding a box.

---

## 2. The defect this round found is ours, and no grep could see it

Putting the criterion in the abstract as math created a failure mode this repo had no check for. In a
paragraph, `\sup_{g\in\mathcal{F}}M(g)` sets its subscript **below** the operator and grows that line's
height; `\sup\nolimits_{...}` sets it to the right and costs nothing. Both compile. Both render. They read
identically to a human. No reference breaks, no overfull box appears, no number changes, and
`verify_claims.py` cannot see it because it cannot read the `.tex`. On a body whose pages carry 0.000pt and
whose §3 pages carry **negative** slack, one silently grown line moves the conclusion off p9 and the body
to ten pages: a desk reject.

So the round added the gate for it, `check_criterion_form`, which asserts (a) no `\sup_` without
`\nolimits` in any document file, and (b) that the abstract and the boxed display spell the criterion's
right-hand side with the *same string*, so a later round cannot "simplify" one of them and leave the paper
stating its central criterion two ways.

**On its first run it failed: on a line written eight rounds before this one.** `related_work.tex:93`,
§2's novelty paragraph (which is your own #7's prescribed one-paragraph novelty statement) rendered line
144 on **p3**:

> **none estimates $\sup_{g\in\mathcal{F}}M(g)$, the *ceiling* of a declared family**

And here is why it survived eight rounds: **p3 is the one body page with real slack** (+6.6pt before this
round), so a line grown there cost nothing observable. Had the same sentence sat on p4, p7, p8, p9 or p10
(all of which carry **0.000pt**) it would have pushed a page. The defect was invisible because it landed
on the only page that could absorb it, which is the least reassuring reason a defect can be invisible. Now
fixed to `\sup\nolimits`, and all three sites are pinned to one string. A gate written for one site's
*future* defect found another site's *present* one, which is the best argument I have for writing them.

**And the round's own new clause was caught on the render, not by any gate.** The abstract's first draft
read *"$M(h)>\sup\nolimits_{g\in\mathcal{F}}M(g)$, **not merely** $M(h)>M(g)$"*, and the boxed display,
the last line of the **same rendered page**, already ends *"— not merely $M(h)>M(g)$"* verbatim, about
thirty lines below. That is exactly the redundancy your review is about, self-inflicted, in the round whose
thesis is *simplify, do not duplicate*. The duplicated half is gone from the abstract; the contrast stays in
the box, and in the paragraph's own opening clause, which makes it in words.

---

## 3. Your §8 is declined, and the paper moved in the opposite direction instead

You ask us to rename Proposition 1 to *"Why the ceiling is the correct statistic"* and to state that it
*"formalizes the criterion rather than introducing a new mathematical result."*

**Round 39 granted the current title. `methodology.tex:192` has said the weaker thing for sixteen rounds:
*"billed as scoping, not as theoretical contributions"*, and round 54 scored Theoretical contribution
7/10 for exactly that under-filing.** Its finding was that §3's four-kinds list filed the paper's own
proved results under the heading ***open***, so the one paragraph a reviewer reads to score theory
contained no proved non-definitional property. One mislabelled word cost two rubric lines. Adding your
sentence would be the sixth time this paper pre-emptively supplied a reviewer's objection in the
reviewer's own words.

So the standing lesson applies: **a pre-emptive concession the paper wrote about itself keeps supplying the
next reviewer's objection verbatim.** Round 54 priced the repair and could not pay for it, flagging it in
print as *"the first thing I would spend page room on if any existed."* This round paid it.
`methodology.tex:192` now reads:

> …but what follows *from* them is not definitional: closure puts a trained readout *inside* the family
> (Prop. 1), the ceiling is then measured non-monotone in resolution (Cor. 2), and **no admissible family
> certifies** (Prop. 3) — not one of the three a property of suprema.

Three things about it. **It names Proposition 3 by its own title** (*"No admissible family certifies"*),
which is round 54's filing lesson applied: an object should be called what it is. **The non-triviality
claim now covers all three** rather than two. And **`certif*` in §3 rises 2 → 3**, and precisely: the two
that were already there are a float caption and a table cell, so **this is the first occurrence of the word
in §3's running prose.** The claim your §8 presses on was, until this round, stated everywhere in the paper
except the section that states the theory.

Cost: **4 rendered lines before and after, p5, slack profile byte-identical.** Funded inside the paragraph
by two cuts (`, and the ceiling` → `, the ceiling`; and a trailing clause, below). The line now ends at
**exactly** the right margin: 0.00pt of tail, so I will say plainly that §3 has no room left at all.

**Two things this repair does not do**, stated because you would find them. It names three
non-definitional results and there is a **fourth**, Prop. 4 (at a twin the ceiling is exact over every
invariant map); it is not in the list for want of a single character, and it is stated as proved 23 lines
below. And the removed clause was *"and every ceiling here had to be re-measured"*, whose content
survives in the same sentence (*"the ceiling is then **measured** non-monotone"*), in Cor. 2's own
statement, and at `methodology.tex:215`.

---

## 4. Nine of your asks measure as already applied. Here is where, and the pages

I am putting this fourth, not first, because leading with *"it is already there"* is what rounds 47, 50, 53
and 54 did on their equivalents and the score stayed 7 every time. §5 is why I think that keeps happening.

| your ask | measured, on current source | where |
|---|---|---|
| **§12** *"reduce terminology, especially replace `skyline'"* | **0 occurrences in the rendered body and 0 in the floats.** All 35 are in the appendix — 33 in prose, 2 inside `\texttt{}` run tags | Part E, below |
| **§12** "falsification certificate", "protocol gate", "provenance", "saturation" | **0 each in the body** | — |
| **§12** "novelty axes" | **0 in the body**, 1 in a float caption | Table 1 |
| **🟡8** revision archaeology to the appendix | **14 of 15 archaeology phrases are 0 in the body.** The survivors are three: *withdrawn* ×2 (one of them a table cell) and *withdrawing* ×1, all three the self-correction disclosure your own §17 asks us to keep. **0 `r`-tags in body prose**; the 6 that render are inside float captions. The incident ledger is Table 11 | **p37** |
| **🟠7** compress related work to four paragraphs, one of them the novelty statement | §2 is **already exactly four paragraphs**, and all four fit on **one page**: `related_work.tex:4`, `:25`, `:93`, `:201`, and **`:93` is the one-paragraph novelty statement you prescribe**, headed *"What is new, given all of that"* | **p3** |
| **🔴4** family-relative + falsification caveat immediately after the definition | abstract P2 puts *"no admissible family can turn it into a certificate"* two sentences after the ceiling clause; §3's four-kinds paragraph sits immediately under Def. 1; and the sentence after the boxed display is `introduction.tex:98`'s three objects, whose third *is* the family-relative one | p1, p2, p5 |
| **🔴3** the twin as the central empirical story | abstract **P3 opens with it**; `introduction.tex` gives it its own bold paragraph (*"The sharpest form of the test: a ceiling that is a theorem"*); Figure 1's band leads with it; §4.2 is its section; rung 4 of Figure 2 | p1, **p2**, p2, p7 |
| **§7** a boxed statement of what a pass means | **Figure 1's graded band is exactly that**, three boxed cells, dark→light: *absolute* / *a pass ⇒ family-relative* / *never mechanism* | **p2** |
| **§15** *"the key object is an equivalence class of explanations"* | **declined, with the reason.** An admissible family is a set of representations *blind to $P$*, not an equivalence class of explanations, and at the twin its supremum is **exact and attained** (Prop. 4), which is a strictly stronger statement than class membership. Recasting it as an equivalence class would lose the one place the ceiling stops being family-relative | §4.2, Prop. 4 |

**One correction to your §2.** Your list of what to cut from the abstract names SCAN and a correction
history. The abstract contains **neither**, no SCAN, no revision history, no correction ledger, and (since
round 46) no GIN number at all. That list describes a document we do not have, which matters because two
of your eight priorities are subtraction from a place nothing is.

---

## 5. Part E: "skyline" is kept, and the real defect your §12 points at is repaired

Your named term measures at **0 in the body and 0 in the floats**; all 35 occurrences are in the appendix,
so there is nothing to replace where you are reading. In the appendix I am keeping it, on four
measurements:

1. It is a **deliberate** exception, not an oversight: `check_protected_claims.py`'s ABSENT pin for
   *"random-encoder skyline"* is scoped to body+floats, with the standing comment *"The appendix uses the
   phrase in its own metric sense, which is why this is scoped to body+floats."*
2. It names the **shipped artifact's identifiers**, and two of the appendix's 35 occurrences are literally
   run tags (`\texttt{r60_separability_predicts_skyline}` and `\texttt{r67_score5_skyline}`) that a
   reader types to reproduce a row. On the other side of those two strings sit
   `run_r67_score5_skyline.py`, `run_r60_separability_predicts_skyline.py`, `run_r69_skyline_sweep.py` and
   `logs/r69_skyline_sweep.json`; the term also appears 4× each in `verify_claims.py`, `AUDITOR_README.md`
   and `REPRODUCE.md`, and in Appendix U's own heading (*"Every Claim Against Its Strongest Skyline"*).
   Renaming desynchronises the paper from the supplement you are invited to run.
3. **Decisively: a skyline and a ceiling are different objects.** A skyline is *one non-learned baseline's
   own score*; the ceiling is a *supremum over a whole declared family, trained readouts included*.
   "Replace skyline with ceiling" would collapse the exact distinction this paper exists to draw.
4. Appendix O's **"Dual-skyline divergence"** is the measurement that proves they are different objects:
   under distribution shift the token-bag skyline reads $0.900$ and the random-encoder skyline $0.124$ on
   **identical forms under an identical protocol**: a 7× divergence, and the passage's own conclusion is
   that *"the random-encoder skyline understates the token-bag ceiling."* A skyline can sit far below the
   ceiling it gets read as. That is the distinction, measured.

**But you were pointing at something real, and it was worse than a bad word: across all 33 occurrences it
then had, the term was never defined anywhere.** So it is defined once, at its first use in the front matter,
in one sentence, pointing at both the contrasting object and its own evidence:

> **That term, defined once:** a *skyline* is **one non-learned baseline's own score**, never the
> *ceiling*, which is a supremum over a whole declared family, trained readouts included (Prop. 1);
> Appendix O measures two skylines diverging $7\times$ on identical forms, one of them far below the
> ceiling it is read as.

**That sentence is on its second version, and the first one was wrong in a way worth reporting.** It read
*"two skylines disagreeing under one ceiling"*, which asserts a measurement Appendix O does **not** make:
there is no supremum in that passage and no ceiling measured above both. The corrected clause quotes what
the passage actually reports, and is the stronger claim for the definition's purpose. We caught it in this
round's own readiness pass, on our own new prose, which is where round 53 taught us to look first.

**This section cost one page: the document is 101 pages, not 100.** Stated rather than buried, because the
body slack profile *cannot* see an appendix edit: `pdfinfo` is the only witness, and it caught this. The
page lands at the tail of a line-numbered code listing; the body is untouched, and Appendix O also gained
the label it had been missing, which is why the definition can point at its own evidence at all.

---

## 6. §17, §18, §22: what I agreed to, and where we differ

**§17, the caveats not to simplify away: agreed, and none of them moved.** *"declared, never complete"*
(`introduction.tex:10`, p1–2); *"no admissible family can turn it into a certificate"* (abstract, p1) and
*"The audit falsifies; it certifies nothing"* (conclusion, p9); *"four primitives are not a library"*
(abstract, p1); the code-modality inversion that fails to replicate: **our own** (abstract P2, p1, and
§4.3); and the ledger's two withdrawals against ourselves (Table 11, p37). This is the section most at risk
from your own #6–#8, and it is where the subtraction stopped: the cuts you asked for were already made
*around* these, and every one of them is still on the page.

**§18, the nine-page structure.** Ours, measured off the `.aux` and the render rather than intended: §1
**p1–2** · §2 **p3** (all four paragraphs on one page) · §3 **p4–7** (§3.2 p4, §3.3 p6, §3.4 p7) · §4
**p7–9** (§4.1 p7, §4.2 p7, §4.3 p8, §4.4 p8, §4.5 p9) · §5 **p9** · body ends **p9** · ethics first on
**p10**. Two deliberate differences from your outline. The novelty table floats to **p4**, one page past
the §2 text that cites it, because it is the argument that the audit is new and §2 is where a reviewer
looks for that: moving it later would put the argument after the method. And the appendix is deep (56
lettered sections) because the disclosure requirements of rounds 30–52 live there rather than in the body,
which is the same trade your §17 asks us to protect.

**§22, the before-submission list.** Everything in it that is ours to do is done and measured in §1–§5
above; what remains is not editorial; the supplementary package is built from the redacted copy
(`artifact/iclr-supplementary`: 0 `__pycache__`, 0 `.pyc`), the verifier was run in the working copy so the
shipping copy is never re-dirtied, and the PDF is exported after the final build rather than shipped stale.

---

## 7. The honest part, and the one question

You are the **second consecutive reviewer to say the evidence is sufficient** (round 54: *"You have enough
experiments"*) and the **first to name both the target axis and the method**; *simplify, do not explain
more.* That is why this round added nothing and removed instead.

But the ledger is what it is:

| ask | rounds it was raised in: counted off the file's own comment ledger | how it was answered | score after |
|---|---|---|---|
| the decision figure as the visual center | **15, 38, 44, 46, 47, 51**, and now **55** | built → promoted to p2 → the criterion as a formula → S1–S3 clause → cue-level/family clause → graded band → **numbered** | 7 |
| the comparison table *is* the novelty argument | **35, 40, 45, 46, 47, 48, 49, 50, 51, 52**, and now **55** | caption re-led on the argument; three columns and a row added; every unit of `\tabcolsep` and rulesep spent | 7 |
| clarity / burial under machinery | **24, 53, 54, 55** | three consecutive rounds now | 7 |

Five reviewers have now asked for objects that exist on pages 1–4, and four rounds answered by making them
more prominent. **The score did not move, which is evidence the answer is not prominence.** Your review is
the first to point somewhere else: at *redundancy* rather than *findability*, and on that reading the
round found three real absences (a formula, four ordinals, a mapping grammar) and paid for all of them by
deleting our own duplication. Summed across the eleven measured pages, slack went from **5.25pt to
17.55pt**: from 0.45 of a rendered line to 1.5 lines, the first time in eleven rounds this paper has had
room to spend on anything.

So the question, and it is the one I would most like answered: **your §2 asks us to cut SCAN and a
correction history from an abstract that contains neither, and your §7 asks for a boxed statement of what a
pass means that has been on page 2 since round 51.** Both are cases of looking for something and reporting
it absent. If you can tell me *where you looked* (which page, which paragraph) that is worth more to this
paper than any rewrite, because it locates the failure in the layout rather than in the content, and the
layout is the thing I can still change.

---

## 8. Verification

0 errors · 0 `(Reference|Citation).*undefined` · 0 `Float too large` · exactly **2** pre-existing overfull
boxes at **unchanged sizes** (`\vbox` 6.4211pt, `\hbox` 3.509pt) · **101 pages** (`pdfinfo`; 100 → 101, from
Part E, attributed and stated in §5) · Figure 1 **p2** · Figure 2 **p3** · Table 1 **p4** · Table 2 **p5** ·
Figure 3 **p8** · §4.4 **p8** · §4.5 p9 · §5 p9 · body ends **p9** · `E THICS S TATEMENT` the first body
line of **p10** · p8/p9 hold **120/127** non-blank lines (`pdftotext -f p -l p | grep -c '[^[:space:]]'`),
unchanged.

**Slack profile, printed rather than summarised**, p4 through p11 byte-identical to the pre-round build,
which was rebuilt from a snapshot to confirm it rather than quoted from notes:

| | p1 | p2 | p3 | p4 | p5 | p6 | p7 | p8 | p9 | p10 | p11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| before | +0.561 | +0.001 | +6.624 | 0.000 | −0.695 | −1.927 | 0.000 | 0.000 | 0.000 | 0.000 | +0.687 |
| after | +0.561 | **+9.463** | **+9.463** | 0.000 | −0.695 | −1.927 | 0.000 | 0.000 | 0.000 | 0.000 | +0.687 |

Four gates PASS; controls **25 / 9 inline / 1 / 2**. `check_reviewer_map`: 18 rows, 305 checks, 52 literal
`load_log()` sites, 56 appendix letters. `check_caption_rows`: 36 caption literals across 38 floats.
`check_figure_provenance`: 10 figure values. `verify_claims.py` **2591/2591**, exit 0, md5
`85e77e416b9b89fce4665bff4805348c` identical across all three copies; `REPRODUCE.md` md5
`a24ec83efcbe97fb7f69758a028e0a66`; 85 indexed runs; no new run and no new log, so no `log_dir` to redact.

**Content-loss diff** against a pre-round `cp -p` snapshot of all 18 sources, comment- and
markup-stripped at sentence level: every change is one of the five parts, and exactly **two spans were
removed**, both authorized and both checked first:

1. Figure 1's caption cross-reference sentence (*"Figure 2 settles each step on a real benchmark; Figure 5
   is the released auditor's screen-by-screen checklist"*): verified to orphan no float (`fig:framework`
   keeps 2 body citations, `fig:procedure` keeps 2), pinned by no gate literal, and named in none of the
   recorded round-46/47 grants.
2. `methodology.tex`'s *"and every ceiling here had to be re-measured"*: content preserved in the same
   sentence and in two other places (§3 above).

Pages 1, 2 and 3 were rendered at 150 dpi and read, not merely extracted as text, which is how both of
this round's real defects were found: the abstract's duplicated *"not merely"* (p1), and, via the gate that
render prompted, `related_work.tex`'s eight-round-old `\sup_` (p3, rendered line 144). The final render
confirms what no gate can: Figure 1's four boxes are legible and unwrapped at the `\resizebox` factor, both
exit arrows still land where they did, the graded band is still two lines, and the abstract's new
$\sup\nolimits$ sets its subscript to the right of the operator rather than below it.
