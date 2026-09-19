# Response to Reviewer (6/10, Weak Accept, confidence 0.86) — the clarity round

Thank you for the report **and** for the second, longer follow-up, which is the most directly actionable
document any reviewer has sent us: it is an implementation spec with its own priority ranking. We took your
own advice — *"if you only make one final revision, I would not add another experiment"* — and ran
**none**. This round is **presentation only**: four edits landed, two of your items were **withdrawn after
measuring what they cost**, and no number, pre-registration, or claim changed anywhere in the paper.

Two things come first, because they change which of your items are actionable.

---

## §0. Provenance: you are one round stale, not ten — and round 32 already answered four of your items

Stated as **information, not rebuttal**. Your report names `main(20260919-020957).pdf`.

- `20260919-020957` = **2026-09-19 02:09:57 UTC** = **07:39:57 IST**.
- Commit **`3d2805e`** (*"Round 31: the reviewer's five surgical changes, no new experiments"*) landed at
  **07:40:08 IST** — **eleven seconds after your PDF was written**. So you read **round 31's build**, which
  is the freshest any reviewer has read. Previous rounds were answering ten-round-old PDFs.
- The head you did **not** see is **`79d39b6`** (*"Round 32: name the two validity distinctions, and the
  inferential unit"*), committed at **09:02:56 IST** — 82 minutes after your build.

**Round 32 landed four edits that bear directly on your report, and none of them is in what you read:**

| Round-32 edit | Site | Which of your items it answers |
|---|---|---|
| predictive validity vs. **attributional** validity, named as such | `introduction.tex:61` + the p3 comparison table | your §6 |
| **construct validity and instrument validity are distinct** | `methodology.tex:78`, `experiments.tex` | your §13 |
| the three-way split: *1–3 diagnose the confound, criterion 4 is the one **identification** requirement, criterion 5 is **robustness**, not a construct-validity test* | `methodology.tex:78` | your §14, *"why exactly these five? Especially criterion 5"* |
| the inferential unit — **target × claim-pair**, "thousands of trials" reduced to **12–23 paired claims per target** | `methodology.tex:81` + Appendix Table 30 | your §21-adjacent multiplicity concern |

**Your own text dates the build independently, so you can check this without trusting us.** Your §14 asks
*"why exactly these five, especially criterion 5"* without engaging the sentence that now answers it
verbatim; and your §14 map assigns criterion 5 a meaning the round-32 text explicitly denies it (see §D).

---

## §A. The honest core of this reply: both of your highest-priority objects already exist — in the appendix

You pre-empted the appendix answer yourself: *"appendices are unlimited but reviewers are not required to
read them, so moving the conceptual argument into the main paper is particularly important."* **We accept
that premise.** We are not arguing that appendix placement discharges the ask. But you should know what
exists, because it changes the request from *"build this"* to *"move this"*:

| Your ask | What already exists | Where |
|---|---|---|
| **§25A**, which you call *"the highest priority"*: a table of *"what existing deception benchmark methodologies test vs. what the identification audit adds"*, with columns for instruction invariance / construct independence / deployed-visible channel / construct recovery / audit protocol | **Table 8, `tab:prior_work_criteria`** — 11 rows in five groups × requirements **(i)–(v)** + a *"Tests attribution?"* column. Your five requested columns **are** (i), (ii), (iv), (v) + protocol. It is strictly richer than the sketch in your §25A | **Appendix, 8 / p21** |
| **Clarity ★★★★★ #2**: *"recast the five criteria as answers to alternative-explanation questions — what each one rules out"* | **Table 5, `tab:criteria`** — already carries a *"What it establishes"* column reading *"Rules out **instruction asymmetry**"*, *"Rules out an **evaluator artifact**"*, *"Robustness, not construct validity"*, under the A/B/C group headers | **Appendix A, 5 / p16** |

**So this round was a placement problem at a hard page limit, not a content problem — and that is the whole
difficulty.** The paper is 9 pages of main text with **zero slack**: it currently ends on p9 at margin
ruler **485**, and p9's last ruler *is* the limit. We measured the price of every item in your list before
deciding, and we report all of the prices below, including the ones we could not pay.

**One measured fact is worth stating because it is counter-intuitive and it governed the round:** in this
document, **an addition upstream of the spill costs about one line per line, while a *cut* upstream of the
spill refunds nothing at all.** Only cuts inside the last two sections buy anything. A prior round's rule
of thumb — that caption text absorbs additions for free — is **false at the current layout**: we measured
+289 characters into Table 2's caption at **3 lines**, and +185 into Figure 2's caption at **3 lines**.
That is why what landed is what landed.

---

## §B. What we changed (four edits), with your own ★ ratings and the measured price of each

### B1 — your clarity ★★★★★ #3 and §25C: every experiment now names the rung it moves the evidence to · `experiments.tex` · **measured cost: 0 lines**

You asked us to *"explicitly tell the reader that every experiment asks whether the evidence moves the
benchmark one rung higher,"* with headings of the form *"3.2 Rung 1 → 2."* All four §3 subsection titles now
carry one. We **augmented** rather than replaced: the Q1/Q2/Q3 tags were a previous reviewer's ask and they
stay, so the two tags compose.

| § | Heading now reads |
|---|---|
| 3.2 | **Q1, then Q2, Rung 1 to 2:** The Prior Detector Collapses Under Equalization (EXP-R1, EXP-R1b/R1c) |
| 3.3 | **Q2, Rung 2 to 3:** What Survives Is Reproducible from Surface Behavior and Model Knowledge |
| 3.4 | **Q2, Rung 2 to 3 Again:** A Third Detector Paradigm, and Supporting Analyses |
| 3.5 | **Q3, Rung 3 to 4:** Criterion 4 on Public Corpora, and on Materials Built for It (EXP-XA/XJ/XL, EXP-C4) |

The table of contents now reads as the ladder. Two notes for the record: *"Experimental Setup"* deliberately
carries **no** rung tag, because it climbs nothing; and **no heading claims rung 5**, which no design audited
here reaches. The tags are ASCII (*"Rung 1 to 2"*, not *"Rung 1 → 2"*) because an arrow inside a sectioning
command corrupts the PDF bookmark string.

### B2 — your §25B: Figure 2's middle column is now the executable audit · `methodology.tex` · **measured cost: 0 lines**

You asked for the protocol *"executable in ~10 lines."* Figure 2's middle column — *"Reached by: the
operational test"* — **already was** the step list, so we numbered it rather than adding an object:

> **1.** the benchmark as published → **2. criterion 1**: one neutral prompt → **3. criteria 2–3**:
> re-extract cross-family → **4. criterion 4**: fix *E*, grade *D* off-label → **5.** do(*D*): *D* set or
> randomised

and the caption now closes on the instruction that makes it a procedure: **"The middle column is the audit:
run steps 1–5 bottom-up and report the highest rung reached."** The vague sentence this displaced (*"each
control rules out one alternative explanation"*) is gone rather than duplicated. The column header stays
*"Reached by: the operational test"* — renaming it *"Step"* would have desynchronized an appendix sentence
that quotes that exact string, so the numbers went into the cells instead. Column geometry is fixed at
56/44/33 mm and we verified on the rendered page that the numbered cells still fit 44 mm without reflow.

### B3 — the defect your report demonstrates: the two five-item numbering schemes, named apart · `methodology.tex:78` · **+146 chars, measured cost: 1 line, funded**

This is the edit we consider the round's real find, and **your report is the evidence that it was needed**
(§D). The paper carries **two disjoint five-item schemes** — criteria **1–5** (the audit's controls) and
requirements **(i)–(v)** (what operationalizes criterion 4) — and §2.2 is the one paragraph where they
collide within a few clauses. It now says so, at the collision point:

> **Criteria 1–5 and requirements (i)–(v) are different lists**: the criteria are the audit's controls,
> (i)–(v) operationalize criterion 4.

This is the cheapest available answer to your *"the reader has to reconstruct the hierarchy."* We did **not**
do a `4a–4e` renaming sweep; one clause, once, at the point of collision.

### B4 — your clarity ★★★★★ #1: the recurring anchor · `introduction.tex`, `experiments.tex` · **measured cost: 0 lines**

You asked for one short repeatable phrase. The paper had **zero** occurrences of any *"identification, not
classification"* formulation. It now has two, and **we are telling you exactly how thin that is**: both are
in **figure captions**, because that is where the phrase was free.

- **Figure 1's caption title**: *"**Why instructed-roleplay accuracy cannot attribute itself: the problem is
  identification, not classification.**"* — folded into the existing bold title, so it cost nothing.
- **Figure 3's caption, final sentence**: *"**The problem is identification, not classification.**"*

We measured the same 58 characters in §3.2's *body* at **3 lines** and could not pay for it there. Two
captions is not the drumbeat you asked for; it is what fit.

### B5 — the funding, which did not work the way either of us expected

Per your §18 we cut round 31's *"accuracy is not even a **monotone** estimator of its magnitude"* at both
sites. **The cut freed zero lines** — it sits upstream of where the document actually spills. So B3 was
funded instead from **291 characters of cuts inside the Conclusion (4) and §3.5 (1)**, which bought **2
lines**; the realized exchange rate was about **1 character of upstream addition per 2 characters of
downstream cut**. Every cut removed a **restatement**, never a fact, and the verifier pins each fact at its
surviving canonical site:

| Cut | Fact removed from | Still stated at |
|---|---|---|
| *"the score moving inside a single deception label"* | Conclusion | §3.4's factorial (*"truth-value's is smaller and changes sign"*) |
| *"—an identification failure, not a detector failure"* | Conclusion | claim (1), same paragraph |
| claim (5)'s gloss, keeping the **(EXP-AD)** pointer | Conclusion | §3.5's EXP-AD narrative, intact at full length |
| *"on four published designs and 28 pinned corpora"* | Conclusion | §2.1 (*"28 pinned public corpora"*), §1 (*"four outside deception"*) |
| *"; effect sizes in Table 2"* | §3.5 | Table 2's last row (0.650–0.903) |

One further Conclusion sentence — *"The alternative reading, that deception is undetectable, is what (4)
tests"* — was cut, measured at **0 lines freed**, and **restored**. We do not trade content for nothing.

---

## §C. Two places where your report contradicts a previous reviewer. We are showing these, not resolving them quietly.

**C1 — your §18 vs. round 31's §21.4.** You write that the monotonicity clause is a distraction: *"a
reviewer might spend time asking 'Why are you introducing τ_E if accuracy isn't estimating it?'"* The
previous reviewer's §21.4 was, in our round-31 words, *"the sharpest item in your report and it was right"*,
and we added that clause **at both sites** in response. **We have done what you asked**, and the substance
they wanted survives: §2.1 still says *"τ_E is the estimand that separation belongs to, not a quantity the
score measures"*, and the abstract's *"not a magnitude accuracy estimates"* is untouched. What went is the
second, redundant formulation. You should know the reversal happened and why.

**C2 — your *"the one thing I would actually delete"* vs. round 29's item 8.** You ask that the epistemic
boundary be stated once rather than repeatedly. Round 29 **added** `introduction.tex:84`, *"What we do not
establish, in plain terms"*, precisely because a previous reviewer wanted the limits on p3 rather than only
inside §2.2's box on p5. **We declined your deletion and kept both**, on a standing constraint we will state
plainly: every reviewer who has commented on the structured caution boxes has named them a strength, and we
will not cut one to buy space. That is a judgment call against you, made explicitly rather than silently.

---

## §D. A correction, with thanks: criterion 5 is *transfer*

Your §14 maps **"C5 → detector reading its own annotation/label mechanism."** That is not what criterion 5
is. **Criterion 5 is cross-target / cross-claim transfer** — and the paper marks it *exploratory*, 2 of 5,
explicitly *"not part of the argument."* Annotation-channel leakage and definitional circularity are
**requirements (iv) and (v)**, which operationalize **criterion 4**; §3.5 earns each of them at a named
finding (*"annotation-channel leakage, whence (iv)"*, *"construct recovery, whence (v)"*).

We are not scoring a point. **A careful reviewer conflated the paper's two five-item schemes at exactly the
paragraph where they collide, which is the strongest possible evidence for your own complaint — and it is
why B3 exists.** Your report diagnosed a real defect by exhibiting it.

---

## §E. What we declined, with the measured price in each case

**E1 — your clarity ★★★★★ #2, *"name what each criterion rules out," in the main text*: withdrawn after
measurement.** We drafted the one-sentence distillation (*"1 instruction asymmetry, 2 an evaluator
artifact, 3 surface form, 4 the elicitation confound itself, 5 target- or claim-specificity"*) and measured
it at **three sites**: Figure 2's caption **3 lines**, Table 2's caption **3 lines**, §2.2's body **2
lines**. With the authorized funding source returning **0** (§B5) and every other compressible span in the
spilling region being a pinned, reviewer-requested addition from rounds 29–32, there was nothing left to pay
with. **The content is Table 5's *"What it establishes"* column, Appendix A, p16.** This is the item we
would land first given one more page.

**E2 — your §25A novelty ledger, which you call the highest priority: withdrawn after measurement, at 5–8
lines.** We designed it as five extra rows on the existing p3 comparison table (a non-float, already in
exactly that rhetorical slot), with every cell **transcribed** from Table 8 rather than recomputed. It
prices at 5–8 lines and there is no funding for it. We also want to be straight about what it would and
would not do: it **relocates** an argument, it does not add one. If your novelty 7 is driven by the
appendix placement of Table 8, this edit fixes it; if it is driven by the substance, it does not.

**E3 — your clarity ★★★, terminology discipline: not swept.** The phrase *"lie-detection accuracy"* has
**0 occurrences** in the paper already, so the headline number is never called that. We tried applying the
rung-1 term (*"instructed-condition discrimination"*) at the two headline sites and reverted it: it bought
nothing and put two cross-site pinned strings at risk. A full sweep lengthens prose at zero slack for a
★★★ item.

**E4 — promoting Table 5 into the main text: standing decline.** This was the user's decision in round 31
and reaffirmed in round 32. Unchanged.

**E5 — your §16's *"the paper is doing too much"* as a structural split into Papers A/B/C: declined.** That
is a different submission, not a revision.

**E6 — new experiments implied anywhere in §25: declined**, on your own instruction.

---

## §F. Carried-forward disclosures — restated, not dropped

- **Generality stays bounded, and we say why rather than claiming otherwise.** §2.1 reads *"outside
  deception the precondition is thus decidable and decided; **the magnitude is measured only for
  deception**."* EXP-AF decides the ECCP precondition on **28** pinned public corpora but measures no effect
  size outside deception. **Measuring one such magnitude is the single change that would move both your
  novelty 7 and your generality 7, and it is a new experiment.**
- **The non-English pilot** (`appendix.tex:770`, *n* = 50 Spanish or Mandarin) is named, scoped, and
  **unrun**.
  Materials are English-only; instructed roleplay is the regime outside criterion 4.
- **EXP-C4B's −30.3 / −28.7 pp surface-rule deltas remain appendix-only.**
- **Table `tab:frontier_panel`**: 50.5% is the same-family sensitivity, 49.5% the cross-family primary.
- **This paper reaches rung 4, not rung 5**, and says so in the abstract, Figure 2, Table 1's claim 5, and
  the §2.2 box.

## §G. Standing declines from earlier rounds

The title (user decision) and the ladder remaining Figure 2 rather than moving earlier.

---

## Verification

`latexmk` exits clean with **0 overfull boxes** and **0 undefined references**; main text still ends on
**p9 at ruler 485** with the Ethics Statement opening p10; all **12 float pins** hold at their committed
pages; and the regression suite is at **1820 checks, all passing** (1735 retained from round 32, of which
13 were *updated* with the round-33 reason recorded in a comment — never deleted — plus 85 new).

One thing this round found is worth recording because it is the kind of error that survives a green suite:
**both of our existing page-budget arbiters reported the paper as fitting while the Conclusion's last two
lines were on p10.** They read the last margin ruler printed *before* the closing sentence, so a sentence
that *wraps* is measured one line short. The suite now asserts on the rendered page content of p9 **and**
p10 directly. We mention it because it means an earlier round's "fits" was measured with an instrument that
could not see the failure — the same class of mistake the paper is about.

---

## What we think this round is worth, stated plainly

- **Clarity 7 → 8.5–9 is credible, and it is what you said was available.** Your follow-up was an
  implementation spec; we landed all three of your ★★★★★ items in some form — #1 and #3 in full at zero
  cost, #2's content acknowledged as existing but stranded in Appendix A — plus the numbering defect your
  own report exposed. Your ★★★★☆ items #4 and #5 were already closed in rounds 29–32, with sites listed in
  §0 and §C2.
- **8.5 overall is not reachable this round, and we are not going to claim it.** Your arithmetic is
  explicit: *"Overall 7-ish,"* novelty 7, theory 7, generality 7, and *"I would not give it an 8 yet because
  the novelty/significance question is still genuinely debatable."* The one lever on novelty is E2, it costs
  5–8 lines we do not have, and it **relocates** an argument rather than adding one. **Realistic landing:
  7.5, with 8 reachable if you credit a relocation.**
- **The residual gap is novelty and generality, and both are evidence-shaped, not presentation-shaped.** No
  amount of rewriting closes them. The experiment that would is named in §F, and it is not in this round
  because you told us not to run one.
