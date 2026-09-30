# Response to review: round 20

**Summary: you scored clarity 6 against eight everywhere else, said clarity was the biggest remaining
lever, and gave a falsifiable test for it. We built the round against the test, and it ran no
experiments**, the second consecutive zero-compute round, and again because you pre-refused the
alternative: *"I would not add another 20 experiments… make the paper much more intellectually
economical."*

Your test:

> *"A reviewer who reads only the abstract, introduction, Figure 1, Figure 2, and conclusion should be
> able to reconstruct the entire argument correctly. Right now, a reviewer needs to read substantial
> parts of the appendix to do that."*

**We ran that as a gate, not as an aspiration**: extracted exactly those five elements from the built
PDF and read them cold. Every element of the argument now reconstructs from them: thesis, the example
that explains it, the method, the impossibility result, all four robustness findings, the named
positive result with its price hierarchy, and the scope limits. What that took is below.

**Main text is still 9 pages** (page 9 runs slots 432–485, `E THICS S TATEMENT` first on page 10). The
verifier moves **1937 → 1949** and `statements.tex` prints the new count, exit 0 in all three copies.

---

## A diagnosis that shaped the whole round

**Three of the results you singled out as compelling were already in the paper: in the appendix.** You
surfaced, unprompted and by quoting them:

1. *"The supremum moves at 4 of the 8 cells and always to the path kernel, by at most +0.038… no
   verdict moves anywhere"* — verbatim in Appendix AT. The body said only *"moves its supremum by at
   most 0.038 and changes no verdict."*
2. The **matched-construction contrast**, `(0.965, 0.880) → (0.832, 0.662)`: Appendices E/W. The body
   gave only Figure 1's pooled gate-C row.
3. The LOPO cost as a **range**, `+0.429` to `+0.845`, with `commute` cheapest: Appendix AU. The body
   printed only the pooled `+0.664`.

You called these *"a very compelling result"*, *"a very good scientific point"*, and read the range off
the appendix table. **You had to go and get all three.** Round 19 diagnosed this failure mode once; it
has now happened three more times, so we will state it as a rule we are accepting: **a result that
exists only in the appendix does not exist.** This round is about salience, not content, which is why
it needed no new compute, and why we are not asking you to take anything on faith that was not already
in the file you read.

---

## Your #1: *"put the thesis on page 1"*. **Done, it is the first sentence.**

§1 now opens on the sentence itself, before any formalism:

> **A stronger baseline is not necessarily a stronger control.**

## Your #2: *"the AI Feynman example immediately after"*. **Done, second and third sentences.**

> Take the claim that a Tree-LSTM recognises algebraic *form* rather than which *variables* appear. On
> AI Feynman a zero-parameter bag of variable tokens scores **1.000** where that encoder scores
> **0.972** (Figure 1, rung S1): the bag is the *better* predictor of the benchmark label, and it is
> worthless as evidence about variable-identity invariance for precisely the reason it wins — it reads
> nothing but variable identity. **Comparator strength and comparator admissibility are different
> dimensions**, and an evaluation that picks the strongest available baseline conflates them.

That is the whole framework in four sentences, and the formalism now follows it rather than preceding
it. **The same pair also opens the abstract**, so the thesis and its example land before a reader has
made any commitment.

## Your #3: *"one figure: S1 → S2 → S3 → admissible control"*. **Figure 1 already was that figure; we made it say so.**

A second diagnosis. Figure 1 has shown the three levels, the gate and the terminal interpretation step
since round 19; you asked for it as if it were missing, which means the caption was not telling you
what to read. It now opens by naming the procedure:

> **Read top to bottom this is the audit procedure**: fail at any stage and the reading is unsupported,
> and the terminal bar is the only point at which a learned number is interpreted — against the family
> just cleared and no wider (Proposition 4).

## Your #4: *"consistently name the positive result"*. **Done: composition-of-known-transformations generalization.**

The name now appears in the abstract's closing sentence, in Figure 2's caption where it is *defined*
against what it excludes, and in §4. Nowhere in the paper does the positive result get called
"compositional generalization" unqualified.

## Your #5 / #10: *"a one-page 'What do we actually establish?' table"*. **Done, and the verdicts against us are in it.**

`tab:entitlements` (Table 2) is rewritten from a generic what-a-result-licenses table into the concrete
grid you asked for; claim, evidence, verdict, and it is the paper's answer to "what is established":

| claim | verdict |
|---|---|
| the score requires S1 | **often false** |
| the score requires S2 | **false for that benchmark** |
| robust to protocol | **sensitive** |
| robust to a wider admissible family | **yes; no verdict moves** |
| composition of known transformations | **supported** |
| unseen arrangement | **supported** |
| unseen depth | **partial** |
| unseen primitive | **not established** |
| general compositional reasoning | **out of reach in principle** |

Both inbound references were rewritten to point at it as what it now is: §1 calls it *"every claim, its
evidence and its verdict on one page"*, and the conclusion opens its final paragraph with **"What we
claim, exactly, is Table 2, the verdicts against us included."**

**One residual we are naming rather than hiding.** Your reconstruction test does not include Table 2,
and the conclusion points at it. We checked that this is not load-bearing: the abstract states all four
robustness findings and the scoped positive claim in its own words, so the argument reconstructs
without the table. The table is corroboration for a reader who wants the whole ledger at once, not a
link in the chain.

## Your #9: *"a figure for the generalization-cost hierarchy"*. **New Figure 2.**

The figure you drew, on one scale, each bar carrying its own verdict:

- novel **arrangement** `+0.012`, every interval covering zero → **supported**
- novel **depth** `+0.200`, `[0.163, 0.237]` → **partial**
- novel **primitive** `+0.429` to `+0.845` → **not established**

