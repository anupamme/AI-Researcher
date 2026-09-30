# Response to the round-26 review

*Not part of the paper.*

**Summary: no new experiments, as you advised, but this is not a presentation round. Preparing it,
we found that Appendix I was still reporting a result our own run index had already recorded as
superseded, and that the correct control makes it a null. We have withdrawn it, in the paper, in
both ledgers, in Table 1 and in the body. The assertion count therefore moves for the first time in
six rounds: 2071 → 2090.** Separately, your Priority 1 is implemented as you framed it: the method
now has a name and its three-point differentiator is on page 2 instead of page 6.

---

## 0. The scorecard, and the axis that decides the paper

| Criterion | R24 | R25 | **R26** |
|---|---|---|---|
| Technical soundness | 7 | 8 | **8** |
| **Novelty** | 7 | 7 | **7 ← binding** |
| Significance | 7 | 8 | **7.5** |
| Experimental rigor | 7 | 8 | **8.5** |
| Clarity | 6 | 7.5 | **7.5** |
| Reproducibility | 9 | 9 | **9** |
| **Overall** | **6** | **7** | **7** |

We take your bottom line literally: *"The remaining obstacle to an 8/10 is not 'more experiments.'
It is making the reviewer believe that admissibility + family-level ceilings + falsification
certificates constitute a genuinely new evaluation methodology, rather than a careful repackaging of
existing shortcut/control-task methodology."* So this round spent zero GPU-hours, and everything
below is either that argument or a correction.

---

## 1. The correction: a portability claim of ours, withdrawn

You single out as the submission's strongest aspect that *"the authors explicitly report cases where
earlier numbers in their own work were wrong and were withdrawn."* Here is a fresh one, found
between rounds, by us.

**What the paper said.** Appendix I reported that on NeSymReS (a published 10M-parameter
Set-Transformer we did not train) the audit found notational sensitivity: plain `0.624` against
column-permuted `0.392`, `ℓ′ = 0.44`, `t = 7.25`, `p < 10⁻⁶`, `d = 1.45`.

**Why that was wrong.** That control (`r28`) permuted **the held-out sets alone**, which breaks the
correspondence between the training centroids and the held-out queries. The drop measures the
control, not the encoder. The correct control applies **one global column permutation to every
centroid sample and every held-out sample**: the permuted corpus is then *isomorphic* to the
original, so a function-level encoder **must** be invariant, and any drop is spurious.

**What the correct control gives (`r62`).** `0.624 → 0.648`, `Δ = +0.024 [−0.036, 0.084]`, 25 seeds,
10 equations, chance `0.10`. **A null, and the point estimate is the wrong sign for a shortcut.**

**Where the failure lived, which is the part worth reporting.** `r62` was run, logged and recorded
in the paper's own run index as superseding `r28`: *"its control permuted held-out sets only"*, and
Appendix I's prose, **100 lines away in the same file**, never mentioned it. And nothing caught the
mismatch because **`verify_claims.py` had zero NeSymReS assertions**, in all three copies. That is
the round-23 gap in a worse place: round 23's unasserted result was a *correct* one, this was a
*withdrawn* one.

**What we changed.**

1. **Appendix I** reports `r62` as the live result, under a protocol paragraph that now states that
   two controls are possible and **they are not equivalent**, and why. It carries a paragraph
   *Withdrawn: the held-out-only arm (tag `r28`)* that retracts the arm and every statement resting
   on it, and notes that `r28`'s **plain** `0.624` reproduces **exactly** under `r62`, which is what
   localises the fault to the control arm rather than to the measurement.
2. **The firewall is intact.** That section already said the result *"is not evidence for the
   leakage claim"*; it now adds *"and under the correct control it is a null."* No result in the main
   text ever rested on it.
3. **The interpretive caveat now cuts the other way, and is stronger for it**: under a permutation
   that preserves the isomorphism, invariance is the *correct* behaviour, so the null is the expected
   result rather than a disappointing one.
4. **Appendix M's scale argument no longer leans on it.** It said the diagnostic *"detects
   sensitivity (ℓ′ = 0.44)"* in a 10M model. It now says the audit establishes that the diagnostic
   **ports** to such a model and **nothing** about whether leakage survives scale, and that the
   paragraph's conclusion rests on the fixed-diversity curve and the hardened recipe alone.
5. **Table 1** gains an against-us row: *Our NeSymReS portability claim · S1 · **withdrawn**: null
   under a global permutation.*
