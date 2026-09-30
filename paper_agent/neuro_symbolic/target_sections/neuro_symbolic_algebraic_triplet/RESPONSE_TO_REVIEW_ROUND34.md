# Response to the round-34 review

*Not part of the paper.*

**Summary: we did what you asked and nothing else, no new experiment, no new table, no new
dataset.** Your closing instruction was that the highest ROI is *"tightening the contribution/theory
framing and making the family-relative guarantee impossible to misunderstand, rather than adding more
tables,"* and that you would not want another major experiment absent a genuinely independent domain.
So this round adds **one paragraph, one sentence, one swapped clause and one navigation table**, and
the paragraph is funded entirely by deleting our own over-claims.

Assertion count **2250 → 2250**. No new run, no new log, no change to `verify_claims.py`.

---

## 1. Your reason (1) was right, and the paper was arguing *both sides of it* two paragraphs apart

This is the round's real diagnosis, and it explains the two axes that fell without any new negative
finding. §3.2 was selling the theorem:

- `:81`: *"The criterion, derived rather than assumed … not one evaluation discipline among several;
they are what a question about a representational property **reduces** to."*
- `:87`: *"Definition 1 is therefore **not a modelling assumption** but the two conditions the
  theorem forces."*

while §3.4, one page later, conceded the opposite in our own words: *"billed as **scoping** rather
than as theoretical contributions … a reader who finds the theorem close to a restatement of what an
admissible family means is not disagreeing with us."*

**A reader who notices both is reading an internal contradiction, and the honest resolution is to make
§3.2 match §3.4 rather than the reverse.** `:81`'s heading is now *"What is forced, and what is
chosen"* and its claim is only that **the direction of comparison is forced**; `:87` is **deleted
outright**. Theorem 1's three-part statement is untouched: round 29 added it on a prior reviewer's
explicit demand and three live sites cite it, so the end state is *scoped*, not retracted.

**Your §9 replacement sentence checked out against the paper, which has happened twice in eight
rounds.** *"The direction of comparison is forced"* is Theorem 1(iii); *"the admissible family is an
explicit methodological choice"* is what §3.3 already said. We used your sentence verbatim as the
conclusion's contribution (1).

## 2. Your §21 paragraph was not missing and not mispositioned; it was **diffuse**

This is a failure class we had not recorded before. Your four items existed at **four different
sites, none of them whole**, and only one was genuinely absent:

| Your item | Where it was |
|---|---|
| 1: what is mathematically necessary | `:81` + Theorem 1, *sold* rather than scoped |
| 2: the declared family stands in for the unenumerable A_P | `:87`, **before** Definition 1, inside the over-claim |
| 3: passing ≠ the family contains all P-invariant explanations | `:95`, before Definition 1; again in other words at `:102`, after |
| 4: family expansion measures **robustness**, not completeness | **absent everywhere**: 0 occurrences of seven phrasings across all `.tex` |

There is now one `\paragraph{What is and is not guaranteed.}` **immediately after Definition 1**,
with four explicitly labelled clauses (*(i) Necessary · (ii) Methodological, and ours · (iii)
Empirical · (iv) Open*), which is simultaneously your §21 and your §20 four-way separation. That is
why you put them adjacent, and we treated them as one edit.

**Round 33 created this gap, and the lesson is worth stating against ourselves.** Round 33 folded the
old post-Definition-1 *"What passing establishes, stated once"* into a new *pre*-Definition-1
intuition paragraph, on that round's reviewer's ask. Intuition-before and guarantee-after answer
different reader questions. **Consolidation is not free when the merged parts serve different reader
functions**: the fix here was a *split*, not a duplication, and this paper's own round-30 lesson
(redundancy is not salience) is what stopped us from simply restating item 3 a third time.

## 3. §10 and §21-item-4 are the same missing sentence, and it is the round's only new claim

