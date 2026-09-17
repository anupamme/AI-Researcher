# Response to Reviewer (6/10, Borderline / Weak Accept, confidence 4/5)

*On `main(20260917-095844).pdf`. Sub-scores: novelty 7, technical soundness 7, experimental rigor 8,
clarity 7, empirical strength of the main negative claim 8.5, empirical strength of the positive criterion-4
claim 5.5, significance 8, reproducibility 9, overall 6.*

Thank you. Your must-fix is real, we have fixed it at every site, and your framing recommendation — *"make
the paper's contribution unmistakably about benchmark validity and identification, while making the
criterion-4 result explicitly modest"* — is the one we adopted, deliberately at the cost of making the
positive result look weaker. It is weaker. Your own note is the right frame: *"That is actually stronger
scientifically, because it makes the paper look honest rather than promotional."*

This round adds **no evidence**. Every change is a precision or framing edit, plus three new appendix
passages answering Q3, Q4 and your §11.

---

## 1. The must-fix: 3/5 vs 2/5 (your §15.1, weakness #1, Q1). Agreed — and the defect was the mirror image of what you saw

**What you reported.** The main text says three of five targets are positive; the appendix says the standing
count is two of five.

**What we found when we audited every site.** The direction was reversed, which matters because it changes
what had to be fixed:

- **Every** main-text site already reported all three counts — 3/5 original, 2 of 3 replicating blinded, 1
  of 5 new: `abstract.tex:4`, `introduction.tex:79` (Table 1), `experiments.tex:107` (Table 3), `:126`
  (§3.5), `conclusion.tex:4`.
- What **no** main-text site stated was the **standing count of two of five**. A reader had to compose it
  from "three positive" and "two of three replicate", and you reasonably read the leading number as the
  claim.
- Meanwhile `appendix.tex` asserted *"any statement that three of five targets are positive at fixed
  elicitation must now read two of five, **and this paper's main text says so**"* — **which was false**.
- And two appendix sites gave an **unqualified** 3/5 with no pointer to the replication: Table 4's
  criterion-4 cell, and EXP-C4's own H1 paragraph heading.

So the fix was not to change a number. It was to **state the standing count in the main text** and make the
appendix's claim about the main text true. **Nine sites:**

| Site | Now reads |
|---|---|
| `abstract.tex:4` | …on three of five targets—all three with power ($p\le0.006$; two nulls underpowered)—**of which a blinded re-run replicates two, so the standing count is two of five**, with **one of five *new* targets positive** |
| `introduction.tex:79` (Table 1) | **Yes: 3/5** positive, 2 underpowered nulls; blinded **2 of 3**, so **standing 2/5**; **1/5** new |
| `experiments.tex:107` (Table 3) | **2 of 3 replicate blinded** (standing **2/5**), **1 of 5** new (EXP-C4B) |
| `experiments.tex:126` (§3.5) | …not the weakest, which falls below its own baseline, **so the standing count is two of five**— |
| `conclusion.tex:4` | …and not the weakest—**so the standing count is two of five**—while on five *new* targets… |
| `methodology.tex:86` (the box) | …**(e) is target-dependent**—two of five standing, one of five new— |
| `appendix.tex:1695` | …**and this paper's main text says so at every site that reports the count**: the abstract, Table 1, Table 3, §3.5 and §5 each give the original three, the two that replicate, the one of five new targets, **and the standing count of two of five** |
| `appendix.tex:1810` (Table 4) | …on three of five targets—**two of five standing** after the blinded re-run of §W |

The ninth site was found not by us but by the check we wrote for this round: EXP-C4's H1 paragraph reported
its own three of five with no forward pointer. It now closes on *"**Read this figure with §W**: the blinded
re-run replicates two of the three, so the *standing* count is **two of five**, which is what the main text
reports."*

**We also added the check that would have caught this.** Our verifier now asserts that *if* the appendix
claims the main text states the standing count, *then* the standing count is present in `abstract.tex`,
`introduction.tex`, `experiments.tex` **and** `conclusion.tex`; and that no appendix paragraph reports
"three of five targets" without the standing count somewhere in the same paragraph. The second of those is
what surfaced the eighth site.

## 2. "Deception is detectable" → "a deception-*associated* signal is detectable" (your §15.2). Done, at every site

Four sites carried the strong verb. All four now read *"a deception-**associated** signal is nevertheless
detectable under a valid fixed-elicitation design"*, and the main-text ones add the target qualifier:

- `abstract.tex:4` — *"—on **some** targets, still not $\tau_D$"*
- `introduction.tex:50` — *"…under a valid fixed-elicitation design, **on some targets**"*
- `conclusion.tex:4` — *"—on **some** targets, not $\tau_D$"*
- `introduction.tex:79`, Table 1's "What it licenses" cell — *"**Deception-*associated* signal at fixed
  $E$**; the instructed benchmark is non-identifying regardless"*

The verifier asserts the unqualified phrasing is **absent** from every section file.

## 3. The evidence asymmetry, stated in one place (your §15.3 — the sentence you said "would substantially improve the paper")

Added as the last line of the "What this paper establishes, and what it does not" box you asked us to keep
(`methodology.tex:86`, p6):

> **The two halves are not equally strong**: (a)–(d) hold by structure or replicate across paradigms, claim
> sets and model families, while **(e) is target-dependent** — two of five standing, one of five new — on
> 3B–14B open-weight targets.

That single sentence also answers your §9 (separate the structural claim from the empirical one, and scope
the model coverage) and your §4 (criterion 4 is deliberately weaker). The appendix's EXP-C4 summary carries
the matching sentence: *"Both halves are now measured rather than argued, and **they are not equally
strong**: the first is structural and replicated across paradigms, the second is target-dependent."*

## Your questions

**Q1 — where the 3/5-vs-2/5 inconsistency is, and which is correct.** The standing count is **two of
five**, and the table in §1 above lists all eight sites. Both numbers are correct statements about
different experiments — EXP-C4 found three of five positive; the blinded EXP-C4B re-run replicated two of
those three — and the defect was that the paper never composed them into the standing count for the reader.

**Q2 — a single sentence stating what is established with high vs low confidence.** §3 above, verbatim.

**Q3 — how sensitive H1 is to how $D$ is labeled, and could a human-only re-run be reported.** New
paragraph, `appendix.tex:1617` (p55). Three things bound it, and one is not possible:

1. **Execution is verified on the axis H1 uses.** The three-category $\alpha$ of 0.728 understates
   agreement on the only distinction H1 depends on: $\alpha = 0.956$ on $D{=}1$ vs. $D{=}0$ in EXP-C4, and
   0.846 on 120 human-coded EXP-C4B items.
2. **The disagreements run conservative.** Nine of ten in EXP-C4 and seven of eighteen in EXP-C4B sit on
   the CORRECTED/EVASIVE boundary, which does not enter $D$ at all; the single EXP-C4 disagreement touching
   $D{=}1$ moves *against* us — the machine label **understates** $D{=}1$. A human-adjudicated relabelling
   would, on the observed disagreements, *add* $D{=}1$ trials.
3. **Grader family is not the driver:** a third-family grader agrees at $\alpha = 0.886$ on the $D$-binary
   axis over 600 trials.

**What we cannot do is re-run H1 on human labels alone**, and we now say so rather than leave it looking
declined. The hand-coded subsamples are **12 items per target** (60 in EXP-C4, 120 in EXP-C4B), while H1's
inferential unit is the *claim*, with folds grouped and permutations run within claim. Twelve items span
too few claims to support a claim-grouped permutation test at any useful power, so a human-only H1 would be
**uninformative by construction rather than reassuring**. The paragraph closes: the construct of $D$ rests
on the belief screen and on the design, and a differently operationalized $D$ is a question this design
cannot settle.

**Q4 — a concise formal statement of the Proposition's assumptions.** This was the one question with no
answer anywhere in the paper. New passage, `appendix.tex:51–55` (Appendix A, p14), three short paragraphs
rather than a theorem environment, because our own position is that the algebra is standard:

- **(A1)** every latent mechanism $M_1,\dots,M_k$ is a descendant of $E$ and none is observed;
  **(A2)** the only available intervention is $\mathrm{do}(E)$; **(A3)** the only observables are
  $(V,E,S)$; **(A4)** *no exclusion restriction* — no observable is a child of exactly one $M_i$;
  **(A5)** no parametric restriction on $S$'s structural equation.
- **(A4) is the assumption doing the work**, and it is a factual claim about the audited designs, not a
  modelling convenience: in an instructed benchmark every observable the detector reads is downstream of
  the same prompt edit.
