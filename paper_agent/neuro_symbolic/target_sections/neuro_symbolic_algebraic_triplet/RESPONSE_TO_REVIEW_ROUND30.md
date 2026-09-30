# Response to the round-30 review

*Not part of the paper.*

**Summary: you told us not to sell Theorem 1 as a major theoretical contribution in the abstract or
introduction. We stopped, and that de-emphasis is what paid for the three sentences you asked for,
so this round is funded entirely out of the previous round's framing rather than out of any claim.**
The abstract's sale sentence is gone, §1's contribution-(1) clause is a bare citation, and §3.4 now
says in the paper's own voice that a reader who finds the theorem close to a restatement of what an
admissible family means **is not disagreeing with us**. All three of your requested sentences are in,
in the positions you named. **No new experiments, no new datasets, no new corpora**; you forbade
both, twice. The assertion count is **unchanged at 2143**, deliberately: nothing this round is a new
measurement, so nothing should move it.

Two findings from executing your asks are worth more to us than the edits themselves, and both are
recorded below in full: **the sentence you asked us to add after the definition already existed in
that exact position, with its one missing clause stated twice one paragraph later**; the paper had
the content three times across two pages and you still read past it, and **two of the fifteen terms
in your own cognitive-load list were used in the body and defined nowhere.**

---

## 0. The scorecard, and the bet that lost

| Criterion | R26 | R27 | R28 | R29 | **R30** |
|---|---|---|---|---|---|
| Technical correctness / soundness | 8 | 7.5 | 8 | 8 | **8.5** |
| Experimental rigor / validation | 8.5 | 8 | 8 | 9 | **9** |
| **Novelty** | 7 | 6.5–7 | 7 | 7 | **7 ← binding, fifth consecutive round** |
| Significance | 7.5 | 7.5 | 7 | 8 | **7.5** |
| Clarity | 7.5 | 7.5 | 7.5 | 8 | **7.5 ← down** |
| Reproducibility | 9 | 9 | 9 | 9 | **9** |
| **Overall** | 7 | 7 | 7 | 7 | **7** |

Confidence rose to **4/5** and `Presentation` left the scorecard.

**Round 29 was a bet and it lost, in a way we can price.** Round 29 asked, twice, for *"a stronger
conceptual theorem, not more algebra."* We added Theorem 1. Round 30's verdict is that it *"is close
to a formal restatement of the definition of an appropriate control family"*, Novelty did not move,
**and Clarity fell 8 → 7.5 naming exactly round 29's additions** (Definition 1, Theorem 1,
Corollary 1, the propositions, all on page 5), as the cognitive-load problem. **So the theorem cost
0.5 clarity and bought nothing on the axis it was added for.**

**We said in advance what we would do in this case.** `RESPONSE_TO_REVIEW_ROUND29.md`: *"If Novelty
holds at 7 after a necessity theorem, we will treat the conceptual argument as exhausted. The honest
next lever is then the one that worked at round 25 — declining the axis in the paper's own text."*
This round is that pre-commitment executed, and it happens to coincide exactly with your own
instruction. Round 28 taught us the qualifier on that play; **declining an axis works only while
there is no cheap way to answer it**, and here you supplied the cheap way: one sentence next to
Table 1.

**This is the third stance reversal on the same object in this review history**, and we would rather
name it than let it look like drift. Round 19 warned against selling a proposition; round 25
reversed it. Round 29 demanded the theorem; round 30 says do not sell it. Our resolution is the same
each time: **the apparatus stays where it is true and used, and only its billing changes.** Theorem 1
is not retracted, not weakened and not moved to the appendix: §3.5 cites `Theorem 1(iii)` and it is
load-bearing there. What changed is that the paper no longer asks you to credit it.

---

## 1. Ask 1: the novelty sentence, next to Table 1

You wrote *"That is the sentence I want to see."* It is now the closing paragraph of §2, immediately
before Table 1, which floats to the top of the next page, so the sentence and the table are
adjacent in reading order:

> **What is new, given all of that.** Prior devices test one comparator or one perturbation in
> isolation; admissibility auditing makes the comparator's *invariance* itself an empirical object,
> tested per instance, and aggregates a declared *family* of such comparators into an explicit
> evidential ceiling (Table 1).

It replaced a bare pointer (*"Table 1 places the criterion against each prior device"*), so the
paragraph now makes the claim instead of delegating it.

**We checked your sentence clause by clause against the table before pasting it, and (for the first
time in five rounds) it checked out.** Round 22's supplied sentence (*"architecture comparisons rely
only on Tree-LSTM"*) was false here; round 24's proposed abstract said a depth-8 control was *"at
chance"* when it is `0.100` against chance `0.005`, and deleted the previous round's entire
contribution; rounds 23 and 27 were wrong about the paper in the same way. So the check is now
standing procedure, and this is the first time it passed:

