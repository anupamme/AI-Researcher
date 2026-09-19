# Response to Reviewer (6.5/10, Weak Accept / Borderline Accept, confidence 4/5) — the prominence round

**You read the current build.** Your report names `main(20260918-165843).pdf` — 16:58 UTC = 22:28 IST,
three minutes after commit `149da0d` — and it quotes `40.0--56.0` and `80.0--90.0`, which exist at
`149da0d` and nowhere earlier. **So there is no provenance section in this letter.** Every item below is
a change made *after* your read, on top of the build you read, and nothing you raised was already fixed.

We also took your scoping instruction literally:

> *I would not add more experiments unless you have an unusually cheap one. At this point, additional
> experiments risk making the paper even harder to read. I would instead make five surgical changes.*

**No experiment was run this round. Not one number in the paper changed.** The consequence for your
score sheet is stated plainly in §D below: **generalization stays at 6, by your instruction and our
choice, and we do not claim this round closes it.**

---

## §A. The honest shape of this round: most of what you asked for was present and invisible

Before answering item by item, here is what we found when we audited your list against the live text.
**Seven of your ten asks were already in the paper.** They were in the wrong place, in the wrong
typographic weight, or two sections away from where a reader needs them. That is a real defect — an
argument a reader cannot find is an argument the paper has not made — but it changes the fix from
*write new content* to *move existing content into the reader's path*, which is why a round with zero new
experiments can still be substantial.

| Your ask | Where it already was | What we did |
|---|---|---|
| §21.1 Contributions 1/2/3 explicit | `introduction.tex`, one dense run-on paragraph: 3 claims × 4 numbered items, `\textsc` markers inline | Split into **three symmetric paragraphs**, each opening on its own bolded label (`introduction.tex:52/54/56`, p2 rulers 083–107) |
| §8/§20 your novelty sentence | In substance, twice: *"the protocol and the audit, not the algebra, are what is new"* and *"Our novelty is using it as the missing construct-validity criterion"* | **Your sentence, verbatim**, as the close of Contribution 2 (`introduction.tex:54`) |
| §11 three-level terminology hierarchy | `fig:ladder`'s rungs 1 / 4 / 5 plus the *"reaches rung 4, not rung 5"* break node | Re-laid out: rungs 1/4/5 solid, 2/3 greyed, a third column added, **no EXP codes left in it** |
| §9 ECCP = standard non-identifiability | Conceded **twice**, at `appendix.tex:93` (A1–A5) and `related_work.tex:75` — but not at the ECCP's own definition | Added **at the definition** (`methodology.tex:19`), with both prior concessions kept |
| §15 readable without EXP codes | 49 of 53 main-text codes were already trailing parentheticals; `experiments.tex` was 35/35 | The remaining bare ones were the **3 inside `fig:ladder`** — the one object you wanted glanceable. Now 0 |
| §21.3 "three independent paradigms" | 2 sites only, both already enumerating the three mechanisms | → **"three mechanistically distinct detector paradigms"** (`introduction.tex:61`, `related_work.tex:75`) |
| §21.4 τ<sub>E</sub> overstatement | 2 sites; `methodology.tex:17` already said accuracy is *"evidence about the resulting $E$-associated separation, not directly about $D$"* | Both reworded, **plus** the monotonicity point you named, stated once at the estimand (`methodology.tex:17`) |

The three that were genuinely absent: **your §17 confirmatory table** (the closest object,
`tab:roadmap`, has different columns and sits in the appendix), **the C4 re-weighting** you asked for in
§21.2, and **the ECCP qualification at its definition site**. Those are the substantive additions.

---

## §B. Your items, one at a time

### §21.1 — "Make contribution 1, 2, and 3 brutally explicit"

`introduction.tex:50–56`, p2. The billing sentence now ends where it ends, and each contribution opens
its own paragraph:

> **Contribution: three claims — I. IDENTIFICATION, II. WHAT A VALID TEST REQUIRES, III. EMPIRICAL
> DIAGNOSIS — in descending order of how strongly they are warranted.** Appendix Table 4 maps each to
> its evidence; Figure 2 shows how far up the evidence ladder they reach.
>
> **Contribution 1 (IDENTIFICATION).** *(1) Framework.* …
>
> **Contribution 2 (WHAT A VALID TEST REQUIRES).** *(2) Protocol* …
>
> **Contribution 3 (EMPIRICAL DIAGNOSIS).** *(3) Demonstration* … *(4) A construct-valid benchmark* …

Two details worth flagging because they were deliberate:

1. **The inner (1)–(4) numbering is kept** inside the three labels. `main.tex`'s ethics statement cites
   claim (4) by number and §2.2's *Establishes* box carries a five-item ledger, so collapsing 4 → 3
   would have broken two cross-references to save one line. The three-level label is the *reading*
   structure; the four-item numbering is the *citation* structure.
2. **Contribution 1 was itself a late fix.** In the first pass of this round, contributions 2 and 3 got
   their own paragraphs and contribution 1 ran on from the billing sentence. That asymmetry was visible
   in the rendered p2 — the exact "present but invisible" failure this round exists to correct — so it
   is now symmetric across all three. The verifier pins all three paragraph breaks, not two.

### §21.2 — "Stop over-weighting the criterion-4 result"

Agreed, and this was the item where we had most to lose. The C4 result is the paper's only *positive*
finding, so the temptation to lead with it is exactly what your objection names.

- **§1, Contribution 3** now carries C4 as *"(4) A construct-valid benchmark"* with the standing count
  inline — **standing 1/5** — and ends at *"rung 4 of Figure 2, not rung 5."*
- **§5 (conclusion), item (4)** was longer than items (1)–(3) combined. It is now shortened **in place**
  and reads: *"a pre-registered covariate audit withdraws one, leaving one of five standing."* The whole
  item is prefaced by **"We establish — (1)–(3) structurally or by replication, (4)–(5) as a weaker,
  target-dependent secondary finding"**, so the weighting is stated before the claims, not after.
- **`tab:claim_ledger` row 5** (new, see §17 below) prints the verdict in the interpretation column:
  **"Weakest claim here, and target-dependent."**
- What we **kept** at both sites, because dropping it would have converted your re-weighting into an
  overcorrection: *"not an estimate of the prevalence or reliability of deception detection"*, and the
  sentence that the standing 1-of-5 **is itself a positive finding** — once the confound is removed,
  detection is markedly less stable across targets than instructed near-ceiling accuracy suggests.

### §21.3 — "three *independent* detector paradigms" overclaims

Fixed at both sites (`introduction.tex:61`, `related_work.tex:75`) → **"three mechanistically distinct
detector paradigms."** You are right that they are not independent: they share claim materials and
targets, so the errors are correlated. What the sentence can carry is the *mechanism* claim, and the
enumeration that follows it is what licenses the adjective — **prior work's black-box probe battery, a
hand-written surface rule, and a white-box linear probe**. The verifier asserts the old wording is at
**0 occurrences in all seven section files**, and guards the likely slip (`mechanically distinct`) by
name.

We left the **seven bare "three detector paradigms"** sites alone. They do not overclaim.

### §21.4 — "accuracy is not a monotone estimator of τ<sub>E</sub>"

This was the sharpest item in your report and it was right. Three changes:

- **Abstract**: the phrase *"the identified $\tau_E$"* is gone. It now reads *"$\tau_E$ — the
  **instruction**'s effect, and **not a magnitude accuracy estimates** — neither bounds nor signs
  $\tau_D$, so no gain in accuracy or scale resolves it."*
- **§1, Contribution 1**: *"Instructed benchmarks identify $\tau_E$"* → *"are **informative about**
  $\tau_E$ … **and their accuracy is not even a monotone estimator of its magnitude**."*
- **§2.1 (`methodology.tex:17`)**, where the estimands are defined, states the point once in full:
  **"Nor is accuracy a monotone estimator of $\tau_E$'s magnitude: $\tau_E$ is the estimand that
  separation belongs to, not a quantity the score measures."**

The word `monoton` previously appeared only in the appendix and never about accuracy-vs-τ<sub>E</sub>.
The verifier asserts `identified $\tau_E$` and `identify $\tau_E$` are absent from both the abstract and
§1.