`experiments.tex` §4.2 previously ended on the bare negative *"Completeness is not claimed and cannot
be."* It now reads **"So what this measures is robustness of the verdict to family specification, not
completeness"**: positive first, negative kept, and the identical wording appears in clause (iii)
of the new §3 paragraph, so the two positions agree word-for-word rather than approximately.

## 4. The round is self-funding, and we prove it by placement rather than arithmetic

De-selling is page-negative: the third time that has paid here. Against the new paragraph's ~9
rendered lines we removed `:81`'s selling sentence, all of `:87`, the tail of `:95` (which *moved*
into the new paragraph rather than being duplicated), part of `:102`, and §3.4's closing control-task
sentence that duplicated what Table 1 visibly prints.

**Result: pages 1–5 and 7–10 have byte-identical last-baseline positions to the round-33 build, and
page 6 moved 731.78 → 731.94 without spilling.** All thirteen body headings are on their round-33
pages (§1 p1 · §2 p3 · §3 p4 · §4 p7 · §5 p9 · Ethics p10), the body still ends on page 9, and page
10's first *body* line is still the Ethics Statement.

## 5. §16: the Reviewer map, and the four defects building it found

Your §16 is now the **first page of the supplement**, 15 rows, one per headline claim, with your
columns: **Claim (quoted from the body) · § · Run · Appendix · Code**. One row per *claim*, not per
run: `REPRODUCE.md` already lists all 42 runs, and a 42-row table answers a different question.

It is gated by a new `check_reviewer_map.py` (259 checks), because **a hand-typed table about the
artifact is precisely the class of prose that has drifted four times here.** Nothing in it is trusted:

- every Run cell must resolve to **exactly one** `load_log()` call site in the verifier, using the
  verifier's own regex: 0 *or* ≥2 both fail, since a substring match is a known loophole here
  (`r78` prefixes four tags, `r87` two, which is why that row spells its tag in full);
- every resolved tag must appear in `REPRODUCE.md`;
- every Code cell must name a file that **exists in the copy you receive** (`iclr-supplementary`,
  94 runners, not our working copy, which has 33: this distinction is itself a defect we would
  otherwise have shipped);
- every Appendix cell must be a `\ref`, never a hand-typed letter: round 33 shipped two false
  appendix letters, so a bare letter is unverified prose;
- every Claim cell must be a **verbatim quote from the body**, markup stripped;
- no appendix may become unreachable, in two tiers;
- and two positive controls plus two negative ones run in the same invocation.

**Four things it caught, all of which we would have shipped:**

1. **Appendix AE (*Auditing the Shared-Variable Positive Result at S2*) was reachable from
   nothing.** Not the body, not the reading map, not the map: only the 26-section range `AA–AZ`
   nominally covered it. This is the appendix-only failure mode one level deeper, and it is why the
   reachability gate has a second tier requiring every per-run section to have a *specific* pointer.
   Now cited from the reading map.
2. **Our own `Appendix~C` pointer was a hardcoded letter, and Appendix C had no label at all.** Fixed
   by adding `\applabel{C}{app:tokenbag}` and referencing it: the same defect class as round 33's
   two false letters, caught this time before the build.
3. **The `E3m` gloss we wrote was wrong.** We described the three AI Feynman variants as
   *"in-library / out-of-library / mixed"*, all 10 equations. `E3m` is an **in-library exp/log/power
   rewrite on the 4 eligible equations**: in-library yet structurally divergent, which is exactly
   what makes it the intermediate rung. Corrected against the appendix's own text.
4. **A navigation defect on page 6, of a class this paper recorded in round 25.** The new paragraph's
   clause (iv) cites Propositions 2 and 3, which are *appendix* propositions: a reader looking for
   them in §3 finds Proposition 1 only. Now named as *"stated with all proofs in Appendix …"*, funded
   by deleting `:81`'s now-redundant *"Proofs: Appendix …"* pointer, so the fix cost zero lines.

The table also cost three overfull hboxes on first build (`\texttt` file names have no legal
breakpoint) fixed with a breakable-underscore macro and tighter column separation, and the gate
expands that macro before parsing so a break hint can never hide a wrong file name.