- *Why it follows*: under (A1)–(A5) every computable quantity is a functional of
  $P(S,V \mid \mathrm{do}(E))$, which is reproduced exactly both by a witness with $D$ severed from $S$
  (so $\tau_D = 0$) and by one in which $D$ carries the whole effect — so $\tau_D$ is not a functional of
  the observed distribution, and since the admissible set spans 0 to all of $\tau_E$, it is **neither
  bounded away from zero nor signed**.
- *What would break it*: an exclusion restriction (an instrument); a parametric assumption strong enough to
  allocate the effect, which then carries the attribution rather than the data; or $\mathrm{do}(D)$, i.e.
  rung 5. **Criterion 4 negates (A3), not (A2)** — it makes $E$ degenerate and grades $D$ from a channel
  outside the detector's input, so $D$ becomes *observed* while remaining *unmanipulated*. That buys rung 4
  and not $\tau_D$.

It ends: *"The algebra is standard; what this paper contributes is the protocol that enforces it on a
published benchmark."*

**Q5 — is the five-criterion framework proposed as necessary, or as one reasonable set.** Proposed as
necessary by us, not established as canonical, and the abstract now says so: *"five criteria **we propose
as necessary** before accuracy licenses a deception claim"* (`abstract.tex:2`; it previously said
"required"). The rest of the framing was already in place: §2.2 states *"the five are **not claimed to
characterize every valid deception benchmark** — they rule out specific alternative explanations"*; Table 2
groups them under headers reading *"Three alternative-explanation diagnostics"*, *"One construct-validity
test"* and *"One robustness test — **not a construct-validity test, and not equally fundamental**"*; and
Appendix A separates the two axes (who can apply a criterion vs. what it identifies).

**Q6 — model coverage, and separating the structural from the empirical claim.** Already answered in the
appendix, and now stated in the main text too. `appendix.tex:502` gives the three-way split verbatim —
identification is **vintage-independent** (it is a property of the design), the *activity* of the confound
is demonstrated on the models we ran, and the **magnitudes are vintage-dependent**. `app:r1d` reports our
attempt at a recency check on four current-generation models as **inconclusive**. The main-text one-liner
is the asymmetry sentence in §3 above, which names the 3B–14B scope of the criterion-4 result explicitly.

## Recommendations already in the build (quoted, not newly added)

**§4 / §13 — keep the establishes/does-not-establish box, and keep criterion 4 explicitly sub-causal.** The
box is at `methodology.tex:85–87` (p6) and this round *extended* it rather than touching anything in it.
`fig:ladder` (p5) draws five rungs with rung 5 dashed and *"no design audited here"*, and prints between the
rungs *"↑ **this paper reaches rung 4, not rung 5**"*. §3.5 closes on *"**The purpose of criterion 4 is not
to establish that deception is generally detectable; it is to establish that the canonical benchmark's
failure is not an impossibility result.**"*

**§7 — the lexical rule is diagnostic, not confirmatory.** §3.3 already said *"we quote the **range**, not
its upper end"*; it now also says *"and the rule was **not pre-specified, so this is diagnostic rather than
confirmatory**"* (`experiments.tex:70`). Table 1's caption already read *"unmarked = exploratory, including
the lexical rule and the factorial"*, and §3.1 already declared the nine pre-registered analyses *"the only
confirmatory results, everything else exploratory"*.

**§8 — "knowledge conflict" reads as causal.** The body already disclaimed it: *"the residual signal
covaries with model knowledge; **this does not identify knowledge conflict as its cause**"*. The causal-
sounding site was the **§3.3 heading**, which now reads *"What Survives Is Reproducible from Surface
Behavior and **Model Knowledge**"* (`experiments.tex:67`). We did not mass-replace the term in body prose,
where it names a mechanism under test rather than an established cause.

**§11 — sharpen the novelty statement against the two adjacent literatures.** Expanded in the related-work
appendix, which is not page-constrained (`related_work.tex:73`):

> **Three questions, and only the third is ours.** The generalization studies ask *does the detector
> transfer*, and answer no; the belief-verified organisms ask *can a valid contrast be built*, and answer
> yes, going *beyond* criterion 4 with $D$ **set** rather than observed. Neither asks *whether the published
> accuracy licensed the deception reading in the first place* — and that is a different question in two ways
> that matter. **It is decidable from a benchmark's description alone**: requirements (i)–(v) are properties
> of a design, so an auditor who never runs the detector can settle them… And **it is invisible in the
> benchmark's output**: the reported accuracy is the same number whether or not the criterion holds, so no
> amount of transfer testing, scale, or held-out evaluation surfaces it.

