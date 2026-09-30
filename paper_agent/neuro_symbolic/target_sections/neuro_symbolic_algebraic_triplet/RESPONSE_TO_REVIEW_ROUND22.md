# Response to review: round 22

**Summary: round 21 worked, and you told us what the last point costs. Generality `5.5` and Theoretical
novelty `6` (the two axes that bound the paper last round) are gone from your scorecard, Novelty went
`7 → 8`, and you endorse the rebilling we made under protest (*"I think that's the correct stance"*).
The only score that fell is Technical correctness, `8.5 → 7`, and every instance you name under it is a
place where our **wording** outran our evidence, not a place where the evidence is wrong.** So this
round costs **zero GPU-hours**, exactly as you asked (*"Do not add another 5–10 datasets… The bottleneck
isn't empirical quantity anymore"*).

We took your path to 8 literally:

> *"If you can make the admissibility → family supremum → non-monotone control strength story absolutely
> unmistakable in the first 2 pages, I think you have a realistic path to 8/10 territory."*

**That chain is now the second half of §1 ¶1, in plain words, before any notation**, and it was moved
there rather than added, out of the Contributions paragraph where it had been sitting in jargon-first
form (*"$M(\phi_d)$ is measured non-monotone in $d$"*). Five claims were downgraded to what was actually
measured. `verify_claims.py` moves `2056 → 2060`, exit 0 in all three copies (`--quick` is `2056`, as
always exactly four lower). **Main text is still 9 pages**, `E THICS S TATEMENT` first on page 10.

**On the framing question.** Round 21's response says in writing *"We are not spending a third round on
framing."* This is a fourth. We are doing it because your ask is narrow and named (the chain is not in
the first two pages, and you say which three links and in which order), rather than open-ended, and
because you paired it with an explicit instruction not to run anything. That is a different request from
rounds 19 and 20, and we are saying so rather than pretending the earlier sentence was not written.

---

## Three of your asks were already satisfied. We are saying which, rather than claiming credit

We checked each against the sources before editing. Three needed nothing:

1. **Priority 3, "composition-of-known-transformations" throughout.** Already the paper's term
   (`abstract.tex`, §4.2). The only unqualified *"compositional generalization"* in the paper is in the
   abstract, in scare quotes, as the thing we explicitly **do not** claim.
2. **§3's "23 corpus configurations… including 15 EQNET variants."** Already verbatim in §1 and §4.1. It
   was missing only from the abstract and conclusion, which now say *"23 corpus configurations spanning
   four benchmark families"*.
3. **Priority 2's formulation.** The sentence you asked for already existed in §3.3's box. What was wrong
   is that **four differently-worded variants of it were in circulation**, so it did not read as one
   recurring principle. It is now one sentence, used in the abstract, §3.3's box and the conclusion:

   > **Passing the audit means only that the declared family of alternative explanations has been ruled
   > out under the stated protocol; it does not certify reasoning or compositionality.**

   We also **deleted** the fourth instance, which sat twenty lines below the box in §3.4. "Stated once,
   precisely" is now true.

---

## Technical correctness: the saturation overclaim was ours, and it lived in one sentence

You quote:

> *"the family provably saturates — it reaches the complete structural fingerprint, so no finer
> admissible member exists to have been missed"*

