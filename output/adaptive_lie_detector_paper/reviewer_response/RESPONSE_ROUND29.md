# Response to Reviewer (6/10, Weak Accept, confidence 4/5) — the clarity round

You set a test rather than a list:

> *after pages 1–3 a reader should be able to state the argument from memory.*

and one constraint on how to pass it:

> *Don't simplify away the intellectual precision. The goal is: less terminology, not less precision.*

**We took the test literally.** Here is the argument as it now reads off pp. 1–3, in three sentences:

1. An instructed-lie benchmark makes a model lie by changing the instruction, but that same edit changes the
   instruction-following behavior a detector reads — so its accuracy identifies the *instruction*'s effect,
   not deception's, and no gain in accuracy or scale repairs that.
2. So the paper supplies an audit: three questions (**Q1** can a detector classify? **Q2** is it the
   deception? **Q3** does it fire with no instruction to comply with?) and five criteria in three lettered
   groups, of which **one — criterion 4, deception at fixed elicitation — no instructed design can supply**.
3. Applied across eight models, three detector paradigms and both public rollout releases, the confound is
   **active** (97.0% → 43.3% under equalization; 69–80% from a parameter-free rule) and **no audited public
   release supplies all five**; on materials we built that do, prior work's own battery separates deception on
   **one of five** targets — rung 4 of five, not causal.

**What made this affordable was your own diagnosis: most of what you asked for already existed in the paper
and was unaligned.** The Q1/Q2/Q3 box, the A/B/C-shaped criteria table, the ladder's *"rung 4, not rung 5"*
node and the five-item *Does not establish* list were all present, but **five competing organizational schemes
were running at once** and the reader had to reconcile them. This round is alignment, relocation and naming.
**It is net −151 words of main text**, and it produced **no new evidence** — every number in the paper after
this pass is a number that was already there.

| | main text |
|---|---|
| abstract | 521 → **388** words (**−26%**) |
| introduction | 1473 → 1340 (**−133**) |
| methodology | 1747 → 1849 (+102) |
| experiments | 2144 → 2144 (**±0**) |
| discussion | 185 → 195 (+10) |
| conclusion | 279 → 282 (+3) |
| **total** | **6351 → 6200 (−151)** |
| appendix (free) | 47,655 → 48,033 (+378) |

The paper still ends on **p9** with **zero slack**, 0 overfull boxes, and **1366 automated checks pass** (1230
retained from previous rounds, 136 new). **Fifteen of the new ones are *inverse* assertions** — they exist
only to prove that this round's simplifications did not drop a qualification, and several loop over every item
they protect. We wrote them because of your constraint above, and before making the edits.

---

## 🔴1 — Organize everything around Q1/Q2/Q3

**Done, and the labels now do work rather than decorate.** Previously Q1/Q2/Q3 were defined in one box on p2
and never used again. Now **all six substantive subsection headings carry the question they answer**:

| Section | Heading |
|---|---|
| §2.1 | **Q2**: Why the Instructed Contrast Cannot Be Attributed |
| §2.2 | **Q2/Q3**: An Audit Protocol for Behavioral Deception Benchmarks |
| §3.2 | **Q1, then Q2**: The Prior Detector Collapses Under Equalization (EXP-R1, EXP-R1b/R1c) |
| §3.3 | **Q2**: What Survives Is Reproducible from Surface Behavior and Model Knowledge |
| §3.4 | **Q2**: A Third Detector Paradigm, and Supporting Analyses |
| §3.5 | **Q3**: Criterion 4 on Public Corpora, and on Materials Built for It |

§3.1 (Experimental Setup) is deliberately untagged. The criteria table's caption now carries the mapping too —
**"Group A answers Q2; group B answers Q3"** — so the five criteria are read as answers to the questions
rather than as a free-standing list.

The evidence roadmap (now appendix Table 4) is the *full* question → evidence → result → warrant mapping, so
**all six of its question rows are Q-labelled**. Three of them previously were not — the equalization row, the
surface-baseline row and the factorial diagnostic, all three of which are Q2 questions. That was our
inconsistency, not a limit of the scheme, and it is fixed.

Cost: **≈ zero words.** This was the highest-yield item in the round.

## 🔴2 — Figure 1 → Figure 2 → Table as the narrative spine

**Stated in prose rather than by moving a float** (moving Figure 2 out of §2.2 would have renumbered every
float and broken twelve position pins for no reading gain):

> **Three objects carry the argument**: Figure 1 shows why instructed accuracy cannot attribute itself,
> Figure 2 shows how far the evidence reaches, and Table 2 records what the audit found in every setting.

It sits at the end of the introduction's prior-work discussion, with forward references, so the reader meets
the spine before the first of the three.

## 🔴3 — Descriptive names, never the bare ID as the noun

**Adopted as a rule, at every prose site:** the noun is descriptive, the ID is parenthetical.

