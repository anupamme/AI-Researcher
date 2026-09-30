# Response to Review: Round 47

Thank you. This is the seventh review on a seventh rubric, and it is the first to take correctness and
rigor off the table and name a single remaining axis:

> *"The experimental rigor is no longer the issue. The main remaining battle is novelty/significance of
> the admissibility framework, not correctness."*
> §18, which you call the most important part: *"I would not add more experiments randomly. … make the
> paper's central scientific contribution unmistakable."*
> §20: *"I would not add another encoder, another symbolic dataset, another 20 baselines, another 50
> seeds. … That's a positioning problem, not an experimentation problem."*

**So this round adds no run, no dataset, no seed and no encoder.** It does change the assertion count,
and we want that stated before anything else, because the last two responses used the count *holding
still* as evidence that a presentation round stayed one:

> **`verify_claims.py` reads 2398/2398, exit 0, in all three byte-identical copies — up from 2366.**
> **None of the 32 new assertions is a new run.** All 32 read one log, `r31_hardened_recipe.json`, which
> has shipped in `logs/` since 17 July. It is the run behind §15's result — the one you asked us to
> elevate — and when we went to elevate it we found it was **cited by no sentence of the nine-page body
> and asserted by none of the 2366 checks.** Reading it in order to assert it is what found **four wrong
> numbers in the appendix that had been printing it, every one of them in our favour** (Finding 3).

Your three-identity question (**#1 benchmark leakage · #2 evaluation methodology · #3 neuro-symbolic
compositionality**) is the spine of what follows. We agree it is **#2, with #1 and #3 as
demonstrations**, and the two most useful things we found are that the paper *said* so in a place no
reader reaches, and that one of its own tables was narrower than the sentence citing it.

---

## Finding 1: the change you call the single most important is already the paper's title, minus two words

§19: *"Retitle to make the contribution unmistakable,"* proposing

> *"When Stronger Baselines Mislead: An Admissibility **Framework** for **Evaluating** Representation-Level
> Claims"*

against what `iclr2027_conference.tex:34` has read for eleven rounds:

> **When Stronger Baselines Mislead: Admissibility Auditing for Representation-Level Claims**

The delta is exactly two words, and **we are declining both, with the reasons in your own review.**
*"Framework"* is the word your §11/§12 identify as the paper's remaining clarity problem
(*"too framework-heavy"*); adding it to the title advertises the thing you scored 7.5 for. *"Evaluating"*
is length, and round 46's reviewer granted the current title explicitly. We have kept it unchanged.

This is the **twelfth consecutive round** in which pasting a reviewer's own wording would have imported a
defect a predecessor asked us to remove: round 44's `⟺` (which asserted the certification the paper
exists to refuse) was the sharpest case. We now check the connective, and the vocabulary, before pasting.

**What we did instead** is treat §19 as a claim about where the identity statement *lands*, not about the
title; see Finding 2.

---

## Finding 2: §18's governing sentence was in the paper, in the last paragraph of §1

All three clauses you ask for in §18 were already written: *"One contribution; the rest is evidence that
it changes conclusions"* (a paragraph title), *"the contribution is a criterion"*, and *"symbolic-expression
encoders are this paper's case study, SCAN and Python code two ports."* Every one of them was in **§1's
sixth and final paragraph**: the densest block in the body, reached only after five paragraphs of
symbolic-mathematics content. **That is why you read identity #1/#3 and not #2**: it is a routing defect,
the same class as round 43's skipped ledger, round 44's uncited float and round 45's two appendices that
did not cite each other.

The fix is a promotion, not a new sentence:

- **Rendered page 2, immediately under Figure 1, before the three-object ladder:**
  > **So this is a paper about evaluation, not about encoders**: the contribution is that criterion — we
  > call it *admissibility auditing* — and symbolic-expression encoders are the *case study* where it
  > revises published conclusions (Table 10), language and code two ports of the same code.
- §1 ¶6 was **retitled and compressed** to pay for it: *"Applying the criterion changes conclusions, in
  three places"*: keeping its (i)/(ii)/(iii) enumeration, the five-object critical path
  `check_critical_path()` counts, and the ledger verdict distribution `check_ledger_distribution()` reads.
  The exact-restatement clauses came out; nothing else did (we prove this below).

