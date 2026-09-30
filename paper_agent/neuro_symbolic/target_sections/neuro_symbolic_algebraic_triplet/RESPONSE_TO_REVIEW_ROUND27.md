# Response to the round-27 review

*Not part of the paper.*

**Summary: your two most important asks (the novelty comparison matrix (§20.1) and a canonical
`Claim | Control | Learned | Verdict` table (§16)) were both already in the body, as Table 1 on
page 4 and Table 2 on page 5, both cited from §1. You proposed building them from scratch anyway.
We take that as the finding of the round: a body float whose *format* does not match the reader's
question does not register any more than an appendix result does.** So both tables have been
rebuilt in the shape you specified, and no new experiment was run. The assertion count is unchanged
at **2090**: every number promoted into a new column was already in the body prose.

Your review also found **one genuine gap**, and it is your Concern 2.

---

## 0. The scorecard

| Criterion | R25 | R26 | **R27** |
|---|---|---|---|
| Technical soundness | 8 | 8 | **7.5** |
| **Novelty** | 7 | 7 | **6.5–7 ← binding, third round** |
| Significance | 8 | 7.5 | **7.5** |
| Empirical quality | 8 | 8.5 | **8** |
| Clarity | 7.5 | 7.5 | **7.5** |
| Presentation | — | — | **7** |
| Reproducibility | 9 | 9 | **9** |
| **Overall** | **7** | **7** | **7** |

We take your instruction literally: *"I would not add more experiments indiscriminately at this
point… The highest-return work now is to make the novelty of the framework absolutely
undeniable."* Zero GPU-hours were spent. Everything below is format, one substantive addition, and
four declines with the measurement behind each.

---

## 1. The finding: both tables you asked us to build were already on pages 4 and 5

| What you asked for | What already existed |
|---|---|
| §20.1, *"the most important"*: a matrix of admissibility auditing vs shortcut baseline / control task / strongest baseline / invariance test | `tab:novelty`, **Table 1, page 4**, four prior devices, cited from §1 |
| §16: a canonical `Claim \| Control \| Learned \| Verdict` table | `tab:entitlements`, **Table 2, page 5**, ten rows, exactly that content |

Table 1 was three *prose* columns (*Prior device / Question it answers / What it leaves open*) whose
rows wrapped to two rendered lines each. Table 2 merged the control and the learned score into one
prose verdict column. Both said what you wanted said; neither was **scannable**, and you read past
both.

This is the ninth instance in this revision history of the same failure mode, and the first where
the material was in the body all along. The previous eight were *appendix-only results do not
exist*. The generalisation is: **a claim registers only if its format matches the question the
reader is asking.**

### Table 1 is now the matrix, with a sixth column that is $\times$ on our own row

Six axes; the two where only we score are columns 3 and 4:

| Prior device | benchmark solvable? | property-relative? | **comparator invariance?** | **family ceiling?** | falsifies only? | certifies mechanism? |
|---|---|---|---|---|---|---|
| shortcut baseline | ✓ | × | × | × | ✓ | × |
| control task | partly | partly | × | × | ✓ | × |
| strongest baseline | × | × | × | × | × | × |
| invariance test | × | ✓ | partly | × | ✓ | × |
| held-out split | × | × | × | × | × | × |
| **admissibility auditing** | ✓ | ✓ | **✓** | **✓** | ✓ | **×** |

Three notes, each deliberate:

- **The last column is $\times$ on every row, ours included.** That is your §20.2 relative-completeness
  ask implemented *inside* the table that answers §20.1, and it is the reason the table does not read
  as advocacy: no comparator-based method certifies a mechanism, and that follows from admissibility
  itself rather than from our engineering.
- **`invariance test` is a new row and the strongest foil**, cited to CheckList (Ribeiro et al., ACL
  2020), whose `INV` *is* the invariance test. §2 now carries the one-clause distinction: a
  behavioural invariance test asks invariance of the **model's** prediction; admissibility asks it of
  a **comparator**. That is a new bib entry, which costs zero body lines.
