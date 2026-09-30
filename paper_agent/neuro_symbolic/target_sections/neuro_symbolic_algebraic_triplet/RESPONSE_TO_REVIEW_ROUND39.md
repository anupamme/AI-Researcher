# Response to the round-39 review

**This review is current.** It cites `iclr2027_conference(20260910-013005).pdf`, which sits after the
previous revision's final build, and the content confirms it: §14's terminology list contains the
renamed *coverage axis*, §7 quotes the relocated scoping sentence, and §3 already frames tree-edit
distance as outside the admissible family. So there is no hand-off table this round and nothing below
argues from staleness. Every ask you made is about text that exists, which makes each one either a real
gap or a real disagreement. We treat them as real gaps.

You wrote: *"The most valuable revision now would be not another large experiment, but a surgical
rewrite of the abstract + first 2 pages + contribution statement + 'why not invariant baseline?'
argument."* That is exactly and only what this revision is. **Zero new experiments, zero new runs, zero
new floats, no net body lines; the body still ends on page 9 and the paper is still 90 pages.**

---

## 1. Priority 1: the paper's strongest result is now in the paper's pitch

Your §3 calls the shape-matched twin *"the paper's strongest empirical idea… probably the experiment I
would emphasize most heavily in an oral presentation."* We measured where it actually appeared and the
answer was damning: **nowhere in the first two pages.** The twin surfaced on page 3 inside Figure 1 and
again on page 7 in §4.2, and `0.994` appeared in those two places and nowhere else. Your §18 asked for an
eight-beat page-1–2 sequence with *"strong test: shape-matched twin"* as beat 6 and *"result: Tree-LSTM
99.4%"* as beat 7. Both beats were missing from the pitch.

They are now on page 1 and page 2:

- **Abstract ¶3 now leads with the twin** instead of reaching it as a protocol-disagreement aside:
  *"**The strongest test holds every lower-level cue fixed.** Against a **shape-matched twin** — same
  tokens, same operators, different *arrangement* — **every admissible order-blind control is pinned at
  exactly 0.500 by proof**, and a Tree-LSTM reaches **0.994**."* The GIN protocol disagreement now follows
  as a *consequence* of that test rather than being its only mention.
- **§1 has a new fourth paragraph, page 2 slots 071–078**, *"The sharpest form of the test, and the result
  we would put first"*: the twin construction, every order-blind member pinned at `0.500` **by
  construction (a *trained* readout over one included at any capacity**, Tree-LSTM `0.994`, and tree-edit
  distance) the strongest order-*sensitive* **non**-member, at `0.723`, so no *admissible* comparator
  narrows the margin. It closes on your beat 8: evidence against the alternatives the declared family
  names, never certification.

**§14, the criterion sentence near the beginning.** Your wording is now the last sentence of §1 ¶1:
*"The criterion, in one sentence: a learned representation is evidence for a property P only if it
outperforms the **best** representation that is invariant to P, evaluated under the same protocol."*
Per Priority 1's *"then immediately introduce the ceiling"*, the ceiling paragraph moved up from third
position to second, so page 2 now reads: criterion → ceiling → the three-level example → the twin.

