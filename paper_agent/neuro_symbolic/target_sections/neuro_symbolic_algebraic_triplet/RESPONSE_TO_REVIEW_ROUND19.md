# Response to review: round 19

**Summary: you listed five changes and named the condition for an 8. All five are in the paper, and
this round ran no experiments.** You wrote *"I would not reject this paper for lack of experiments
anymore… the remaining vulnerability is primarily conceptual"* and pre-refused the alternative
(*"Your answer should not be 'we added five more baselines'"*). We took that literally: **round 19 is
placement, naming and one table**, and the compute budget was zero.

**Main text is still exactly 9 pages** (`E THICS S TATEMENT` first on page 10), the verifier moves
**1928 → 1937** and `statements.tex` prints the new count, exit 0 in all three copies.

---

## Your #1: *"make the epistemological limitation the centerpiece"*. **Done, and as a numbered result.**

**A diagnosis first, because it changes what the fix had to be.** The argument you asked for was
already in the paper: §3.3's last paragraph read *"An exhaustive family would license certification,
and Proposition 3 says why it is not merely unbuilt but unreachable."* You read the paper closely
enough to cite it by section and still formed the objection. **That is a packaging failure, not a
missing argument**, so the fix was to give it a name and put it where the reader decides what the
paper claims.

**Proposition 4, *No admissible family certifies*, now opens §3.4** and the prose paragraph it came
from is deleted:

> Membership requires invariance to $P$, so $\mathcal{F}_t$ contains no explanation of $M(h)$ that
> *reads* $P$; and by Proposition 3 it cannot be extended to contain one without forfeiting the
> invariance that made its members evidential. Hence $M(h)>\sup\mathcal{F}_t$ rejects exactly the
> explanations $\mathcal{F}_t$ encodes and licenses nothing about the rest — for **every** admissible
> family, so **certification is unreachable by admissibility rather than merely unbuilt by us**.

**One deliberate difference from your formulation.** You proposed *"no **finite** control family can
certify"*. Finiteness turns out not to be the binding constraint, and the paper now says so: **an
infinite admissible family is bounded by the same argument**, because the obstruction is admissibility
itself. That is a sharper claim than the one asked for, and it is the one we can prove.

**We were careful not to overclaim.** The proof is in Appendix AN with a scope note in the style of
Proposition 5's: it bounds *comparator-based* evidence of the form Definition 1 defines. It is **not**
a claim that compositional reasoning is unmeasurable: mechanistic or interventional evidence is
simply not of this form, and **it does not excuse a small family**, since an audit's reach is exactly
what it enumerates. That is why §4.2 still stress-tests $\mathcal{F}_3$ rather than resting on the
proposition.

The sentence itself now opens the **conclusion**, in your words: *the framework issues a falsification
certificate relative to a declared control family, never a reasoning certificate.*

## Your #2: *"rename the positive result consistently"*. **Done; we were using two names.**

You are right, and worse than you knew: the paper carried **two** narrow names: *"compositional
interpolation within a learned transformation basis"* in the abstract and conclusion, and
*"composition-of-known-transformations generalization"* in §4.2. The first is retired. One name,
everywhere.

## Your #3: *"make the GIN twin result the central empirical figure"*. **Table 3, and the section moved.**

`experiments.tex` had **no float at all**. It now has the contrast you asked for, promoted from
Appendix AO rather than invented:

| \textsc{boolean8}, $K{=}190$, same weights | UnseenEqClass | shape-matched twin | verdict |
|---|---|---|---|
| *strongest non-learned* | $.596$ *upper bd.* | $.500$ *pinned* | — |
| Tree-LSTM | $\mathbf{.955}$ $[.925,.979]$ | $\mathbf{.934}{\pm}.015$ | clears both |
| **GIN** | $\mathbf{.881}$ $[.850,.909]$ | $\mathbf{.511}{\pm}.026$ | **clears S3, at *chance* on the twin** |
| Transformer | $.669$ $[.588,.746]$ | $.606{\pm}.061$ | clears neither |

**And it is no longer last.** The subsection moved ahead of the coverage section, so the experiments
now run audit → clearing every bag → **one encoder, two protocols** → coverage: your own Finding 1–5
order. Nine new verifier assertions pin every value the table prints, plus the verdict column as a
conjunction, so a rerun that promoted the GIN would break the table rather than agree with it.

