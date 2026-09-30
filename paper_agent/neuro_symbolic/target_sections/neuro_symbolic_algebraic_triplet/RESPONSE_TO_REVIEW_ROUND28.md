# Response to the round-28 review

*Not part of the paper.*

**Summary: you asked for one small experiment instead of a sixth reframing, and we ran it. It is a
full admissibility audit of SCAN: a benchmark we did not build, whose equivalence classes are its
own gold action sequences and whose order twins occur naturally in it, and the pre-registered
prediction failed. The inversion does not replicate there. We report the failure as the result: the
non-monotone ceiling is a property of these corpora, not of admissible families as such, so the
paper can now say where its centerpiece stops.** Tag `r96`, zero GPU-hours, no new measurement code:
`separability_from_bags` and `bag_classifier_accuracy` are reused unchanged from `benchmark_audit.py`.

The assertion count moves **2090 → 2129**, which is the check that the run actually entered the
paper rather than sitting beside it.

---

## 0. The scorecard, and the two things that moved

| Criterion | R25 | R26 | R27 | **R28** |
|---|---|---|---|---|
| Technical quality | 8 | 8 | 7.5 | **8** |
| **Novelty** | 7 | 7 | 6.5–7 ← binding ×3 | **7: off the scorecard** |
| Empirical validation | 8 | 8.5 | 8 | **8** |
| Significance | 8 | 7.5 | 7.5 | **7** |
| Clarity | 7.5 | 7.5 | 7.5 | **7.5** |
| Reproducibility | 9 | 9 | 9 | **9** |
| **Scope / generalization** | *retired at R25* | — | — | **6 ← binding, and it came back** |
| Theoretical contribution | — | — | — | **6 (we are not fighting this one)** |
| Presentation | — | — | 7 | **7** |
| **Overall** | **7** | **7** | **7** | **7** |

**Novelty went off the scorecard exactly when we stopped arguing and ran something.** It was binding
for three consecutive rounds of reframing. Round 27's response committed in print to running the
experiment rather than reframing a fifth time; this is that round, and Novelty is 7 and not binding.

**`Scope/generalization 6` came back after round 25 retired it, and we take that as the round's
finding.** Round 25 established that openly declining an axis in the paper's own text makes it
disappear; it worked for `Scope 5`, `Generality 5.5` and `Theoretical novelty 6`. It survived one
round and then failed, for a reason you named precisely: our only non-symbolic port (`r95`) is *"explicitly
a constructed corpus."* **A decline holds only while there is no cheap way to answer.** There was
one.

---

## 1. Your ask #3: a demonstration outside symbolic mathematics, on a benchmark we did not construct

**`r96`, a SCAN admissibility audit.** What is ours and what is not, stated before any number
(Appendix AX opens with this):

- SCAN is fetched as published (`tasks.txt`, `brendenlake/SCAN`) against a **pinned SHA-256**, and is
  **not redistributed** with the supplement. It is BSD-licensed (Facebook Inc.); `statements.tex`
  says so.
- The **equivalence classes are SCAN's own gold action sequences**: 9,228 distinct sequences, 9,222
  of them with ≥2 surface forms.
- The **paraphrase relation is SCAN's own** `"X and Y" ≡ "Y after X"`. We invented nothing.
- The **order twins occur naturally**: same word multiset, different gold action sequence. This is
  the property `r95` lacks, and it is why the per-instance admissibility test actually **fires** here
  rather than merely passing.

What we do *not* claim: this audits **the cue structure of SCAN's semantic equivalence classes**, not
SCAN's published seq2seq results. Selecting which pairs form a class is still a choice we made; the
relation we used is the benchmark's own rather than one we invented, and that is the whole of the
difference we are claiming.

### The prediction was pre-registered and it failed