| Your clause | Verified against |
|---|---|
| *"test one comparator … in isolation"* | the `control task`, `matched control` and `counterfactual eval.` rows, all `×` in the **family ceiling** column |
| *"one perturbation in isolation"* | `invariance test` and `counterfactual eval.`, which perturb the input rather than constrain the comparator (§2) |
| *"the comparator's invariance itself an empirical object, tested per instance"* | the twin test in §3.3: a member is pinned at exactly `0.500` per instance, and the **comparator invariance** column, `×` or `partly` on every prior row |
| *"aggregates a declared family … into an explicit evidential ceiling"* | Proposition 1 and Corollary 2; the **family ceiling** column is `×` on all seven prior rows |

We used the phrasing above rather than yours verbatim in one respect only: *"Prior devices"* instead
of *"Prior methods"*, because the paper and Table 1 both say `device` throughout.

---

## 2. Ask 2: F3's epistemic status, and the reason it did not register

**The sentence you asked for already existed, in the exact position you asked for it.** Immediately
after Definition 1, under the heading *"What passing establishes, stated once"*, the paper already
said that passing means only that performance exceeds a **prespecified, enumerated** family under the
stated protocol, and Definition 1's own title reads *"relative to the declared family, never
absolutely."* The one thing missing was your completeness negation, and **that was stated twice, one
paragraph later**: *"admissibility here is family-relative, like completeness: the audit tests
invariance to a declared family, it does not establish invariance"*, and *"F3's enumeration is what
we could build under Definition 1, not its boundary."*

So the content was present **three times across two pages, and it still did not register.** That is
the round's most useful finding, and it inverts a lesson we had drawn eight times before. Rounds
19–27 kept teaching us that *a result existing only in the appendix does not exist*. This is the same
failure with the opposite cause: **the content was not scarce, it was diffuse. Redundancy is not
salience: position and form are.** Three hedges spread over two pages read as hedging; one sentence
in the place a reader looks reads as a statement.

The fix was therefore a **consolidation, and it is net-negative in length.** The paragraph after
Definition 1 now reads:

> **What passing establishes, stated once:** not compositional reasoning, only that the learned
> representation exceeds *every member* of a **prespecified, enumerated** family under the stated
> protocol — **it does not establish that F3 contains all P-invariant explanations**. We say it
> **passes the F3 audit**, so the family travels in the name (Propositions 2, 3).

and the two downstream restatements collapsed to *"so admissibility here is **family-relative**"* and
*"**The enumeration is not the family's boundary**: a reader can admit a candidate we never considered
by running the same test."* **The reader-can-admit-a-candidate affordance and the `r74` residual
numbers are kept verbatim**: round 25 taught us that cutting a "repeated" caveat can silently
unscope a claim, so only exact restatements and lead-ins went. **This is simultaneously your
cognitive-load fix**: page 5 lost two paragraphs' worth of duplicated hedging.

We used the paper's own `passes the F3 audit` rather than your *"Passing F3"* because the next clause
explains why the short form is licensed afterwards: the family travels in the name.

---

## 3. Ask 3: the headline result, long form first

The abstract's final paragraph now leads with your phrasing and defines the compression after it,
rather than the reverse:

> **So what we claim is generalization to unseen *compositions of known transformations* beyond
> bounded order-blind structural controls — *composition-of-known-transformations* generalization,
> scoped to K≥200 here and, for the coverage mechanism, to the polynomial setting — and not
> compositional reasoning**: four primitives are not a library.

The conclusion keeps the short form unchanged, now licensed by that definition. **The conclusion was
not touched at all this round**; it is the last thing on page 9 and the page-9/page-10 boundary is
this paper's most fragile gate.

---

## 4. The Major-Concerns asks

- **`passes the F3 audit` → long form on first use.** §1's contribution (3) now reads *"a Tree-LSTM
  passes the F3 audit **under the declared admissible family** up to unseen **compositions of
  *known*** separately-trained rewrites."*
- **The central result as evidence, then as interpretation.** §4.2's depth-8 paragraph now closes:
  *"**The evidence is sensitivity to global arrangement beyond the declared order-blind family**;
  calling that **composition-of-known-transformations** generalization is an interpretation, and
  rules out no other admissible structural explanation."* You asked for the non-establishment repeat
  *"occasionally"*; the §1 box carries the first instance, this is the second, and the sentence after
  Definition 1 is the third.
- **Cognitive load.** Addressed three ways: the two consolidations above remove hedges from page 5;
  the **St ↔ Ft relation is now in the glossary**, where previously it was derivable only from
  Definition 1 on the page you called overloaded; and; see §5.
- **Multiplicity.** You wrote *"The best defense is the one you already have: report the failed and
  withdrawn analyses too. I would emphasize this in the paper rather than add more statistical
  machinery."* Agreed, and no machinery was added. §1 now ends the flaw paragraph *"and four of them
  ours (Table 10), **including a pre-registered prediction of ours that failed**"*: the `r96` SCAN
  audit, whose registered prediction the data refuted. It reuses already-asserted numbers, so
  `verify_claims.py` is untouched.