- **IDs opening a parenthesis: 29 → 40**, out of 51 total occurrences (was 29 of 57). We checked the other 11
  individually: **none is a bare ID doing a noun's work.** Three are cells inside Figure 2's ladder
  (*"EXP-C4: our own materials"*), two are the second ID in a heading's shared parenthesis
  (*"(EXP-R1, EXP-R1b/R1c)"*), and six are a later ID inside a parenthesis a descriptive name already opened
  (*"(the covariate audit, EXP-AE)"*).
- **An automated check now forbids the failure mode you named**: an `EXP-` token may not open a sentence or a
  paragraph as its grammatical subject. It currently finds zero.
- Names are established **once, at first use**, and reused verbatim: *the pre-registered equalization
  collapse* (EXP-R1c), *the white-box probe audit* (EXP-WP), *the criterion-4 contrast and its blinded
  replication* (EXP-C4/C4B), *the covariate audit* (EXP-AE), *the probe-substitution demonstration* (EXP-AD).
- The Tier-1 line in §3.1 was rewritten from a list of five bare IDs into those five descriptive names.

## 🔴4 — Less notation introduced early

**§2.1's opening prose now uses four symbols, not six: E, D, C, S.** `V` (claim truth-value) and `B` (model
belief) are gone from the prose; the sentence that used them now reads *"the claim's truth-value and the
target's belief are all parents of S"*, which keeps the load-bearing claim — **the ground-truth label is an
experimental condition, not an observation of latent intent** — exactly as strong.

`V` reappears once, in the sentence that sets up the Proposition, because the Proposition's observables really
are `(V, E, S)`. `B` does not reappear at all. Figure 1's `V` and `B` nodes are **self-labelling** (*"V: claim
truth-value"*), so they cost the reader nothing and were left alone. A check pins the four-symbol set.

## 🔴5 — Criterion 4 visually distinguished from diagnostics 1–3 and robustness 5

**Your 3 + 1 + 1, with your letters:**

- **A. Confound diagnostics (1, 2, 3)** — *testable on any published benchmark by whoever did not build it*
- **B. Construct-validity test (4)** — ***different in kind***: *must be designed in, and cannot be added by
  an auditor*
- **C. Robustness (5)** — *not a construct-validity test, and not equally fundamental*

Group B carries a **filled** marker (■) against **hollow** markers (□) on A and C, so the asymmetry is seen
before it is read. The same A/B/C naming now runs through the 3+1+1 paragraph *and* Table 2's caption, so the
audit table's columns inherit the grouping.

We also added the clause you asked for, stating *why* 4 is different rather than asserting it:

> The division is *who can apply* a criterion: **A and C can be checked on someone else's benchmark, from the
> artifact as released; B requires building materials that no instructed design can supply**, which is why it
> is different in kind and not merely one item of five.

## 🔴6 — The abstract as Problem → Insight → Method → Results → Implication

**Your shape, adopted; your word count, not reached. Both facts stated plainly.**

| | before | after |
|---|---|---|
| words | 521 | **388** (−26%) |
| sentences | 16 | 13 |
| numeric tokens | 17 | **7** |
| **result** numbers | 13 | **4** — 97.0, 43.3, 69, 80 |

The remaining three numerics are not results: `3` and `70` are the scope line's model-size range (3B–70B) and
`4` appears as a *label* (criterion 4, rung 4). So the abstract does carry **only your four headline numbers**,
in the closing sentences, as you drafted it.

**Why 388 and not ~250, stated rather than hidden.** Ten of the thirteen sentences are pinned verbatim by
earlier rounds' must-fixes: the round-27 reviewer's opening sentence, the pathway-non-separability statement
and the τ_D demotion required in round 23, the round-28 contribution sentence, *"The audit has five parts"*,
the 97.0 → 43.3 and 69–80% results, the standing-1-of-5 chain required in round 25, the rung-4 implication,
and the Scope line. **Reaching 250 would mean reversing those.** We removed everything that was *not* pinned —
the white-box collapse detail, the annotation-leakage and construct-recovery mechanisms, the 35-cell audit,
the nine-of-ten count, the rung-4 arithmetic and the ECCP name, all of which have main-text homes — and 388 is
where that bottoms out. If you would rather we broke one of those earlier pins to reach 250, say which and we
will.

**One of your requests reshaped another reviewer's, and we flag it rather than let you find it.** Your item 11
wants *"as opposed to instruction-induced behavior"* in the **first sentence**; round 27's reviewer pinned that
sentence's wording verbatim. Both now hold in one sentence, theirs first and your contrast appended after the
em-dash:

> **Accuracy on instructed-lie benchmarks does not identify deception: the intervention that creates the lie
> also changes instruction-following behavior** — so its accuracy cannot be read as evidence of deception **as
> opposed to instruction-induced behavior.**

## 🟠7 and 🔴13/🔴14 — §3.5, compressed and restructured

**Partially, and the measurement is not what we projected.** §3.5 went **614 → 600 words**:

| paragraph | before | after |
|---|---|---|
| public corpora (the three failure modes) | 142 | **115** |
| *Stated exactly* | 62 | 62 |
| the 1-of-5 progression | 270 | **283** |
| the probe-substitution demonstration (EXP-AD) | 139 | **139** |