6. **Both appendix ledgers were recounted**: *What running the audit changes* is now **eight** rows
   (four other people's, four ours) and the revision-incident table is **seven** incidents, the new
   row naming how it was found. §1 and §2 follow: **eight** published results revised, **four of them
   ours**.
7. **The Ethics Statement's count is reconciled**; it said the audit changed *five* claims of our
   own while §1 said *three of them ours*, with nothing explaining the difference. It now reads
   *"**six** claims of our own — the four already-published numbers among them are the *Our…* rows of
   Table 10, and the other two are protocol-level"*, with the withdrawal as the sixth.

**The assertion count moves, 2071 → 2090, and we are flagging it rather than letting it look like
drift.** The 19 new assertions cover both arms: `r62`'s three means and intervals; the delta
recomputed **paired per seed** from the two 25-seed arrays, and its mean recomputed from those pairs;
that **all 25 permutations are non-identity**, because a guard that cannot fire proves nothing; the
log's `supersedes_control_in == "r28"`; and `r28`'s withdrawn `0.392` and `ℓ′ = 0.4427` beside its
**identical** plain mean, so the two controls' disagreement is itself asserted. A missing log fails
the verifier rather than being skipped.

---

## 2. Priority 1, implemented as you framed it: a named method, differentiated on page 2

**The method had no name.** The paper had *admissible-control ceiling* and *passes the F₃ audit*, but
nothing naming the method as a whole, which is exactly why it can read as good practice formalized
rather than as a framework. We have adopted your word. It is **admissibility auditing**, in the
abstract's second paragraph, in §1's contribution (1) and once in §3.5, at a cost of **−1 word** of
abstract (`449 → 448` source words).

**Your three-point differentiator was in the paper: on page 6.** §3.5 already carried it as
(i)/(ii)/(iii) with the same content. It is now the **opening of §1's contributions paragraph**,
stated against both foils and with the evidence attached to each point:

> **Unlike a shortcut baseline or a control task:** **(i)** admissibility is a *test* a comparator
> must pass, run per instance, not a judgement of its strength — five structural descriptors we did
> not choose were admitted that way and three refinements failed; **(ii)** the statistic is that
> family's *ceiling*, never a selected strongest baseline, because refining a control either
> preserves its invariance or forfeits its membership; **(iii)** the output is falsification of the
> alternatives the family names, never certification, which no wider family can change.

§3.5's copy is now one sentence (*"§1's three differences are each **measured** here, not argued"*),
which is what paid for the addition, since the paper is at a hard 9-page body limit with zero slack.

---

## 3. Priority 2: the three external validations, and the third modality in the body

You are right that the paper already had them and that they were not visible. Measured before the
edit: Lample--Charton was the fifth and sixth sentences of one dense §4.1 paragraph, the Python
Type-2 clone corpus was the last clause of that same paragraph, and **NeSymReS was body-absent**
except as a citation. §4.1 now carries a labelled paragraph (*Three input modalities, two encoders
we did not build*) that names all three, and its NeSymReS clause is the honest one:

> **And where the same protocol runs on *numerical point-sets* — NeSymReS's published 10M
> Set-Transformer — it returns a *null*** under a global column permutation (`+0.024`
> `[−0.036, 0.084]`, 25 seeds), **withdrawing a portability claim of our own** that an earlier,
> weaker control had scored as a drop.

What that establishes is **portability of the machinery, not prevalence of leakage**, and the paper
says so in the same breath. It is also the version that survives your own §9 caveat about column
identity carrying legitimate semantics.

---

## 4. Your §11: why `K ≥ 200`

The answer was in the appendix and it is **not statistical power**. §4.2 now says so in the body: at
`K = 50` the admissible family genuinely **exceeds** the encoder's lower bound, **under the widened
family as well as the published one**, so the small-`K` overlap is a measured effect rather than
wide intervals.

## 5. Your §16: the unit of analysis

`66`–`100%` now reads **of class *pairs*** in §1 as well as in the abstract and the conclusion, so
the unit travels with the statistic everywhere it appears.

---

## 6. Three things we are declining, in print

- **The title stays.** *Beyond the Strongest Baseline* is the opening line of both the abstract and
  §1, and three reviewers have praised it. We accept the consequence you imply: the novelty case then
  has to be won in the first two pages' text, which is what §2 above is.
- **§12's ask (make the Tree-LSTM the primary vehicle) is already satisfied**, and we would rather
  point at the sentences than add a fourth. §4.3's takeaway opens *"GIN is where we caught that, not
  what it rests on"*; §4.2 says *"no claim rests on their point values"*; §4.3 says *"every
  architecture comparison here is claimed as an **ordering**."* We note that **round 22 asserted the
  opposite about the same passages** (that comparisons rely *only* on the Tree-LSTM), which is why
  we now quote locations rather than rewrite.
- **The appendix is not restructured** (your §15). Re-lettering breaks the `\applabel` letters cited
  from the body, and we measured in round 21 that splitting it into a second PDF orphans 21
  references. The four-part reading map at the head of the appendix, added in round 25, is our
  answer.

---

## 7. Two defects no automated gate could have caught

Recorded because they are the same class of failure twice, and the fix is a gate that is a person
reading the built page.

- **A reference that pointed at the wrong appendix, latent for ten rounds.** Appendix I's label was a
  bare `\label`, so it inherited the enclosing section's counter and the new table cell rendered
  *"Withdrawn (**F**)"*: Reproducibility Details instead of Appendix I. Zero undefined references;
  no warning. Every other citation of that section is textual, which is why it had never surfaced.
- **A subject--verb disagreement introduced by the renaming**, in the abstract: *"Admissibility
  auditing therefore evaluates… and score it."* Every gate passed it.

And one our own tooling caught in text we had just written: `check_tex_numbers.py` flagged that the
`ℓ′ = 0.44 [0.36, 0.51]` interval and the `± 0.086` we quoted into the withdrawal sentence **are in
no log**. We deleted them rather than loosening the check.

---

## 8. Gate state

0 LaTeX errors · 0 unresolved references · 0 `Float too large` · exactly 2 overfull boxes, both
pre-existing · **79 pages, up from 76: every added page is appendix** · abstract ends page 1, body
ends page 9, page 10 opens with the Ethics Statement · `verify_claims.py` exit `0` at **2090/2090 in
all three copies** · `check_tex_numbers.py` clean on the rewritten Appendix I, the new incident row
and the Ethics paragraph.

**Still deferred, and named as such:** independent-domain evidence, a real external benchmark in a
non-symbolic domain. If Novelty stays at 7 after a named method with a page-2 differentiator, that is
the next thing we run, not a fourth reframing.