- **We did not paste your cells.** Your matrix gave *strongest baseline* a ✓ for shortcut-testing. A
  superiority comparison over a sophisticated comparator does not test whether the benchmark is
  solvable without the claimed capability, so that cell is $\times$ here. This is the fourth
  consecutive round in which reviewer-supplied text was false about the paper, and the pattern is
  now expected rather than surprising: **use your structure, never your text.**

### Table 2 is now `Claim | Level | Best admissible control | Learned | Verdict`

Same ten rows, same float, **one rendered line each**, no new numbers: `0.100` and `+0.038` were
already in §4.4 and §4.2, the rest were already in the table. `check_tex_numbers.py` confirms all
**13** numeric literals in the rebuilt block trace to a log.

Reformatting it exposed four cells where the meaning would have been silently lost, all caught by
diffing the row set against the pre-edit file rather than by any automated gate:

- row 9's verdict *not established* had become *no*, **not the same claim**;
- row 10's *out of reach* had lost **in principle**, which is Proposition 4;
- row 8 had lost **depth-8**, so `0.736` no longer named what it was measured at;
- `+0.024` had been typed into the **Learned** column, where it reads as a score rather than a delta.

Row 5 is the one place we did **not** follow your column scheme: it stays an against-us row about
*protocol* sensitivity, because its verdict is `sensitive`, not `passes`, and forcing it into a
control-vs-learned pair would have converted a verdict against us into one for us.

---

## 2. Your Concern 2, which is the one real gap: the twin is a membership test, not a proof

You ask *"why does passing one twin test establish invariance to the entire claimed property?"* and
propose *"the twin is an operational membership test for the declared family, not a proof of global
invariance."*