**That is the abstract, and it is nowhere else.** §3.2 and §4.2 already state it narrowly and correctly
(bag equality asserted against $\phi_8$; poly8's maximum tree depth is 4). So the paper contained a
correct statement of the result and an overclaimed advertisement for it, and you read the
advertisement, which is the right thing to hold us to. It now reads:

> **the family saturates** at the complete order-blind fingerprint of the tree representation, **and that
> finest member is its weakest**

Round 21's own plan listed *"saturation must not be overclaimed"* as a risk. The abstract is where it
leaked, and we did not catch it.

The other four downgrades:

| Where | Was | Now |
|---|---|---|
| §4.2 | Proposition 5 cited as licensing the inversion | *"measured; Proposition 5 **explains** it under our feature-support retrieval protocol rather than licensing it"* |
| §3.4 | Round 21 rebilled Proposition 4 only | **all** of §3's propositions billed as *"scoping and formal machinery, not theoretical contributions"* |
| abstract, conclusion | *"Across 23 corpora"* | *"23 corpus configurations spanning four benchmark families"* |
| abstract ¶1 | the AI Feynman clause led with the `84%` mechanism | leads with `1.000` against `0.972` and says why the better predictor is worthless evidence |

---

## §15: your proposed sentence is false about this paper, and the true one is stronger

You propose adding:

> *"All quantitative conclusions requiring architectural comparisons rely only on Tree-LSTM;
> GIN/Transformer results are descriptive."*

**We cannot add that, because the protocol-disagreement result is a GIN claim, and it is in the abstract,
§4.3 and the conclusion.** One set of trained GIN weights reads as clearing S3 under one protocol
(`.881 [.850,.909]` on UnseenEqClass, against a strongest-non-learned bound of `.596`) and as at chance
under the other (`.511 ± .026` on the shape-matched twin). Pasting your sentence would make the paper
contradict its own third contribution.

The honest version is stronger, and §4.3 now says it in the body:

> **Neither GIN number is reproducible and the finding does not need them to be**: GIN training here is
> not run-to-run reproducible on MPS and these runs are not separately replicated, but the largest GIN
> drift ever *measured* in this harness is `0.013` in a five-seed mean and `0.065` per seed (Appendix AJ)
> against a **`0.370`** disagreement whose intervals are disjoint — which is why every architecture
> comparison here is claimed as an *ordering*.

Two things we want to be explicit about, because both were nearly written wrongly:

- **The envelope is borrowed, and the paper says so.** `0.013`/`0.065` are measured on **poly8** (Appendix
  AJ, two identical invocations per architecture). The `boolean8` runs the `.881`/`.511` numbers come from
  have **no replicate of their own**. An earlier draft of this sentence quoted a `±0.03` envelope and a
  "roughly 12×" factor; both would have been an extrapolation across corpora, so the sentence now cites
  the largest drift measured *anywhere* in the harness and states that these runs are not separately
  replicated.
- **The per-seed number is the one that binds.** Quoting only the `0.013` five-seed mean would have
  flattered the argument by a factor of five. The body prints both.

**On the disclosure being new: it is not, and we were wrong about that internally.** §4.1 already said
*"Neither the GIN nor the Transformer trains reproducibly here, so no claim rests on their point
values."* What was missing is that this sat in §4.1 about `poly8`, without a magnitude, while the
load-bearing GIN claim is in §4.3 about `boolean8`. The gap was **the magnitude next to the claim**, not
the fact of irreproducibility.

**New assertions (`2056 → 2060`).** The gap is **recomputed** from both logs rather than quoted (
`0.8807` (r86b unseen) − `0.5110` (r85 twin)), because a gap is the one quantity that survives a change
in either arm; the per-seed drift it is compared against is asserted separately; the comparison is
asserted as the inequality; and the interval disjointness is asserted as `unseen lower > twin mean + 2sd`
rather than as two numbers that happen to sit apart, so a rerun that widened either arm into overlap must
**fail**. Both operands are indexed directly: a `.get()` here would turn a renamed key into a silent
skip.

---

## Figure 1 (§16, "what should I remember?")

The header line is now the question the figure answers, rather than a description of the figure:

> *"What a held-out-form score actually tells you: each level, and the result that settles it"*
> → **"Can a non-learned control that is *blind* to the claimed property explain the score?"**

The ladder is unchanged: the columns clear by about 0.2 cm and the `\resizebox` hides collisions from
every text-based check, so it was re-rendered and looked at rather than only rebuilt.

**Where Figure 1 sits.** It is at the top of page 3, not within the first two pages. Page 2 has seven
unused line slots and the float needs about fourteen, so moving it up would push seven lines past the
nine-page limit. §1 ¶1 is therefore written to carry the chain **without** the figure: it states all three
links in prose and ends with the one-sentence takeaway you asked for.

---

## What paid for it, since the paper was already full

Round 22 added about ten rendered lines and had roughly one to spend. The funding, in the order we found
it, and the useful part is that **hoisting the chain into ¶1 made four other passages redundant**, which
is what made the round affordable:

- **Figure 1's caption** closed with *"Because refinement destroys invariance, levels must be coarsenings
  and S3 is audited by the supremum over a family; $M(\phi_d)$ is measured non-monotone in $d$"*, which
  is now, verbatim, the chain in ¶1. Deleted. **This was the single largest recovery, and it is the only
  one that moved more than a line.** Two further caption clauses restated what the figure prints
  (*fails/fails/clears*, and gate C's own subtitle).
- **§1 ¶4's** restatement of the chain became a pointer, and its novelty-cost triple
  (`+0.012`/`+0.200`/`+0.664`) now points at Figure 2 instead of reprinting numbers that appear in the
  abstract, in Figure 2's caption and in §4.2 with intervals.
- **§2 ¶3** restated Table 1's own caption and §1 ¶4's opening sentence; it is now the two float pointers
  it was structurally load-bearing for.
- **§3.4's opening** repeated the boxed formulation twenty lines below the box.
- **The conclusion** lost a third instance of *"which is what makes the choice of control a scientific
  question"* and had its scope list compressed; all three scopes kept.

**Nothing scope-bearing was cut.** We have unscoped a claim this way before by deleting a caveat that
looked repeated, so only exact restatements went, and every deletion was checked for orphaned
cross-references (`prop:ceiling` keeps five, `tab:novelty` and `tab:audit_changes` keep one each in §1).

**Gates.** 9-page body, `E THICS S TATEMENT` first on page 10, 76 pages, 0 errors, 0 unresolved
references, 0 `Float too large`, 2 overfull boxes (both pre-existing: a `6.4211pt` vbox and a `3.509pt`
hbox), 1 standing `TS1/ptm/m/sc` font warning. `verify_claims.py` `2060/2060`, exit 0 in all three
copies.

---

## What we did not do

- **No new corpora, no new runs.** You asked us not to, and nothing in the round needed one.
- **We did not restructure Figure 1**, and did not narrow its columns.
- **We did not add a fifth instance of the falsification formulation.** Priority 2 was satisfied by
  deleting one and unifying three, not by repeating it more prominently: the paper has been penalised
  for restatement density before, and that is the same complaint as your Clarity score.