### §21.5 / §17 — "compress to a five-object spine" and "one extremely prominent table"

These two turned out to be the same edit, and it is the only funded item in the round.

**The table.** `tab:claim_ledger`, **Table 1, page 5** — the first table a reader meets — with your
columns exactly: **Claim | Confirmatory experiment | Primary metric | PR? | Rep? | Final
interpretation.** Five rows:

| # | Claim | Confirmatory experiment | Primary metric | PR? | Rep? |
|---|---|---|---|---|---|
| 1 | Instructed accuracy cannot attribute itself to $D$ | *none* — structural | — | — | — |
| 2 | The confound is **active**: signal collapses at fixed $E$ | prompt equalization (EXP-R1c) | **97.0% → 43.3%**, every target | ✓ | ✓ |
| 3 | The scored accuracy is surface-accessible | parameter-free lexical rule | **69–80%**, no fitting | **✗** | ✓ |
| 4 | No audited public release supplies all five requirements | rollout-release audit (EXP-XA/XJ/IT2) | **9 of 10** rollout sets cannot express criterion 4 | ✓ | ✓ |
| 5 | A fixed-$E$ design **does** yield a deception-*associated* signal | criterion-4 contrast (EXP-C4/C4B/AE) | **standing 1 of 5** targets | ✓ | partly† |

Caption: **"Nothing in the argument sits outside this table."** Three things about it are deliberate:

- **Row 3 marks itself not pre-registered.** The lexical rule was written after seeing the data; it is
  diagnostic, not confirmatory, and the table says so rather than leaving it to a footnote.
- **Row 4's metric is the *release* audit** — 9 of 10 rollout sets cannot express criterion 4. It is
  **not** the `0/28` figure a reader might expect: *28 pinned corpora, 2/21/3 supplying each of the
  three auditability properties, none supplying all three* is EXP-AF (Appendix Table 7), a different
  claim about a different population.
- **Row 5 prints the *standing* count, 1 of 5, not the pre-withdrawal 3 of 5**, and the dagger spells
  out the asymmetry: two of three positives reproduce blinded, one of five *new* targets is added, then
  the covariate audit withdraws one.

**The spine.** §1 now names **four** objects, in reading order, and the paper has no fifth:
**Figure 1** (why instructed accuracy cannot attribute itself) → **Figure 2** (how far the evidence
reaches) → **Table 1** (every claim with its experiment, metric, pre-registration and replication) →
**Table 2** (what the audit found in every setting).

**How it was funded, and what it cost.** The main text is at **zero slack** — it ends on p9 at margin
ruler 485 of a hard 485 — so a new p5 table had to be paid for. Two disclosures:

1. **We did not fund it by compressing §3, as we planned to.** Declaring `tab:claim_ledger` immediately
   *before* `fig:ladder` put both on p5, and p5's float stretch absorbed the table at **zero ruler
   cost**. No sentence of §3 was cut to pay for the table. All §3 numbers, all six Q-tags, all three
   caution boxes and EXP-AD's three-line narrative are pinned unchanged by the verifier — 26 numeric
   tokens in §3 asserted present by name.
2. **`tab:criteria` was demoted to Appendix A** (now Table 5, p16) to make room — see §C.

### §8 / §20 — the novelty framing

Your sentence is in the paper verbatim, closing Contribution 2:

> **The novelty is not the observation that confounding exists; it is turning a previously implicit
> causal-validity requirement into an auditor-executable protocol and showing that existing behavioral
> deception benchmarks fail it in empirically distinct ways.**

We did not paraphrase it. You wrote the sentence that makes the contribution legible; a reworded version
would have been a worse answer.

### §9 — the ECCP "risks sounding broader than what is actually proven"

Correct, and the failure was one of placement. `methodology.tex:19`, at the definition:

> **The ECCP names a benchmark-design instance of standard pathway non-identifiability, not a new
> theoretical result** — its premises (A1)–(A5) are stated in full in Appendix A, and **what is new is
> the audit it licenses**, not the constraint.

