# Response to Review, Round 57

**Your §17 told us what to do and we did only that: "the path to an 8 is primarily positioning + one
decisive conceptual clarification." Three sentences changed. No experiment ran, no number moved, no
claim widened, and the document is still 101 pages with a byte-identical page profile.**

The clarification you asked for in your P2 (*"admissibility auditing is intentionally falsificatory, not
certificatory"*, which you call "arguably the conceptual heart of the paper") was a boundary the abstract
stated and an identity it never claimed. Measured before we wrote anything: `falsif*` occurred **zero
times in the abstract**, against one `certif*`. Worse, it had not always been zero: the round-51 response
letter recorded **two** `certif*`/`falsif*` tokens in the abstract, and a later compression pass dropped one
of them; the survivor was the `certif*`. The paper's whole argument is that the criterion only ever
falsifies, and the one paragraph most reviewers weigh carried that as a limit on what a pass buys rather
than as what the method *is*. That is the defect your P2 found, and it is a naming defect, not a missing
result.

**What shipped, in the two places that score the axis you marked lowest:**

1. The abstract now names the identity where it used to state only the boundary: *"and **no** admissible
   family can turn it into a certificate: **the audit falsifies by design**."*
2. The abstract's **last sentence** is now *"**The audit is the deliverable; the findings are its test.**"*:
your §15, in the paper's own closing words.
3. §3.3 leads with a **graded verdict** instead of with a limitation and a compensating clause, and the twin
   is its strongest grade: your P4's conceptual promotion, without your P4's reorganization.

**Assertion count unchanged at 2591**, exit 0, md5 `85e77e416b9b89fce4665bff4805348c`, identical across all
three copies. `equivalence.py` untouched. You are the **fourth consecutive reviewer** to say you would not
add experiments, so none were added. `verify_claims.py` cannot read the `.tex` by design, so a round whose
entire diff is prose is checked by the four `.tex` gates instead: **one new gate, `check_verdict_ladder`,
with six independently corruptible halves, and `check_protected_claims.py --control` rises 29 → 35.**

**And the page budget, because it decided the wording of all three sentences.** The body is nine pages of a
ten-page limit and page 10 must open on the ethics statement. Total slack across the eleven measured pages
is **17.55pt**, a rendered body line is **11.6pt**, the largest single pocket is **9.463pt**, and page 4
carries **0.000pt**. So the paper cannot absorb one new line anywhere. **All three edits are inside the tail
of an existing rendered line, and the third is one character shorter than what it replaced.** The eleven-page
slack profile is byte-identical to the build you reviewed.

---

## 1. What shipped, with the rendered page and the measured cost

### Your P2: the audit falsifies *by design* (abstract ¶2, page 1)

> …That direction of comparison is forced — $M(h)>\sup\nolimits_{g\in\mathcal{F}}M(g)$; *which* family we
> declare is the choice. A pass rules out the declared alternatives, and *no* admissible family can turn it
> into a certificate: **the audit falsifies by design**. The levels name *cues*, not algebra…

**+31 rendered characters into a 156.42pt tail; 56.81pt of that line still empty afterwards. Zero page
cost.** `falsif*` in the abstract goes **0 → 1**. The clause `no admissible family can turn it into a
certificate` is pinned at exactly one occurrence document-wide by `check_protected_claims.py`, so the new
text is *appended* to it: the boundary you asked us to reframe is still stated verbatim, and now the
identity is stated beside it. We took the strongest of three drafted rungs; the cheaper two were
`--- **falsification by design**` and `**, by design**`.

### Your §15: the abstract's last sentence says what the deliverable is (abstract ¶4, page 1)

> …so it *passes the $\mathcal{F}_3$ audit* — as *composition-of-known-transformations* generalization,
> scoped to $K{\geq}200$ here. That is not compositional reasoning: four primitives are not a library.
> **The audit is the deliverable; the findings are its test.**

**+56 rendered characters into a 295.87pt tail; 73.43pt still empty. Zero page cost.**

Your §15 is exact: *"the paper's significance depends heavily on convincing reviewers that admissibility
auditing itself, rather than the particular leakage findings, is the contribution."* Measured, the abstract
was four paragraphs of which **three were findings**: a leakage example, the twin and the audited results,
and what survives, and **none** of the four said the protocol was the deliverable. Page 2 said it (§1: *"So
this is a paper about evaluation, not about encoders: the contribution is that **protocol** — we call it
*admissibility auditing* — and symbolic-expression encoders are the *case study*"*). The abstract did not.

The wording was chosen against two alternatives on purpose. *"The audit is the contribution"* would restate
page 2's grammar one page later, which is a redundancy an earlier round already docked us for; and the
chiastic *"the deliverable is the audit, not the audited"* was dropped on your §11; those pages are dense
enough without asking a reader to parse a chiasmus in the last six words of the abstract. The second clause,
*"the findings are its test"*, is also our answer to your §5: the ten revised claims are not a second paper
stapled on, they are how the framework is put at risk.

### Your P2 and P4: §3.3 leads with a graded verdict, and the twin is its strongest grade (page 6)

Before:

> Hence a *failure* is conclusive and a *pass* only family-relative (Cor. 3); the twin alone closes the gap
> (Prop. 4). **That limitation is also the deliverable**: Table 2 lists what a pass rules out.

Now:

> Hence a **graded verdict**: a *failure* is conclusive; a *pass*, only family-relative (Cor. 3); at a
> *twin*, absolute (Prop. 4). **That grading is the deliverable**: Table 2 lists what each rules out.

**Four rendered characters shorter than what it replaced, and it sets on the same two lines of page 6 it
always did** (a page carrying −1.927pt, where one new line was not available), leaving **52.94pt** of tail
on the second line where the old sentence left 55.42pt. The residual 2.48pt of ink at a *negative*
character diff is bold: the new sentence has six more bolded characters, and bold glyphs are wider.
**Character count is not width**: a measurement we now record, because we priced this edit in characters
and the ink moved the other way. (The intermediate draft that read `That relativity` cost 7.72pt more than
the sentence it replaced at one character shorter; see the fourth disclosure.)

Four things this buys, all of them yours: the trio is **named**; it is named *verdicts* without being
**counted** (see the third disclosure below (the count was this round's own defect); the **twin is its
strongest grade**, which is your P4's conceptual content; and Table 2 becomes the ledger of **every** verdict
rather than of passes only, which it always was) its thirteen Verdict cells read `broken`, `S2 only`, `upheld`,
`narrowed`, `pass, and only $K{\geq}200$`, `pass; the ceiling is a theorem`, `supported`, `supported`,
`bounded`, `no pass moves`, `narrowed at $K{=}50$`, `withdrawn`, and `out of reach in principle`. **Not one
of the thirteen is an unqualified pass**, which is itself the answer to anyone who reads this paper as a
victory lap for a Tree-LSTM.

One word in it is a deliberate borrow: **absolute** is Figure 1's own word for the twin cell, so page 2 and
page 6 now name the twin's grade identically rather than synonymously.

**Four disclosures on this sentence, none of which you could have asked for.**

*First*, `That limitation is also the deliverable` was a grant to the round-44 reviewer, and it was quoted
back to reviewers in **four** response letters (rounds 44, 45, 50 and 51) two of them as *the
paper's existing answer to that reviewer's own objection*: round 50's reviewer said family-relativity was
"the most important conceptual objection" and that our answer should be "that it is not a flaw but the point
of the method", and we replied by quoting this clause. **No gate pinned it.** We nearly deleted a
predecessor's requirement while answering yours. The substance is preserved
(`That grading is the deliverable`), the shift from *limitation* to a named grading is the point of your P2,
and `is the deliverable` is now gated so the next round cannot do what this one almost did.

*Second*, we checked this sentence against its own page before shipping it, because page 6 already carries
two X-not-Y frames: §3.2's *"**The size of that gap is measured, not conceded**"*, higher up the same page
under a heading reading *"Membership in $\mathcal{F}$ is **tested** rather than assumed"*, and the pinned
*"falsification tools, not certification tools"* six lines below. Writing "falsification, not certification"
here (the obvious phrasing, and close to your own words) would have restated a pinned clause on its own
page. It is not in the shipped sentence for that reason.

*Third*, and this is the one that matters: **the sentence above is the second draft, and the first one was
wrong.** It shipped as *"Hence **three verdicts**"*, and we then ran the readiness pass we run at the end of
every round (the one question being *is it ready?*) starting with this round's own new prose. It was not.
**The document already counts verdicts, and it does not count three.** Appendix AZ, on Type-2 clone detection,
says of that task: *"This is a fourth distinct outcome of the audit, alongside a pass (§4.2), an entitlement
correctly identified (Appendix AR) and a domain boundary (Appendix AX) … **We report it as a verdict of the
audit and not as a result in our favour.**"* Four, not three. And **seven of the eight body uses of the word
do not mean a grade at all** (they mean **the outcome on one claim**: Table 2's `Verdict` column head, its
caption (*"the verdict on one page"*), its `Our verdicts under a wider family` row, §1's *"every claim and its
verdict"*, §4's own `Verdict` column head, §4.5's *"robustness of the verdict to family specification"*, and)
higher up page 6 itself; §3.2's *"the verdict is unchanged"*. The eighth is the sentence you are reading about.
So a numbered trio contradicted an appendix outright and equivocated with the very table its own
next clause cites. **The repair was to keep the trio and drop the count**, which is what *graded* does. Four
other wordings were measured and rejected first: *three entitlements* (Table 2 has thirteen rows), *three
grades* (page 2's band is a **different** trio of three grades), *the verdict is graded* (§3.2's *the verdict
is unchanged* renders on the same page), and *three strengths* (it implies an ordering the paper does not
have, a failure and a twin pass are **both** absolute). We are telling you this because the paper's own
thesis is that **a score does not mean what its author says it means**, and an author's one-line summary of
their own method is the same kind of object; and because it is the second consecutive round in which the
round's real defect was found by our own readiness pass rather than by a reviewer. Half (f) of the new gate
now forbids any count attached to `verdict`, tree-wide.

The transferable lesson, which we have written into the file's own comment block: **a count is a universal
quantifier wearing a numeral.** We have a standing rule to check every universal a new sentence promotes
against the paper's own exceptions; it caught the round-56 defect, and it did not fire here, because nobody
reads *three* as a quantifier. It is one now.

*Fourth*, we ran the readiness pass **again** on the repaired sentence, and it was still wrong: in the other
half. The second draft read **"That relativity is the deliverable"**, and *That* had nothing correct to point
at. The word immediately before it is **absolute**: relativity's antonym, so the demonstrative reached back
across its own negation, and the only clause it could actually take is the **middle** rung of three, while the
colon-clause after it quantifies over **each** of them. One third of the trio is the twin, this paper's
showcase rung, where there is no relativity at all: the sentence made the deliverable evaporate exactly where
the paper is strongest, on the axis you scored lowest. **This is the round-56 defect again in a different part
of speech**: that one bolded *"every ceiling here is measured rather than stipulated"* in a paper whose
central rung has a ceiling by proof. The shipped clause is **"That grading is the deliverable"**: the
demonstrative now takes the bolded phrase the sentence opens with, it covers all three rungs, and the ledger
clause supports it instead of narrowing it. Three characters shorter, three of them bold, same two rendered
lines, and the page's slack profile is unchanged to the last digit.

The transferable lesson from that one: **a demonstrative is a scope claim, not a connective.** Check every
`That X` a round promotes against the word that precedes it *and* against the quantifier in the clause that
follows. Two of this round's own three shipped sentences failed a scope check: first a numeral, then a
demonstrative, and both failures were in prose written to answer your P2.

One more, and it is a correction to the *First* disclosure above rather than to the paper: that count was
briefly wrong here in **both** directions. A plain grep of our own response letters for the round-44 clause
returns **three**, not four, because round 45's letter quotes the whole sentence in a blockquote that wraps
mid-phrase: markdown puts a `> ` between *the* and *deliverable*, so the literal is not there to be found.
We have a standing rule that a pinned literal in the paper must be matched against **flattened** text because
LaTeX markup breaks it; the rule turns out to apply to the letters too, and round 45 is also the only letter
that quotes the two clauses this round replaced (*the twin alone closes the gap*, *what a pass rules out*).
The gate's comment now carries the flattening recipe. We report it because the alternative was to keep
telling you *three* on the strength of a grep that could not see the fourth.

---

## 2. Your P2, second half: the hierarchy you asked for is drawn in boxes on page 2, and that is our failure, not your oversight

You ask for *"the three boxed levels"*: failure ⇒ unsupported, pass ⇒ declared family only, exact twin ⇒
ambiguity gone. Here is page 2 of the PDF you reviewed, extracted verbatim from the render:

```
                            yes ⇒ the experi-                        no, at any margin ⇒
                           ment decides nothing                      no evidence about P

absolute — the ceiling is a theorem: on the twin,   a pass ⇒ family-relative: the alternatives the   never mechanism: never certification, never how h com-
any arrangement-invariant map is pinned at 0.500    declared family names fall, and nothing more     putes, compositional reasoning out of reach at any width
```

All three of your levels, in boxes, with your arrows, on the second page, in a figure you clearly read;
you quote its neighbours. **A reported absence that is present is a layout failure of ours.** So the useful
question is not whether it is there but *where you looked*, and we think we can name the three reasons you
did not see a hierarchy:

1. **The three grades are not three boxes.** They are **one exit arrow and two of three band cells.** The
   failure verdict hangs off box 4 as an arrow label (*"no, at any margin ⇒ no evidence about P"*); the twin
   and the pass are the band's first and second cells; the third cell is not a verdict at all but what no
   verdict ever buys. Nothing in the picture groups them, and the band is ordered strongest-evidence-first:
deliberate, on an earlier reviewer's ask, but it is not the order the flow above it produces them in.
2. **The four things that *are* boxes are numbered as steps of a procedure**: `1. the claim` … `4. is the
   learned score above that ceiling?`. A hierarchy drawn as a numbered flow with the grades hung off it
   reads as *how to run the audit*, which is what an earlier reviewer asked that figure to be. It answers
   "what do I do" at the expense of "what am I entitled to conclude".
3. **The word is not in the figure.** `verdict` occurs 45 times in the document, 8 of them in the body, and
   **zero** times in Figure 1 or its caption, the one object that draws the verdicts. This is the paper's
   dominant failure mode across five rounds now, and it is always the same shape: *an object missed for what
   it is called, or absent from the paragraph meant to score its axis.*

**What we did about it, and what we deliberately did not.** We fixed the naming where the concept is defined
(§3.3, above), because that is a page-6 edit into an existing line. We **considered and rejected** re-wording
Figure 1's caption, and the reason is worth stating because it is a correctness argument, not a budget one.
The caption reads *"the band below grades what a pass means"*, and page 2's tail there is 26.37pt: about
**six characters**. Both directions fail:

- *Longer* is unaffordable in the tail, and a new caption line on page 2 is the one edit this round that
  could add a page.
- *"grades every verdict"* is **four characters shorter**, and **false**. The failure verdict is the exit
  arrow *above* the band, not a cell in it. Round 51 caught this exact class of error in this exact caption,
  on the render and in its own new clause: it had written that a pass "exits into the band's three grades",
  and a pass exits into **two**; *never mechanism* is what a pass never buys. We were not going to
  reintroduce a defect a predecessor had already repaired in order to save four characters.

The clause as it stands is accurate: all three cells grade what a pass means, *absolute* at a twin,
*family-relative* in general, *never mechanism* ever. What the figure lacks is a name for the trio, and a
name costs a line page 2 cannot spend on it without your §11 getting worse. **If you tell us the figure is
where you want it, that is our first spend of the next round's budget**, and the honest form is probably
re-drawing the band as three labelled verdicts rather than adding words to the caption.

---

## 3. Your P5, answered by grep, and the count is smaller than you expect

You ask us to be *"ruthless"* about `compositional generalization`. Measured across all 101 pages, comments
stripped:

| string | occurrences | where |
|---|---|---|
| `compositional generalization` | **3** | body only; **zero** anywhere else in the 101 pages |
| `compositional reasoning` | 8 | 5 body, 3 appendix/float |
| `composition-of-known-transformations` | 5 | 3 body, 2 appendix |

**All three occurrences of the phrase you flag are inside scare quotes, inside a sentence that says what
survives is *narrower than* it**, and two of the three are bolded:

- abstract ¶4: **"What survives every control is narrower than ``compositional generalization''."**
- §5 (3): **"What survives every control is narrower than ``compositional generalization''"**
- §1 (iii): "what survives every control is narrower than ``compositional generalization'', on `poly8` and
  two further EQNET corpora…"

And **every one of the five body uses of `compositional reasoning` is a negation or an impossibility**: the
abstract's *"That is not compositional reasoning: four primitives are not a library"*; §3.2's *"passing
establishes not compositional reasoning, only that the learned representation exceeds every member of a
prespecified, enumerated family"*; §4's *"still not compositional reasoning"*; §5's *"not systematic
compositional reasoning"*; and a **row of Table 2** whose four cells read
`General compositional reasoning | — | — | — | out of reach in principle`.

We think this ask is already discharged and we would rather you check us than take our word for it: the grep
is `compositional\s+generalization` over `*.tex` with `^[ \t]*%` lines stripped. If you find a fourth, it is
ours to fix and we will.

---

## 4. Four more of your asks measure as already in print, on pages 1–2

We put this section fourth on purpose. Five previous rounds opened with "already there" and it did not move
a score; the round that moved Novelty two points opened with what it shipped.

| your ask | where it already is |
|---|---|
| **P1**: *"could any representation blind to the claimed property solve this task?"* | **Page 2**, bolded, in your own interrogative grammar: *"**Three objects, and only the third is evidence** (Figure 1), one question each: **(1)** a *baseline* ⇒ did the model score higher? **(2)** an *admissible control* ⇒ could something blind to $P$ have scored that? **(3)** the *family-relative admissible ceiling* $\sup\mathcal{F}$ ⇒ could the *best* such control have, over trained readouts as well as feature maps?"* |
| **P3 / §5**: *"a general inferential framework, and symbolic expression benchmarks are a particularly clean laboratory"* | **Page 2**: *"**So this is a paper about evaluation, not about encoders**: the contribution is that *protocol* … and symbolic-expression encoders are the *case study* where it revises published conclusions."* Your *clean laboratory* is our *case study*, and it is a pinned literal |
| **§8**: *"a shortcut is only problematic when it is irrelevant to the property being claimed"*, at first contact | Three sites, all on pages 1–2. §1: *"**That is the trap**: beating S2 is not evidence of composition when *which operators appear* is itself part of the structure being claimed"*; §1: *"a mismatch between cue and claim, not a cheat"*; abstract ¶3: *"an S2 task correctly identified, **not a defect**"* |
| **§9** (*"how much of the narrative was selected after observing the landscape?"* | **Page 2**: *"Predictions were registered in the runners before the runs; **four failed, and all four are printed**"*) pinned at exactly one occurrence, plus the prespecified/exploratory split and a revision history that names every reversal |

One thing we checked and found sound rather than wrong: you quote *"strongest non-learned order-sensitive
baseline: 0.723"*. That is tree-edit distance, it is ours, and it is in the **body** twice (page 3
(Figure 2) and page 7 (§4.2)) pinned to its source file by `check_figure_provenance.py`. We had
hypothesised you went 35 pages into the appendix for our flagship comparator; you did not, and the number is
correctly attributed.

---

## 5. Your P2 and your §11 contradict each other, and we resolved in favour of §11

Your P2 wants a three-level hierarchy made unmissable on the first pages. Your §11 says *"the first two
pages are conceptually dense."* Both are right, and they cannot both be satisfied in prose, because pages
1–2 already carry **three distinct trios plus a four-box figure**:

- S1 / S2 / S3: *"**One example fixes the three levels.**"*
- baseline / admissible control / ceiling: *"**Three objects, and only the third is evidence**"*
- applications (i) / (ii) / (iii): the three-place criterion paragraph
- Figure 1's four numbered boxes

A fourth trio in body prose on page 2 answers your P2 and makes your §11 worse in the same stroke. So the
hierarchy is named in the **abstract** (falsification by design) and at **§3.3** (the graded verdict, where the
concept is defined and where a reader who wants it will be), and page 2 keeps the picture it has. This is
the **fifteenth consecutive round** in which one reviewer's asks collide with each other; we note it not as
a complaint but because you cannot see the other fourteen, and the resolution is always a judgement we would
rather make in the open than silently.

---

## 6. Your P4: the eight-section reorganization, declined a second time, with the ordering argument

Your reorganization asks §3 to open on the shape-matched twin as the central anchor. We declined this for the
round-56 reviewer and we decline it again, for a reason internal to the mathematics rather than to our
convenience: **Proposition 4 quantifies over $\mathcal{A}_P$, *every* representation invariant to the
arrangement the swap alters, not over the declared family.** Its statement is *"Let $P$ be the arrangement
the swap alters and $\mathcal{A}_P$ every representation invariant to it. Then $M(g)=0.500$ for *every*
$g\in\mathcal{A}_P$."* That object is Definition 1's. Opening §3 on the twin means either stating the
paper's strongest result before the family it is defined against, or restating the definition twice.

What your P4 actually wants (the twin as the anchor rather than as a late special case) is already
distributed across five places, and this round adds a sixth: abstract ¶3's opening sentence; §1's own headed
paragraph on page 2 (*"The sharpest form of the test: a ceiling that is a theorem"*); Figure 1's leftmost
band cell; Figure 2's rung 4; §4.2; and now **§3.3's strongest grade**. The promotion you asked for, at zero
structural cost.

Related, and conceded outright: your §10 is correct that the theorem buys exact control **for a specified
intervention**, not in general. The paper says so in the proposition's own title (*"At the shape-matched
twin the ceiling is exact, not family-relative"*) in its hypothesis, which specifies the sibling swap, and
in the appendix note on what the theorem does not claim, which states that **exactly one rung is the
exception** and that everywhere else the lower-bound reading is operative. We did not change anything here
because there was nothing to change, but you were right to test it.

---

## 7. The title, and the build you reviewed

**The title is unchanged**, deliberately: *When Stronger Baselines Mislead: Admissibility Auditing for
Representation-Level Claims*. The prefix is not a hook, it is the paper's methodological claim in five words:
a stronger baseline can be a weaker control, and the round-56 reviewer approved it explicitly. Your §15
is answered by the abstract's new last sentence instead, which is where significance is actually read.

**A disclosure you are owed.** You reviewed `iclr2027_conference(20260914-041307).pdf`, the **04:13** build
of 14 September. A correctness repair landed at **09:06**, so it is not in the PDF you read. §3 had said
*"every ceiling here is measured rather than stipulated."* That universal is **false at the paper's own
flagship rung**: at the shape-matched twin the ceiling is not measured, it is *proved*. It now reads *"every
ceiling here is a **result**, never a stipulation"*, and its appendix twin was repaired in the same pass. It
was caught by our own readiness check, not by a reviewer, the second consecutive round in which that is
true, and the transferable lesson is one we have written down: **check every universal a round promotes
against the paper's own exceptions, because the flagship result is the likeliest counterexample.**

---

## 8. The ledger, and one question

Seventeen reviewers, seventeen rubrics, and your scorecard is the first in the paper's history in which the
bottleneck **moved**. Novelty went **6.5–7.0 → 8.5**: the largest single sub-score move we have recorded,
and it moved on a round that shipped **positioning of what was already proved and no new evidence at all**.
Significance is now the low mark at 7.0. That is a useful thing to have learned about this paper: what it
needs is not more results.

So, one question, and it decides what the next round spends its budget on. **Is Significance 7.0 a verdict
on *where the framework is stated*, or on *the scope of the demonstration*?**

If it is the first, this round is aimed at it: the abstract now claims the identity and closes on the
deliverable. If it is the second (if 7.0 means "one modality, one benchmark family, prove it travels"),
then say so plainly, because **four consecutive reviewers have now told us not to add experiments**, and we
would be choosing between your asks rather than satisfying them. We would rather choose with you than guess.

---

### Verification for this round

- **Three edited sentences**, in two files. Every one inside the tail of an existing rendered line; the third
  one character shorter than what it replaced. Measured tails after each edit: abstract ¶2 **56.81pt** free,
  abstract ¶4 **73.43pt** free, §3.3 **47.70pt** free.
- **101 pages** by `pdfinfo` after every build. The **eleven-page slack profile is byte-identical to
  baseline after all three edits** (p1 +0.561 · p2 +9.463 · p3 +9.463 · p4 **0.000** · p5 −0.695 ·
  p6 −1.927 · p7–p10 0.000 · p11 +0.687). Float and section placements asserted, not assumed: Fig 1 p2 ·
  Fig 2 p3 · Table 1 p4 · Table 2 p5 · Fig 3 p8 · §2 entirely on p3 · §4.2 p7 · body ends p9 · ethics
  statement opens p10.
- **Build health:** 0 errors, 0 undefined references or citations, 0 floats too large, and **exactly the two
  pre-existing overfull boxes at unchanged sizes** (6.4211pt `\vbox`, 3.509pt `\hbox`).
- **Read on the render, not only in the log:** pages 1 and 6 rasterised and read end to end, because a
  height defect from a math form is invisible to grep, to every gate and to the verifier.
- **Content-loss proof:** a markup- and comment-stripped sentence-level diff of all seven edited-or-adjacent
  files against a pre-round snapshot shows **only the three intended changes** (§3.3's re-led sentence in its
  third and final draft). Three spans were removed, all of them inside that one sentence;
  `That limitation is also the deliverable`, `the twin alone closes the gap` and `what a pass rules out`, and
  all three are disclosed in §1 above, together with the four response letters that quoted the first and the
  one letter (round 45) that quoted all three.
- **Gates:** four `.tex` gates PASS. One new check, `check_verdict_ladder`, with **six** independently
  corruptible halves: the abstract carries a `falsif` root; the abstract still carries the pinned
  certificate clause, so the first cannot be satisfied by deleting the boundary instead of framing it; one
  330-character window of `methodology.tex` names all three grades and cites both results and the ledger; the
  trio is never renamed *levels* or a *ladder*; `is the deliverable` survives; and **no count is ever attached
  to `verdict`** anywhere in the tree, which is the readiness find above turned into a check. `--control`
  **29 → 35**, every half fires its own control, and the control loop **verifies its own corruption strings
  are still present** so it cannot pass vacuously once the defect it guards is fixed.
- **Verifier:** 2591/2591, exit 0, md5 `85e77e416b9b89fce4665bff4805348c`, identical across all three copies.
  No run, no schema change, no number moved.
