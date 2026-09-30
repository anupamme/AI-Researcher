# Response to the round-24 review

*Not part of the paper.*

**Summary: a clarity round. No experiments, no new claims, no change to the assertion
count, and the review's two headline presentation asks turned out to describe a figure
the paper has had in its appendix since round 13, which a reviewer five rounds ago also
asked to have in the body.**

---

## 0. The ask, and what we did with it

You scored Clarity `6` and said it is the cheapest axis to move without more
experiments. We agree, and we spent the round entirely there. **`verify_claims.py` still
reports `2071/2071`**: deliberately. It never reads the `.tex`, so a presentation round
*cannot* legitimately move the count, and a moved count would mean something unplanned
entered the pipeline.

| Criterion | You | This round |
|---|---|---|
| Clarity | 6 | the whole target |
| Scope / generalization | **5** | **not addressed; see §8** |
| everything else | 7–9 | untouched |

---

## 1. Your items 1 and B: the recipe already existed, in the appendix

You asked for *"the entire argument in one 30-second mental model… the four-step recipe…
at the end of the first page"* (item 1) and for a *question / test / if-it-fails /
if-it-passes* table (item B). Both describe **Figure 4, `fig:procedure`**: already in the
appendix, already drawing corpus → S1 → S2 → S3 → twin → gate C → *only now interpret*.

**Round 19's reviewer called that figure "the clearest thing in the paper" and asked for
it as the centerpiece.** We declined then, for page reasons, and added its terminal step
to Figure 1 instead. Two independent reviewers, five rounds apart, asking for the same
buried object is enough evidence that the call was wrong.

**§1 now carries it as a box, on page 2:**

> **The audit in one sentence.** A learned score supports a structural claim only once it
> exceeds the best score obtainable by controls that are *invariant to the property
> claimed*, under the same protocol. **Four questions, asked in order:** S1 can variable
> identity alone explain the score? → S2 can the operator/arity inventory? → S3 can
> bounded local structure? → gate C was the held-out transformation already in the
> training library? **Only then interpret the score, and only at the level just cleared.**

A box rather than a float, because a float cannot be pinned to a page. It absorbed the §1
prose it made redundant, so it is nearly free.

Your item 3 also asked for the S1/S2/S3 levels as a compact table. **§3.3 is now that
table**, with a fourth column you did not ask for and which we think is the point (
*So it can falsify*) naming, per level, the claim that level's control can refute.

---

## 2. Your item 5: the abstract, and why we did not paste yours

**You were right that it needed rewriting, and it was worse than a style problem: the
abstract had regrown to 523 source words, its exact size before round 20 cut it to
264, and no longer fit on page 1.** Rounds 21, 22 and 23 each added a clause. It is now
**436 words**, in your problem → method → evidence → takeaway order, and it ends on
page 1.

**We used your structure and not your text, for two reasons.**

First, your draft deletes all four audits of other people's published results. Those were
the entire content of the previous round, and the round-23 reviewer named them as the
difference between a 6 and an 8. It also drops the protocol-disagreement result, which
is your own item 9, the thing you asked us to *elevate*.

Second, **your draft contains a factual error about our paper**: *"At depth 8 it reaches
0.736 accuracy, while a matched structural control remains at chance."* The strongest
non-learned control at depth 8 is `0.100` against chance `0.005`: 20× chance, not
chance. The controls pinned *at* chance are the twin's `0.500`, which is a different
protocol. We flag this rather than quietly correcting it because it is the third
consecutive round in which a reviewer has handed us a sentence to paste that was false
about this paper, and the pattern is worth naming.

**What we cut instead** (your item 8, fewer numbers in prose): the three novelty-cost
figures, which Figure 2 prints; the breadth listing *"three corpora, two algebras, both
protocols, five independent class partitions"*; and the family-widening detail. Every
protected qualifier survived, checked claim-by-claim against a saved copy.