## Your #4: *"make the three axes a major contribution"*. **Promoted to contribution (2).**

It was a bolded clause mid-paragraph. §1 now states it as a finding in its own right: **an unseen
arrangement of known primitives costs $+0.012$, unseen depth $+0.200$, an unseen primitive $+0.664$;
novel arrangement is far cheaper than novel inventory.**

## Your #5: *"trim the main-text density"*. **A whole table left the body.**

You wrote that the main paper *"risks making the central contribution look like an enormous audit
apparatus"*. **Table 1, *What running the audit changes* (the six-row ledger of every published claim
we revised) is exactly that apparatus, and it moved to Appendix F.** It was the paper's most
audit-log-shaped object, and demoting it is what paid for Table 3. Also cut: prose that Figure 1 and
Table 3 already display, the §3.3 contract paragraph, and Corollary 1 of the old numbering, folded
into a sentence.

## Your Figure 3 request: **answered inside Figure 1 instead, and here is why.**

You called the appendix procedure figure the clearest thing in the paper and asked for it as the
centerpiece. At 9 full pages the body cannot hold both. **But Figure 1 already *was* that procedure**:
its rungs chain S1 → S2 → S3 ⇢ gate C with real arrows, and was missing only the terminus. It now
ends in a bar reading **"only now interpret the learned score — and only against the family just
cleared"**, and the caption says to read it top to bottom as the audit procedure. You get the pipeline
in the main text without losing the three exemplar results the rungs carry. Figure 3 stays in the
appendix as the auditor's checklist.

---

## §9: *"coverage is no longer a universal explanation"*. **Scoped inside the claim sentence.**

Agreed, and the fix went where the claim is made rather than where it is qualified. Abstract and
conclusion now read *"…the dominant axis governing the observed transfer **in the polynomial
setting**"*. The `boolean8` non-monotone ladder is no longer an exception a reader meets three
paragraphs later.

## §13: *"the Lample–Charton experiment is over-weighted"*. **Demoted for the third time, and further.**

It occupied four sites; it keeps two. The **S2 verdict moved out of the centerpiece section into the
audit section**, reframed exactly as you put it: *evidence that operator content is readily
accessible in a trained representation, not a defect in that system*, and the abstract's parenthetical
is gone. **What we kept is the non-monotonicity replication**, folded into the centerpiece sentence,
because it is the only such replication on a model we did not train and Claim 2 rests on it.

## §12: *"architecture dependence is now a finding"*. **Promoted out of the caveats.**

The conclusion now reports it as a **second finding** rather than a limitation: composition's price
orders *strictly*, $+0.079$, $+0.258$, $+0.481$–$0.519$ for Tree-LSTM, GIN and Transformer, **no
replicate's interval touching another's**, so inductive bias decides which form of transfer emerges.

## §7: *"the theoretical contribution is weaker than the empirical"*. **Agreed, and the apparatus shrank.**

We did not argue with this. The old Corollary 1 was one clause of qualification standing as a numbered
environment; it is now a sentence. §3.3's contract paragraph is gone. Adding Proposition 4 leaves the
count of numbered environments unchanged at six, and the prose around them is shorter, and the one we
added is a **limitation**, not a novelty claim.

## §11: small class counts. **Disclosed, unchanged.**

You called this a generalization limitation rather than a soundness failure and noted we usually
disclose it. We do, and we have not tried to dress it up this round.

---

## Two things you read that we had written badly

Both are our fault, and both are fixed.

**You wrote *"2520 unseen primitive orders"***, as though 2520 orders were tested. Ours said *"each one
of 2520 orders"*, which invites it. The truth was already in Appendix AU and is now in the abstract and
§4.2: **188 distinct orders realised over the 200 classes, of 2520 possible.**

**You wrote *"25 seeds in many key experiments"***. That figure belongs to the external audit alone; the
sentence now binds it to that run.

---

## Reproducibility

No new experiments, so no new `REPRODUCE.md` row, no log to redact and no negative-control suite. The
verifier gains **nine assertions** pinning the values Table 3 promotes into the main text, moving
**1928 → 1937** (full run; `--quick` is 1933 and is *not* what `statements.tex` prints). Exit 0 in the
working tree and both shipped copies, `pyc: 0`, and `equivalence.py` untouched as always.
