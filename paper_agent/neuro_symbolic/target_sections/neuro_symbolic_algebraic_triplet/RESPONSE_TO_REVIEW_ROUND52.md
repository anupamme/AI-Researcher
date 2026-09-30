# Response to Review: Round 52

Thank you. This is the twelfth review on a twelfth rubric, and the first to score the paper below 7. We take
that seriously, and we take your diagnosis at face value:

> *"The main risk is novelty and evidential scope, not experimental sloppiness."*

You state your 7 → 8 lever twice, in §18.1 and again in your closing paragraph, and it is the only thing this
round works on:

> *"Make the novelty of admissibility auditing undeniable by constructing one minimal example where every
> existing evaluation device in the related-work table would license the wrong conclusion, while your
> admissibility ceiling correctly refuses it."*

**Round 52 adds no run.** It changes one sentence and one opening clause in §2, one clause in §2's closing
paragraph, two clauses in Table 2's caption, one item in the appendix's index, and one gate. Everything else in
the paper is byte-identical to the copy you read.

**Four things before anything else. One is about your copy of the paper, one is a defect we are conceding, and
two are defects the round found *in this round's own work* after every gate was green.**

**First, `verify_claims.py` does not move: 2486 assertions, exit 0, all three shipped copies byte-identical
(md5 `5fa64467ef226550c86145934245bc85`).** The standing rule in this correspondence is that the first
paragraph says whether the assertion count had to rise and why. It did not, and that is the correct outcome
here: your ask is a *routing* ask, not a measurement ask, and a rise would have meant we had quietly added a
result to a round that claims to add none. What did rise is gate coverage:
`check_protected_claims.py --control` goes **19 → 20**, via one new check with four assertion groups.

## 1. The build you reviewed predates eight of our sources

You name it: `iclr2027_conference(20260912-060109).pdf`. That timestamp, `2026-09-12 06:01:09`, is earlier
than every source file in the paper except the abstract:

| source | last edited before this round | vs your build |
|---|---|---|
| `abstract.tex` | 2026-09-11 09:10:00 | before |
| `appendix_domain_guards.tex` | 2026-09-12 08:23:34 | **after** |
| `introduction.tex` | 2026-09-12 10:46:36 | **after** |
| `methodology.tex` | 2026-09-12 11:19:11 | **after** |
| `experiments.tex` | 2026-09-12 12:14:04 | **after** |
| `related_work.tex` | 2026-09-12 12:18:07 | **after** |
| `conclusion.tex` | 2026-09-12 12:25:23 | **after** |
| `check_protected_claims.py` | 2026-09-12 12:59:47 | **after** |
| `statements.tex` | 2026-09-12 13:00:19 | **after** |

This is the **fourth consecutive round** in which the reviewed build predates the sources, so we now date the
build before reading the review. It matters most for the two asks you rest your score on:

- **§18.1 / §15, "emphasize the comparison table."** Table 1 in your copy has **seven** columns and **nine**
  rows. The current Table 1 has **eight** columns and **ten**: round 50 added the `searches a class?` column
  and the `adversarial baseline` row *specifically* because a previous reviewer asked whether this work was a
  repackaging of adversarial evaluation. That row and that column are the direct answer to your own novelty
  complaint, and they were not in front of you.
