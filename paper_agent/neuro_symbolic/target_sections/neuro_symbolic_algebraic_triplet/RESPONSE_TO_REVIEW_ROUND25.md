# Response to the round-25 review

*Not part of the paper.*

**Summary: a billing round. No experiments, no new claims, the assertion count unchanged at
2071, and three of your five changes turned out to already be in the paper, needing a label,
a placement and an ordering rather than content.**

---

## 0. The scorecard, and the axis that disappeared

| Criterion | R24 | R25 |
|---|---|---|
| Technical quality | 7 | **8** |
| Empirical quality | 7 | **8** |
| Clarity | 6 | **7.5** |
| Significance | 7 | **8** |
| Novelty | 7 | 7 |
| Reproducibility | 9 | 9 |
| Scope / generalization | **5** | **— absent** |
| **Overall** | **6** | **7** |

We want to flag one thing, because it has now happened three times. **Round 24 scored
Scope/generalization at 5 and we deliberately did not address it**; we said in both the response
and the change log that the fix needed a real external benchmark in a new domain, that we were
not doing it that round, and that we would rather say so than let a 5 look answered. The axis is
absent from your scorecard and Significance rose 7 → 8. The same thing happened to Generality
(5.5) and Theoretical novelty (6) after round 21, each time after we scoped the limitation
explicitly in the main text rather than running something. Your §7 says exactly why: *"I wouldn't
necessarily add another huge experiment. Instead, make the limitation explicit in the main text."*

---

## 1. Three of your five changes were already in the paper

We are reporting this rather than quietly implementing them, because *where* they were is the
useful information.

**③ "Put the family stress test in the main paper."** It was already in §4.2: *"Widening the
family with five descriptors we did not choose moves the ceiling at 4 of 8 cells… and moves no
verdict anywhere"*, but **unlabelled and buried mid-paragraph**, after the non-monotonicity
result. You are right that it is *"probably the single most important robustness experiment for
the entire framework"* (your §13), and right that the fix is a label. It is now its own paragraph:
**Family stress test: does a wider family change any verdict?**; including the sentence your §13
asks for, that completeness of the family is not claimed and cannot be, and that what is measured
is that the conclusions are not an artifact of where we drew its boundary.

**⑤ "Add one 'What this framework does NOT establish' box."** That box already existed; it is the
§3.3 `fbox`, but it was titled *What passing this audit establishes*, and it sits on page 5.
Round 24 had also put a box on page 2 stating what the audit **does**. You did not mention either.
Our reading is that the object readers keep asking for is the **pairing**, in one place, early;
splitting it across a page-2 box and a page-5 box means neither is that object. **The page-2 box
now carries both halves**, and the §3.3 box has been cut back to what it uniquely says.

**② "Promote the S3 non-monotonicity result."** §4.2 already called the inversion *"the paper's
centerpiece"* and the conclusion already carried it. What was true is that **the abstract** buried
it in the middle of the third paragraph. It now opens that paragraph, in your framing and ours:
*"The finding we did not expect: the ceiling is non-monotone in resolution — raising a control's
resolution can lower it."*

---

## 2. ④ The formal machinery, and a disclosure

**The body now carries Definition 1, Proposition 1 and Proposition 2, exactly as you asked.**
*No admissible family certifies* has moved to Appendix AN beside its own proof; §3.4 keeps the
claim as prose with a pointer, opening with the sentence your predecessor asked for
(*"Comparator-based audits are falsification tools, not certification tools"*).

**This reverses a previous round, and we would rather say so than have it discovered.** Round 19's
review made *promoting* that exact proposition its named condition for an 8/10, and we promoted
it. Round 21 then said it is *"essentially a consequence of the definition of admissibility"* and
must not be sold as a theoretical result, so we re-billed it as scoping. Round 24 asked us to
de-emphasise it rhetorically. You now ask for it out of the body. We think the through-line across
21, 24 and 25 is consistent; it is the *formal apparatus* that draws the objection, not the
stance, so the stance stays in the body in plain prose and the proposition sits with its proof.
If a future reader wants it back in §3, the argument for that has already been made once and lost
three times.