**§17, the abstract's latter half.** Cut, not rearranged. ¶1 is untouched; it is the part you called
*"excellent"*. ¶2–¶4 lost roughly five rendered lines of connective machinery and one restatement, and
every self-limiting clause survives: the `K≥200` scoping, the polynomial limit on the coverage mechanism,
*"out-of-distribution is not a scalar"* (your §8's second-most-publishable idea), and the SCAN/code
negative: *"where **our own** inversion does **not** replicate"*. **We deleted no negative result to
buy space.** Measured: 39 rendered lines before, 34 after. The three things you wanted a reader to leave
with are now the openers of ¶2, ¶3 and ¶4: *strong baselines are not necessarily admissible controls* ·
*we define and measure a ceiling* · *what survives is narrower than compositional generalization*.

## 2. Priority 2: "why not just use a single invariant baseline?", answered with numbers

Your §19 called this *"probably the most obvious reviewer objection"* and the measured chain *"probably
the most important missing rhetorical piece."* You were right that the paper only argued it
qualitatively: Proposition 1, Corollary 2 and Table 1's `family ceiling?` column all made the point
without ever printing `M(g₁) < M(g₂) < sup M(g)` as numbers.

**§3.3 is retitled *"Why a Single Invariant Baseline Is Not Enough"*** (page 6) and now opens with the
chain, at `poly8 K=500`, the cell §4.2 and Figure 1 both print:

| what a reader is handed as *the* invariant baseline | score | apparent margin under `0.894` |
|---|---|---|
| the Laplacian spectrum, the most sophisticated member | `0.020` | `+0.874` |
| `F₃`'s best *single* member, one fixed readout | `0.276` | `+0.618` |
| that same member with the readout **fitted** | `0.284` | |
| the bound over **every** readout, nothing trained | `0.296` | `+0.598` |
| the **full-token bag**: order-blind too, but reading the variable identity every `φ_d` anonymises away | `0.517` | `+0.377` |

So the apparent margin swings by more than a factor of two according to which single control is chosen,
which is why the statistic has to be a family's supremum and why Definition 1 requires clearing **every**
level's ceiling rather than the highest-numbered one. **Every number was already in the appendix; nothing
was run for this paragraph.**

**Then, in the direction that costs us.** Fitting the readout raised the ceiling at *every* cell we
measured, by up to `+0.107`, and closing the family over readouts leaves **one of our own passes unproved
by `0.0027`** (`boolean8` at `K=50`, `0.8706` against a bound of `0.8733`), where that cell's strongest
single member, `0.732`, would have shown a comfortable `+0.139`. The principle "use an invariant
baseline" cannot bound a comparator nobody ran; a family closed under post-composition can.

**§6, in the same breath.** The paragraph now ends: *"**And the family is incomplete by construction**:
the audit falsifies **within** `F₃`, never outside it — the standing limitation of the method."*

## 3. A correctness defect we found while measuring, and it was in the entry-point figure

Figure 1 labelled a bar `sup F₃` and printed **`0.277`**. That value is the **tree-local bag**, the row
*below* the ceiling in the appendix table: a descriptor Definition 1 does not enumerate, so it cannot
set the ceiling the figure labels. The declared family's supremum at that cell is **`0.276`**, and the
appendix states the correction twice. The figure printed the pre-correction number under the corrected
label, on precisely the declared-family axis your §20 is about. **Fixed.**

Worth recording *why* it survived a round: the previous round's check decoded each bar's TikZ fraction
and compared it to the number printed beside it. Both read `0.277`: internally consistent and wrong. **A
consistency check is not a provenance check.** The new gate `check_figure_provenance.py` asserts each of
Figure 1's ten printed values against *its appendix source row*, not against its own bar, and fires a
positive control that must fail.

The same measurement found a second understatement, which is why `0.517` appears in the table in §2
above. §4.2 has always reported the honest denominator: *"0.894 against the strongest non-learned
baseline (full-token bag) at 0.517 — 1.7×, not the flattering 6.1×"*. A §3.3 chain that stopped at
`0.296` would have quoted `+0.874` as the spread's top while a stronger admissible control sat at
`+0.377` in the figure on the facing page: the exact error the section condemns.

## 4. The smaller explicit asks

| Your ask | What changed |
|---|---|
| **§20** *"'complete' alone can sound stronger than what you mean"* | Definition 1 is renamed **"admissibility-complete relative to `F` through level S`T`, and coverage-gated"**: the relativity is in the name now, not in a subtitle, and the subtitle is deleted. Three appendix sites renamed with it. |
| **§7** do not oversell Theorem 1 | Retitled in your own words: **"A simple formal justification for why admissibility ceilings are the appropriate statistic"**, and clause (i)'s two-regime construction moved to the proofs appendix. De-emphasis, not retraction: the *billed as scoping* clause and the non-definitional consequence stay in the body. |
| **§12** partition-dependence belongs in the main results | Table 2's `poly8` row verdict cell now reads **"sensitive; pass only K≥200"**. Zero new rows, zero body lines. |
| **§13** the 90-page appendix | The appendix now opens with **the fifteen-minute path: four objects**, Figure 1, Table 2, §4.2's twin, §3.3: *"then the readout-closure and family-stress appendices if you want the ceiling checked. Nothing else is on the critical path."* Free: it is outside the page limit. We added nothing to the body about length. |
| **§5** keep composition-vs-reasoning prominent | Untouched in the abstract, §1, Table 2's last row and the conclusion. |

**On §13 and the appendix's length, plainly:** we did not cut A–K. Those seventeen pages are cited from
Table 2's caption, from the reviewer-map gate and from §3.1; every later letter would need re-lettering
across ~45 subsection titles. Your own scorecard puts reproducibility at 9/10, and that is the one score
we are not willing to risk to save appendix pages. The reading path is our answer instead.

## 5. Priority 3: the mapping, item by item

Your nine-item list *is* what the body contains, in that order: counterexample §1 · definition §3.2 ·
theorem §3.2 · twin §4.2 · core symbolic results §4.2 · composition §4.2 · SCAN §4.3 · limitations
§3.2/§5 · conclusion §5. Only two body sections fall outside the list, and we are keeping both, for
reasons that come from earlier rounds of this review:

- **§4.1's 23-corpus survey** is what makes AI Feynman *"the severe case, not the typical one"*. Without
  it the paper's central counterexample reads as a claim about prevalence, which it is not. An earlier
  round asked for exactly this self-limitation.
- **§4.4**, which you call the second most publishable idea in the paper.

## 6. What we did not do

- **No new experiments.** Fourth consecutive round in which you asked for none.
- **No new defence anywhere.** Your §11 note that the paper is *"still too defensive"* has been standing
  since round 36, and every de-escalation so far has been a deletion. This round removed one redundant
  caption sentence and two restatements; it added no rebuttal.
- **We did not paraphrase the concession.** *"The audit falsifies; it certifies nothing"* still closes the
  conclusion.

## 7. Verification for this revision

- Build: `pdflatex → bibtex → pdflatex ×2`. 0 errors, 0 undefined references or citations, 0 bibtex
  warnings, 0 "float too large", **exactly the two pre-existing overfull boxes** (`6.4211pt` vbox,
  `3.509pt` hbox), **90 pages**, abstract ends p1, **body ends p9**.
- Placement unchanged: Figure 1 p3, Table 1 p4, Table 2 p5, Figure 2 p8, §4 p7, §5 p9.
- `check_protected_claims.py`: **PASS**, 19 protected claims survive, 4 absences hold over 6+5 files, 3
  hold over all 15. The three literals that live only in the abstract survived its rewrite.
- `check_reviewer_map.py`: **PASS**, 16 rows, 272 checks, 43 log tags, 53 appendix letters.
- `check_figure_provenance.py`: **PASS** on 10 values, positive control fires with 2 failures.
- `check_tex_numbers.py` over Table 2: the edited cell's numbers (`0.894`, `200`) both resolve to logs.
- `verify_claims.py`: **exit 0, 2304/2304 assertions**, in all three code copies.
- Pages 1, 2, 3, 5 and 6 rendered and read as images, no text gate sees a TikZ collision.

## 8. One page-mechanics note, recorded because it constrains the next round

Page 9 looks as though it has nine spare lines. It does not. Whether §4.3's heading still fits on page 8
under Figure 2 is **bistable**: about two additional body lines anywhere in §1–§3 pushes the whole §4.3
block to page 9 and the conclusion off page 9 in one step of roughly fourteen slots, with no intermediate
state. So this revision is at the largest length that keeps the body on nine pages, and every addition
above was funded by a deletion in the same zone. The note is now a comment in `methodology.tex` beside
§3.3 so it is not rediscovered by measurement a third time.
