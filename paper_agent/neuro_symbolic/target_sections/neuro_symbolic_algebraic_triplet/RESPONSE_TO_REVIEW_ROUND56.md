# Response to Review, Round 56

**You named the battle yourself, twice: whether admissibility auditing is a methodological contribution
or "a formalization of good experimental hygiene." Here is the answer in one sentence, and it is not a
new claim; it is the one thing in §3 that is *proved* rather than defined, which the paper had left out
of three of the four places it compresses itself.**

Good experimental hygiene tells you to pick a strong control. Admissibility auditing tells you which
comparisons *can* be evidence at all, and it does that by making the object of inference a **ceiling**
rather than a score: the supremum $\sup\nolimits_{g\in\mathcal{F}}M(g)$ over a **declared** family whose
membership is **tested per instance** and which is **closed over trained readouts**, so the number a
paper prints is a **result, not a stipulation**: measured at every rung, and at the shape-matched twin
*proved* (Proposition 4). That last clause is the load-bearing one, and it is why this is not hygiene:
hygiene has no theorem. Proposition 1 proves that a *trained* readout over an
admissible feature map is *itself* an admissible member, which means (a) a ceiling reported with one
fixed readout is a **lower bound on the paper's own statistic** (we found that defect in our own
instrument and repaired it, at $0.276 \to 0.2962$; (b) the ceiling is **non-monotone in resolution**, so
"use the strongest baseline" is not merely incomplete advice but wrong advice (Corollary 2); and (c) **no
admissible family can certify**, at all, ever) certification is *unreachable by admissibility*, not
merely unbuilt by us (Proposition 3). None of (a)–(c) is available to anyone who combines invariance
tests, counterfactual evaluation and adversarial controls, because none of those three names a family or
estimates its supremum.

**What changed this round: the paragraph headed "What is new" now says the new thing; it did not, before
you read it, and so does the criterion sentence on page 1.** Of the four places the paper compresses
itself, three were missing readout closure; two of those three are fixed, and the fourth, the
conclusion's recipe, is short by one character of tail, which we price and account for at the end of this
letter rather than leave you to find.

**Assertion count: unchanged at 2591**, exit 0, md5 `85e77e416b9b89fce4665bff4805348c`, identical across
all three copies. No experiment ran, no number moved, `equivalence.py` untouched. You wrote that you
"would not add more experiments": the third consecutive reviewer to say so, so none were added and
none were needed. `verify_claims.py` cannot read the `.tex` by design (its own note, line 6337), so a
round whose diff is entirely prose structure is checked by the four `.tex` gates instead: **two new gates,
`check_contribution_closure` and `check_ceiling_universals`, and `check_protected_claims.py --control` rises
25 → 29** (four, not two: each check has two independently corruptible halves, and each half fires its own
control).

**And the page budget, because it decided the shape of every edit below.** The body is nine pages of a
ten-page limit and page 10 must open on the ethics statement. Total slack across the eleven measured
pages is **17.55pt**; a rendered body line is **11.6pt**; the largest single pocket is **9.463pt**. So
the paper cannot absorb one new line anywhere. **Every change this round is either inside the tail of an
existing rendered line or net-negative in length.** The eleven-page slack profile is byte-identical to
the 14 September build you reviewed, and the document is still **101 pages**.

---

## 1. Your #1 and #3, shipped, with the rendered page and the measured cost

### #3: the Related Work paragraph that answers the novelty objection (your own highest-value item, "0.5–1 reviewer point")

This is where the round's real defect was, and it was worse than you diagnosed. **§2's paragraph is
literally headed "What is new, given all of that", and it omitted readout closure, the one item in the
paper that is proved rather than definitional.** Readout closure is a *column of Table 1*. It is what
round 48's reviewer named as the differentiator. And the paragraph a reviewer reads to score novelty did
not mention it. That is not a rhetorical failure; it is a routing failure, and it explains a Novelty
score that has not moved in four rounds of promoting the comparison table.

Page 3, both halves funded by swaps inside the same paragraph:

