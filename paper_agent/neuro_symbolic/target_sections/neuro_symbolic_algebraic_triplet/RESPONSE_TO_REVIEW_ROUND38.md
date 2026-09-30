# Response to the round-38 review

**Read this section first.** The review cites `iclr2027_conference(20260909-163649).pdf`. That file
predates the previous revision entirely, so **the version you read is two revisions old**, and several of
the changes you ask for are already in print. This is our hand-off failure, not a disagreement, and the
list below exists so no time is spent a third time on things that are done. Nothing in the paper itself
argues from this: the paper stands on the change described in §2.

---

## 1. What changed since the version you read

| Your ask | Where it already is, in the build before this round | Page |
|---|---|---|
| §25 "make the paper about one question" | abstract: *"The levels name **cues**, not algebra, so symbolic-expression encoders are this paper's case study, not its scope"* | p1 |
| §12 "a methodological paper with symbolic expressions as the primary case study" | §1: *"a falsification framework for **representation-level** claims"*; §4.3 is one row per modality (symbolic math / natural language / code) | p2, p9 |
| §20 "OOD is not a scalar. Your five-axis analysis makes that concrete" | §4.4's five-axis tabular, *"out-of-distribution names **five separable axes**, free to fatal"*; **this phrase appears zero times in the PDF you read**; you reconstructed the principle from scattered numbers | p9 |

Measured, not asserted: five literals from that revision (`not a scalar`, `axes`, `What the split makes
novel`, `conventional report`, `audit licenses`) count **0** in the text layer of the file you cite and
1–5 in the current build. We treat the credit in §20 as a verdict on a paper you had to assemble
yourself, and the remedy is procedural: the next hand-off ships the built PDF and this document together.

## 2. The one conceptual move, as asked, and it is a deletion

You wrote: *"I would not add another 15 experiments. The paper has enough experiments. Instead, make one
conceptual move much stronger."* **Zero new experiments were run, zero floats added, and the body is not
one line longer.**

§26 asked for the centre of gravity to be the falsification test, and you drew the diagram by hand. **That
diagram was already in the paper, in the wrong form, twice.** The ASCII chain in your §26 is
`introduction.tex:6–23` line for line: a boxed 7-row tabular titled *"The audit in one sentence."* on
page 2. Figure 1 was a *results* ladder, which is exactly your §11 complaint, *"Figure 1 contains
essentially the entire framework, multiple levels, results, caveats and scope qualifications."* And the
appendix procedure figure was a third encoding. Three objects spent roughly **31 gutter slots (0.57 of a
page) restating one ladder**, and none of them was the object a reader enters by.

So Figure 1 is now **the entitlement diagram, and the boxed tabular is gone**:

- five decision nodes: *the claim: the representation encodes $P$* → *can a $P$-invariant control solve
  the task?* → *no, so **declare the family** (S1 variable identity, S2 operator/arity inventory, S3
  bounded local structure)* → *and measure its **ceiling** $\sup\mathcal{F}$, readouts included* → *is the
  learned score **above** that ceiling?*
- **two exits, each of which ends the inference**: *an invariant control matches it ⇒ the experiment
  decides nothing*; *not above the ceiling, at any margin ⇒ no evidence about $P$*
- a terminus: *evidence against the alternatives the family declared, and nothing more*, **never
  certification**, never *how* the representation computes, and *compositional reasoning* out of reach at
  any width
- each node still carrying **the published result that settles it**, which the old ladder already had

Net **−11 gutter slots**, which is what paid for everything else in this revision. Round 19 asked for this
same figure and we answered that the main text *"cannot afford both"*; that answer is now recorded as
wrong in both figure files' header comments. Consolidation was the affordable form all along.

## 3. The shape-matched twin is now the centrepiece

Your §5: *"The strongest empirical result is actually the shape-matched twin… This is the experiment I'd
put at the center of the paper."* It was the fourth paragraph of §4.2. Now:

1. **It is a rung in Figure 1**, in the slot gate C vacated, and it earns that slot for a reason the
   inference diagram makes visible: it is **the one rung whose ceiling is a theorem rather than the
   result of exhausting comparators**. Tree-LSTM `0.994`; every order-blind $\mathcal{F}_3$ member pinned
   at exactly `0.500` *by construction*, **including a trained readout over one, at any capacity**; and
   tree-edit distance (the strongest order-sensitive **non**-member) at `0.723`, so no admissible
   comparator narrows the margin.
2. **It is the lead paragraph of §4.2**, immediately after the corpus setup.
3. **It names the section**: *The Shape-Matched Twin: A Ceiling Known by Proof* (was *Does Clearing Every
   Bag Make a Score Evidence of Composition?*).

The independent SCAN evidence you pair it with is unchanged and already the second row of §4.3's
one-row-per-modality table: `0.987` against an admissible ceiling of `0.0005`, on Lake & Baroni's own
grammar and held-out split, with the ratio deliberately not quoted because *their design puts the
admissible bar on the floor*.

**§15, the K-dependent story:** folded into the S3 rung's verdict (*"clears, and the margin grows with
scale — but only from $K{=}200$ ($K{\leq}100$ overlaps)"*), rather than built as the separate figure you
suggest. There is no page budget for a new float, and the scoping belongs next to the number it scopes.

## 4. Originality 7 / §9: the new scientific object, named

You asked, for the third round: *"What is the new scientific object?"* It is now one sentence in §1:

> the **family-relative admissible ceiling** $\sup\mathcal{F}$, the best score attainable by *any* control
> invariant to the declared property, over trained readouts as well as feature maps. **No published
> evaluation reports it**, and it is what makes the verdict falsifiable rather than comparative.

And the contributions paragraph is re-billed to your §12: heading *"One contribution; the rest is evidence
that it changes conclusions"*, with the audit of published claims, the protocol-disagreement finding and
the composition demonstration as (i)–(iii) under *"Applying it changes conclusions, in three places."*

**On the sentence you have now quoted back three rounds running**: *"A reader who finds the theorem close
to a restatement of what an admissible family means is not disagreeing with us."* **It has been moved to
the proofs appendix, as clause (e) of "What this theorem does and does not claim". It is relocated, not
retracted.** Both of the things it was there to protect stay in the body: the theorem is still **billed as
scoping** rather than as a theoretical contribution, and the consequence that is *not* definitional stays
in the same position, the statistic ranges over **trained** readouts, so every ceiling in this paper had
to be re-measured, which is the corollary the readout-closure bound exists to discharge. Two earlier
rounds credited that sentence for candour; we have kept the candour and stopped putting it where it reads
as the verdict on the section.

## 5. §17; coverage: you found a real inconsistency

*"Coverage is an independent axis of novelty, not a universal monotonic gate."* Correct, and the paper
disagreed with itself: it called coverage a **gate** in four places and an **axis** in one. It is now an
axis everywhere, and the correction is stated in the direction our own measurement supports:

- **Figure 1**: *"Coverage is not a rung"* but one of the five novelty axes costed in §4.4, *"and not a
  monotone gate: its ordering fails on `boolean8`."*
- **Appendix procedure figure**: *"neither a cue level nor a universal gate"*; S1–S3 are representational
  invariances, coverage is a property of the train/test split, and it is **measured non-monotone** on
  `boolean8`.
- **§3.2's heading and the glossary**: *"and a Coverage **Axis**"*, `axis C`.
- **The abstract**: *"three cue levels S1–S3, with training-library coverage **a separate axis**"*.

The formal predicate name *coverage-gated* remains in Definition 1, because there it names a specific
screen: is the held-out form's rewrite outside the training library?, and that screen is what the
non-monotonicity is a fact *about*.

A gate that fails on `boolean8` was never a universal gate, and that failure is our own published result
(`the coverage-closure mechanism is polynomial-specific`), not a concession.

## 6. §16: provenance out of the conceptual foreground

Kept, moved. §4's opener keeps only the clause that is a real scope limit: inferential claims restricted
to the prespecified primary contrasts, everything else descriptive, and the tag-trail sentence is gone.
*"Released as `audit-symbolic-benchmark`"* moved from §3 to the statements section, outside the page
limit. **The 13 body `(tag rNN)` citations were deliberately kept**: you called the reproducibility story
excellent, and they are the audit trail, not decoration. What we removed is the *foregrounding*, not the
provenance.

## 7. §14: the untrained encoder on `boolean8` (`.698` over `.596`)

You concede family-relativity answers it; the paper's answer is sharper than that and is already in print.
**The untrained encoder fails the per-instance membership test, so it is an extension $\mathcal{X}$ and
not an $\mathcal{F}_3$ member at all**: the falsification corollary does not apply to it, which is why it
is reported outside the criterion at no cost. The positive counterpart is now in Figure 1: on the twin the
untrained encoder sits well below the trained encoder's `0.994`, and the appendix splits the `boolean8`
anomaly into a *readout* artifact there and a *proved* family property above it.

## 8. What we did not do

- **No new experiments**, per §25. Every number in this revision was already in the build.
- **No glossary for §18.** The notation load was concentrated in the deleted box: seven `\scriptsize`
  rows of $P$, $\mathcal{F}$, $\sup\mathcal{F}$, S1–S3 and gate C inside an unbreakable frame. Replacing
  it with a labelled chain that carries one symbol per node is the fix; a glossary would add lines.
- **No defence added for §13, §7 or §21–24.** The SCAN degenerate-ceiling disclosure and the code result
  are the §4.3 table you never saw. On §11's *"still too defensive"*: deleting the box and demoting the
  provenance **is** the de-escalation, and nothing was added to argue about it.

## 9. Gate state

`err 0` · `undef 0` · `0 Float too large` · **exactly 2** overfull boxes, both pre-existing (`6.4211pt`
vbox, `3.509pt` hbox) · **90 pages** · abstract ends p1 · **body ends p9** · p10's first body line is
`ETHICS STATEMENT`. All thirteen body headings and all four body floats on their pre-revision pages
(Fig 1 p3 · Table 1 p4 · Table 2 p5 · Fig 2 p8), with per-page geometry identical to the pre-revision
baseline on all eleven pages. `check_protected_claims.py` **PASS** (19 protected claims, 4 absences over
11 files, 3 document-wide over 15). `check_reviewer_map.py` **PASS** (16 rows, 272 checks, 43 run tags, 53
appendix letters). **Every one of the rebuilt figure's nine bar fractions was decoded back out of its TikZ
coordinates and checked against the number printed beside it**, with a positive control confirmed to fire
on a corrupted digit. `verify_claims.py` **exit 0 at 2304/2304 in all three code copies**. Pages 1–5 and
7–9 were read as rendered images, which is how three `\resizebox`'d TikZ collisions in the first build of
the new figure were caught; no text-level gate can see one.