- **§15's sixth device, contrast sets.** You list it as missing. Round 51 named it in the `counterfactual
  eval.` row's own citation slot — `(contrast sets; Gardner et al., 2020)` — which renders as one
  parenthetical on p3. Also after your build.

We are not offering this as a rebuttal of your score. We are offering it because two of the items you count
against novelty were already answered, and the *reason* you could not see them is the same reason for the
defect we concede next.

## 2. What we concede: the taxonomy had no instance, and the instance had no taxonomy label

Your barb is the most useful sentence in the review:

> *"Table 1 currently feels somewhat like a taxonomy constructed to make the proposed method win."*

We measured before conceding, and the measurement is worse than your criticism. **All three halves of your
§18.1 ask were already in the paper, and nothing joined them:**

| half of your ask | where it already was | what it was missing |
|---|---|---|
| the *"extremely crisp paragraph"* answering what admissibility auditing establishes that the five devices cannot | §2's closing paragraph: *"none estimates $\sup_{g\in\mathcal{F}}M(g)$, the ceiling of a declared family"* | it said **"Prior devices"**; it named none of them, and it carried **no number** |
| the named taxonomy | Table 1, all ten rows, including every device you list | **no number, no case**: hence "built to win" |
| the *minimal example* you ask us to construct | Table 2's **row 1** (`0.972` reported, `1.000` admissible, verdict **broken**) *and* §3.3's chain (`+0.874` to `+0.22` on the same evidence) | it named **no device from Table 1** |

So the counterexample you ask us to construct was already printed twice, two pages from the taxonomy it is a
counterexample for, with no label connecting them. **This is the third round in which a reviewer has missed or
mis-credited an object because of what it is called**: round 40's reviewer credited the wrong table for §3.3's
comparison, round 47's did not register the `strongest baseline` row that was his own stated 7 → 8 condition.
Both times our in-source notes recorded the cause and we fixed only the instance. This time it cost 1.0 of
overall score, and we are treating it as the paper's dominant failure mode rather than as three coincidences.

**The fix is a join, not new content**, which is also the only reason it is affordable. The body has
**≈7.2pt of total slack across nine pages**, about 0.6 of one line (§6 below).

## 3. What changed

**(a) §2's closing paragraph now carries the number (your §18.1).** The sentence that already answered your
question now attaches the case to it:

> **Table 2's row 1 is the cost of guessing wrong**: `0.972` read as structure, where an admissible map
> reaches `1.000`.

On the rendered page this sits four lines below the paragraph that names *matched control*, *counterfactual
evaluation (contrast sets)*, *control tasks* and *invariance tests*, and in the same sentence as *adversarial*
search. Figure 2's top rung, **on that same page**, prints `1.000` / `0.972` / *fails* as bars. So the device
names, the numbers, and the verdict are now all on p3, and the certificate that licenses the refusal is Table 2
row 1 on p5.

**(b) We did not write your sentence, and this is the one place we are pushing back.** Your literal ask is
that *every* device in Table 1 license the wrong conclusion on the example. **That would be false.** A matched
control or an invariance test *does* catch the AI Feynman variable-identity leak: **if the practitioner
guesses to perturb variable names.** Writing the unanimous version would have been exactly the
taxonomy-constructed-to-win you suspect, and you would have been right to say so.

The true claim is about **who has to guess**, and we think it is the stronger one:

- prior devices are correct **conditional on** naming the right perturbation in advance;
- the ceiling is correct **unconditionally over a declared family**, and **exactly** so at the twin, where
  `0.500` is a theorem and not a search result.

Hence *"the cost of guessing wrong"* rather than *"every device fails."* The one thing we ask of a future
round is not to "strengthen" this into the universal claim; there is a note in the source saying so.

**And the paragraph now says who guesses.** Its opening clause reads *"Prior devices test **a guessed**
comparator, perturbation, or adversarial search in isolation"*: three rendered lines above *"the cost of
guessing wrong"*, in the same paragraph on p3. That word was not there when we first drafted this letter, and
its absence is §5(c).

We also note the audit errs in **both** directions on published cells, which your §5 already credits: AI
Feynman is prior practice being too **generous** (`0.972` read as structure), and `poly8` `K=500` is prior
practice being too **flattering** by ~4× (`+0.874` / `+0.618` / `+0.598` / `+0.377` versus the family ceiling's
`+0.22`, §3.3).

**(c) The audit certificate is named where it already lives (your §18.2).** You ask us to define
*(M(h), sup<sub>g∈F</sub>M(g), F, protocol, invariance test)*. That object is Table 2, on rendered **p5**, with
**13 rows**, and you missed it because we called it an *entitlements* ledger. Its caption now says: **"Each row
is an audit certificate; the columns are its parts (Def. 1)."**

We name it rather than build it, and we want to be exact about the mapping, because "the columns are its
parts" is only true with one qualification. **Three** of your five components vary per row and are therefore
columns: `F` and `sup` are the *Strongest admissible control* cell (e.g. *"variable bag 1.000"*), `M(h)` is
*Reported*. The other **two are held constant by construction** and so do not get a column: there is **one
protocol for every row** (*"under the same protocol"*, Definition 1, on that same page) and the per-instance
membership test (§3.3). The `(Def. 1)` pointer routes you to the **first** of those: Definition 1 fixes the
protocol (*"under the same protocol"*) and does **not** restate the membership test, which is §3's own
paragraph *"Membership in $\mathcal{F}$ is **tested** rather than assumed — the test is the twin, per
instance"*, reached from the appendix index's pointer. We state it that precisely because an earlier draft of
this letter claimed the single pointer routed to both components, and it does not; see §5(c).

**(d) "The strongest admissible control" is qualified at both real sites (your §6).** There were exactly three
occurrences in the source and one was a comment. Both live sites now read *"the strongest admissible control
**we found**"* (Table 2's caption) and *"the strongest admissible control **our search family found**"* (the
appendix index). Your own carve-out is left standing verbatim, because there the ceiling is a theorem and
*"we found"* would be **false**: Table 2's twin row reads *"**any** arrangement-blind map, `0.500` **by
proof**"*, and the conclusion reads *"— except at a twin: `0.500` by proof."* The abstract already said
*"the strongest order-blind control **an adversarial search finds**."*

**(e) One new gate.** `check_certificate_join()` in `check_protected_claims.py` parses Table 2's row block,
derives row 1's ceiling and reported number **from the table itself rather than from a hard-coded constant**,
and fails if §2's new sentence quotes anything else, so a future round that edits either number silently
un-joins your §18.1 and the gate says so. It also asserts that *audit certificate* is named in both the caption
and the appendix index, and that the `we found` qualifier is present in the caption **while the twin row still
says `by proof`**. Its control reverts one number at one site and fails: **19 → 20**.

## 4. Six asks already satisfied, answered by measurement rather than by edit

We grep and read the render before conceding, because in **nine consecutive rounds** a reviewer's proposed
edit would have deleted a predecessor's requirement.

| your ask | what the paper already says |
|---|---|
| **§10**: say *"cross-domain portability demonstration"*, not general validation | §4.4 already reads *"a new modality needs only a parser and a level assignment — **portability, not general validation**, never prevalence."* Your preferred framing is the paper's own italics. **No edit.** |
| **§7**: make *"generalization of a learned transformation family, not symbolic reasoning"* central | It is numbered finding **(3)** of the conclusion, not a caveat: *"**What survives every control is narrower than 'compositional generalization'**: it passes the $\mathcal{F}_3$ audit as composition-of-known-transformations generalization … **not systematic compositional reasoning**."* **No edit.** |
| **§19/§20**: reposition as a falsification framework | The conclusion's **last sentence** is *"The audit falsifies; it certifies nothing; Table 2 is the ledger,"* pinned by a gate at exactly one occurrence, and the abstract's *"**no** admissible family can turn it into a certificate."* **No edit.** |
| **§18.3**: a killer example outside symbolic mathematics | Two exist and are the **last two rows** of the audit-changes ledger (Table 10): **SCAN `add_prim_jump`** (Lake & Baroni's own corpus and split) and a **Type-2 clone** class at S2, both verdicts *"only this revision's audit settled."* The remaining gap (a **third party's headline claim overturned outside symbolic math**) stays **disclosed** in §4.5 (*"What we cannot yet show is a reversal on a non-symbolic benchmark built by others"*) rather than papered over. **No new experiment**: third consecutive round declining one. |
| **§9**: §3 is too complicated; reorganize around the 6-item critical path | The critical path is gated against §1's parenthetical, so the two representations move together or not at all. On the mechanics: §3 spans **the paper's only two negative-slack pages** (p5 `−0.695pt`, p6 `−1.927pt`), and `placeins [section]` means §3 cannot borrow slack from §4. A reorganization here is a repack of the whole body, not a local edit; we would rather do it in a round whose budget is that and nothing else. |
| **§11-class self-counts** | Repaired and gated in round 51 (`check_artifact_counts`, `check_ledger_pointer`); the current measured totals are 2486 assertions and 81 logs. |

## 5. Three defects this round found in its own work, after every gate was green

We ask at the end of every round whether the paper is ready. **Four** rounds running, that question has found a
real defect on a fully green board. It did again, and (c) is the most serious defect in this round, because it
was in the one sentence the round exists to write.

**(a) An appendix is not page-cost-free, and the document silently became 100 pages.** Our first draft of the
appendix index spelled your five-tuple out in full. That took the entry from **one rendered line to four**, and
the document went **99 → 100 pages**, because a 3-line insertion **86 pages above the end** pushed Figure 6,
the last float, onto a page of its own. The eleven-page body profile was *identical* throughout, so nothing in
our usual measurement could see it; only `pdfinfo` could. The entry is now **two** lines, the parts live at the
table where the columns are, and the document is back to **99**. The craft reason is the better one anyway:
every other entry in that index is one line, which is what makes it a scan-able index of the six objects.

**(b) The gate caught a fabricated label in our own note about (a).** The comment recording that measurement
cited `\ref{fig:volume}`, which does not exist. `check_comment_refs()` (added in round 48 after a reviewer's
round found two invented theorem labels in comments) fired on the very next run. The real label resolves
against the `.aux` to `fig:scale_curve` = **Figure 6, p99**, which independently confirms the diagnosis in (a).
We mention it because it is the only check in the paper that reads the design record, and it earned its keep on
the round that wrote it into the record.

**(c) The round's central argument was in our notes and in this letter, but not in the paper.** With all four
gates green and 2486/2486 verifier assertions passing, we grepped the live body prose for `guess*`. It occurred
**exactly once in the whole paper**: in the phrase we had just shipped, *"the cost of guessing wrong"*, and
**nothing anywhere said that anyone guesses**. The conditional claim of (b) above, which is the whole reason we
declined to write your universal one, existed only in an in-source comment and in a draft of this letter. So a
reader arriving at p3 met a bolded key term with **no antecedent**, and this letter asserted an argument the
paper did not make. That is the same routing defect as §2, committed by us, against ourselves, in the round that
concedes it.

The repair is **one word**, and it had to be a **swap** rather than an addition: p3's last line on that
paragraph had `9.73pt` of tail (**2.6 characters**) and the page carries `0.57` of a line. Funding it with the
two repeated `one`s makes it free: *"test **one** comparator, **one** perturbation, or **an** adversarial
search"* → *"test **a guessed** comparator, perturbation, or adversarial search"*, **91 → 90** rendered
characters. Measured after: the paragraph is **line-for-line identical**, same hyphenation break at
`adver-/sarial`, same tail to `0.01pt`, and the eleven-page slack profile is unchanged. `in isolation` still
governs all three items, which is a round-50 requirement. We checked the swapped span against all four gates
and the verifier before cutting: zero hits.

## 6. Verification

Everything below is measured on the shipped build, not asserted.

- **Build:** `pdflatex → bibtex → pdflatex ×2`. **0** errors · **0** undefined references or citations · **0**
  `Float too large` · exactly **2** overfull boxes, both pre-existing at unchanged sizes (`\vbox` 6.4211pt,
  `\hbox` 3.509pt) · **99 pages**.
- **Page geometry, printed in full rather than summarised as "unchanged"** (saturation `732.013922pt`):

  | page | p1 | p2 | p3 | p4 | p5 | p6 | p7 | p8 | p9 | p10 | p11 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | slack (pt) | +0.561 | +0.001 | +6.624 | 0.000 | −0.695 | −1.927 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

  **Identical to the pre-round baseline at all eleven pages.** Figure 1 p2 · Figure 2 p3 · Figure 3 p8 ·
  Table 1 p4 · Table 2 p5, none moved. Body ends **p9**; the Ethics Statement is the first body line of p10.
- **How the new line on p3 was paid for.** p3 carries `+6.624pt` = 0.57 of a line, so the new sentence needed
  a line **bought**, not found. §2's closing paragraph ended with `encoder.` alone on a line holding 51.47pt,
  so a **14-character** stylistic cut there (`… renaming alike, which locates the mechanism in the benchmark
  rather than the encoder` → `… renaming, which locates the mechanism in the benchmark, not the encoder`)
  retired that line and funded this one. **No citation was touched**: all three symbolic-regression
  references remain, and the deleted span is pinned by none of the four gates and by no verifier assertion.
- **Table 2's caption is still six rendered lines.** `(Def. 1)` spent 34.02pt of the 47.45pt measured free on
  its last line, leaving **13.43pt ≈ 3 characters**. That caption is now exhausted; a later round needing room
  there has to buy it.
- **Content-loss diff** against a `cp -p` snapshot taken before the round, markup- and comment-stripped at
  sentence level across all seven body and appendix files: **−4 / +6**, and all four deletions are
  replacements (Table 2's caption, §2's closing paragraph, §2's `What is new` opening clause, the appendix
  index entry). `abstract.tex`, `introduction.tex`, `experiments.tex`, `conclusion.tex` and `statements.tex`
  are **byte-identical**. The only prose actually removed anywhere in the paper is the two words in the funding
  cut above and the two repeated `one`s that paid for §5(c)'s word.
- **§5(c)'s swap is provably height-free**, which is why it was affordable at all: on the rendered p3 the
  `What is new` paragraph is **line-for-line identical** before and after: same four lines, same hyphenation
  break at `adver-`/`sarial`, last-line tail unchanged, so nothing downstream of p3 could move.
- **Four gates PASS; controls fire 20 / 9 inline / 1 / 2.**
- **`verify_claims.py`: exit 0, 2486/2486, three copies md5-identical** (`5fa64467ef226550c86145934245bc85`).
- **Cold reconstruction, your §18.1 applied to the render rather than to our intention.** Reading **only
  p3–p5**: the five devices are named (p3, §2), one published cell is named with the number it licenses
  (`0.972`, p3 prose and Figure 2's top rung), the admissible ceiling is given (`1.000`), the verdict is given
  (**broken**, Table 2 row 1, p5), and the row is labelled an audit certificate whose columns are its parts.
  What a reader **cannot** do from p3 alone is see the five device names and the number in the *same sentence*:
  the roll-call was priced at +141 characters and did not fit in 66.17pt of tail on a page with 0.57 of a line
  to spare. It sits in the immediately preceding paragraph instead. We are reporting the rung of the ladder
  that shipped, not the one we planned.

## 7. What we did not do

- **No new experiment.** Third consecutive round, and the previous two reviewers each instructed it.
- **No unanimity claim.** §3(b) above is deliberate and we would defend it in discussion.
- **No §9 reorganization of §3**, for the page-mechanics reason in §4: stated as a deferral, not as a denial.
- **No third-party reversal outside symbolic mathematics.** Your §18.3 remains the honest open item, and it is
  disclosed in the paper's own §4.5 rather than in this letter only.