> **before** — "…**none estimates $\sup\nolimits_{g\in\mathcal{F}}M(g)$, the *ceiling* of a declared
> family**. […] recent theory derives shortcut bias from training-data structure (Lippl & Stachenfeld,
> 2025); we ask what a comparison is *capable* of establishing."
>
> **after** — "…**none estimates $\sup\nolimits_{g\in\mathcal{F}}M(g)$, a declared family's *ceiling*
> over *trained* readouts**. […] theory derives shortcut bias from training data (Lippl & Stachenfeld,
> 2025); **the *ceiling itself* is our inferential object**."

The second half adopts your phrase. You asked for "the ceiling itself is the inferential object"; the
paper had the same object under a different name ("the audit statistic"). Naming an object two ways is
this paper's dominant failure mode across sixteen reviews, so your word wins.

**Cost: −8.4 rendered characters.** Six rendered lines before, six after; the paragraph's last line went
from 2.6 to 11.0 characters of tail. Round 50's "in isolation" clause and round 52's "a guessed
comparator, perturbation, or *adversarial* search" are untouched, and `\sup\nolimits` is byte-identical
to the boxed display on page 1.

### #1: the contribution sentence, explicit in the abstract *and* the first paragraph, family closed over trained readouts

The abstract half has been shipped since round 46 ("*trained* readouts included", page 1 ¶2). The first
paragraph was the half that was missing. Page 1, last three lines before the boxed display:

> **The criterion, in one sentence: a learned representation $h$ is evidence for a property $P$ only if
> it outperforms the *best* representation in a *declared* family $\mathcal{F}$ invariant to $P$ —
> ***trained* readouts included** — under the same protocol and score $M$; declared, never complete.**