**§22, your stated 7→8 condition** (*"make a skeptical reviewer immediately understand why 'strongest
baseline' and 'strongest admissible control' are fundamentally different scientific objects"*) has the
same shape. That comparison **is** Table 1, and one of its nine rows is literally **`strongest baseline`,
`×` in all six columns**, against ours at five. You did not register it, and the reason is legible: the
caption framed the table as a novelty defence (*"not a control task with extra steps"*) and the first
column header says *"Prior device."* So **the caption now leads on that row**:

> **Takeaway: "strongest baseline" clears *nothing*** — `×` in all six columns: strength is not blindness,
> which is what the two **bold** columns test. **The last column is `×` on every row, ours included** (§3.3).

Sized at **+1 rendered character**, because page 4 carries `0.000pt` of slack. The novelty framing is not
retired; it is this table's cited section's own name (§3.3) and the lead of the Related Work paragraph
directly above it.

**§8, the evidence hierarchy made visually unavoidable.** Figure 1's terminus was a single full-width
shaded one-liner. It is now a **three-cell graded band, dark → light, across the same width**, built only
from wording the paper already used:

| | | |
|---|---|---|
| **absolute**; the ceiling is a *theorem*: on the twin, *any* arrangement-invariant map is pinned at `0.500` | *a pass* ⇒ **family-relative**: the alternatives the declared family names fall, and nothing more | **never mechanism**: never certification, never *how* `h` computes, *compositional reasoning* out of reach at any width |

Rendered and read at 150 and 200 dpi: no tikz collision, three cells legible at their shrunk size, and tier 1
(by proof) present in the picture for the first time. The band's antecedent reads *a pass*, not *yes*, for the
reason in defect 4 below.

---

## Finding 3: the result you asked us to elevate was invisible twice over, and printing it wrong

§15: *"I would elevate this result slightly in the main paper."* We measured before elevating, and the
measurement is the finding:

| | before this round | now |
|---|---|---|
| `hardened`, `E3b`, `leakage index` in the six body files | **0 hits** | one sentence, §4.4 |
| `grep -c hardened verify_claims.py` | **0** | 32 assertions |
| `r31_hardened_recipe` in `REPRODUCE.md` | **absent** | row R46, with its command |
| `r31_hardened_recipe.json` in `artifact/audit-sym/logs/` | **absent** (shipped copy had it) | present |

**The body sentence, beside the axis row it scopes** (§4.4, the *inventory: library membership* row, which
is the largest move in the paper and the one your objection targets):

> **And this is no capacity failure**: our hardest recipe reaches only `0.480` out-of-library, against
> `0.992` in-library (App. H).

Deliberately one sentence and deliberately without `ℓ'`: the symbol is defined only in Appendix H, and
importing an undefined symbol into the body on the round whose binding axis is clarity would trade your
§15 against your §11.

**And reading the log to assert it found four wrong figures in Appendix H, all four flattering to us:**

| Appendix H printed | the log says |
|---|---|
| E3 renamed `0.752 ± 0.098` | **`0.660 ± 0.091`** |
| E3 `ℓ'` interval `[0.29, 0.44]` | **`[0.33, 0.41]`** |
| E3b renamed sd `± 0.043` | **`± 0.084`** |
| E3b `ℓ'` interval `[0.95, 1.00]` | **`[0.91, 1.08]`** |

The first is the worst: `0.752` is not even arithmetically consistent with the `ℓ' = 0.37` the same
appendix printed beside it (it implies `0.27`). All four are corrected **against the log**, and the E3b
interval's upper limit is printed **above 1** as measured, with the reason: renamed accuracy falls below
chance for some seeds (minimum `0.0` against chance `0.1`), which is what a leakage index at ceiling looks
like. E3's minimum is `0.5`, which is why only the E3b row carries that note; `check_hardened_recipe()`
asserts that asymmetry rather than the prose alone.

The 32 assertions cover the recipe's five parameters, every printed cell recomputed from the per-seed
arrays, `ℓ'` recomputed from the two **means** rather than read from the stored scalar, both intervals as
printed (and stable to two decimals under three independent RNG seeds, the runner used numpy, the
verifier has none, so the printed digits survive a change of generator as well as of seed), and **the
point, which is negative**: hardening lifts the in-library score to `0.992` and buys *nothing* out of
library (`0.480` against the un-hardened run's own `0.500`), while `ℓ'` *rises* in both regimes
(`0.17 → 0.37`, `0.88 → 0.99`).

**`REPRODUCE.md`'s self-check moves 76 → 77 and the paper says so.** Its runtime-decline count moves
5 → 6: this log stores a date and no elapsed time, so its cell says *not recorded* rather than carry a
plausible estimate; that literal is pinned, which is the only reason an estimate could not be typed in
later. The Reproducibility Statement now reads *"all 77"*, *"six runs"*, and separates the 32 that were a
self-check defect from **the 33rd, which is this revision's own and is worse**: indexed and asserted are
two different properties, and this log failed both while sitting on disk.

---

## Finding 4: §21 is partly right, and partly a false count in §1

You write: *"there is no single case where the paper's method reverses a conventional conclusion on a
non-symbolic benchmark."* Testing that means reading Table 10, the ledger of what the audit changed,
which §1 introduces as revising results **"across three modalities."** It had **eight rows, every one of
them symbolic mathematics**, no modality column, and no SCAN or code row. `check_ledger_distribution()`
reads that table's *Verdict* column against §1 and passed, because it never checked the modality count.
**A countable claim in §1 was false of the table it cites, and every gate we own was blind to it.**

The two non-symbolic revisions did exist: in §4.3, whose own three-row table names all three modalities.
They are now **in the ledger, which is 8 → 10 rows with explicit modality bands**:

| Claim as audited | Level | Verdict after the audit |
|---|---|---|
| *natural language: their grammar, their split, our encoder and our audit* | | |
| Our SCAN `add_prim_jump` `0.987` | S3 | **narrowed**: it *passes*, but `sup F_3 = 0.0005`; *their* held-out design puts the bar on the floor, so we quote no ratio (App. AY) |
| *code: our corpus, built from public Python* | | |
| Our Type-2 clone S2 `0.987` | S2 | **settled below S3**: *every* `F_3` member attains `0.990`, the maximum this corpus admits |

§1's sentence is now *"revise **ten** claims across **three** modalities — **eight** already-published
results, four of them other people's"*, and the abstract's pinned *"Four of the audited results are other
people's"* stays true and untouched: four external of ten.

**A deviation from our own plan, stated because it would otherwise be invisible.** The plan for this
round labelled the SCAN `0.987` as Lake & Baroni's: *"their grammar, their split"*, and would have put
that row in a table whose caption premise was *"every row is an already-published number."* Appendix AY
says the number is **ours** (tag `r97`): their grammar and their split, our encoder, our audit. Neither
new row is an already-published number. So the caption was **re-premised** rather than the row
re-labelled: *"Eight rows are already-published numbers, and four of those are systems and leaderboards
built by other people; the last two are claims of ours."* An attribution table is the last place to guess
an attribution, and the wording that invited the guess was the reviewer's.

**New gate, from the round's own near-miss.** `check_ledger_modalities()` parses the ledger's bands, checks
that no band is empty, that they account for all ten rows, and that the body literally says *"revise ten
claims across `\emph{three}` modalities"*. `check_protected_claims.py --control` now fires **7** FAILs
(was 6); the new one returns early on a band mismatch so that one defect yields one message.

**And the part of §21 we cannot deliver, stated plainly.** A *reversal* (the conventional conclusion
overturned) is what we have on **code**: the admissible control reaches the corpus's attainable maximum,
so the `0.987` licenses nothing above S2. But that corpus is **ours**. On the published non-symbolic
benchmark (SCAN) the audit **narrows** rather than reverses. So: a reversal on a non-symbolic corpus, yes;
a reversal on *someone else's* non-symbolic benchmark, **not yet**, and it is named as future work in the
§4.4 *Scope of inference* close rather than blurred:

> What we cannot yet show is a *reversal* on a non-symbolic benchmark built by others: the code corpus we
> settle is ours, and on SCAN the audit *narrows* (Table 10).

On your §10 (*"the SCAN result carries little weight because `sup F_3 = 0.0005` means the control is
weak"*): a floor-level ceiling is a finding **about that split's design**, not a weakness of our control,
and §4.3 already declines to quote the `1973.6×` ratio it would license for exactly that reason.

---

## The smaller asks

- **§9, `boolean8`'s coverage failure.** Agreed that it is evidence *for* the framework, and now said in
  our voice, in the *Scope of inference* close: *"**Where our own results break is the audit working**:
  the coverage mechanism does not port off polynomials — a family-relative bar exists to expose that
  rather than absorb it."*
- **§6, LOPO.** The composition paragraph, where a reader forms the overclaim, now carries the limit:
  *"calling that composition-of-known-transformations generalization is an interpretation **that does not
  reach a primitive held out of the library**."* Delivered **horizontally**, into ~66 characters of
  measured tail room at that paragraph's end: page 8 has `0.000pt` of vertical slack and the §4.3
  boundary sits at its foot, so one added line there would have pushed the conclusion off page 9.
- **§12, confusables.** Figure 1's caption now separates a **level** from a **family**: *"S1–S3 name
  *cues*; `F_3` is the controls reading *only* cues up to S3, and *coverage* is a separate axis, not a
  fourth level."* It **replaces** the caption's old coverage clause. `\mathcal{A}_P` **stays**: it occurs
  3× in the body, all on page 6, and it is round 45's grant (the ideal-vs-declared display a previous
  reviewer required).
- **§14, three-way uncertainty separation.** The sentence existed, as the last sentence of §3's
  *Audit protocol* paragraph. It is now split: §3 keeps *"**Three uncertainties, kept apart**: seeds
  quantify training stochasticity only, and split construction and family *specification* are the other
  two, each bounded on its own,"* and §4.4's *Scope of inference* close carries the unit of inference and
  the class-level bootstrap, where a reader looks for limitations.
- **§16 / your predicted Reviewer B (*"the central theorem is largely definitional"*).** Pre-conceded
  twice in the paper's own words: §3.3 bills the numbered results *"as scoping, not as theoretical
  contributions"* (a pinned literal), and says what is *not* definitional; readout closure (Prop. 1) and
  the **measured** non-monotone ceiling (Cor. 2).
- **Your predicted Reviewer C (*"too long"*).** The body is nine pages and self-contained; the appendix is
  the audit trail, routed by round 42's reading path and round 44's five-object critical path.

---

## Four defects the round found in its own new prose

Consistent with the last five rounds, the readiness pass caught more than the review did, and this time
all four were self-inflicted, in material written this round, two of them in the same figure.

1. **A caption count contradicting its own figure, one round after the same defect class.** The new tier
   band's caption clause read *"a pass exits into the band's three grades."* **No pass exits into the
   third one**; *never mechanism* is what a pass never buys, so the count of grades a pass can exit into
   is **two**. Caught by rendering page 2 and reading it against the picture, which is how seventeen of
   the last nineteen rounds' real defects were found. Fixed by making the band the subject rather than the
   pass (*"and the band below grades what a pass means"*) at **two characters shorter**, because page 2
   has `0.001pt` of slack.
2. **A gate that read `%`-comments as body text: in both directions.** `check_reviewer_map.py` FAILed
   with *"lead says E3b appears nowhere in the body, but it is in experiments.tex."* The string was in the
   round's own **in-source note recording that absence**: a note about an absence became its
   counterexample. The false FAIL is the cheap half. The expensive half is latent and is why comments are
   now stripped when the body is *read* rather than inside that one loop: **check 5b requires each
   reviewer-map Claim cell to be a verbatim quote of the section its row names, and a quote surviving only
   in a comment would have passed a check whose whole purpose is that a reviewer can read the sentence.**
   Re-run after the strip: **287 checks, PASS**, the same count, so no existing row had been relying on
   it.
3. **A dropped word in the one sentence this round added to the body.** The §4.4 hardened-recipe sentence
   read *"reaches only `0.480` out-of-library, against `0.992` in (App. H)"*: the second half of the
   contrast lost its noun. It survived the build, all four gates and 2398 assertions, because **no check
   here reads for grammar and a missing word is not a missing `\ref`.** Fixed to *"`0.992` **in-library**"*,
   at 8 characters, which the paragraph's last line had room for: page 9's slack, its line count and the
   §5/Ethics boundary are all unchanged after the fix. Found by reading the rendered page: the same way
   defect 1 was.
4. **The same band had a second defect: a branch word colliding with the box above it.** Cell 2 read
   *"**yes** ⇒ family-relative."* That `yes` answers box 4 (*is the learned score above that ceiling?*), but the
   cell sits horizontally under boxes 2–3: **directly below `yes ⇒ the experiment decides nothing`, which is
   box 2's `yes` and the fatal branch.** Two `yes ⇒` clauses stacked ~14pt apart with opposite polarity, each
   correct with respect to an antecedent the reader cannot see. Fixed to *"**a pass** ⇒ family-relative"*, which
   is unambiguous wherever the cell sits and is the caption's own subject; +3 characters, absorbed by the cell's
   second line, so the band held two lines and page 2's slack is unmoved. **Round 44's cross-panel
   axis-direction defect in a new form**, and found on the *final* read of the page, after every gate was green
   for the third time.

---

## And a fifth, inherited: the centrepiece figure was quoting our weaker control

The last check of the round was to read pages 1–5 **as a unit** and ask your §22 question of them: could a
reader who sees only those pages say why *strongest baseline* and *strongest admissible control* are
different objects? They can, the boxed criterion (p1), Table 1's `strongest baseline` row (p4) and Table 2's
`Strongest admissible control` column (p5) each state it independently. But that read found the one place in
the front matter where the paper prints the weaker number:

- **The abstract (p1) and Table 2 (p5) quote the *searched* composite, `0.676`, as the strongest admissible
  control on our headline cell; Figure 2's `poly8` rung (p3) topped out at the *catalogued* full-token bag,
  `0.517`.** So the picture showed a `+0.377` margin where the paper's own honest margin is **`+0.22`**.
  Three of that figure's four rungs agree with Table 2 cell for cell. The fourth (the one the paper's
  headline result is read off) did not.
- **Round 39 put the `0.517` bar there for exactly this reason** and wrote the principle into the source:
  *"omitting it would have let this paragraph quote `+0.874` as the margin while a stronger admissible
  control sat at `+0.377` in Figure 2 — precisely the error the paragraph condemns."* Round 41's adversarial
  search then raised the top of that chain to `0.676` in the abstract, in §3.3 and in §4.1, and left the
  figure at the catalogued line, **and pinned `0.517` into `check_figure_provenance.py`, so the gate was
  enforcing the stale top.**
- **Fixed as a relabel, not a fourth bar, and the reason is measured.** A fourth bar costs ≈`6.4pt` of
  rendered height against page 3's `6.624pt` of slack, with pages 4–5 at `0.000`: a `0.2pt` margin. The
  relabel costs nothing: same node count, same coordinates, and the picture's width is set by that rung's
  verdict line, not by the bar. The rung now reads **`0.894` / `0.676` / `0.276`**: the encoder, the
  strongest control anyone has found, and the declared family's ceiling. `0.517` is not lost: §3.3 prints
  the whole six-number chain and Appendix BB's table prints it beside the composite.
- **The composite is still not a member of `F_3`** and still does not set `sup F_3`, which stays `0.276`
  (Appendix BB). Drawing a non-member here is this figure's existing practice: `0.517` was one too, and
  the stronger non-member is the honest one to draw.
- **The gate moved with the number.** `check_figure_provenance.py`'s pin now resolves to Appendix BB's own
  sentence with the four-decimal value inside the row pattern, and it learned to accept a correctly
  *rounded* bar (`0.676` against a source `0.6758`) only from a longer literal in the same row, never the
  reverse. 10 values checked, PASS, control still fires.

We would rather report this than have it found: a paper titled *When Stronger Baselines Mislead* had a
centrepiece figure understating its own strongest baseline, and it took reading five rendered pages in one
sitting (not any of the four gates, and not 2398 assertions) to see it.

---

## What we did not do, with the measurement

- **No new run, dataset, seed, encoder or baseline** (§20), and the log behind the one elevated result was
  **copied** between two directories that ship, not regenerated. Its `provenance` block was checked for an
  absolute path and for nested `log_dir` keys before and after the copy; both copies are md5-identical.
- **The title's two words** (§19): refused, with the reason above.
- **A reversal on a published non-symbolic benchmark** (§21), not in the paper's evidence; named as
  future work rather than implied.
- **Nothing new in §4.2 or on page 8.** Pages 4–11 carry `0.000pt` of slack and the §4.3 heading sits at
  the foot of page 8 with its opening paragraph, so any line added upstream of it flips the boundary and
  spills the conclusion past page 9. Every addition this round is either after that heading or horizontal
  into measured tail room. Page 3's `+6.624pt` is trapped behind `placeins`' section barrier and can fund
  only §1/§2 horizontal growth, which is what paid for the identity statement.

---

## Verification

- **Build**: `pdflatex → bibtex → pdflatex ×2`. **0 errors · 0 undefined references or citations · 0
  *Float too large* · exactly 2 overfull boxes, both pre-existing** (a `\vbox` 6.42pt on p31, an `\hbox`
  3.51pt on p59, neither touched this round) · **94 pages**.
- **Body ends page 9**, Ethics is the first body line of **page 10**. §4.3 **p8** (the boundary's other
  legal state), §4.4 p9, §5 p9. Slack: p1 `+0.561` · p2 `+0.001` · p3 `+6.624` · p4–p5 `0.000` · p6
  `−1.927` (descender ink on a page ending in a parenthetical, confirmed by render, the only overfull
  `\vbox` in the document is on p31) · p7–p11 `0.000`.
- **Placements asserted, not assumed**: Figure 1 p2 · Figure 2 p3 · Figure 3 p8 · Figure 4 p15 · Figure 5
  p16 · Table 1 p4 · Table 2 p5 · Table 10 (the change ledger) p26 · APPENDIX p14. The word *ledger*
  occurs **once** in the body, and it names Table 2; Table 10 is *"what running the audit changes."*
- **Gates**: `check_protected_claims.py` PASS (21 protected claims, 4 absences over 6+6 files, 3 over all
  16), `--control` fires **7** · `check_reviewer_map.py` PASS (17 rows, 287 checks, both positive controls
  inline) · `check_caption_rows.py` PASS (34 caption literals over 36 floats), `--control` **1** ·
  `check_figure_provenance.py` PASS (10 figure values), `--control` **2**. `check_critical_path()`,
  `check_float_routing()`, `check_ledger_distribution()`, `check_ledger_modalities()`,
  `check_reproduce_index()`, `check_holdout_join()` all green.
- **`verify_claims.py` 2398/2398, exit 0, in all three copies**, md5-identical
  (`c1cc08ae6d33ffe9b5bb4ffe387cd24b`); `equivalence.py` deliberately **not** synced, as always.
- **Every rewritten `\ref` resolved against `iclr2027_conference.aux`**: `sec:coverage`→4.4,
  `app:hardened_recipe`→H, `app:scan_split`→AY, `sec:outside_symbolic`→4.3, `tab:audit_changes`→10,
  `prop:ceiling`→1, `sec:not_control_task`→3.3, `app:split_robustness`→AL.
- **No content lost in the compression**: markup- and comment-stripped sentence diff of the six body files
  against a pre-round snapshot: 17 sentences out, 20 in, and every removed span accounted for. The two
  that were not rewordings were checked to survive elsewhere: *"falsification … never certification"* is
  in the abstract (a pinned literal), Figure 1's third band cell and §4.4's *Scope* close; *"the class is
  the primary unit; every interval is a class-level bootstrap"* is in that same close.
- **Pages read as images, not as text**: p1, p2, p4, p9 and the ledger page. That is where defect 1 above
  was found.
