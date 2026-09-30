# Response to Review, Round 54

**Assertion count: unchanged at 2591.** No experiment ran, no number moved, `equivalence.py` was
untouched, and `verify_claims.py` cannot read the `.tex` by design (its own note, line 6337: *"this file
cannot read the .tex, so the .tex is checked against the log separately by `check_tex_numbers.py`"*).
This round's change is a source-structure change, so the check that would have caught it belongs in the
`.tex` gates, not in the verifier. **One new gate assertion was added there; `check_protected_claims.py
--control` rises 22 → 23.**

You asked for no new experiments (§22) and no widened claims (§23). Both accepted literally: **the entire
body diff this round is two lines of one file, +78 characters, 0 rendered lines, 0 pages.**

---

## 1. The build you read, and what has moved since

You name `iclr2027_conference(20260910-032034).pdf`. Eleven of eighteen source files are newer than that
timestamp, so you are the most current reviewer in six rounds, but three bookkeeping numbers you quote
have moved:

| you quote | current | note |
|---|---|---|
| 2304 assertions | **2591** | grew in rounds 49–53 |
| 43 experiment tags | **85 indexed runs** | |
| 90 pages | **100** | appendix growth only; body still ends p9 |

**Every result number you quote is current**: 0.994/0.500, 0.872/0.941, +0.012/+0.200/+0.429–0.845,
0.987/0.0005, 0.723. Nothing you scored on has changed underneath you.

Files newer than your build: `abstract` (9-11), `figure_audit` (9-11), `figure_framework` (9-12),
`introduction` (9-12), `conclusion` (9-12), `related_work` (9-12), `experiments` (9-13), `statements`
(9-13), `figure_novelty_cost` (9-13), `appendix_domain_guards` (9-13), `methodology` (9-13, this round).

---

## 2. The defect, and it is ours: §3 filed the paper's own proved result under "open"

You scored **Theoretical contribution 7** and wrote (§7) that *"Theorem 1 is essentially a formalization
of [the intuitive claim]"*, against your stated bar: *"we prove useful properties of this principle."*

**You were reading the body correctly. The body was wrong about itself.**

§3's paragraph *"What is and is not guaranteed. Four kinds of claim, kept apart"* enumerated (i) necessary,
(ii) methodological, (iii) empirical, and: verbatim, before this round:

> and *(iv) open*: completeness is unreachable (Cor. 3; Props. 2, 3).

Proposition 3 is a **proposition with a proof**. Its own statement ends *"certification is unreachable by
admissibility rather than merely unbuilt by us"*, and the commentary beneath it reads *"What the
proposition does **settle** is the question a reviewer is entitled to press."* **The appendix said
settled. The body said open.** So the one paragraph a reviewer reads to score "theoretical contribution"
presented a four-item list in which nothing was a proved non-definitional property, because the two that
were had been filed under *open*.

That is also, exactly, the idea your §22.2 asks us to make impossible to miss. One mislabelled word cost
us two rubric lines.

**Repaired.** `methodology.tex:174` now reads *"and **(iv) Proved, not open**: completeness is
unreachable (Cor. 3; Props. 2, 3)"*: renders **p6, line 273**. The standing concession phrase
*"completeness is unreachable"* is preserved verbatim and all three references are unchanged. Cost: **+12
characters, no rendered line.**

One thing this repair does *not* do, stated because you would find it: the clause keeps the word *open* only
as a negation; it does not say what **is** still open (which family to declare). Naming that costs a rendered
line, and clause (iv)'s final line has **1.73pt ≈ half a character** of tail on a page carrying **−1.927pt** of
slack, with §3 sitting on the paper's only two negative-slack pages. So the label is corrected and the open
question is left unnamed *here*; it is named in the commentary beneath Prop. 3: *"the reach of an audit is
exactly what it enumerates, so **which** controls are declared still decides how much a result rules out."*

**No gate here could have caught it, and that is the more useful finding.** Every check in this repo asks
whether a claim is *present*, or *cited*, or *reachable from the body*. None asked what a present, cited,
reachable claim is **filed as**. This is the fifth occurrence of that failure class in this paper's
history: an object missed for what it is *called*, and the first to land on the theory.

So the round adds the gate that would have caught it (`check_proved_not_open`). It locates the four-kinds
items by their `\emph{(n)~label}` structure, collects every label declared inside a `theorem` /
`proposition` / `corollary` / `lemma` environment document-wide, and asserts: **an item that cites a
proved result must say it is proved.** It currently reports *"9 proved labels; 2 of 4 four-kinds items
cite one (i→1, iv→3), and every such item's label says so."* Its control reverts the label and FAILs with
the round-54 defect by name.

The assertion runs *from the citation*, not from the label, deliberately. My first version checked only
items already labelled "open", which would have passed **vacuously** the moment the defect was repaired,
and would still have passed if a later round relabelled (iv) to something merely *neutral*. Both
weaknesses were caught before shipping and both now fire.

---

## 3. What else shipped, and what did not

**§3 now states the twin-exactness result as a proved property** (`methodology.tex:176`, renders **p6
line 277**):

> The test is the twin, per instance: a member is pinned at exactly 0.500 — ***every* invariant map is, by
> proof (Prop. 4)** — so a baseline reading arrangement cannot enter however well it scores.

This is the direct answer to your §8 (*"is admissibility just matched controls?"*): the supremum over
$\mathcal{A}_P$ (**every** arrangement-invariant map, declared or not, at any capacity, readouts
included) is **exact and attained** at the twin. Matched controls are a practice; this is a property that
practice does not have.

It was written as an *additive* aside rather than a replacement, on purpose. The appendix note at
`prop:twin_exact` warns that the caveat governing observation⇒invariance and the proposition's
invariance⇒0.500 *"are not the same statement"*, and that reading one as the other *"is exactly the
conflation it is stated to remove."* An earlier draft of this edit committed that conflation. The shipped
version states both directions and keeps them distinct. Funded by two same-paragraph cuts (`, so ` → `: `
and `by running the same test` → `by the same test`); no claim removed.

**Figure 1's caption was not changed, and here is the measurement.** Your §21 sentence deserves to be on
the object you nominate as the visual center. I could not pay for it. The caption's last rendered line has
**30.25pt ≈ 8 characters** of tail on a page carrying **+0.001pt** of slack; the cheapest principle-lead
rewrite I could draft measures **+29pt in bold**. And no cut is available inside it: the S1–S3/coverage
clause is a round-47 requirement that *"replaces, rather than adds to"* its predecessor, the "two steps"
count is a round-46 correction caught by reading the figure against its own caption, and the band mention
in the lead answers round 47's §8. Cutting any of them would delete a predecessor's requirement to answer
yours. The principle is on **p1** (abstract, first sentence) and **p2** (`introduction.tex:10`, bold:
*"The criterion, in one sentence…"*).

**§15, intervals: swept rather than asserted.** You write that run-to-run uncertainty is *"around
±0.03"* while *"some results are reported without intervals reflecting this uncertainty."* I greped every
GIN, Transformer and Tree-LSTM numeral in the six body files, comment-stripped:

- **Every GIN and Transformer number in the body carries an interval or an explicit non-reproducibility
  statement.** `experiments.tex:250` prints **.881 [.850,.909]** and **.511±.026** and states *"Neither
  GIN number reproduces on MPS"*; `:271` gives the Transformer as an interval only, **[.588,.746]**, with
  no point value. **Neither encoder appears with a number in the abstract at all**: round 46 removed
  both for this reason, and the removal holds.
- **Every inferential contrast carries a bootstrap interval**: `+0.012` *CI covers 0*, `+0.200`
  **[0.163,0.237]**, `+0.070` **[0.021,0.115]** (`experiments.tex:309–311`), and the discipline is stated
  in print at `:379`: *"every interval above is a class-level bootstrap"*, with inferential claims
  restricted to the prespecified contrasts.
- The headline Tree-LSTM accuracies are point values in prose (0.994, 0.987, 0.894, 0.736), each quoted
  against a comparator that is **exact by proof** (0.500), **on the floor** (0.0005), or **at chance**
  (0.005): gaps of 0.49, 0.99, 0.73. `0.894` additionally prints *"0.181 clear of the encoder's
  bootstrap lower bound."*

One correction worth making: **our own envelope is wider than yours.** Round 53 measured four-invocation
bounds of **0.047** (GIN) and **0.062** (Transformer) in Appendix AK. Your ±0.03 is the Transformer's
*two*-invocation figure. The paper is already more conservative than the complaint, so there was nothing
to repair, but you were right to make it checkable, and it is the one place in the review that named a
falsifiable claim about our reporting.

**What I could not pay for, stated plainly.** §3 still contains this sentence (p5, line 254):

> These numbered results are billed as *scoping*, **not as theoretical contributions** — they fall out of
> the definition below — but what follows *from* them is not definitional: closure puts a trained readout
> *inside* the family (Prop. 1), and the ceiling is then measured non-monotone in resolution (Cor. 2).

It names **two** of the four non-definitional results, naming neither Prop 3 nor Prop 4. It is the
sentence your §7 score comes from, and it tells a reviewer not to score what follows it. Its last rendered
line has **46.14pt ≈ 12.5 characters** of tail, and every candidate cut in that paragraph is a
predecessor's requirement (round 39 granted the *"billed as scoping"* clause itself). §3 spans p5 and p6,
the paper's **only two negative-slack pages** (−0.695pt and −1.927pt); the p7–p10 run carries 0.000pt, so
one new line in §3 moves the conclusion off p9 and the body to ten pages. **I am flagging this rather than
forcing it, and it is the first thing I would spend page room on if any existed.**

---

## 4. Your five §22 changes, measured: with the rendered page for each

You anticipated this section yourself (§22.2 *"You already do this"*; §22.5 *"You have essentially this
already in Table 1"*; §21 *"The current paper says this, but it gets buried"*), so I am **not** offering
it as a rebuttal. §2 above is the concession. This is only the page numbers, so you can check them.

| ask | where it is | page |
|---|---|---|
| **§22.1** decision-tree flowchart as the visual center | **Figure 1** (a node-for-node match to your ASCII sketch: claim → *"can a P-invariant control solve the task?"* → yes-exit *"the experiment decides nothing"* → declare $\mathcal{F}$, measure its ceiling → *"above that ceiling?"* → no-exit *"no evidence about P"*) plus a graded band you did not ask for | **p2** |
| **§22.2** "falsification, not certification" unmissable | abstract: *"A pass rules out the declared alternatives, and **no** admissible family can turn it into a certificate"*; Figure 1's terminus cell *"never mechanism: never certification"*; Table 2's row *"**falsification tools, not certification tools**"*; conclusion's pinned exit *"The audit falsifies; it certifies nothing"* | p1, p2, p6, p9 |
| **§22.3** never say "compositional reasoning" unaccompanied by a denial | **6 rendered body occurrences, all 6 negated or disclaimed, zero affirmative** (counted off the render, not the source; one lives in a float): *"That is **not** compositional reasoning"* (p1), Figure 1's terminus cell *"compositional reasoning **out of reach at any width**"* (p2), Table 2's row *"General compositional reasoning — **out of reach in principle**"* (p5), *"passing establishes **not** compositional reasoning"* (p6), *"still **not** compositional reasoning"* and *"**not** systematic compositional reasoning"* (both p9) | p1, p2, p5, p6, p9 |
| **§22.4** compress revision history to one paragraph | **already done: 0 comment-stripped instances in the rendered body.** It lives in source comments and in Table 11 | Table 11, **p37** |
| **§22.5** make the comparison table the novelty argument | **Table 1**, 8 data columns, 3 bold, `strongest baseline` row **×** in all eight, and a caption that already *is* the argument: *"**Takeaway: ``strongest baseline'' clears nothing** — × in all eight columns: strength is not blindness, which is what the three bold columns test, and **no prior row attains any of them**: that conjunction is what is new"* | **p4** |
| **§21** the one sentence | `introduction.tex:10`, bold: *"**The criterion, in one sentence:** a learned representation h is evidence for a property P only if it outperforms the **best** representation in a **declared** family $\mathcal{F}$ invariant to P… declared, never complete"*, and the abstract's opening | p1, **p2** |

Two of your objections **are** our claims, and I agree with both rather than defending against them:

- **§1, does the Tree-LSTM show compositional generalization?** No. `experiments.tex:68` says
  *"composition-sensitive structural discrimination, not algebraic-equivalence generalization"*, and
  Figure 1 puts *"compositional reasoning out of reach at any width."*
- **§7, not mathematically deep.** Agreed, and we wrote it first. The appendix already says *"A reader who
  finds the theorem close to a restatement of what an admissible family means is not disagreeing with
  us."* §2 above is why you could not see the results that are not restatements.

**§13, the contribution hierarchy.** §1's three items sit under the heading *"Applying the criterion
changes conclusions, in three places"*: the criterion is the paragraph's premise and the three items are
its applications, which is how round 50's identical ask was resolved (by demoting a label, not
re-ordering). A fourth item is doubly pinned: a gate compares the counted parenthetical to the appendix
list, so the word *"three"* is frozen, and the paragraph's last rendered line ends on p3 at **98 of ~100
characters** against p3's 0.57 of a line.

---

## 5. The honest part: these positioning answers have not landed, four rounds running

| ask | rounds it was raised | how it was answered | score after |
|---|---|---|---|
| decision figure as the visual center | 19, 26, 38, 46, **54** | Figure 1 built, then promoted to p2, then given a graded band | 7 |
| make the comparison table the novelty argument | 47, 50, **54** | caption rewritten to lead on the `strongest baseline` row (47), two columns added (48, 50) | 7 |
| contribution hierarchy in §1 | 50, **54** | label demoted so the criterion reads as premise | 7 |
| clarity / burial under machinery | 53, **54** | consecutive | 7 |

Four reviewers have now asked for objects that exist on pages 2–4, and each round answered by making the
object more prominent. The score did not move. **That is evidence the answer is not prominence**, which is
why this round spent its effort on §2 instead: a mislabel that made a real result invisible *as a result*,
which is a different failure from a real result being hard to find.

So the question I would most like answered: **Table 1's caption already states the novelty argument in the
words you asked for. You read it and asked for it anyway.** What does a reader need that the caption
cannot give them: a different object, a different location, or a claim we are not making? A reviewer who
reads the takeaway and still reports it missing is telling us something the caption cannot fix, and I
would rather learn what it is than rewrite the caption a third time.

---

## 6. Verification

0 errors · 0 `(Reference|Citation).*undefined` · 0 `Float too large` · exactly **2** pre-existing overfull
boxes at **unchanged sizes** (`\vbox` 6.4211pt, `\hbox` 3.509pt) · **100 pages** (`pdfinfo`) · Figure 1 p2,
Figure 2 p3, Table 1 p4, Table 2 p5, Figure 3 p8 · §4.3 p8, §4.4 p8, §4.5 p9, §5 p9 · body ends p9 ·
`E THICS S TATEMENT` the first body line of p10.

**Slack profile byte-identical to the pre-round baseline** across all three edits: p1 +0.561 · p2 +0.001 ·
p3 +6.624 · p4 +0.000 · p5 −0.695 · p6 −1.927 · p7–p10 +0.000 · p11 +0.687.

Four gates PASS; controls **23 / 9 inline / 1 / 2**. `check_reviewer_map`: 18 rows, 305 checks, 52 literal
`load_log()` sites, 56 appendix letters. `verify_claims.py` **2591/2591**, exit 0, md5
`85e77e416b9b89fce4665bff4805348c` identical across all three copies; `REPRODUCE.md` md5
`a24ec83efcbe97fb7f69758a028e0a66`. Content-loss diff against a pre-round `cp -p` snapshot: **one file
changed, two lines, nothing removed but `, so ` → `: ` and the word `running`.** Renders of p5 and p6 read
at 300 dpi. `artifact/iclr-supplementary`: 0 `__pycache__`, 0 `.pyc`, 0 home-path hits, 0 author-name hits.