**Measured before editing: `globally invariant` and `global invariance` appeared zero times in
`methodology.tex` and zero times in the appendix.** The distinction was genuinely absent: in a
paper that states every other *what-this-does-not-establish* pairing explicitly (the §1 box,
Definition 1's title, Proposition 1's asymmetry note, §3.4's opening). This is the one place our own
discipline was not applied to our own construction. It is now stated twice:

> **Passing the twin admits $g$ under this operational definition; it is not a proof that $g$ is
> *globally* invariant to S3** — a candidate can be blind to the swap the twin makes and sensitive to
> some other arrangement, which is why admissibility, like completeness, is relative to the declared
> family and to the published test.

and, where the test is *specified* rather than used, in Appendix AB beside the ladder: with the
rotation-twin column named as a case where the ordering of the very same baselines changes.

**We bill this as a Novelty move as much as a soundness one.** Your §14 lists *"operational
admissibility test"* among the six things that make the combination interesting; this is the
sentence that makes it legible as *operational*, which is exactly what a formalized principle does
not have.

## 3. Your §20.2, relative completeness, in a numbered main-text result

Definition 1's title already carried it. `cor:supremum` now closes with it, so it is in a **numbered
main-text result** rather than a definition's parenthetical:

> S3 completeness therefore follows from no single member of the family, **and is completeness
> relative to $\mathcal{F}_t$, never over all representations.**

## 4. Your §20.3 and §7: the narrative now ends on what survived

**The arc, not the billing.** §1's contribution (4) still reads *"billed as evidence the procedure
is usable, not as the thesis"*: your own §21 warns against broadening, and that restraint is what
makes *composition-of-known-transformations* survive scrutiny. What changed is the **conclusion's
order**: it now ends on the positive phenomenon rather than on a scoping clause.

It is funded, not added: two **third statements** were cut, the `66–100%` statistic (already in the
abstract and §1) and *"the same GIN weights clear the unseen-class criterion and sit at chance on the
twin"*, which was verbatim-equivalent to the abstract's version, plus *attained by the coarsest
member*, whose two other statements are §4.2's paragraph title and the abstract. Every claim and
every scoping clause survives: `non-monotone`, `K ≥ 200`, *polynomial setting*, *no claim of
architecture independence*.

**Your §7** asked what evidential role each experiment plays. §4's opener now names four:
AI Feynman a *motivating failure case*, the 23-corpus survey *prevalence*, `poly8` the *positive
validation*, the composition ladder a *demonstration*.

## 5. Your §10, the overclaim, and a worse one you did not see

You object to *"the finding confirms that what it learns is variable-identity dependent"*
(Appendix AI). Grepping `confirms` found **eight appendix instances and none in the body**. Six are
within-scope: a measurement confirming a stated hypothesis on the corpus it was run on. Two were
not, and the one you quoted is the **milder** of them:

- Appendix A concluded from **10 equations** that variable-identity leakage is *"a general mechanism
  affecting neuro-symbolic tasks."* **That is precisely the inference this paper exists to forbid.**
  It now says what 10 equations can establish (not an artefact of *our* benchmark design), says
  explicitly that they cannot establish a general mechanism, and points at the 23-corpus survey as
  the prevalence evidence, which finds S1 exposure **confined to one family**.
- Appendix AI now reads as you proposed: *the learned invariance does not transfer to the tested
  out-of-library forms under this protocol*: a statement about these forms and this protocol.

Both are appendix-only, so the fix cost zero body lines.

---

## 6. Four declines, each with the measurement

- **§15, terminology: `E3`, `E3b`, `E3m` do not appear in the body, 0, 0, 0 occurrences.** All
  three are appendix run tags. Of the body's named terms, `ceiling` occurs 18 times, `twin` 15,
  `skyline` 6, `gate C` 4: each load-bearing and glossary-defined in §3.3. We had planned to retire
  `$\mathcal{X}$` (2 body uses) and found on measuring that **the appendix depends on it 20 times**,
  so retiring it in the body would orphan the notation at 20 sites. The measurement *is* the answer:
  every body term is either used four or more times or introduces notation the appendix needs.
- **§9, the token-bag/random-encoder narrative in the main text: measured at one clause**
  (`related_work.tex`). Your conclusion (use both, neither is universally sufficient) is already
  the paper's; the material you are reacting to is appendix.
- **§8, restructure or split the appendix.** The developmental chronology **already** ships
  separately as `REVISION_HISTORY.md`. Re-lettering breaks the `\applabel` letters cited from the
  body, and round 21 measured that a second PDF orphans **21** `\ref`s. What we have added instead is
  one clause in the reading map marking **(i) as audit trail and (ii)–(iv) as scientific content**,
  so a reader who wants the science can skip **A–K** entirely.
- **§12 and the title** were declined in rounds 26 and 25 respectively, for reasons that have not
  changed.

## 7. Two defects that only a rendered page would have caught

- **A caption grew four lines and repacked five pages of floats.** Table 1's new caption pushed §3.3's
  levels table off page 4, which pushed §4.2's heading off page 7, which pushed a table off page 8,
  which pushed **the entire conclusion onto page 10**: a hard-limit violation, from a caption. Every
  automated gate except the page count was green. The caption was cut back to what only a caption can
  say; the two points it dropped are stated once each elsewhere, in §2's prose and in the table's own
  column headers.
- **Five prose columns do not fit at `\footnotesize`.** The rebuilt Table 2 threw a **97.1pt**
  overfull hbox: the largest in this paper's history. Fixed at `\scriptsize` with `\tabcolsep` at
  3pt and shorter cells, which also made the float **shorter** than the three-column version it
  replaced.

## 8. Gate state

0 LaTeX errors · 0 unresolved references or citations · 0 `Float too large` · exactly 2 overfull
boxes, both pre-existing (`6.4211pt` vbox, `3.509pt` hbox) · **79 pages, unchanged** · abstract ends
page 1, body ends page 9, page 10 opens with the Ethics Statement · pages 3–9 measure `0.00` free
lines · `bibtex` clean with the new entry, which resolves (no `[?]` anywhere in the PDF) ·
`verify_claims.py` exit `0` at **2090/2090 in all three copies, unchanged** · `check_tex_numbers.py`
clean on the rebuilt Table 2 (13/13 literals in a log) · Table 1 and Table 2 inspected as **rendered
images**, since `\checkmark` is new to this paper and a missing glyph drops silently from
`pdftotext` · the conclusion re-read as rendered output.

**Still deferred, and named as such for the second round running:** independent-domain evidence, a
real external benchmark in a non-symbolic domain. Novelty has now been the binding axis for three
rounds. If a scannable matrix, an operational membership test and a numbered relative-completeness
result do not move it, the argument is not the problem, and that experiment is the next thing we
run rather than a fifth reframing.