It closes by conceding the constraint itself is *"a standard non-identifiability result, whose premises we
state in full"* — now a live pointer, to the Q4 passage above.

**§14 — ICLR 2027 formatting.** You checked and found it compliant; nothing changed.

## What we are declining, and why

**§10 / §12 / §15.4–15.5 — reduce the machinery, restructure §3, cut the number of headline results.** We
are declining the restructure, and the reason is a budget fact we would rather state than disguise: **the
main text ends on line 485 of page 9 against a ceiling of 485 — zero slack**. §3 already *is* four
experiments (§3.2 equalization, §3.3 surface behavior and model knowledge, §3.4 the third paradigm, §3.5
criterion 4), the framework already precedes the empirics, and the machinery is one pointer paragraph plus
an appendix roadmap table. Any further restructure would have to be paid for by deleting a result, a null
or a disclaimer.

**What we did instead, in the same spirit:** we **compressed the abstract**, which is where the discipline
you are asking for was actually affordable. Cut from ¶2: the paraphrase-probe diagnostic (retained in
fuller form at `experiments.tex:65`), *"two mechanistically distinct detectors failing under one control"*
(retained at `introduction.tex:69`), and two parentheticals. The abstract is now net shorter, and the
paragraph leads on the three things you said a reader should retain. Two further main-text details — the
resample design and the 16.8–68.2% realization rate — moved to the appendix to pay for the additions above;
both are stated there in fuller form, and the verifier asserts it.

**No new experiment, and no new criterion-4 targets.** The roster is sealed by `PREREG_EXP_C4B.md`'s
substitution rule, all ten targets are graded, and re-drawing after seeing counts is precisely the move
that rule exists to prevent.

## Where we agree the paper will not improve

**Novelty 7 stands, and we are not going to argue it.** The paper says it itself: *"the protocol and the
audit, not the algebra, are what is new"* (§1), and the related-work appendix concedes the constraint is a
standard non-identifiability result. Your remark that *"one reviewer could reasonably give it a 5 because
the central conceptual result is largely obvious"* is not something an edit closes, and we have not tried
to edit around it. The new Q4 passage makes the algebra *more* explicitly standard, not less.

**The criterion-4 result is what it is:** three of five in EXP-C4, two of those three replicating under a
blinded Holm-corrected re-run, one of five *new* targets positive. This round makes it look weaker on
purpose. It also stays observational — stratified at fixed $E$ — so a latent $U$ with $U \to D$ and
$U \to S$ survives it, which is why the paper stops at rung 4.

**EXP-R1d remains inconclusive** and is reported as inconclusive.

## Provenance (a footnote, not a defence)

The build you read, `main(20260917-095844).pdf`, predates five same-day commits: `617afe2` (11:33, EXP-R1d
reported inconclusive), `6be0c8c` and `1e74165` (12:49, the scikit-learn 1.8.0 reprint), `999ff78` (14:29)
and `6826848` (15:21, the previous round's precision fixes). **None of them touches anything you raise**, so
unlike our previous response there is no staleness story here — your review applies to the current text, and
the must-fix was live in it.

## Verification

`latexmk` exit 0; **79 pages** (9 of main text, unchanged); 0 overfull hbox, 0 overfull vbox, 0 undefined
references or citations; bibtex 0 warnings; main text ends p9 at ruler 485 with **slack 0**; all eight float
pins on their recorded pages (Figure 1/p2, Table 1/p3, Table 2/p5, Figure 2/p5, Figure 3/p6, Table 3/p8,
Table 4/p14, Table 6/p18 — the last moved by one page because the Q4 passage is upstream of it). An
automated checker of **688 assertions** passes, up from 601, with 87 new ones for this round: the standing
count present at all six main-text sites and both corrected appendix sites; the unqualified "deception is
nevertheless detectable" absent from every section file; the asymmetry sentence present *inside* the box; no
appendix paragraph reporting three of five without the standing count; the five assumptions (A1)–(A5) and
the statement of which one criterion 4 negates; the "12 items per target" limit; the three novelty
sentences; that the two details moved out of the main text are present in the appendix; and the
cross-file consistency check described in §1 — the one that would have caught the defect you found.
