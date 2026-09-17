# Response to Reviewer (7/10, Accept, confidence 4/5)

*On `main(20260910-132832).pdf`. Sub-scores: problem importance 8.5, originality 7.5, technical
correctness 8, empirical rigor 9, reproducibility 9.5, clarity 7.5, significance 8, overall 7.*

Thank you. Your two terminology objections were right, and one of them found a defect we had not seen: the
same overstatement appeared at four sites, and two of our own tables contradicted each other about it. We
have fixed all four. Both fixes are below, along with an answer to every numbered weakness.

**One thing we have to say first, because it changes how to read the rest.** The build you read predates
almost all of the revision history. `main(20260910-132832).pdf` is earlier than commit `0f192ea`
(2026-09-11), and therefore earlier than every one of these:

| Commit | Date | What it did |
|---|---|---|
| `1a8cecb` | 09-11 | round 15 (framing) |
| **`1752912`** | **09-11** | **reframed the paper as an identification audit; added the evidence ladder** |
| `f50b19e` | 09-11 | round 17 |
| `7f64737` | 09-11 | audited four adjacent constructs against requirements (i)–(v) |
| `d80cfb7`, `c862a11` | 09-14/16 | EXP-C4B, the blinded replication |
| `b418fae` | 09-16 | model-vintage documentation |
| `1cec740`, `f872444` | 09-16 | rounds 21–22 |
| `f0418a4`, `a6ab290` | 09-16 | round 23 text edits, incl. the current title |
| `617afe2`, `999ff78` | 09-17 | EXP-R1d |

We say this not to deflect the review but because **your recommendations B, C, D and E, and weaknesses #4,
#5/#10, #7, #12 and #13, are already implemented in the current build**, several of them by `1752912` —
which is the commit that does the reframing your framing recommendations ask for. Rather than claim credit
for edits we did not make this round, we quote the existing text below with file references so you can
check it. **The current build is 78 pages (9 of main text) and we would be grateful if you would re-read
it**; on the copy you have, your review is accurate and our response would be almost entirely "agreed".

**Two things that landed after your build make the paper weaker, not stronger**, and you should see them:
EXP-C4B, a pre-registered blinded replication, is positive on only **1 of 5 new targets** (`§3.5`); and
EXP-R1d, a recency check on four current-generation models, is **inconclusive** — three targets void on a
pre-registered probe-channel gate, one admissible target falling 46.0 pp (`Appendix R1d`). Neither was in
the PDF you read. Both are reported at full strength.

---

## A1 — "Rules out instruction-following" (your weakness #2). Agreed, and it was worse than you saw

**What you observed.** Equalization cannot rule out instruction-following, because the neutral prompt is
still an instruction. What it rules out is the asymmetric deception-instruction explanation.

**You were right, and the error was inconsistent as well as wrong.** Three tables in the paper name what
criterion 1 tests, and only one of them was loose:

- `tab:roadmap` (§1, p3) already asked *"Does it survive removing the instruction **asymmetry**?"* ✓
- `tab:criteria_taxonomy` (Appendix A) already said *"Whether accuracy depends on the instruction
  **asymmetry**"* ✓
- `tab:criteria` (§2.2, p5) said **"Rules out *instruction-following*"** ✗

So the main text's own criterion table disagreed with the main text's own roadmap table. Two further sites
carried the same imprecision: `fig:ladder`'s rung 2 was labelled *"Instruction-independent signal"* — at
the site that *defines* the rung — and Appendix A's closing sentence licensed the statement that a signal
is *"instruction-independent and robust"*.

**What we changed (four sites).**

| Site | Now reads |
|---|---|
| `tab:criteria` row 1 (p5) | Rules out *instruction asymmetry* |
| `fig:ladder` rung 2 (p5) | **2. Asymmetry-independent** signal |
| Appendix A, closing sentence | …licenses the statement that a signal is *independent of the instruction asymmetry* and robust |
| Appendix A, new paragraph | see below |

Both main-text edits are deliberately **length-neutral or shorter** (31 vs 30 and 30 vs 32 visible
characters), because the main text is at a hard 9-page limit with zero slack and `tab:criteria` is a pinned
float. That is also why we did not put your fuller wording — *"rules out the asymmetric
deception-instruction explanation"* — into the table cell. We put it in the appendix instead, where there
is room to state it properly:

> **What criterion 1 rules out, stated precisely.** Equalization removes the *asymmetry* between the two
> conditions' prompts; it does not remove the instruction. Both conditions remain instructed, and
> following the neutral instruction is itself instruction-following. So what a fall to chance rules out is
> the explanation that the detector was reading the **deception-instruction asymmetry** — **not
> instruction-following as such**, which no prompt-level intervention can remove. This is why Table 2
> records criterion 1 as ruling out *instruction asymmetry*, and why, where the main text names
> instruction-following, it names a *pathway* that equalization leaves in place rather than one the design
> eliminates.