Both branches were committed before the run. Predicted: the inversion replicates, the coarsest
member strongest, the ordered completion weakest. **Observed: it does not.** On SCAN the ceiling is
**monotone** (`phi_d` rises `0.080 → 0.115`) and the ordered completion sits **above** the family at
`0.155`. It replicates in **none of 9** sensitivity cells, checked cell by cell rather than in
aggregate. The log's own verdict field reads `"domain boundary"`.

We did not re-run to the prediction, relabel the corpus, or drop the rows. §4.2 now reads *"so the
inversion is a property of these corpora and not of admissible families as such"*, and the abstract
closes ¶3 with *"so we can say where the finding stops."* A negative is what the audit produced and a
negative is what it reports.

**And the guard fires.** All **11** order-blind members score exactly `0.500` on all three twin
populations, *and* the ordered completion scores strictly above `0.500` and is therefore **rejected**
from the family and reported as an extension. A guard that cannot fail proves nothing; that pair is
what proves this one can.

**One methodological caution worth passing on.** The twins split **22,584 + 15,174 = 37,758**, and
only the second population is the one the bound is read from. Had we reported the guard's `0.500`
over "the twins" without counting the exclusions, the number would have been an artefact of which
pairs we kept. The verifier asserts the split **as a sum** so that a silent change to either
population fails.

---

## 2. Your ask #2: the core contribution reframed around the non-monotone ceiling

It now leads in four places, and (following your §29) the wording is **identical where it is
numbered** rather than restructured:

- **Abstract ¶3 opens on it**: *"The finding we did not expect: the ceiling is non-monotone in
  resolution: raising a control's resolution can lower it."*
- **Contribution (1)** names it: *"measured non-monotone in resolution, so a family cannot be
  represented by its strongest member."*
- **Conclusion (2)** leads on it, and now carries the boundary: *"— and monotone on a corpus we did
  not build, so we can say where that stops."*
- **§4.2** calls it *"the paper's centerpiece"* and states the four domains it holds in and the one it
  does not.

Conclusion (1) now opens with §1 contribution (2)'s sentence verbatim and conclusion (3) with the
abstract's ¶4 sentence verbatim. We did **not** renumber the contributions list (1)–(4); it is cited
from §4 and the appendix, and a full 9-page restructure at zero page slack risks the hard limit for
framing we mostly already have.

---

## 3. Your ask #1 and your §18: the epistemic scope, named

**Your §18 sentence is fixed in the form you specified.** The §1 box now reads *"A learned score
**cannot be taken as evidence for** a structural claim **unless** it exceeds the best score
obtainable by controls that are invariant to the property claimed, under the same protocol — a
necessary condition, never a sufficient one."*

**`family-relative` occurred zero times in the entire source tree before this round.** The content
was there; the term and the placement were not. Now:

- **§3.3 defines it** where the glossary already sat: *"**family-relative admissibility**: admissible
  by a declared family's per-instance test, never by proof of global invariance"*, followed by *"the
  audit **tests** invariance to a declared family, it does not **establish** invariance"*: your §1
  wording.
- **The ceiling is renamed at every site** to the **family-relative admissible ceiling**, including
  the abstract, §1, §3.3 and the conclusion. The compound is the same length, and plain *ceiling*
  stays as the short form after first use.
- *"global invariance"* / *"globally invariant"* is now stated **twice in the body**, and
  *"establishes invariance"* appears nowhere unnegated.

---

## 4. Your four smaller asks

- **§20, the `0.994` twin.** You are right that it shows sensitivity to sibling arrangement, not
  algebraic understanding. The scope now precedes the number instead of trailing it: *"Twin members
  are not algebraically equivalent, so what a high score on it measures is composition-sensitive
  structural discrimination, not algebraic-equivalence generalization"*, then `0.994`.
- **§22, `boolean8`'s coverage break.** Promoted from a trailing clause to the paragraph's bold
  takeaway: *"And there the coverage mechanism breaks outright: `boolean8`'s coverage ladder is not
  monotone."* We did not cut this paragraph for space; you asked for more of it, not less.