The public-corpus prose lost 27 words to Table 2, which already carried every verdict; the mechanism
narratives moved to the appendix. But **your item 14 asked us to restate the 1-of-5 progression as four clean
lines plus one conclusion, and doing that cost 13 words rather than saving any.** We took the clarity and
report the arithmetic honestly: it is now **(a) three of five separate → (b) blinded replication keeps two,
adds one of five new → (c) the covariate audit withdraws one → (d) the standing count is one of five**, then
your conclusion. It is four labelled clauses in running prose rather than a displayed list, because a list on
p9 does not fit the page budget at zero slack.

**EXP-AD is unchanged at 139 words.** Round 28's reviewer required it not be shortened below its three-line
narrative, and it was not a funding source this round.

**The funding actually came from the abstract (−133) and the introduction (−133), not from §3.5.** Our plan
projected −197 from §3.5 and it delivered −14.

## 🟠8 — "What we do not establish" moved earlier

**It is now on p3, in plain terms, in the introduction** — a reader meets the paper's limits before the
methodology rather than on p5 inside a notation-heavy box:

> **What we do not establish, in plain terms.** That deception is undetectable; that published detectors
> encode only instruction-following; that equalization shows a deception signal to be *absent* rather than
> removed along with the confound; that the audited corpora contain no deception; or that the signal we do
> find at fixed elicitation is deception rather than a correlate of it.

The precise five-item version, with the evidence that bounds each, stays in §2.2's box. A check asserts all
five items survive verbatim at both places, and that the two lists agree on the count.

## 🟠9 and 🔴16 — Repeated caveats consolidated

*"Deception-associated, not causal"* is established once and then referred to by the short phrase. Same for
the same-battery portability caveat and the different-claim-sets limitation. **No structured caution box was
touched** — the main text still carries all three (the Q1/Q2/Q3 box, the would-settle-it design box, and the
proven/shown/unresolved box), and a check pins the count, because every previous reviewer named them a
strength.

## 🟡10 — Secondary bookkeeping to the appendix

Three moves, all disclosed because each takes a number out of the main text:

1. **Table 1, the evidence roadmap, is now Table 4 in the appendix's reader's guide.** This one carried a
   risk: a round-23 reviewer asked for exactly that question → evidence → result → warrant mapping. **It is
   preserved complete** — all three claim groups, the Q-labels, the pre-registration marks and the
   NOT-ESTABLISHED row — and the introduction keeps a two-line pointer naming the three groups and directing
   the reader to it. Demoting it removed one of the five competing schemes from pp. 2–3, which is the actual
   clarity gain; the budget did not depend on it.
2. **The 2×2 factorial's β coefficients** moved to the appendix; the main text keeps the effect in SD.
3. **The below-chance cell's (39.0–44.0%) range** moved to the appendix; the main text keeps *"below chance."*

---

## Your two precision phrases, adopted verbatim

1. **Criterion 4's purpose.** At **both** sites — the abstract and §3.5's conclusion — it now reads: *a
   demonstration that **criterion-4-valid materials can produce a deception-associated signal**, **not an
   estimate of the prevalence or reliability of deception detection***.
2. **The scope of the verdict.** Every statement of it names the audited releases: *"no public release we
   audited supplies all five"* (abstract), *"no audited public set satisfies all five"* (§3.5), *"No audited
   public release supplies all five requirements"* (§2.2). A check now **forbids** the generalizing forms
   (*"deception benchmarks generally"*, *"all deception benchmarks"*, and three near variants). None appears.

## Simplify to three claims

**Three named claims, with the inner numbering kept.** They are **I. Identification** / **II. What a valid
test requires** / **III. Empirical diagnosis**, and they are now **three separate blocks on p2** rather than
one 22-line wall.

We did **not** renumber the claims themselves, and the reason is mechanical: the ethics statement cites
*claim (4)* by number, and the conclusion carries a five-item *establishes* ledger. Renumbering would break
the first and widen the gap to the second. So (1)–(4) sit nested under the three names — three things to
remember, every existing cross-reference still valid.

## A defect we found in our own text, and fixed

`conclusion.tex` said *"We do not establish the **four** negatives boxed in §2.2"* while the box lists
**five**. It predates your read, it was ours, and it is now *"the five negatives."* A check forbids the string
*"four negatives"* from returning.

## Where the paper does not move

- **Novelty (6) is untouched by this pass.** This was a presentation round by construction. The paper already
  concedes the algebra is standard, and that concession is now stated more sharply, not less:
  **"the protocol and the audit, not the algebra, are what is new."** Two phrases we used to lean on —
  *"structurally non-identifying"* and *"causal-identification theorem"* — are **gone from the paper
  entirely**, because both oversold a d-separation argument. What replaced them is the plainer and more
  defensible bound above.
- **Criterion 4 remains observational, at rung 4.** One surviving positive out of five, and it is
  indeterminate against sixteen surface covariates. We report that as the finding rather than as a
  disappointment, in your words.
- **No new experiments were run**, and we make no claim on your empirical-rigor score.