## 6. §13, third time asked: the answer is navigation, not more hedging

Measured first: `random encoder`, `Johnson`, `Lindenstrauss`, `linear aggregation` and
`random projection` occur **zero times** in the numbered body, and Appendix C already opens by
stating its own limits (*"It is not a theorem, and a randomly initialised recursive network is **not**
a random projection of the token multiset"*) with its own `Validity domain.` paragraph and a
counterexample where the account fails outright.

So the hedging was already maximal and a second decline would not retire the axis. Instead the
Reviewer map's lead says once, at the head of the supplement, that the account is
**restricted-validity empirical and not a theory, that no claim in the body depends on it**, and what
it is actually for (why an *untrained* encoder scores above chance, which is what makes the
random-encoder row a meaningful skyline). **Both halves of that are gated**, not asserted.

## 7. §15: three of your fifteen terms glossed, at zero body cost

`E3`, `E3b` and `E3m` are now defined in one sentence in the map's lead. All three are appendix-only
in the numbered body, which the new gate now enforces rather than assuming.

**One measurement worth reporting because it corrects our own earlier reading.** We initially thought
`E3`/`E3b` were printed in the body as Figure 1 bar labels, and started rewriting them. They are
not: `figure_overview.tex` is `\input` **after** `\appendix`, so those labels are appendix text. We
reverted the rename and kept the tag names, which are the traceability handle. What we did keep is the
removal of two orphan `†`/`‡` markers on those labels, which had no legend anywhere in the document.

## 8. §11, §14, §17, §22: measured, not edited

Adding a fourth statement of an already-thrice-stated claim is redundancy, and round 30 proved
redundancy is not salience. So each of these is a measurement, and we report the numbers rather than
the edit:

- **§11 (don't sell the positive broadly).** Already scoped in four distinct phrasings in the body:
  `composition-of-known-transformations` ×3, `does not establish systematic compositional reasoning`
  ×1, `not compositional reasoning` ×3, `four primitives` (are not a library) ×2.
  **You praise this in your §3 and ask for it in your §11.** We are not arbitrating that; we
  shortened where we could and are telling you the measurement rather than deciding quietly.
- **§14 (unit of analysis prominent).** Already bolded in the body on page 7: *"The class (equation)
  is the primary unit, so every interval is a class-level bootstrap and seeds quantify training
  stochasticity only."* And `25 seeds`, `5 seeds` and `n{=}25` occur **zero times** in the body, so
  the misreading you were guarding against is not reachable from the body at all.
- **§17 (do not remove the corrections/retractions).** Kept, all six. Three are gated literals in
  `check_protected_claims.py`, so they cannot be dropped silently in a future round.
- **§22 (title).** Kept, on your own stated condition: the terminology *is* built around it,
  `admissib*` ×29 in the body, `family-relative` ×5, `admissible ceiling` ×5.

We also skipped a fifth, deliberately: the plan reserved ~5 words for §1's contribution (1) marking
the family as *declared, not discovered*. Pages 1 and 2 measure at exactly zero slack, and `placeins`
partitions the document per section so nothing outside pages 1–2 can fund it. The substance is
already there (*"an explicitly declared family"*, *"no admissible family can turn it into a
certificate"*), so we left it rather than push the conclusion onto page 10 for five words.

## 9. Verification

**Gates on the final build:** `0` errors · `0` undefined references or citations · `0` `Float too
large` · exactly **2** overfull boxes, both pre-existing · **88 pages** (+1, all of it appendix,
which is page-limit-exempt) · abstract ends page 1 · body ends page 9 · page 10's first *body* line
is the Ethics Statement · all thirteen body headings on their round-33 pages · per-page last-baseline
position identical to round 33 on nine of ten body pages, page 6 `+0.16` with no spill ·
`check_protected_claims.py` PASS at 19 claims and 2 required absences with both controls firing ·
`check_reviewer_map.py` PASS at 259 checks · `verify_claims.py` exit `0` at **2250/2250 in all three
code copies** · `check_tex_numbers.py` clean on both rewritten blocks · pages 6, 9, 14 and 15 read as
rendered images · cold reconstruction read of the abstract and §1 from the PDF.

**One process note.** Our own shell word-splitting bug recurred for the sixth time and silently
returned `0` for **every** §8 measurement above, which would have read as a genuine finding that the
paper says none of those things. It is caught only because the re-run carries a positive control and
a file-count assertion. We mention it because the same failure shape has cost this paper real
measurements before, and because it is the reason every count in this document was produced by a
command that also proves it can return non-zero.

---

## 10. Readiness pass (run after the above, before sending)

A direct readiness question triggered one more audit rather than a re-reading of the gate list, and it
found **three false statements about the artifact: one of them ours from this round.** All three are
fixed and all three are now gated.

1. **One map row's run tag and command were wrong.** The row for *"the coverage-closure mechanism is
   polynomial-specific"* cited `r87_boolean_tier3` and `run_r71_tier3_baselines.py --corpus boolean8`.
   That claim is boolean8's **coverage ladder**, reported in the appendix the body itself points to,
   whose runs are `r83`/`r84`; `r87` is reported in a *different* appendix. Corrected to `r84` and
   `run_r81_composition_primitives.py --corpus boolean8`, per `REPRODUCE.md`'s own entry. **Every
   individual cell check passed**: the tag resolved uniquely, was in `REPRODUCE.md`, the script
   existed, the appendix had an `\applabel`, the claim was a verbatim body quote. What no check
   examined was whether the **Run and Appendix cells refer to the same experiment.**

2. **Two runs were tagged nowhere in the appendix, and one of them carries a headline number.**
   Appendix K states that every EQNET run is tagged in the appendix subsection that reports it. Of the
   verifier's 42 tags, `r72_structure_twin` and `r73_swap_twin` appeared in **no appendix section in
   any form**, while the appendix section that *does* report their numbers (`0.788`, `0.994`, the
   `0.206` residual, the rotation-twin column) named only `r75`. So the paper's own convention was
   broken exactly where the twin result (one of §4.2's two lead findings) needed it. That caption
   now names all three tags with what each contributes.

3. **A hardcoded tag range had been outgrown by eight runs.** Appendix K said the runs tagged in their
   own subsections were *"`r70`–`r91`"*. `r92`–`r99` (family stress, deep composition, order
   diversity, the code audit, both SCAN runs, family robustness and the code S3 ladder) follow the
   same convention and sit outside the stated range, so the sentence was false for eight of the runs it
   was describing. Now stated as *"every run from `r70` onwards"*, which is measured: all 32 such tags
   are named in a subsection. The gate additionally **fails if a literal range is ever written back
   in**, since a hardcoded range is what drifted.

**Two checks added, taking `check_reviewer_map.py` from 180 to 259.** First, each row's Claim must
appear in the **section its own row names**, not merely somewhere in the body: checked by chunking the
body per `\label{sec:...}` (all 15 rows pass). Second, tag **registration** is derived rather than
read: every tag from `r70` up must be named in some appendix subsection, everything below it in
Appendix K's table. That matcher is substring-safe, because a bare `r79` occurs inside the unrelated
tag `r78_r79_bag_ties`, and it ships with three controls: an absent tag must not match, the
short-form-inside-a-longer-tag case must not match, and a legitimate short reference must.

**Re-verified after these edits:** 0 errors · 0 undefined references or citations · 0 `Float too
large` · exactly **2** overfull boxes, both pre-existing · **88 pages** · body ends page 9 · page 10's
first body line is the Ethics Statement · all six section headings on their baseline pages · the map's
lead and table still together on page 15 · `check_reviewer_map.py` **PASS at 259 checks** ·
`check_protected_claims.py` PASS at 19 claims and 2 absences · `verify_claims.py` untouched, so
**2250/2250** stands · 0 `__pycache__`, 0 home-path and 0 author-name hits in the shipped copy.