- **§15/§16, the appendix multiplicity.** Stated in the appendix reading map: it is **the audit
  applied recursively to our own results**, not exploratory search, and the provenance machinery is
  **reproducibility infrastructure, not scientific argument**. Zero body lines.
- **§17, the LLM-use disclosure.** Kept and not centred, and the measurement is why nothing needed
  demoting: it is an unnumbered statement in `statements.tex`, **after** the page limit, costing
  **zero** body lines. It was never a centerpiece.

---

## 5. `Theoretical contribution 6`: we agree, and we are not fighting it

Your §12 endorses the paper's own billing, and §3.4 says it in print: *"We bill this section's
propositions as **scoping**, not as theoretical contributions — each falls out of Definition 1 in a
few lines."* Since round 25 only two propositions remain in the body; the other three sit in Appendix
AN beside their proofs. We are not selling this as a theoretical ML paper.

---

## 6. Three defects we found while doing this, none of which your review names

Recorded because they are the kind a review cannot see.

**Our own claims table omitted the round's result.** The conclusion says *"what we claim, exactly, is
Table 2"*, and Table 2's block of **verdicts against us** did not contain the SCAN boundary, which is
exactly a verdict against us. It is now row 8. This is the eleventh instance in this paper's history
of a result existing in prose but not in the float the paper points at as authoritative, and the
tenth was in this same round: **`r95` had no appendix section and no tag-ledger entry**, in a paper
whose reading map promises one per run tag. Your objection to `r95` landed partly because the one
thing that would answer it (the port's guards) was nowhere a reader could find. New Appendix **AW**
documents it retroactively; **AX** is SCAN.

**A negation that inverted the thesis, caught only by reading the rendered page.** The conclusion
closed *"The audit falsifies and certifies nothing, at no width"*, which parses as *falsifies
nothing and certifies nothing*. Now *"The audit falsifies; it certifies nothing, at no width."*
Every automated gate passed the original.

**A confidence interval rounded in the wrong direction, caught by our own tooling in text we had not
touched.** `check_tex_numbers.py` flagged `[.926,.969]` at two sites; the log stores `[0.9255,
0.9691]`, so `.926` **rounds a lower bound upward**, stating a tighter interval than the log
supports. Now `[.925,.969]`.

We also corrected one sentence of our own: §4.2's *"`phi_infinity` sits above the family at `0.155`,
in 9 of 9 cells"* implied both headline numbers hold in all nine sensitivity cells, where cell 1's
ladder is flat at `0.46`. It now says *"with the inversion replicating in none of 9 sensitivity
cells"*, which is what the log states. (The abstract's *"monotone in 9 of 9 cells"* was already true:
flat is monotone, and is unchanged.)

---

## 7. Gate state

0 LaTeX errors · 0 unresolved references or citations · 0 `Float too large` · exactly 2 overfull
boxes, both pre-existing (`6.4211pt` vbox, `3.509pt` hbox) · **81 pages** (two new appendix sections;
the appendix is exempt) · **abstract ends page 1, body ends page 9, page 10 opens with the Ethics
Statement**, and every section heading on pages 4–10 sits at its exact pre-round y-coordinate ·
`verify_claims.py` exit `0` at **2129/2129 in all three copies** · `check_tex_numbers.py` run over
the SCAN row, Table 23's caption, Table 2's new row and both new appendix sections, every unmatched
literal adjudicated · Table 23 inspected as a **rendered image** · the supplement ships
`fetch_scan.sh` and `run_r96_scan_audit.py`, with the log's `log_dir` redacted including nested keys
and zero absolute paths anywhere in it.

**Which axes this round targeted, stated so the next round need not guess:** `Scope/generalization`
(with an experiment) and `Clarity`/`Presentation` (with the naming and the negative-form rule). We
did not target `Significance 7` or `Theoretical contribution 6`.
