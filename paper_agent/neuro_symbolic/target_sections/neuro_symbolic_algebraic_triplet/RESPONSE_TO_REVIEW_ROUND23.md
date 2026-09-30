# Response to the round-23 review

*Not part of the paper.*

**Summary of the round: no experiments, no new propositions, no page growth, and the one thing the
review named as the difference between 6 and 8 turned out to be four results the paper already had
and had buried in the appendix.**

---

## 0. First, the scorecard, because the Overall moved the wrong way

| | R22 | R23 | |
|---|---|---|---|
| Novelty / Originality | 8 | 7 | |
| **Technical correctness** | **7** | **8** | ← round 22's target |
| Empirical rigor | 8.5 | 8.5 | |
| **Experimental breadth** | — | **7** | *new axis* |
| Significance | 7.5 | 7 | |
| **Clarity** | **7** | **8** | ← round 22's target |
| Reproducibility | 9 | 9 | |
| **Overall** | **7** | **6** | |
| est. acceptance | ~70% | ~60–70% | *flat* |

We record this without using it as an excuse. **Both axes round 22 targeted rose by exactly one
point.** Generality (5.5) and Theoretical novelty (6), which bound round 21, are absent for the
second round running. The acceptance estimate is unchanged. A new axis entered at 7. **We therefore
reverted nothing from round 22** and treated the Overall as a different draw rather than as
evidence that the last round was wrong.

---

## 1. §19 #2 and §20: "one real external benchmark where the framework changes the conclusion"

**You are right that this is what the paper needed. You are also right that we had not shown you it
was already there.** The paper audits **four** already-published results produced by other people,
and every one of them was appendix-only:

| Audited | Verdict | Was in |
|---|---|---|
| AI Feynman held-out `0.972` | **broken**: a variable bag scores `1.000` | Table 10, App. F |
| Lample–Charton 80M integration encoder `0.872` | **S2 only**: op/arity bag `0.941` | Table 24, App. AR |
| `score_5` leaderboard, 14 SemVec corpora | **upheld** | Table 13, App. V |
| StructEmb ablation, 14 corpora | **narrowed**: an *untrained* encoder reaches it on 5 | Table 13, App. V |

The body's entire coverage was two clauses. And the table you asked us to build in §20 (
*"published interpretation → audit result"*) **already existed as Table 10**, whose own caption
said *"four of the seven are systems and leaderboards built by other people; the audit revises in
both directions."*

**What we changed.** Table 2 in the body is now that ledger: column 1 heads `Result audited`,
column 3 `What the audit licenses`, and the top block names **four external systems with their
numbers**, above the block of verdicts that go against us. §4.1 states the Lample–Charton audit with
its numbers: a released 80M-parameter encoder at `0.872` `[.847,.913]` against a **zero-parameter**
operator/arity bag at `0.941` `[.926,.969]`, one protocol and one set of splits for every row. The
abstract says four of the audited results are other people's.

**We ran no new experiments.** You said not to, and nothing here required any.

### An honesty problem we had to fix before promoting anything

Table 10 called the Lample–Charton result **`broken`**. Appendix AR says the opposite in as many
words: *"It would be wrong to read this as a defect in their benchmark… an operator bag is not
exploiting a flaw — it is reading the label."* **Promoting that row unchanged would have shipped an
overclaim about a system we did not build.** Both the body row and Table 10 now read **`S2 only`**,
and §4.1 gives AR's reading: the four family labels are *defined* by which operators appear, so
this is **an S2 task correctly identified**, and its numbers are evidence of operator-inventory
sensitivity and of nothing above it. That is the framework's contribution here: the *entitlement*,
not a defect claim.

### And a count error in our own paper, which we found doing this

`introduction.tex` sold Table 10 as *"revise five of our own claims."* The table is **four external
rows and three of ours**. The sentence was both wrong against the table it cited and actively
hiding the half you said was missing. It now reads *"seven already-published results — four of them
systems and leaderboards built by other people — in both directions — and three of them ours."*
Related Work carried the same error and is fixed with it.

**For the record: this is the seventh time in this paper's revision history that a result existing
only in the appendix has functioned as a result that does not exist, and it is the costliest.**

---

## 2. §19 #1: non-monotone admissible control strength as the novelty centerpiece

§4.2 already called the inversion *"the paper's centerpiece."* What it had never said in the body is
that **it replicates on a corpus and a model built by other people, with trees deeper than any of
ours**: `φ_d` *falls* `0.752 → 0.726` as `d` rises, `WL_h` `0.818 → 0.776` as `h` rises, and `φ_∞`
sits at the family's floor (Appendix AR, tag `r90`).

That was measured in round 21 and **already asserted** by `verify_claims.py`, including
`"r90: phi_d is non-increasing in d"` and `"r90: the F_3 supremum is attained at a COARSE member"`.
It is now in §4.2, and the conclusion's consequence (2) reads *"the strongest admissible control is
the coarsest, on five class partitions and on a published 80M-parameter encoder's corpus."*