A side effect worth naming: with two propositions now in the appendix, the body cites Propositions
3 and 4 without them appearing in §3. §3.3 now says so explicitly (*"the proofs, and the two
propositions that only scope the result, are in Appendix AN"*), rather than leaving a reader
hunting.

---

## 3. Your item 10 was a real overclaim of ours

Appendix E read *"the trained-vs-random gap in the plain regime is **entirely** variable-token
statistics."* You are right, and this is our error rather than a concession: the evidence
establishes it **under this retrieval protocol**, and the paper's own asymmetry argument (§3.3)
forbids stating a protocol-bound result protocol-free. It now reads *"is **explained by**
variable-token statistics **under this protocol**."*

## 4. ⑭, and a fix we found ourselves

**⑭ adopted, in the abstract and the conclusion.** *"rules out the declared alternative
explanations"* → *"rules out the **explicitly declared** alternative explanations **that family
represents**"*, so it cannot be read as *"they only ruled out the ones they thought of."*

**And a defect we shipped in round 24, found by reading the built page rather than the source.**
The §3.3 box rendered as *"…upgrades that to certification. **— nor is anything above S*T* licensed
(Proposition 4).**"*: a sentence beginning with an em-dash after a full stop. It was the pointer
added when round 24 demoted a different proposition, and it was never re-read as rendered text.
Fixed, and reading both boxes as rendered output is now part of our gate list.

## 5. Your item 4: the toy example moved to §1

You said ours *"is actually good but comes relatively late"*, and you are right that it makes
exactly the point that needs making early: an operator bag separates the classes **perfectly**,
and that is precisely why beating it is not evidence of composition, *which operators appear* is
part of the structure being claimed. The `x+y` / `y+x` / `(x+0)+y` example now sits in §1,
immediately after the box, before any formalism. §3.3 keeps only the one consequence it needs.

## 6. ① The contribution, rebilled

Contribution (1) read ***"the strongest baseline" is an invalid principle***. You are right that
this *"sounds almost tautological"* and invites the novelty objection. It now reads, close to your
own wording: **a criterion for deciding whether a comparator is *admissible* evidence for a given
representation-level claim, and a procedure for aggregating admissible controls into a measurable
ceiling**, not the observation that benchmarks contain shortcuts.

**We take the point that this is one paragraph against your binding axis.** If the next reader
still hears "good experimental practice", the answer is not another reframing round; it is the
independent-domain evidence we have deferred since round 24.

## 7. Your item 8: how independent are the 23?

Fair question, and the answer is now inline: of the 23 configurations, **15 are EQNET variants,
split 7 polynomial and 8 boolean**. We did not add a table; there is no page for one, and the
survey table already carries every row.

## 8. Your item 12: the appendix

We did not restructure it. The appendix's `\applabel` letters (A–AV) are cited from the body, and
round 21 measured that splitting it into a separate document would orphan 21 body references. What
we did instead is make its shape explicit in its own first paragraph: it is **four things**,
provenance (A–K), protocol specifications (L–Z), one self-contained section per run tag (AA–AV),
and proofs (AN), and *"a reader checking one number needs only (i) and the one section in (iii)
that names its tag."* If the perception problem is *"why 67 pages"*, that sentence is the answer;
the pages themselves are what makes the provenance claim true.

## 9. Gate state

0 LaTeX errors · 0 unresolved references · 0 `Float too large` · exactly 2 overfull boxes, both
pre-existing · **76 pages, unchanged** · abstract ends page 1, body ends page 9, page 10 opens with
the Ethics Statement · `verify_claims.py` exit `0` at **2071/2071** in all three shipped copies,
unchanged as it must be for a round that adds no measurement · `check_tex_numbers.py` clean on the
reordered abstract and the new §4.2 paragraph · both figures rendered and inspected · both boxes
re-read as rendered output · the five elements a cold reader gets extracted from the built PDF and
re-read.
