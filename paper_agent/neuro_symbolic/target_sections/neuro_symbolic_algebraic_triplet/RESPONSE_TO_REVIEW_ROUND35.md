# Response to the round-35 review

*Not part of the paper.*

**Summary: no new experiment, no new dataset, no new table; you asked for none, and we added
none.** Your instruction was explicit (*"I would not add another 20 experiments. The paper already has
enough empirical work"*), and your one experimental suggestion you withdrew in the same breath
(*"You already have the shape-matched twin, which goes a long way"*). So this round is framing,
correction and compression, and every addition is funded line-for-line by a deletion.

Assertion count **2250 → 2250**. No new run, no new log, no change to `verify_claims.py`. Body still
**9 pages**, 88 total, exactly the 2 pre-existing overfull boxes.

---

## 1. Your binding question, and what we think went wrong last round

You asked:

> *"Is 'admissibility auditing' genuinely a new methodological contribution, or is it a carefully
> formalized restatement of the obvious principle that a control must be invariant to the property
> under test?"*

A reader with that question turns to the subsection titled **"What Is New About Admissibility
Auditing"**, and in the reviewed file that subsection was, measured against its own PDF text layer,
roughly **3.5 of its 9 lines a concession** that the theorem is close to definitional, **3 lines a
limitation**, **2 lines a pointer**, and **half a line of assertion**. We wrote that concession in
round 34 to answer a *different* reviewer's objection that we were overselling the theorem, and on
your scorecard it worked: Technical soundness 7.5 → 8.5 and Empirical rigor 8 → 8.5. But we put it in
the one subsection whose job was to assert.

**The lesson we are recording: a concession placed in the section that must assert is priced as an
absence of novelty.** The two reviewers are different draws, so we are not claiming causation: the
*placement* is the measurement, and it was ours to get right.

The fix is not to re-sell the theorem. Three consecutive reviewers have now told us not to. It is to
**move the concession next to the theorem it scopes** and let the novelty subsection carry the deltas.

## 2. What changed, against your five 7→8 items

**(1) The boxed "what admissibility auditing adds beyond control tasks" subsection; you called it
"probably the highest-return revision".** Done, under your title, as §3.3. It is now a four-row
*existing idea ⇒ what this paper adds* table, each row naming where it is evidenced:

| Existing idea | This paper |
|---|---|
| a *strong* baseline | **admissible**: a non-*P*-invariant comparator bounds nothing at *any* score (Thm 1(iii)) |
| a *control task* | invariance **tested per instance**, by a twin, not assumed (tag `r74`) |
| a *matched* control | a **declared family** and its *ceiling*, which no member replaces (Prop. 1, Cor. 2) |
| a *good score* | read **only above that ceiling**: **falsification tools, not certification tools** |

The concession (*"billed as scoping … a reader who finds the theorem close to a restatement of what an
admissible family means is not disagreeing with us"*) now sits **immediately after Corollary 1**, a
page earlier, where a reader forming an impression of the theorem's weight is actually standing. That
single move is also your item (3) and your §15, and it is what pays for the four rows.

**(2) The family-relative nature in the headline.** It was in neither headline sentence. Measured:
`passes the F_3 audit` occurred at §1 and §3.2 and **zero times in the abstract and zero times in the
conclusion**; `family-relative` occurred in the abstract and §3.2 and **zero times in the conclusion**.
Both headline sentences now carry it; the abstract's *"what passing means is that the encoder passes
the F3 audit: it exceeds the declared admissible family under the stated protocol"*, and the
conclusion's *"a family-relative verdict under a stated protocol"*.

**(3) Theorem 1 demoted visually.** Retitled from *"Admissibility is necessary, and the ceiling is the
only instrument"* to **"Formal justification for the audit criterion"**, which is your own phrase. The
three-part statement is untouched: it was added in round 29 on a prior reviewer's explicit demand and
is cited from three live sites.

**(4) Compression.** Measured, not estimated: about **19–21 line slots** removed from §3, §4 and §5,
roughly 15% of their prose, every one of them a verbatim duplicate, a restatement derivable from a
neighbouring sentence, or defensive meta-prose. Nothing scoped was cut. Two examples: the conclusion
stated Theorem 1's asymmetry for the **third** time in the paper, and a `\paragraph{What is forced, and
what is chosen.}` restated the theorem's own clauses (i)/(ii) from the same page. The savings paid for
§3.3's table and the box below, so the body is still 9 pages rather than 8, which is the trade you
implicitly asked for when you said the additions were the highest-return change.

**(5) Figure 1 "extraordinarily simple".** We did not add a float. `fig:framework` is cited on page 1
but renders on page 3, and a float cannot be pinned to a page; the flowchart-shaped figure you may be
remembering is an appendix figure. So the audit's decision logic now lives **inside the boxed panel on
page 2**, which is where "tells the whole paper in 20 seconds" has to happen: one chain from *the
claim* to three named terminals (**claim unsupported** · **no evidence** · **evidence against the
declared alternatives, and nothing more**) with gate C drawn *below a rule*, off the chain.

## 3. Your §22 was right, and we had already fixed it in the wrong place

The page-1/2 box said **"Four levels, cleared in order"** and listed gate C as a fourth row. Two figure
captions in the same document say *"coverage gates interpretation, **not a fourth level**"*, and §3.2
says *"three levels"*. Worse: a comment in the figure source records that **a prior reviewer had
already reported this**, and it was corrected in the figure and never in the prose.

**The lesson: a defect fixed in one representation recurs while another representation still states
it.** This round found four instances of that class, and two of them are now permanently gated (§6).

The box now reads *"Three cue levels, cleared in order, and then a separate interpretation gate"*, and
the gate C row reads *"not a level … gates interpretation, not screening"*.

## 4. §17: the paper was taking your side in one file and contradicting it in another

You asked that the token-bag skyline be the canonical control and the random encoder a secondary
diagnostic. §3.2 already disqualified the untrained encoder: it *"fail[s] [the per-instance test] and
[is] reported as [an] extension X **outside the criterion**"*. But Related Work called it *"our
random-encoder skyline"*, supplying the control-task analogue. Related Work now names the
**zero-parameter bag** as that analogue, *"which the per-instance test admits, an untrained encoder
being a secondary diagnostic that fails it (§3.2)"*.

## 5. §14, §20, §23, §24, §25: done, and cheap

- **§14 (the family's own enumeration).** The rationale existed two pages away, phrased as a finding.
  Definition 1 now carries it where the family is declared: *"the depth ladder doubling to the point
  where it **saturates**, since poly8's deepest tree is 4 and no member finer than φ4 exists (§4.2),
  and the WL radii being the **conventional 1–3 rather than derived**."* We state the WL radii as a
  convention because that is what they are; we will not imply a rationale no text of ours has.
- **§20 (move SCAN earlier).** The strongest external result sat behind three dampeners, including its
  own heading, *"where the inversion stops"*. SCAN is now the **first** paragraph of §4.3, led by
  *"The sharpest test of the whole procedure is one somebody else built"* and by `add_prim_jump`. Zero
  page cost: identical text, reordered.
- **§23 (define the term at first use).** Your one-sentence definition is now attached to the
  **first** of the three occurrences of `composition-of-known-transformations`, in the abstract:
  *"each rewrite trained alone, the held-out forms unseen combinations of them."* Not to all three:
  round 30 taught us that a fourth restatement is redundancy, not salience.
- **§24 (the twin's logical chain).** Made explicit in §4.2, from facts already in that sentence:
  *"what the pair shares is every lower-level cue, token and operator multisets alike; what it differs
  in is arrangement alone; so any score above chance must be read off arrangement."* No new run, as
  you allowed.
- **§25.** *"Failure is informative; passing is not certification"* is now the closing line of §3.3.

## 6. §18; you were right, and our measurement was scoped too narrowly

You asked us to replace *"The token-bag skyline is a universal audit."* We first measured `universal`
across the six body files and five body floats and found **zero occurrences**, and were about to
report the claim as non-existent. It exists. It is in `appendix_domain_guards.tex`, verbatim:

> *"Second, the token-bag skyline is **a universal audit**: any benchmark where bag-of-tokens exceeds
> reported accuracy has not demonstrated structural learning under natural evaluation; renaming
> controls are required."*

**Grep absence over the body is not absence over the document**, and an appendix is exactly where a
claim the body scopes can quietly stand unscoped. Worse, the clause immediately before it read
*"variable-identity leakage is **pervasive**"*, which contradicts our own measured survey result in
§4.1 (*"the S1 flaw is real and **confined to one family**"*) and our own refusal in §1 (*"a
constructed counterexample, **not evidence of prevalence**"*).

Both are fixed. The sound part of the claim (the one-directional conditional, which is Corollary 1)
is kept and its direction stated: the skyline is *"**portable**, not universal, and licenses one
direction only … **while clearing the bag certifies nothing**"*; and the prevalence clause becomes
*"structural diversity is no protection … but this is **one** corpus, and **no prevalence follows**"*,
with the survey cited. This honours your §19 (*"portability, not general validation, never
prevalence"*), which we have left untouched in §4.3.

**This is now gated, document-wide** (§8).

## 7. §21: declined, with the measurement, and disclosing a conflict

You asked us to cut the error-history material in the main narrative to one sentence. The main
narrative contains **three** clauses, not a history:

1. `Four of the audited results are other people's`: abstract
2. `The same screens revise eight already-published results`: §1
3. `withdrawing a portability claim of our own`: §4.1

All three are gated at exactly one occurrence in `check_protected_claims.py`, because each is
load-bearing: they are why the audit is credible when applied to us. The *detailed* chronology is in
`statements.tex`, which renders on **page 10**: ICLR's page limit does not count it, and the full
history ships as `REVISION_HISTORY.md`.

**We are also disclosing a direct conflict rather than arbitrating it: round 34's reviewer explicitly
asked us not to remove these.** We have kept them and told you why, which is the same thing we did
when two reviewers disagreed about new datasets.

## 8. What we made permanent, and a gate of ours that had been silently under-running

`check_protected_claims.py` gets three changes, and the round's durable artifact is the third.

1. **Two body-scoped absences added**: `Four levels` and `random-encoder skyline`, the two
   contradictions of §3 and §4 above. Both survived every existing gate, and one had already been
   reported once by a reviewer.
2. **A stale entry in the checker's own file list had been silently dropped for several rounds.** The
   list named `table_entitlements.tex`; Table 2 moved inline into `methodology.tex` some rounds ago, so
   a `glob`-filtered comprehension quietly ran the gate over **one file fewer than it reported**. A
   missing input is now a **failure**, never a skip. This is the fifth silent-skip defect this project
   has found in its own tooling, and the pattern is always the same: a filter that tolerates absence.
3. **A document-wide absence scope, with the file list derived rather than typed.** §6 is a class of
   defect the old gate structurally could not see, so `ABSENT_ANYWHERE` now checks `universal audit`
   and `leakage is pervasive` across **all 15 `.tex` files the document actually `\input`s**, read off
   the main file's input graph, because a hand-kept list is prose, and prose is what rotted in (2).
   It also fails if a body or float file stops being `\input`'d at all. `random-encoder skyline`
   deliberately stays body-scoped: the appendix uses that phrase six times in its own metric sense.

Both scopes carry a sentinel that must be absent and a corpus-size positive control, and the new one
was **negative-controlled against the defect itself**: run over the last committed version of the
appendix, it reports `universal audit` = 1 and `leakage is pervasive` = 1; over the current file, 0
and 0. A gate that has never fired on a real defect is not yet evidence of anything.

## 9. One defect this round's render gate caught, and the audit it triggered

Reading the built page 2 as an image showed the gate C row citing **§3.3** (the novelty subsection),
where gate C is defined in **§3.2**, whose title literally names the coverage gate. A real `\ref`,
aimed at the wrong section, in the most-read box in the paper, with every text gate green. We then
resolved **all 23 `\ref{sec:…}` sites in the body** against the heading each label actually sits under;
the other 22 are correct.

## 10. Not done, and why

- **Promoting §4.4 (the protocol-disagreement result) ahead of §4.3.** You called it *"arguably the
  strongest empirical result"* and asked for more prominence; it is already in the abstract and in §1's
  contribution (2). Moving it would shift prose across the page-7-to-9 float region, and in round 27 a
  single caption growing by four lines repacked five pages of floats. Pages 1, 2, 3, 4, 7 and 8 are at
  **exactly zero slack**. We took the prominence gains that cost no float movement and left this one.
- **A fourth reordering of §4.** Same reason.

---

## Gate state

`pdflatex → bibtex → pdflatex ×2`: **0** errors, **0** undefined references or citations, **0**
`Float too large`, **exactly 2** overfull boxes (`6.4211pt` vbox and `3.509pt` hbox, both pre-existing),
**88** pages, abstract ends p1, body ends **p9**, and p10's first body line is `E THICS S TATEMENT`.
All thirteen body headings and all four body floats are on their reviewed-version pages (Fig 1 p3 ·
Table 1 p4 · Table 2 p5 · Fig 2 p8), and per-page `yMax` is unchanged to 0.01pt, so every region nets
≤ 0, proved by placement rather than by arithmetic.

`check_protected_claims.py`: **PASS**, 19 protected claims, 4 body absences, 3 document-wide
absences over 15 files, all controls firing. `check_reviewer_map.py`: **PASS** at 259 checks, 15 rows,
42 tags, 52 appendix letters. `verify_claims.py`: **2250/2250, exit 0, in all three copies.**