- **"Paper A dominates Paper B", no edit, a measurement instead.** Your suggested narrative
  (problem → audit methodology → expose failures → recover one narrower positive) is already the
  order of the abstract's four paragraphs, of §1's three contributions and of the conclusion's three
  numbered items. We think the dominance you are reading is real but correctly proportioned: the
  methodology is what generalises and the finding is scoped to `K≥200` on `poly8`, and the paper says
  so in both places. We would rather leave the balance visible than restructure to flatter it.
- **SCAN / clone / NeSymReS boundary language: kept verbatim**, as praised. Likewise
  `verify_claims.py`: *"I'd retain this exactly."* It is retained exactly, at 2143 assertions,
  exit 0.

---

## 5. Two of your fifteen terms were used in the body and defined nowhere

You listed fifteen simultaneous terms as the cognitive load: property P, S1, S2, S3, F1/F2/F3,
admissibility, family ceiling, skyline, twin, gate C, protocol, coverage, identification,
discrimination, composition. **We checked the glossary against that list, and `identification` and
`discrimination` were both in use in §4: §4.1 and §4.2 respectively, and absent from *"Terms,
once."*** They are now defined there: *"**identification**: recovering the held-out form's own class;
**discrimination**: telling it from a non-equivalent match."*

This is a real defect that **no automated gate in this repository can detect.** We verify numbers
against logs (`verify_claims.py`, `check_tex_numbers.py`), references against the build, and pages
against the PDF, but nothing checks that a term the body relies on has been introduced. Finding it
required reading your list against the glossary by hand. We are recording it as the class of defect
our apparatus is blind to.

---

## 6. What we did not do, and one pre-commitment

**No experiments, no datasets, no corpora, no new statistical machinery.** You forbade the first two
twice and argued against the fourth; we agree on all counts.

**We did not remove Theorem 1 or move it to the appendix.** You did not ask for that, you explicitly
approved the §3.4 scoping mechanism, and §3.5 cites `Theorem 1(iii)`. Removing it would free about
five lines and would be a fourth reversal on the same object in as many rounds.

**One residual we are disclosing rather than fixing.** The conclusion's item (1) still reads *"The
method is forced, not chosen … (Theorem 1)."* That is neither the abstract nor the introduction, the
two places you named; it is a claim about the *method* rather than about the theorem's standing as a
contribution; and §3.4 now disclaims that standing explicitly. We left it because the conclusion is
the last text on page 9 and any growth there breaks the page limit. If you read it as a residual
sale, say so and it becomes a one-line edit.

**And a pre-commitment, in the same spirit as the one that governed this round.** Novelty has now
been binding for five consecutive rounds and has survived a reframing (25), a hoist into the intro
(21–22), a table (27), an experiment (28) and a theorem (29). If it holds at 7 after the axis has
been **declined in the paper's own text and answered with the exact sentence you specified**, then we
will conclude the paper is at its ceiling for this reviewer on that axis and **stop reframing it**
rather than open a round 31 on the same question. Continuing to re-litigate a fifth lever would cost
clarity again, which is what round 29 demonstrated.

---

## 7. Verification

All measured after the final build (`pdflatex → bibtex → pdflatex ×2`):

- **0 errors, 0 undefined references or citations, 0 `Float too large`, exactly 2 overfull boxes**:
  the pre-existing `6.4211pt` vbox and the `3.509pt` hbox at lines 1398–1413. 83 pages.
- **Abstract still ends on page 1** (*"four primitives are not a library"*), **the body still ends on
  page 9** (*"what we claim, exactly, is Table 2"*), and **page 10's first non-folio line is still
  `ETHICS STATEMENT`.**
- **Every region netted ≤ 0 of rendered pressure, and the proof is placement rather than arithmetic:
  all thirteen section headings land on the same page as the pre-round baseline, with at most one
  line of drift** (§3 at 187→188, §3.4 at 317→316). Zero float repacking, which round 27 showed is
  the failure mode a caption change causes. Page slack is unchanged: p1 722.55 against a full page's
  732.0, every other body page at 731.9–732.7.
- **`verify_claims.py`: 2143/2143, exit 0, in all three code copies.** `check_tex_numbers.py` traces
  12/12 literals in the rewritten §4.2 paragraph.
- **Both tables rendered as images and inspected**: `\checkmark` drops silently from `pdftotext`, so
  Table 1's ✓/× grid cannot be verified from text alone. **All nine body pages were read as rendered
  output**, which is the only gate here that has caught the last three rounds' real defects: an
  inverted negation, a sentence beginning with an em-dash after a full stop, and a clause number with
  no clause labels, each with every automated gate green.