The two pre-existing concessions are **kept**, not relocated: `related_work.tex:75` (*"The constraint
itself is a standard non-identifiability result"*) and `appendix.tex:93` (*"The algebra is standard; what
this paper contributes is the protocol that enforces it on a published benchmark"*). Three sites, three
different readers. The verifier pins all three.

### §11 — "make the three-level terminology hierarchy even more visually dominant"

`fig:ladder` (Figure 2, p5) was re-laid out rather than rewritten:

- **Rungs 1, 4 and 5 are solid; rungs 2 and 3 are greyed** as diagnostics between them, so the
  three-level terminology — *instructed-condition discrimination* → *deception-**associated** at fixed
  elicitation* → *causal $D\to S$* — reads before the detail does.
- The break node **"↑ this paper reaches rung 4, not rung 5"** sits between rungs 4 and 5.
- A **third column** was added: *"Reached by: the operational test."* This is where the operational
  content of the demoted `tab:criteria` went (§C), so each rung now states the test that reaches it —
  `do(D)`: D set or randomised / **criterion 4**: fix E, grade D off-label / **criteria 2–3**: re-extract
  cross-family / **criterion 1**: one neutral prompt / the benchmark as published.
- The column geometry was rebalanced to **56 + 44 + 33 mm, summing to exactly the band's 133 mm**, with
  columns 2–3 set `\scriptsize`. In the build you read it was 50/47/35 mm at the band's `\small` — 132 mm
  of a 133 mm band, which rendered without overflow but left no room for the third column. The verifier
  now pins the arithmetic as well as the text, so a later edit cannot widen a cell past the band.

### §15 — "make the reader able to understand the paper without knowing a single EXP code"

Nearly done before this round and finished in it. The audit: 49 of 53 main-text codes were already
trailing parentheticals and `experiments.tex` was 35/35. The exceptions were **3 bare codes inside
`fig:ladder`'s rung labels**. They are replaced by the mechanism in words — *equalization*, *the
parameter-free lexical rule*, *materials we built* — and **`fig:ladder` now contains 0 `EXP-` tokens**,
asserted by the verifier against the figure's own node text, not the file.

`tab:claim_ledger` was built to the same rule: every id in its *Confirmatory experiment* column is
inside a parenthetical after a description in words, and the verifier walks each `EXP-` match in the
table to assert the preceding character is `(` or `/`.

---

## §C. What this round changed that you did not ask for, disclosed

Four things moved that are not on your list. Each is a consequence of landing the table at zero slack,
and each is a place where the round could have quietly cost the paper something.

1. **`tab:criteria` left the main text for Appendix A** (Table 5, p16). This is the criterion-by-criterion
   specification of the protocol, and it was float 1 on p5 — the slot Table 1 now occupies. Mitigation,
   in three parts: its **operational column is folded into `fig:ladder`'s "Reached by" cells**, so the
   auditor-executable protocol stays in the main text; the **A/B/C division paragraph stays in §2.2**;
   and the appendix table says what it is — *"it is the specification behind Figure 2's 'Reached by'
   column."* The verifier asserts that every main-text citation of it now reads **"Appendix Table 5"**,
   never a bare "Table 5", and that the table was **moved, not copied** (its A/B/C markers must appear 0
   times in `methodology.tex`).
2. **A round-29 sentence was superseded.** §3.1 used to name the five Tier-1 results in words — the
   de-acronymization a previous round added. Table 1 does that job for every load-bearing claim, with
   two columns the sentence never had, so §3.1 now reads *"Table 1 is the Tier-1 ledger."* The check
   that pinned the old sentence was replaced by a **five-part conjunction** (§3.1 must point at the
   ledger; the ledger's four descriptive cells must be present; EXP-WP and EXP-AD must each still state
   their own pre-registration in §3), so the property survives the sentence.
3. **Every float renumbered.** The main-text float count went 5 → 6. `tab:criteria` 1/p5 → 5/p16,
   `tab:prior_work_criteria` 7 → 8, `tab:eccp_decidability` 6 → 7, `tab:frontier_panel` 8 → 9,
   `tab:experiment_summary` 9 → 10, `tab:dimension_transfer` 49 → 50, `tab:covariate_audit` 50 → 51.
   **All at unchanged pages** — numbers shifting while pages hold is the signature of a pure
   renumbering. All 12 pins re-measured from `main.aux`; `main.log` reports **0 undefined references**
   and the rendered PDF has **no `??` on any of its 90 pages**.
4. **Three regressions from earlier rounds were found and repaired** while auditing this one, all of them
   silent losses from previous edits: the conclusion's item (4) had lost a clause, §3.5 had lost the
   "positive finding rather than a disappointment" sentence, and **`tab:external_audit`'s caption had
   lost the "two senses of *necessary*" clause** a round-27 reviewer specifically asked for. All three
   are restored verbatim.

**Verification.** 1643 automated checks pass, up from 1489 — the round-30 suite retained in full, plus
this round's group. Where a check had to change because this round deliberately changed what it pinned
(the abstract's word ratchet, the float positions, the superseded §3.1 sentence), it was **updated with
the round-31 reason in a comment, never deleted**. Build: exit 0, **0 overfull hbox, 0 overfull vbox, 0
undefined references, 0 BibTeX warnings**, main text ending on **p9 ruler 485**.

---

## §D. Where the paper does not move, and why

**Generalization stays at 6.** We want to be exact about this rather than let a long letter imply
otherwise.

You scored generalization 6 and also wrote *"I would not add more experiments."* Those two instructions
point in opposite directions, and we followed the second. **No text edit moves that axis** — the open
grounds are empirical, and we can name them precisely:

- **Language.** Every claim is English-only. A cross-lingual arm is identified and scoped; it is
  **unrun and not pre-registered**, and we say so rather than describing it as future work in a way that
  implies it is nearly done.
- **Regime.** Outside the criterion-4 materials, the targets are instructed roleplay. The criterion-4
  contrast is the one setting that never instructs deception, and it is **five targets, 3B–14B
  open-weight**.
- **Scale.** The frontier panel (EXP-FS, seven organizations) is the round-30 addition that moved this
  axis 5 → 6. It reports the surface rule at 80–90% and the pipeline at 40–56%; it does not extend the
  criterion-4 contrast to frontier scale, which is the experiment that would.

**So the realistic landing of this round is 7.5, not 8.** Novelty and clarity are each plausibly +1 —
and if landing your own novelty sentence verbatim, with a claim ledger as Table 1 and a glanceable
ladder, does not move novelty 6, then nothing text-only will. The remaining point is an **evidence**
round: cross-lingual, or uninstructed deception at frontier scale. We would rather say that than claim
a presentation round closes an empirical gap.

---

## §E. Carried-forward disclosures (open since round 30, restated rather than dropped)

1. **The surface-rule adversarial deltas (−30.3 / −28.7 pp) and the per-target claim-pair N (12 and 17)
   remain appendix-only.** At zero main-text slack there is no room to promote them, and we would rather
   disclose the placement than quietly leave the numbers unmentioned.
2. **The cross-lingual arm is unrun and not pre-registered** (also stated in §D, because a reader of one
   section should not have to read the other).
3. **`tab:frontier_panel`'s Anthropic pipeline cell prints 50.5%, which is the *same-family*
   sensitivity.** The cross-family primary is **49.5%**, disambiguated in the adjacent paragraph. The
   cell is correct and the asymmetry is deliberate, but it is the kind of thing that reads as an error
   if it is not flagged.

## §F. Standing declines, with reasons

1. **The title stays.** *"What Does Lie-Detection Accuracy Measure? An Identification Audit of
   Behavioral LLM Deception Benchmarks."* Inserting "Instructed" would under-scope two of the paper's
   five claims: the public-corpus audit covers rollout releases that are not instructed-lie designs, and
   the criterion-4 materials **never instruct deception**. The identification failure is what the paper
   is about; the instructed benchmark is the instance where it bites hardest.
2. **`fig:ladder` does not become Figure 1.** It renumbers every float in the paper for no reading gain.
   `fig:dag` is Figure 1 because *why accuracy cannot attribute itself* is the paper's first claim, and
   the ladder answers *how far the evidence reaches*, which is the second. As of this round they are on
   **facing halves of the same spine**: Figure 1 on p2, Figure 2 and Table 1 together on p5.