**And per your item 9, the protocol-disagreement result moved up**; it is now in the
evidence paragraph rather than last.

---

## 3. Your item 2: one name for the statistic

Adopted, including your word. `sup F_t` is **the admissible-control ceiling** throughout,
replacing four circumlocutions we had been alternating between. The proposition *The
admissibility ceiling* already carried half the name.

One complication worth reporting: **"ceiling" was already doing other work.** The appendix
used it ~14 times for the *metric's* attainable maximum: including a table row label and
a column header, and once for a corpus's primitive limit. Adopting your term without
touching those would have added a fourth sense of the same word, which is the opposite of
what you asked for. The metric sense is now the **attainable maximum** and the corpus
sense the **limit**; the body carries one sense.

We did **not** retire *skyline* or *twin*. A skyline is a specific object: a control
built from one level's cue and blind above it, and round 7's review turned on our
distinguishing it from an ablation. Cutting the word would re-open that.

---

## 4. Your item 10: audit vs. proof

Adopted verbatim in substance. The conclusion read *"Passing the audit still certifies
nothing"*; it now reads **"Passing the audit rules out the declared explanations and
proves no mechanism."** You are right that the old phrasing sounded more negative than the
result is.

## 5. Your item 6: the impossibility result, de-emphasised

§3.4 now opens with your sentence: **"Comparator-based audits are falsification tools,
not certification tools"**, and then moves on. The round-21 billing (*scoping, not a
theoretical contribution*) is kept, but it had been stated three times across §1, §3.3 and
§3.4; it is now stated once.

## 6. Your item 8: the paper stops arguing with reviewers

You named the tell exactly. §4.2 opened *"The objection is that a stronger member was
missed, or that ours was picked after seeing the scores"* and closed with *"'search harder
for a stronger control' is not a coherent instruction."* Both are gone; the paragraph now
states the result: every member's number is reported, the ceiling lands on the coarsest
member, the family provably saturates, so there is no stronger member to find.

That also removed the body's **only occurrence of the word "reviewer"** (§4.2 credited
five stress-test descriptors to *"a reviewer"*), which was odd in a paper that has not
been reviewed.

## 7. Where your review pulls against itself, and what we did

**Figure 1.** §1.3 calls it effective and praises its logic; §6 says it packs too much in
and should be split into a concept figure and a results figure. **We did not split it.** A
second float costs ~14 of a page's 54 line slots, and rounds 15 and 19 merged those two
figures deliberately. The new §1 box is the five-second conceptual object you want;
Figure 1 keeps the evidence that makes each rung concrete. Its caption is cut from seven
rendered lines to four, since the box now states the procedure.

**Your item 7** (*Result / Interpretation / Scope* as three labelled sentences per
experiment) **we did not do, and we are telling you rather than letting it pass.** The
body ends on the *last* of page 9's 54 line slots. Every addition this round was paid for
by a deletion in the same region, and that pattern was the pre-committed first thing to
drop when the space ran out. It did.

## 8. What this round does not touch

**Scope/generalization `5` is the lowest number on your scorecard, and we have not moved
it.** Your fix (one genuinely independent domain with a *real* external benchmark rather
than our constructed Python-clone corpus) is right, and it needs a corpus and compute
rather than an edit. The ask this round was clarity. We would rather say that plainly than
let a `5` look addressed by a round that did not address it.

## 9. Gate state

0 LaTeX errors · 0 unresolved references · 0 `Float too large` · exactly 2 overfull boxes,
both pre-existing · **76 pages, unchanged** · **abstract ends page 1**, body ends page 9,
page 10 opens with the Ethics Statement · `verify_claims.py` exit `0` at **2071/2071** in
all three shipped copies · `check_tex_numbers.py` clean on every rewritten block · both
figures and the new table rendered and looked at, since text gates cannot see TikZ
collisions · the five elements a cold reader gets (abstract, §1, the box, both figures,
the conclusion) extracted from the built PDF and re-read cold.