Caption opens `**Takeaway:** novel arrangement is nearly free, novel depth costs something, a novel
primitive is fatal`, and it reports **the range you read, plus the pooled value, and says which is
which**: `commute` named as the cheapest to withhold, `double_negate` as the dearest, pooling to
`+0.664`. Your #4's inconsistency was real reporting drift, not just framing: the body printed the
pooled number and the appendix the span, and a reader who checked would have thought one was wrong.

## Your #7 / #14: roadmap and takeaways. **Both.**

§4 opens with four questions mapping one-to-one onto its four subsections. **All five main-text float
captions now open with a bolded `Takeaway:` line** (Figure 1, Figure 2, Tables 1--3); there was not
one in the paper before.

## Your #6: the notation box. **§3.3's terms are now a labelled list, not prose.**

The paragraph was already a glossary; it was written as a sentence, so nothing in it could be found.
`S1`/`S2`/`S3`, gate C, cue, skyline, twin and `sup F_t` are now a `description` list and take about ten
seconds to look up.

## Your #13: *"cut 15–25% of main-text prose"*. **The abstract paid for the round.**

**The abstract lost half its length** (517 words of source down to 264 (401 as rendered, since it
prints numerals)) restructured to problem → observation → method → evidence → conclusion. That single
block funded Figure 2, the establish-grid, the page-1 thesis and the roadmap inside the same 9 pages.

**We diffed the old abstract against the new claim by claim before deleting it**, because losing a
hard-won qualifier to brevity was the one way this round could have gone backwards. Everything
protected survived: the falsification-not-certification sentence; S2 separability as *"a statistic over
pairs, not a held-out accuracy"*; the `K≥200` scope; *"for the coverage mechanism, to the polynomial
setting"*; `188` orders of `2520`; and the continued **absence** of the withdrawn *"order of magnitude"*.

Your #13 also asked for the repeated caveats to be stated once. We did this **selectively and said so**:
a caveat that appears three times is often three different scopes, so we deleted only exact
restatements, the triply-stated caveat in contribution (4), the §3.3 contract paragraph, and the §4.3
sentence Table 3's new caption duplicates. Where two statements differed in scope, both stayed.

## Your #11: *"reframe the self-audit as credibility"*. **Done, in one lead-in.**

The revision history now opens **"Read this as verification, not as a bug count"** and closes on
**"None reversed a conclusion the paper draws."** Same evidence, and it is now doing the job you
identified it could do.

## Your #12: the audit-issue → effect grid. **It exists; we moved it.**

`tab:audit_changes` was a body float competing for main-text space. It is now in Appendix F with the
index line updated, which is where a reader looking for the credibility ledger will be.

## Your #8: *"compress the 74-page appendix"*. **Partially, and we will tell you exactly how far.**

We compressed the **superseded** material and added supersession banners so a reader is not left
guessing which of two similar appendices is current: Appendix AH now says *"a reader checking the
current claims can skip to AU"*, and Appendix T says *"Appendix V carries the figures the paper
uses."*

**We did not delete evidence, and we are not going to.** You scored reproducibility 9/10 on this
material and three earlier reviews praised specifically the tree-edit analysis, the diversity sweep and
the tie-breaking appendices. The appendix is 74 pages because the verifier recomputes 1949 assertions
against it. If the 74 pages are still a liability after the banners, we would rather you tell us which
appendix to cut than guess.

## Your #9 (*"complete lower-level shortcut"*): **qualified in the same breath.**

The phrase read as unconditional. It now carries *complete relative to the declared family* at the
point of use, not three paragraphs later.

## Your #4 (framing): **Feynman is now explicitly the severe case, not the typical one.**

§4.1 says it in the same sentence that reports it: *"a constructed counterexample, not evidence of
prevalence"*, and immediately before it, **"S2 is where the exposure is."* The survey always said this;
the framing did not.

## Your #13 (tone): **less debunking, same findings.**

The abstract's third paragraph now opens on the claim we actually want to make:

> **Published results can be perfectly reproducible yet support weaker interpretations than their
> protocols suggest.**

**The title is out of scope on purpose**; it is the round-16 reviewer's own wording, and we are not
going to churn it between rounds.

## Your #17: the AI-assistant disclosure. **Reordered and shortened.**

`statements.tex` (page-exempt) now leads the section with the author's responsibility sentence and puts
the division of labour before the tooling detail.

---

## What we did not do

- **No new experiments.** Zero GPU-hours, no new logs, no `REPRODUCE.md` row.
- **No appendix evidence deleted** (above).
- **The title unchanged** (above).
- **The `+0.664` / range mismatch is now reported as both numbers**, not resolved to one, because both
  are correct and they answer different questions.

## Verification for this round

- 9 pages, body ends page 9 (slots 432–485), `E THICS S TATEMENT` first on page 10; 75 pages total.
- 0 errors, 0 `??`, 0 `Float too large`, 1 pre-existing overfull hbox (3.509 pt), 0 real rerun or
  bibtex warnings.
- `verify_claims.py` **1949/1949**, exit 0 in the working tree and both artifact copies. The 12 new
  assertions cover exactly what this round promoted into the main text: the five-partition summary
  statistics, Figure 2's `commute`/`double_negate` endpoints and the strict primitive > depth >
  arrangement ordering, and the matched-construction quadruple.
- **Two pre-existing verifier gaps surfaced and closed** while checking the new text: the five-partition
  means `0.224`/`0.266` were printed in the paper but never asserted, and `r63_matched_contrast` was
  never read by the verifier at all.
- Figure 2 rendered and **looked at**; it had a column collision twice before it was clean, which no
  text-based gate would have caught.
- Appendix-orphan check clean after the consolidation.
- The reconstruction test above, run against the built PDF.