So the two questions a cold reader of the abstract, intro, both figures, Table 2 and the conclusion
must be able to answer (*does a real published external system get audited here?* and *does the
non-monotone result hold outside the authors' own corpora?*) are now both answerable **without
opening the appendix**. We check this by extracting exactly those elements from the built PDF and
reading them cold; it is the only gate we have that catches this class of failure.

---

## 3. §19 #3 and §12: a construction rule, and the temporal ordering

**§21 says do not add more propositions. We added none.**

§3.3 now says what was already true: **Definition 1 *is* the construction rule**, every
representation determined by the cues at levels `≤t` alone, and `F_3`'s enumeration is *"what we
could build under it rather than its boundary — a reader can admit a candidate we never considered
by running the same test."* The test is concrete and already run: a candidate enters only by scoring
exactly `0.500` on the twin, per instance. Five descriptors a reviewer named entered that way and
three refinements failed it.

**On §12, we claim only what is recorded.** §4.2 now says: every member's number is reported rather
than the best; the supremum lands on the **coarsest** member, which is the opposite of what choosing
a winner produces; and the widening that stress-tested the family was specified by a reviewer who
had already seen our results. **We did not write a preregistration claim**, because the logs and
history do not record one, and a false sentence there would be worse than a missing one.

---

## 4. §9: "no admissible family can do better"

Agreed that this over-reached as written; it could be read as *no conceivable control can ever be
stronger evidence*. The abstract now reads **"no admissible family can turn the audit into a
certificate: membership *requires* invariance to the very property a certificate would have to
detect"**, which binds the claim to certification, where Proposition 4 actually applies.

---

## 5. §22: the title

Changed: ***Beyond the Strongest Baseline: Auditing Structural Claims in Neuro-Symbolic
Benchmarks***. The paper already said "audit" everywhere: *passes the `F_3` audit*, "the auditor",
the released `audit-symbolic-benchmark`, so `Falsifying` was the outlier, and we agree it promised
something about our action rather than describing it.

---

## 6. Two places the review pulls against itself

We are flagging these rather than silently picking a side.

**§10 vs §17: the code port.** §10 asks that the Type-2 clone result be made less prominent. §17
introduces **Experimental breadth at 7/10** for domain concentration, and the code port is the
paper's *only* non-symbolic evidence. **We shortened it in both the abstract and §4.1 and did not
delete it**, keeping the `96%` and the *"a constructed corpus, not a published benchmark"* scope, so
it reads as evidence the auditor **ports** and not as a prevalence claim. Deleting it would have
answered §10 by worsening your newest axis.

**§13 vs round 22's review: the GIN paragraph.** §13 asks that the GIN details be demoted. Round
22's review *required* the irreproducibility disclosure, and the protocol-disagreement result is the
paper's third contribution, named in the abstract and the conclusion. §4.3 now **leads with the
protocol claim** (*"the protocol, not the model, decides what is concluded — GIN is where we caught
that, not what it rests on"*) with GIN billed as the instance. Round 22's disclosure sentence is
intact **including both drift numbers**: the per-seed `0.065`, not just the `0.013` five-seed mean,
because quoting only the mean would flatter the argument fivefold.

---

## 7. A verifier gap our own tooling found, and we closed

`check_tex_numbers.py` exists because `verify_claims.py` never reads the `.tex`. Run over every
block this round touched, it reported that **`0.932` and `0.312` (the shared-variable-pool pair
§4.1 prints) appear in no assertion.** Nor did Appendix AF's interval `[0.184, 0.460]`, its
skyline `0.140`, or its residual gap `+0.172` `[0.044, 0.300]`. **The entire `r61`
operator-scrambling result had zero assertions**, while the Reproducibility Statement claims every
quantitative claim in the paper is mechanically traceable to a log.

Eleven assertions now cover it, including that renaming **preserves** the score (which is what §4.1
claims of it), that scrambling **collapses** it, and that the residual interval **excludes zero**
(which is what makes it a residual rather than noise). **2060 → 2071**; `statements.tex` prints
2071; all three shipped copies exit `0`.

---

## 8. What we did *not* do

- **No new experiments** (§20's ask was a presentation of results already run and already asserted).
- **No new propositions** (§21).
- **No new float**, and **no page growth**: the body had ended on the *last* of page 9's 54 line
  slots, so all fourteen rendered lines this round spent had to be recovered from restatements the
  promotions themselves created. The largest single recovery: the conclusion's opening sentence had
  become a **verbatim third statement** of the scope sentence already carried by the abstract and by
  §3.3's box, and since that box says *"stated once, precisely"*, deleting the third instance made
  the box's claim true.
- **No claim of a preregistration** we cannot evidence (§12).
- **No reversal of round 22.**

## 9. Gate state

0 LaTeX errors · 0 unresolved references · 0 `Float too large` · exactly 2 overfull boxes, both
pre-existing (`6.4211pt` vbox, `3.509pt` hbox) · 1 warning, the standing `TS1/ptm/m/sc` font
warning · **76 pages, unchanged** · body ends page 9, page 10 opens with the Ethics Statement ·
`verify_claims.py` exit `0` at **2071/2071** in all three copies · both main-text figures rendered
and inspected, since text gates cannot see TikZ collisions.