**Cost: 0pt.** Measured before writing it: that sentence's last rendered line had **155.00pt** of tail on
page 1. The insertion consumed ~30 characters of it and the paragraph still ends on the same line, with
12.1 characters to spare. The second em-dash pair required swapping one comma to a semicolon; nothing
else in the sentence moved, and the boxed display below it (round 44's grant) is untouched.

### Your §9: the Type-2 clone negative result, now a claim in running prose

You are right that it was buried, and right about why it matters: *"it demonstrates the method can say
No."* It existed only as a cell in the modality table on page 9. The one narrative sentence in the paper
about negative outcomes used a *different* example and mentioned the clone corpus only as a scope limit.
Page 9, inside that same sentence:

> "…the code corpus we settle is ours **(a refusal, at the corpus maximum)**, and on SCAN the audit
> *narrows*."

**Cost: 35 rendered characters into 221.80pt of measured tail**, no new line. It quotes no number, so the
table row keeps $0.987$ and $0.990$ and no assertion in `verify_claims.py` is touched. We did not write
the longer version we had drafted, because it restated "the code corpus we settle" from one line above:
"settle" already means settled below S3, which already means refused.

---

## 2. Your §3, §4 and §18, answered together, and the concession we deleted

You wrote three versions of the same objection: §3, *"the theoretical results are largely consequences of
the proposed definition"*; §4/§18, *"much of the theoretical machinery formalizes this limitation rather
than overcoming it."*

**You were quoting the paper back to us.** §3 said, in the paper's own voice: *"These numbered results
are billed as scoping, **not as theoretical contributions** — they fall out of the definition below."*
That is the seventh time in sixteen rounds that a pre-emptive concession the paper volunteered has come
back as the reviewer's objection, in the reviewer's own words. Three consecutive reviewers (54, 55, 56)
paraphrased that clause while scoring the axis at 7.

So the paragraph now **leads with its results** instead of with its disclaimer. Page 5:

> **before** — "**These numbered results are billed as *scoping*, not as theoretical contributions** —
> they fall out of the definition below — but what follows *from* them is not definitional: closure puts
> a trained readout *inside* the family (Prop. 1), the ceiling is then measured non-monotone in
> resolution (Cor. 2), and **no admissible family certifies** (Prop. 3) — not one of the three a property
> of suprema."
>
> **after** — "**Three of these numbered results are not definitional**: closure puts a trained readout
> *inside* the family (Prop. 1), **so every ceiling here is a *result*, never a stipulation**; the
> ceiling is then non-monotone in resolution (Cor. 2); and **no admissible family certifies** (Prop. 3:
> ***unreachable*, not unbuilt**) — not one of the three a property of suprema. **Theorem 1 itself is
> billed as *scoping*.**"

Three things to note, because each is a decision and not a rewrite:

1. **"billed as *scoping*" survives verbatim.** It was round 39's explicit grant and it is pinned by
   `check_protected_claims.py` at exactly one occurrence. It is now scoped to **Theorem 1 alone**, which
   is what it was always true of. What was deleted is the part that was doing damage: *"not as
   theoretical contributions"* and *"they fall out of the definition below."* Neither was pinned by any
   gate; neither is quoted by any row of the reviewer map.
2. **"every ceiling here is a *result*, never a stipulation" is not new text, and its first draft was
   wrong.** The claim was the *unbolded second half* of clause (e) of an appendix paragraph, on page 70,
   while the *bolded first half* of that same clause was your objection, pre-written for you. It is now in
   the body, where it answers §3. It first shipped as *"every ceiling here is **measured** rather than
   stipulated"*, and we caught that ourselves before sending: the universal is **false at the one rung this
   paper cares most about**, because at the shape-matched twin the ceiling is $0.500$ **by proof**, not by
   measurement, as §1's and §4.2's own headings say (*"a ceiling that is a theorem"*). Both copies now
   read *"a result rather than a stipulation"*, which is true of a measured supremum and of a proved one,
   and a new gate assertion forbids the present-tense "measured" universal document-wide while requiring
   the twin's proved ceiling to stay in print. Appendix BA's *"every printed $\sup\mathcal{F}_3$ was a
   lower bound on our own statistic"* had the same over-generalization and now reads *"every printed
   $\sup\mathcal{F}_3$ **but the twin's**"*.
3. **Your §18 is Proposition 3, and it is now stated as a property of the object.** "Certification is
   *unreachable by admissibility* rather than merely unbuilt by us" is the proposition's own language.
   The asymmetry is not a shortcoming of our method that fuller machinery could overcome; it is what the
   theorem says about *every* admissible family. A framework that only ever falsifies is the contribution
   precisely because the alternative is proved impossible.

**Cost: net-negative on a page carrying −0.695pt of slack.** Same rendered line count, and the
paragraph's last line gained 14.30pt of tail where it had 0.00.

**And the appendix twin was repaired in the same round**, because a disclosure fixed in the body and left
standing in the appendix is not fixed. Clause (e), page 70, strictly a re-lead: the affirmative half is
now bolded and first, the restatement concern is now the subordinate clause, and the clause is **35
rendered characters shorter**, with the page count held at 101. (An appendix edit can add a page that the
body slack profile cannot see; last round's did. This one was checked with `pdfinfo`.)

---

## 3. Your #2 (restructuring around the shape-matched twin) respectfully declined, and here is where it already is

We are declining this one, and citing your own §22 (*"be cautious about substantial changes"*) as part of
the reason. The other part is measurement: **the twin is already the paper's structural centrepiece in
four rendered places.**

| where | page | what it is |
|---|---|---|
| abstract ¶3 | 1 | opens on it: "every arrangement-invariant representation, declared or not, is pinned at exactly $0.500$ by proof" |
| §1 ¶5, under its own heading | 2 | *"The sharpest form of the test: a ceiling that is a theorem"* |
| Figure 1's graded band, cell `t1` | 2 | first cell, darkest shade: "**absolute** — the ceiling is a *theorem*" |
| Figure 2, rung 4 | 3 | the only rung whose ceiling is labelled *by proof*, $0.994$ against $0.500$ |
| §4.2 | 7 | the measured result |

**And §3 cannot open on it.** Proposition 4 quantifies over *every* arrangement-invariant map, not over a
declared family's members, so it needs Definition 1 to have been stated before it can be read as
stronger than the family-relative case. Opening §3 on the twin would put the proposition ahead of the
definition that makes it surprising, and would move Definition 1 off page 5.

If the twin is not registering as the centrepiece despite those five placements, that is worth knowing,
but it is a layout question, not a content one, and we would rather hear *where you looked* than add a
sixth copy.

---

## 4. Six of your asks measure as already in print

Not offered as a rebuttal: offered because in each case what is already there is more specific than what
was asked for, and if it is not being read, the fix is placement rather than addition.

| your ask | what the shipped PDF says |
|---|---|
| **#5** "I would not lead with 'neuro-symbolic'" | The title is **"When Stronger Baselines Mislead: Admissibility Auditing for Representation-Level Claims."** `neuro-symbolic` occurs **once in 101 pages**, on page 22, inside a sentence that *refuses* the general claim: *"They cannot establish that it is a general mechanism of neuro-symbolic tasks."* Zero occurrences in the abstract, in §1, or in the title. §1 already says, on page 2, *"So this is a paper about evaluation, not about encoders"* |
| **§5** never say "we establish that the model has learned structure" | Page 6 already states your formulation, in the paper's own words: *"passing establishes not compositional reasoning, only that the learned representation exceeds **every member** of a prespecified, enumerated family under the stated protocol — **it does not establish that $\mathcal{F}_3$ contains all $P$-invariant explanations**"* |
| **§8** do not count SCAN among the strongest validations | Page 9 already prints *"against $\sup\mathcal{F}_3{=}0.0005$ — **and their design puts the admissible bar on the floor**, so we quote no ratio"*, and the same page says *"on SCAN the audit **narrows**."* Your ask is our own caveat |
| **§17** make the statistical unit visually explicit in every major table | Table 2's caption, page 5: *"The unit of inference is the equivalence class on our corpora and the individual expression on the two external ones."* Page 9 in prose: *"**The unit of inference is the equivalence class** … every interval above is a class-level bootstrap."* **Deliberately not added to Table `score5`**: that table contains no interval and no $\pm$ anywhere; it transcribes published numbers and deterministic non-learned scores, so a bootstrap-unit line would assert a statistic the table does not compute |
| **#4** reduce notation in the first two pages | Measured on the shipped PDF with `pdftotext` rather than asserted: **these items on your list do not appear on rendered pages 1–2 at all**, F1, F2, the five novelty axes, E3, E3b, E3m, UnseenEqClass, class-level bootstrap, leakage. `coverage` appears **once**, in Figure 1's caption, where it is round 47's granted clause distinguishing a cue *level* from the family that reads it. $\phi_d$ appears **once**, at its own definition of order-blindness, not as a forward reference |
| **§11** the 90-page appendix must not be load-bearing | See §6 below: answered as a check, not a promise |

---

## 5. Your #1 and your #4 contradict each other; we resolved in favour of #1

**#1** asks for readout closure to be explicit in the abstract and the first paragraph. **#4** lists
readout closure among the notation to defer off the first two pages. Both cannot be done.

We chose **#1**: it carries your higher weight, and it addresses the axis you named as the bottleneck.
The consequence is measurable and we would rather state it than hide it: "readout" now appears **six**
times on rendered pages 1–2, at six distinct sites: abstract ¶2, §1's criterion, Figure 1's box 3,
§1's three-object ladder, §1 ¶5's twin sentence, and §1's audit-versus-baseline list. If you consider that a net loss on clarity, say so and we will invert it; but a
Novelty score of 6.5–7 and a Clarity score of 7.5 make the trade look one-directional.

This is the fourteenth consecutive round in which a reviewer's proposed edit would delete a predecessor's
requirement. This round's three, named for the record: **#4** (deferring `coverage` deletes round 47's
granted Figure 1 clause; deferring readout closure deletes your own #1); **§17** (a bootstrap-unit line
on Table `score5` asserts a statistic that table does not compute); **#2** (restructuring §3 around the
twin puts Proposition 4 ahead of Definition 1).