**What we deliberately did not do.** We did not replace "instruction-following" throughout. It appears in
nine other places — the abstract's *"separate a detector response mediated by deception from one mediated
by instruction-following"*, §2.1's corollary, §3.4, `related_work`, and the "Does not establish" box — and
in every one of them it correctly names a **rival pathway**. Your objection was to the verb *rules out*,
not to the term, and a blanket substitution would have destroyed the sentences that state the confound.

## A2 / #3 — "bounds surface behavior" should be a demonstrated lower bound. Agreed

**What you observed.** The 69–80% lexical-rule result is a demonstrated lower bound on surface-accessible
accuracy, not an upper bound on anything, and "bounds" invites the wrong reading.

**Where the paper was already right, and the one place it was not.** The main text never claimed an upper
bound: the abstract says the accuracy is *"reachable with no learned features at all"* and calls the figure
*"surface-accessible accuracy, not a decomposition of the detector's signal"*; `tab:criteria` row 3 says
*"Shows how much is reachable from surface form"*; `tab:roadmap` says *"Reachable without learned
deception-specific features"*; disclaimer (3) says a rule *reaching* benchmark accuracy *"shows what is
surface-reachable without decomposing the detector's signal"*; and §3.3 already states *"we quote the
**range**, not its upper end"*.

But one appendix sentence — the pattern-sensitivity analysis — said the baseline should be read as
**"bounding the benchmark at 69–80%"**, and a second appendix site said to read the figure *"rather than as
a bound"*. Those two contradict each other, and the first is exactly the misreading you flagged. Now:

> The baseline should therefore be read as a **demonstrated lower bound on surface-accessible
> accuracy** — 69–80% depending on pattern choice — and **not as a bound on the benchmark**, nor as a
> single value. A rule that *reaches* 69–80% shows that at least that much of the reported accuracy needs
> no learned deception-specific features; it says nothing about how much of the detector's signal is
> surface form, and it is not a ceiling on anything.

The second site now reads *"inventory-dependent rather than as a bound **on the benchmark**"*, so the two
agree.

---

## Recommendations already in the current build

**B — make the contribution explicitly empirical, early.** `§1 ¶1` (p2):

> **What is new**, given prior work that already reports poor generalization and already builds
> fixed-elicitation, belief-verified settings: not a causal-identification theorem, but that the standard
> instructed benchmark is *structurally non-identifying*, that this is operationalizable as an audit
> protocol applicable to a benchmark one did not build, and that the failure is *empirically active*
> across three detector paradigms and both public releases.

and the contribution paragraph closes on *"the protocol and the audit, not the algebra, are what is new"*.

**C — put the falsifier in the main text as a boxed statement.** It is a boxed statement, in §1 on p3:

> **This is falsifiable, and we say how**: a single public corpus supplying (i)–(v) in which a detector
> separates deception would overturn claim (3). We ran that test on materials we built, and report where it
> fires and where it does not.

**D — make the external audit more prominent.** It carries the abstract's second half (nine of ten rollout
sets, the +84.3 pp annotation-channel leakage, construct recovery, 3/5 with 2/3 replicating blinded and
1/5 new); it is claim (4) of §1; it is the answer to Q3 in §1 ¶2; it is two of the six rows of Table 1; it
is in the falsifier box; and it is in the Discussion. Table 3 has a main-text reference (added in
`a6ab290`, which postdates your build).

**E — compress ADAGE.** ADAGE appears **twice** in the entire main text, both in §3.4, where it is
introduced as *"an apparatus, not a contribution, and no claim rests on it"*. Its five features, the ICC
study and the pipeline are appendix-only.

## Numbered weaknesses

**#1 — theoretical novelty is modest; the non-identification result is a standard do-calculus
application.** We agree, we say so in the paper, and we are not going to argue with it. §1: *"the protocol
and the audit, not the algebra, are what is new."* `related_work`: *"The constraint itself is a standard
non-identifiability result; what is new is enforcing it on a widely used paradigm and turning it into the
five-criterion protocol."* If your 7.5 originality reflects a judgment that auditing an existing benchmark
is a smaller contribution than a new method, that is defensible and nothing in this round answers it. We
would rather carry a 7.5 for an accurate claim than a higher one for an inflated one.

