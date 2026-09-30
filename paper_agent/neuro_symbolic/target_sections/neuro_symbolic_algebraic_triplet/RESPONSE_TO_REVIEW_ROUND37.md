# Response to the round-37 review

*Not part of the paper.*

**Summary: your three strategic changes are made, with zero new runs, and first, a disclosure you
are entitled to before reading any of it.** Your review cites
`iclr2027_conference(20260909-105431).pdf`. That file was built at **10:54:31**. Round 36's only
experiment, `r100`, **started at 11:02:48** and **finished at 14:31:22**. So the paper you read was
finished **8 minutes 17 seconds before that experiment began**, and **3 h 36 m 51 s before it
produced a result**. Weakness 2 and Questions 1–2 are answered in print in the current file, by
material that could not have been in yours. Details and the arithmetic are in §1 below. This is a
disclosure, not a rebuttal: everything after §1 is a change we made because you asked for it.

You wrote: *"I would not add more appendices. I would not add another 20 ablations. I would make
three strategic changes."* We made exactly those three and nothing else.

Assertion count **held at 2304**, no new run, no new log, no new tag, no new appendix. Both new
objects are **format conversions of prose that was already on the page they now occupy**, so the body
is still **9 pages** and per-page `yMax` is byte-identical to the pre-round baseline on all ten pages.

| Axis | R36 | **R37** |
|---|---|---|
| Novel problem framing | 7 | 8 |
| Core methodological idea | — | 8 |
| **Theoretical novelty** | 6 | **4.5** |
| Experimental rigor | 8 | 9 |
| **Empirical breadth** | — | **6** |
| Reproducibility | 9 | 9 |
| Clarity | 7 | 7 |
| **Significance** | 8 | **6.5** |
| Overall ICLR fit | 6.5–7 | 7 (recommendation **5/10**) |

---

## 1. The reviewed file, with timestamps

| Object | Time | Source |
|---|---|---|
| The PDF your review cites | **2026-09-09 10:54:31** | its own filename stamp, `20260909-105431` |
| `r100` starts | **2026-09-09 11:02:48** | `provenance.timestamp` in `logs/r100_learned_invariant.json`; that field is `t0`, the run's **start** (`run_r100_learned_invariant.py:814,822,922`) |
| `r100` runs for | **12 513.3 s** = 3 h 28 m 33 s | `elapsed_sec`, same log |
| `r100` finishes | **2026-09-09 14:31:22** | `t0 + elapsed_sec`; the log's mtime agrees to the second |

What that means concretely. The reviewed file contains round 36's *prose* referring to `(tag r100)`
prospectively, and **none** of its evidence: no readout-free bound over all trained readouts, no
Appendix BA, no Table 2 row *under every trained readout*, no Table 1 row `learned invariant control`,
no split of the `boolean8` untrained-encoder anomaly into a readout artifact and a proved family
property, and no four-way answer in §6. Consequently:

- **Weakness 2** (*"the analysis of what F_3 can and cannot represent could be sharper"*): the
  current file bounds the supremum over **every** trained readout at once, with nothing trained, via
  the collision partition: 12 of the 13 admissible maps induce the *same* partition, the 13th coarser,
  so **one bound covers the family at any capacity** (§4.2, tag `r100`, Appendix BA).
- **Question 2** (*"how sensitive are conclusions to independently designed control families?"*):
  answered twice: `r92`/`r98` widen the family by **five descriptors we did not choose**, moving the
  ceiling at 5 of 8 cells by at most `+0.038`, and **every cell the union passes is passed by all 8191
  of its sub-families** (65 527 of 65 528 family-cell pairs, by exact enumeration); and `r100` removes
  the readout degree of freedom entirely.
- **Question 1** is now answered in the body rather than in a subordinate clause; see §4 below.

We are **not** asking you to re-score on that basis. We flag it only so the next read is not
evaluating a file that predates its own cited experiment.

---

## 2. Change 1: the contribution is a general evaluation principle; symbolic work is the case study

Your framing: *"make the general evaluation principle the contribution, with symbolic work as one
case study."* Three edits, no new prose block:

1. **The abstract now names the principle** (¶2, appended to the sentence that already said *"The
   levels name **cues**, not algebra, so symbolic-expression encoders are this paper's **case study**,
   not its scope"*): *"and since a family is declared against **one** axis of novelty at a time,
   **'out-of-distribution' is not a scalar**: we separate and cost **five** axes, free to fatal, ranked
   differently on different corpora."*
2. **§1's definitional sentence was narrower than the paper's own title, and is now not.** It read
   *"We turn that into a falsification framework **for claims about symbolic-expression encoders**"*:
   in a paper titled *Admissibility Auditing for **Representation-Level Claims***. It now reads *"a
   falsification framework **for representation-level claims**"*. This was found by the cold
   reconstruction gate, not by a reviewer, and it is 13 rendered characters **shorter**, which paid for
   the two additions below.
3. **Contribution (4)** already carried *"symbolic-expression encoders are this paper's detailed case
   study, SCAN and Python code two ports where the same code instantiates the same ladder, billed as
   portability and not as the thesis"*. Unchanged: a fourth restatement is load, not salience.

**We did not restate the principle a fifth time.** Round 30 established here that the sentence a
reviewer asks for can already be in the exact position asked for, three times over, and still be
missed: **redundancy is not salience; position and form are.** So this round spent its effort on
*form*, which is §3.

## 3. Changes 2 and 3, and the discovery that they are the same statement

Your change 3: *"OOD is multidimensional … A benchmark split should specify what is novel: primitive,
composition, arrangement, schema, or inventory."*

**Every one of those five axes was already in this paper as a measured number.** The words `axes`,
`multidimensional` and `not a scalar` measured **zero** occurrences in the body. Nothing was named as
a principle, and the numbers were spread across a figure panel and two prose paragraphs. So change 3
needed no experiment; it needed one object. `§4.4` now carries it, as a five-row tabular under the
heading *Novelty is not a scalar, so a split must declare which axis it varies*:

| What the split makes novel | Measured cost | Verdict |
|---|---|---|
| **arrangement** of known primitives | `+0.012`, CI covers 0 | free |
| **composition depth**, never composed | `+0.200` `[0.163, 0.237]` | graceful decay |
| **schema**, vs. a wrong-schema control | `+0.070` `[0.021, 0.115]` | at the *family*, not the rewrite |
| **inventory**: library membership | `.965/.880 → .832/.662` | plain / renamed; held-out tree *byte-identical*: largest move |
| **primitive**, held out of the library | `+0.429`–`+0.845` | not established |

**And our version is stronger than the one you asked for.** You asked for a split to declare its axis.
The paper can say more, because the second-order finding you asked us to feature (*"the coverage
mechanism breaks"*) is exactly what breaks the *ranking*: `boolean8`'s coverage ladder is **not**
monotone, so **the coverage-closure mechanism is polynomial-specific**. The tabular closes with it:
*"And the ranking is corpus-specific … So a split reporting one OOD number reports nothing: name the
axis, and declare the family against **it**."*

Your change 2 asked for *"conventional baseline says X / admissibility audit says Y"* outside symbolic
mathematics. **That artifact already existed in this paper across three modalities, as prose, and as
an appendix ledger cited from §1 (Table 10).** §4.3 is now that contrast, in the body, in your form:

| Modality | Conventional report | What the audit licenses |
|---|---|---|
| symbolic math | a released 80M integration encoder scores `0.872` on its own test distribution | a *zero-parameter* operator/arity bag scores **`0.941`**: an S2 task correctly identified, and evidence of nothing above it |
| natural language | a Tree-LSTM reaches **`0.987`** on SCAN `add_prim_jump`, where **the grammar and the held-out set are theirs** | it **passes**, against `sup F_3 = 0.0005`, *and their design puts the admissible bar on the floor*, so we quote no ratio: what clears it is composition of *one known* transformation onto *one* unseen primitive, still not compositional reasoning |
| code | S2 reaches `0.987` over `300` Type-2 clone classes *we* built from Python stdlib code | **Program representations: settled below S3**, *every* `F_3` member attains `0.990`, exactly the maximum this corpus admits |

Two things to say about that table honestly.

- **Your reading of the code result is a reading of a reversal.** You wrote that *"the framework bottoms
  out"* there. What the row reports is that a conventional write-up would call S2 at `0.987` strong
  structural retrieval, while every `F_3` member reaches `0.990`: **the corpus maximum**, so the claim
  is settled *below* S3. That is the sharpest X-vs-Y pair in the paper, and it was buried in prose.
  It is not the framework failing; it is the framework returning a verdict against the flattering
  reading of our own corpus.
- **Only the first row is somebody else's *result*.** Rows 2 and 3 are ours, on someone else's split
  and on a corpus we built, and each cell says so in its own words (*"the grammar and the held-out set
  are theirs"*, *"classes **we** built"*). The closing sentence of §4.3 names the sharpest case
  explicitly: *"The sharpest test of the whole procedure is one somebody else built."*

**This is also the quantified answer to Question 3** (*"how often do real claims pass or fail?"*):
**eight already-published results audited, four of them systems and leaderboards built by other
people, across three modalities**, one upheld, two rescoped to the level they actually test, one
withdrawn, one passing with the admissible bar on the floor. §1 now points at **§4.3** as well as at
appendix Table 10, so the ledger is no longer appendix-only. That pointer was missing until the cold
gate caught it.

## 4. Theoretical novelty 4.5: the concession was being read as the verdict

`methodology.tex` says, immediately after Corollary 1: *"These numbered results are billed as
**scoping**, not as theoretical contributions … A reader who finds the theorem close to a restatement
of what an admissible family means is not disagreeing with us."*

Round 35's review **rewarded** that sentence. Round 36's **quoted it back** as a reason not to give an
8. Round 37 scores the axis **4.5**. That is the second time a decline-in-print has been quoted back
here as a reason to withhold points, and it is the axis's lowest score in 37 rounds.

**We did not delete the concession**: two reviewers credited it, it is gated `== 1` by
`check_protected_claims.py`, and removing it would be arguing rather than answering. We **extended the
same sentence** so the reader cannot stop at the concession:

> *"…they fall out of the definition below in a few lines — **but what follows *from* them is not
> definitional**: the statistic ranges over *trained* readouts, so every ceiling in this paper had to
> be re-measured (Cor. 2)."*

That consequence is not a positioning claim: it is why round 36 existed. And **we added no numbered
environment.** Rounds 30, 34 and 35 all told us to de-sell Theorem 1; re-selling it now to answer a
novelty score would contradict three consecutive reviews.

**Weakness 6 / Question 1** (*why does `F_3` approximate the relevant invariant class, and why depth
`{1,2,4,8}` and WL `{1,2,3}`?*) was answered inside a subordinate clause of a `Definition` environment,
which is why it did not register. It is now the **bolded terminal sentence** of Definition 1:

> **The depth ladder is not a hyperparameter: it *terminates*** — `poly8`'s deepest tree is 4, so
> `φ_{d≥4}` *is* the complete order-blind fingerprint and no finer member exists (§4.2).

That is a **proof**, not a choice: past depth 4 there is no finer member to add on this corpus. The WL
radii are declared **conventional 1–3 rather than derived**, in the same sentence, because that is the
honest description of them.

*One thing we did not do, and why.* We wanted this sentence **outside** the definition environment, as
a standalone paragraph; that is what our own plan called for. A new paragraph costs roughly one line
slot; page 6's slack is **0.07 pt** and the 9-page body limit is hard, so the sentence stays as the
definition's last, bolded, standalone sentence. Salience without the page cost; we would rather say so
than have it read as an oversight.

## 5. Table 2 now shows the five axes

Table 2 (*every claim, its evidence and its verdict, on one page*) had the row
`arrangement / depth / primitive | C | — | — | yes / partial / open`. Its evidence cell now reads
**`3` of *five* axes (§4.4)**: the row that used to imply three axes exist now says how many there
are and where the other two are costed.

## 6. What we declined, and why

- **A new domain, run from scratch.** Your own path was explicit that this is not what you wanted
  (*"I would not add another 20 ablations"*), and every axis and every modality you asked about is
  already measured here. The round's cost was zero GPU-hours by design.
- **Deleting the forensic self-audit / revision history.** This is a **2–2 tie** across rounds and we
  are declining it by disclosure rather than arbitration. Round 34 §17 asked us to **keep** it; round
  35 §21 asked us to **keep** it; round 36 and now round 37 want it **gone**. Standing policy here is
  measurement plus disclosure, never picking the most recent reviewer. Body cost is three clauses, each
  gated `== 1`; the full chronology ships as `REVISION_HISTORY.md`, outside the paper; the page-10
  statements are outside the 9-page limit.
- **Removing or softening the AI-use disclosure.** You called it *"directionally appropriate"* and said
  retaining a precise one is important. It stays exactly as precise as it is.
- **Re-selling Theorem 1.** See §4.

## 7. What the prose→table conversion cost, stated

A table cell is shorter than the sentence it replaces, so a conversion loses content. We diffed both
new tabulars **cell by cell** against the page-9 prose of the reviewed build (round 27 silently changed
four cells' meaning in a table rewrite here). The diff caught two real losses and both were repaired:

- The inventory row had lost its **`(plain, renamed)`** labelling, so `.965/.880 → .832/.662` was four
  bare numbers. The label is now in the verdict column.
- The code row had lost the **ours-vs-theirs** disclosure. It now says *"`300` Type-2 clone classes
  **we** built from Python stdlib code"* in the conventional-report cell itself.

**Deliberately dropped, all of them still in the appendices and all still asserted by
`verify_claims.py`:** SCAN's `3595` test classes and its `0` surface / `0` class overlap; *"3 seeds,
worst lower bound `0.976`"*; the SCAN ceiling's CI `[.0001, .0010]`; the `1003` stdlib functions the
clone corpus is drawn from; the identifier bag at `0.770` against chance `0.0033`; *"five libraries ×
four schemas"*; and the SCAN twin **positive control** (every order-blind member pinned at exactly
`0.500` on their own twins, the ordered completion rejected).

**One duplication we accepted:** §4.3's symbolic-math row restates §4.1's *"Two encoders we did not
build"* paragraph four pages earlier. The X-vs-Y format needs the row, and a reader who arrives at
§4.3 has not necessarily retained page 7.

## 8. Gate state

`err 0` · `undef 0` · `0 Float too large` · **exactly 2** overfull boxes (`6.4211pt` vbox, `3.509pt`
hbox, both pre-existing) · **90 pages**, abstract ends p1, **body ends p9**, p10's first *body* line is
`E THICS S TATEMENT`.

**Net-zero proved by placement, not arithmetic.** All thirteen body headings on their round-36 pages
and all four body floats on theirs (Fig 1 p3 · Table 1 p4 · Table 2 p5 · Fig 2 p8); per-page `yMax`
identical to the pre-round baseline on **all ten** pages (`p1–4,7,8,10 = 732.01` · `p5 = 731.79` ·
`p6 = 731.94` · `p9 = 731.94`).

`check_reviewer_map.py` **PASS**: 16 rows, 272 checks, 43 tags, 53 letters. This was the round's
largest risk: **five of the sixteen map rows quote, verbatim, the exact prose these two tabulars
converted**, and a map row's claim cell must be a markup-normalised body quote living inside the
section its `\ref` names. All five survive verbatim in the right sections.

`check_protected_claims.py` **PASS**: 19 claims, 4 body absences, 3 document-wide absences over 15
files, all controls firing. Two of the at-risk literals (`portability, not general validation`,
`billed as scoping`) are gated `== 1` and sat inside the converted prose; both survive.

`check_tex_numbers.py` traces **8 of 8** literals in the §4.3 tabular and **14 of 14** in the §4.4
tabular to asserted log values. *A caveat worth recording:* our first two invocations reported **zero**
literals and passed; the tool's block runs from its marker only to the next blank line, so a prose
marker placed above a tabular scans nothing. We re-ran with markers **inside** each tabular, and then
ran a **positive control** (perturbing `.832` to `.831` in a scratch copy), which fired with
`NOT in any log: 0.831`, exit 1.

`verify_claims.py` **2304/2304, exit 0, in all three copies** (`artifact/audit-sym`,
`artifact/iclr-supplementary`, the workplace copy). The shipping copy was purged of every
`__pycache__`/`.pyc` **after** its verifier run and grepped clean of the absolute home path and the
author name.

**Pages 1, 2, 4, 5, 6, 8 and 9 were read as rendered images**, and the cold reconstruction gate was run
over the extracted abstract, §1, both tabulars, §3's saturation statement and the conclusion. That gate
produced three of this round's edits, none of which any automated check could see:

1. §4.4's heading read *"and What the **OOD Axis** Names"* (singular) sitting directly above the
   tabular whose entire point is that there are five. Now *"and What OOD Names"*.
2. §1's framework sentence was scoped narrower than the paper's title (§2 above).
3. §1's eight-results ledger cited only the appendix table; it now cites **§4.3** first.