---

## 6. §11: what the body proves without the appendix

Answered as a check rather than a promise. Every item below is printed on pages 1–9 with its number, and
a reviewer who reads no appendix can verify each one against the figure or table cited:

- **the criterion**, boxed display, page 1: `evidence about P requires M(h) > sup_{g∈F} M(g)`, not
  merely $M(h) > M(g)$;
- **the twin's exact ceiling**: $0.500$ by proof against a Tree-LSTM's $\mathbf{0.994}$, page 2 (§1 ¶5),
  page 3 (Figure 2, rung 4), page 5 (Table 2);
- **the AI Feynman inversion**: a zero-parameter variable bag at $\mathbf{1.000}$ against $0.972$, pages
  1, 3 and 5;
- **the adversarial search**: best of 706 candidates at $0.676$ against $\mathbf{0.894}$, pages 1 and 3;
- **the clone refusal**: every $\mathcal{F}_3$ member at $0.990$, the corpus maximum, page 9 (table and,
  as of this round, prose);
- **the SCAN narrowing**: an operator/arity bag at $\mathbf{0.941}$ against an 80M encoder's $0.872$,
  pages 3 and 9;
- **the novelty grid**: Table 1, page 4, six axes, no prior device attaining all of them;
- **every audited claim, its strongest admissible control and its verdict** on one page: Table 2, page 5.