**#4 — criterion 4 is observational; make "deliberately weaker than causal identification" prominent.**
It is now the organizing device of the paper. `fig:ladder` (p5) draws five rungs with rung 5 (causal,
`do(D)`) dashed and marked *"no design audited here"*, and prints between the rungs: *"↑ **this paper
reaches rung 4, not rung 5**"*. `tab:criteria` row 4 establishes *"Deception-**associated** signal at fixed
E — necessary, but not τ_D"*. §2.2 adds that passing criterion 4 establishes deception-associated behavior
*"conditional on the operational belief criterion, not deception in a philosophically or causally
privileged sense"*, and that any latent U with U→D and U→S survives it. The "Does not establish" box ends
on *"**Nor** causal identification of D→S, which is rung 5."*

**#5 / #10 — frame the belief experiment as association, not explanation.** §3.3: *"the residual signal
covaries with model knowledge; **this does not identify knowledge conflict as its cause**"*, and the
surface result is *"**surface-accessible accuracy**, not a decomposition of the rest"*.

**#6 — narrow claim distribution.** Agreed and scoped rather than defended. The abstract ends on
*"**Scope:** English, instructed-roleplay evaluations, open-weight models 3B–70B"*, and the Discussion
repeats it. We make no scaling, recency or effect-magnitude claim; EXP-R1d was our attempt to test recency
and it came back inconclusive, which we report as inconclusive.

**#7 — of ADAGE's five features only correction-marker density clears reliability.** Correct, and it is
our own disclosure: the Discussion prints Krippendorff's α = 0.606 for correction-marker density against
0.070–0.264 for the other four, and then states the consequence — *"**human rating is not a premise of the
identification result**"*: EXP-R1/R1b/R1c and the lexical audit use neither LLM-extracted features nor
human ratings.

**#12 — the main paper carries too much machinery; restructure §3 into four experiments.** §3 already is
those four experiments, in your order:

| Your requested experiment | §3 subsection |
|---|---|
| 1. Canonical detector collapses under equalization | §3.2 *The Prior Detector Collapses Under Equalization* |
| 2. Residual is surface form / knowledge conflict | §3.3 *What Survives Is Reproducible from Surface Behavior and Knowledge Conflict* |
| 3. Persists across paradigms, incl. white-box | §3.4 *A Third Detector Paradigm* |
| 4. Fixed elicitation, public corpora and built materials | §3.5 *Criterion 4: on Public Corpora, and on Materials Built for It* |

The machinery is one compressed pointer paragraph (§3.4, *"Three supporting diagnostics"*) plus Table 4's
appendix roadmap. We are **declining a further restructure**, and the reason is a budget one we would
rather state than disguise: the main text ends on line 485 of page 9 against a ceiling of 485, i.e. **zero
slack**. Any restructure has to be funded by deleting a result, a null, or a disclaimer, and we are not
willing to do that. If you think the four-experiment spine still is not visible enough, the cheapest fix
is to rename the four subsection headings, and we will do it on request.

**#13 — the title is slightly adversarial.** Changed in `a6ab290`, before your review reached us. It is now
*"What Does Lie-Detection Accuracy Measure? An Identification Audit of Behavioral LLM Deception
Benchmarks."* Beyond your reason, there was a substantive one: the paper's disclaimer (1) denies claiming
that detectors measure *only* instruction-following, which the old title mildly contradicted.

---

## What this round did not do

- **It added no evidence.** All five edits are precision fixes; two of them corrected contradictions
  internal to our own text. Nothing here moves the originality question in #1.
- **No new detector architectures, no new criterion-4 targets.** The criterion-4 roster is sealed by
  `PREREG_EXP_C4B.md`'s substitution rule, all ten targets are graded, and re-drawing after seeing counts
  is the move that rule exists to prevent.
- **No abstract or title change.** Both already carry the framing you asked for.

## Verification

`latexmk` exit 0; 78 pages; 0 overfull hbox, 0 overfull vbox, 0 undefined references; bibtex 0 warnings;
main text ends p9 at the ruler ceiling with slack 0; all eight float pins unchanged (Figure 1/p2, Table 1/p3,
Table 2/p5, Figure 2/p5, Figure 3/p6, Table 3/p8, Table 4/p14, Table 6/p17). An automated checker of
**601 assertions** passes, including 47 new ones for this round: that the corrected wording is present at
all four sites, that the overstated wording is absent from every main section, that all three tables
naming criterion 1 now agree, that the nine correct uses of "instruction-following" survive, that no site
calls the 69–80% figure a bound on the benchmark while another calls it a lower bound, and that the text
we quote to you above for B, C, D, E, #4, #5/#10, #7 and #13 is still there — so that a later revision
cannot quietly remove something we told you was already present.