The appendix is where the searches, the seeds, the negative results and the released auditor live. It is
not where any of the eight items above is established.

---

## 7. Your §22: before submission

- **No substantial restructuring**, per your own caution: the round shipped four prose changes and one
  gate, and the eleven-page slack profile is byte-identical to the build you reviewed.
- **Supplementary packaged from the redacted copy**, not the working tree.
- **AI-use disclosure reconciled with the OpenReview form**, without softening what it discloses.
- **PDF exported at send time**, after the final gate and verifier pass.

---

## 8. The ledger, and one question

Honest accounting: six of your asks measure as already in print, and across sixteen reviews on sixteen
different rubrics the overall score has never risen above 7. Last round we asked, "which of these did you
look for and not find, and where did you look?" **Your review supplies part of the answer: you asked us
not to lead with "neuro-symbolic," and the paper's title is "When Stronger Baselines Mislead:
Admissibility Auditing for Representation-Level Claims."** So the failure is not findability. Something
in how the paper is *shaped* is causing careful readers to reconstruct a version of it that is not on the
page.

Your review also contains the most useful sentence any of the sixteen has written: the battle is whether
this is a method or a formalization of hygiene. Our answer is Proposition 1 and its consequences (a
ceiling that is a result rather than a stipulation) measured at every rung, and at the twin *proved*:
non-monotone rather than improved by strength, and
provably incapable of certifying. Until this round, the paper said all three of those things and then, in
its own §3, told you they were "not theoretical contributions."

**So the question worth asking is narrow: does the objection survive the re-lead, or was it the
concession all along?** If it survives, the next round should stop promoting the object and change it. If
it does not, we would like to know that the paper had been arguing against itself.

---

### Verification for this round

- **101 pages** (`pdfinfo`), body ends page 9, ethics statement is the first body line of page 10.
- **Slack profile byte-identical** on all eleven pages to the build you reviewed: p1 +0.561 · p2 +9.463 ·
  p3 +9.463 · p4 0.000 · p5 −0.695 · p6 −1.927 · p7–p10 0.000 · p11 +0.687. Total 17.552pt.
- Float placements held: Figure 1 p2 · Figure 2 p3 · Figure 3 p8 · Table 1 p4 · Table 2 p5.
- **0 errors · 0 undefined references or citations · 0 "Float too large" · exactly 2 overfull boxes, both
  pre-existing, at unchanged sizes** (6.4211pt `\vbox`, 3.509pt `\hbox`).
- **Four `.tex` gates PASS.** `check_protected_claims.py --control` 25 → 29 with two new checks.
  `check_contribution_closure` was tested the only way that means anything: deleting this round's own
  clause from §1's criterion makes it FAIL, and it keys on the concept rather than on the strings shipped
  here, so a later round may rephrase freely. `check_ceiling_universals` forbids any present-tense
  universal calling ceilings *measured* (the error we caught in our own first draft of the §3 clause),
  while requiring the twin's proved ceiling to remain in print, so the check cannot be satisfied by
  deleting the exception instead of scoping the claim.
- **`verify_claims.py`: 2591/2591, exit 0**, md5 `85e77e416b9b89fce4665bff4805348c` identical across all
  three copies.
- Sentence-level diff against the pre-round snapshot, markup and comments stripped: **exactly five
  changed spans**, all four listed above plus the appendix twin, and three more from our own readiness pass
(the §3 clause, its appendix twin, and Appendix BA's lower-bound sentence). No other sentence in the body or the
  appendix moved.
- One change measured, priced and **not** shipped: the conclusion's audit recipe is five verbs to your
  §3's six, and the missing one is readout closure. Its rendered line has **4.92pt** of tail on a page
  carrying 0.000pt of slack: one character. Every candidate trim inside that sentence deletes a claim to
  buy a word, so it stands as five, and the sixth step is two rendered lines above it in the figure that
  sentence already cites: Figure 1's box 3 reads *"declare the family $\mathcal{F}$, and measure its
  ceiling $\sup\mathcal{F}$: readouts included."* The price and the exact edit are recorded in the source
  for the first round that frees a line.
