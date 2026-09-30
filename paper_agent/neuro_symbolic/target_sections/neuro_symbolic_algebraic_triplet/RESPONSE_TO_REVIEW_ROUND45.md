# Response to the round-45 review

**We ran the experiment you called "the single experiment I would most want", and it was already half-run, in
two appendices that did not cite each other. Frozen after a search that had oracle access to the split we
report, the strongest order-blind composite was re-scored on four partitions it had never seen. It does not
reach the encoder on any of them: margins `+0.16` to `+0.27`, class-level intervals disjoint in all five
partitions. `verify_claims.py` now reads `2366/2366`, up from `2353`. That number rose because runs were
added; we say so here rather than let you find it.**

The rise is the one thing in this response that could be read as defiance of a reviewer's instruction, so it
goes first. You forbade *indiscriminate* additions and then named one specific run as the thing that would move
your score. We ran that one and nothing else. **No encoder was trained, nothing was downloaded, and no new
script was written**: `run_r101_adversarial_family.py` already had a `--holdout_seed` flag. Three invocations,
~10 minutes of CPU each. The 13 new assertions are all about those three logs.

Body still ends on page 9. 94 pages, up from 93: the new appendix table.

---

## 1. Your §26.2: search on one split, freeze, evaluate on an untouched split

You wrote that this is the experiment that would most move your assessment, and you were right that the paper
did not have it. What the paper *did* have, we found by measuring rather than remembering:

- **Appendix BB** already held the adversarial composite frozen after a search with oracle access to partition
  70 and re-scored on `shuffle_seed 71`: `0.7395 [0.677, 0.794]`.
- **Appendix AL**, the five-partition sweep, already held the *trained encoder* on that same partition:
  `0.9030 [0.866, 0.931]`.

And Appendix BB declined to put them together, in its own words: *"there is no trained row on that partition to
read it against."* That sentence was **true of the appendix and false of the document**. The half you asked for
existed thirty pages earlier in the same PDF.

So the round did two things: joined them, and (because one holdout split is an anecdote) re-scored the frozen
winner on partitions 72, 73 and 74 as well. **Table 36** (Appendix BB, cited from §4.2):

| split | search saw it | Tree-LSTM (95% CI) | frozen composite (95% CI) | bag | margin |
|---|---|---|---|---|---|
| 70 | **yes, oracle** | 0.8966 [.860, .925] | 0.6758 [.610, .735] | 0.5174 | +0.2208 |
| 71 | no | 0.9030 [.866, .931] | 0.7395 [.677, .794] | 0.5498 | +0.1635 |
| 72 | no | 0.8750 [.831, .910] | 0.6641 [.586, .731] | 0.5236 | +0.2109 |
| 73 | no | 0.8715 [.825, .907] | 0.6045 [.529, .673] | 0.4387 | +0.2670 |
| 74 | no | 0.8955 [.856, .926] | 0.6562 [.583, .722] | 0.4939 | +0.2393 |
| **71–74** | mean±sd | 0.8862±0.0154 | 0.6661±0.0556 | 0.5015±0.0477 | **+0.2202** |

**The margin is smallest at 71: the one holdout the paper already had.** Removing the search's oracle access
does not change the verdict, and the split where it came closest is the split the paper had already published.

**Four branches were written down before the runs**, in the run note and in
`CHANGES_SINCE_REVIEWED_VERSION.md`, exactly as `r92` and `r101` did: composite below the encoder everywhere
(print the range); at or above on one (narrow the claim to where it holds); above on all three (the pass is
broken out of sample and the body must say so); a run that fails to reproduce the search arm (report
unavailable, change nothing). Branch (i) is what happened. All four invocations return the **same
six-component winner** and the **same `0.6758`** on the search arm, which is the determinism check that makes
them comparable at all.

### What licenses the join, and what we refuse to claim

The two halves come from **different scripts**. Reading one against the other needs a shared control, and there
is one: both report the **full-token bag** on each partition, and they agree digit for digit
(`0.5498` at split 71 in both). That agreement is now asserted per split by a new gate check, and it is the
*only* thing that licenses the comparison. If it had failed on a partition, that partition would have been
dropped rather than explained.

Three caveats are printed **in the same appendix paragraph**, not in a footnote:

1. **This is not a new ceiling.** On 71–74 the composite is a frozen out-of-sample control, not a search
   result. It does not set `sup 𝓕₃`, which Track 1 still leaves at `0.276`.
2. **Both sides come from the sweep's environment**, where the encoder at split 70 reads `0.8966` and the body
   prints `0.894`. That is the `0.0023` cross-environment envelope the paper already documents. We use the
   sweep's rows on *both* sides and state the difference rather than print the flattering number.
3. **The composite is the most split-sensitive object in the comparison**: `±0.056` across 71–74, against the
   bag's `±0.048` and the encoder's `±0.015`. That dispersion is itself the argument for reading a *ceiling*
   off four partitions instead of one.

**This also answers your §9 better than §9 asks it.** You asked us to disclose that `0.676` is split-adaptive.
It is, and the disclosure is now a measurement: here is what happens when the adaptation is removed.

---

## 2. Your §26.1 and Weakness 1: the ideal family vs. the declared one

> *"the paper sometimes sounds as though it has solved the general problem of validating representation-level
> claims, whereas what it has actually developed is a powerful, family-relative falsification methodology."*

We measured before writing anything. Across the six body files, `𝓐_P` (the ideal family) occurred **three
times, all three on page 6**, and the statement you want (`sup 𝓕_t` is only a *lower bound* on `s`) existed
**only in the appendix**. The distinction you call fundamental was carried by prose on one page. That is a
routing failure, not a disagreement.

It is now **the body's second display equation**, in §3.3 on page 6:

> sup<sub>g∈𝓕ₜ</sub> M(g)  ≤  s  =  sup<sub>g∈𝓐_P</sub> M(g)
>
> Hence a *failure* is conclusive and a *pass* only family-relative, and widening can overturn a pass but never
> manufacture one (Cor. 3); the twin alone closes the gap (Prop. 4). **That limitation is also the
> deliverable**: Table 2 lists what a pass rules out.

Four deliberate choices:

- **Not boxed.** Round 44's box is the criterion; a second box would compete with it rather than subordinate
  itself to it. This is a scoping remark *about* the criterion.
- **`\sup\nolimits` on both operators**, for the reason round 44 recorded: in display style the subscript sets
  *below*, doubling the height. Page 6 had `+0.070pt` of slack.
- **Every symbol is already bound on page 6**: checked, not assumed, after round 44's promotion trap.
- **Funded by the prose it replaces.** Net-zero measured: identical per-page slack, identical placements,
  identical per-page line counts.

**The reframing matters more than the equation.** The finite-family limitation is not an apology in the paper's
margin; it is the research programme. `≤ +0.038` (widened by hand, `8191` sub-families), `+0.1584` (widened by
adversarial search) and now Part 1 above (searched, frozen, out of sample) are each an attempt to **raise the
paper's own lower bound and fail**. And there is one rung where the gap is exactly zero: at the shape-matched
twin every arrangement-invariant representation ties by construction, so `sup 𝓕₃ = s = 0.500` *by proof*
(Prop. 4). Your favourite result is the one place the ideal-vs-declared gap vanishes. The paper now says that.

**Your §7** (*the theorem is close to definitional*) is answered by the same edit rather than by argument. The
paper already pre-concedes it twice: `methodology.tex:106` bills the numbered results *"as scoping, not as
theoretical contributions"*, and Appendix AN says a reader who finds Theorem 1 close to a restatement *"is not
disagreeing with us"*. What was missing was the structural role: the theorem fixes the **direction** of
comparison; everything empirical is about the lower bound.

---

## 3. Your §14 and §13: four uncertainty sources, and S1–S3 as one decomposition among others

**§14, in the body, in one clause** (§3.4, where two of the four were already named): the class (equation) is
the primary unit, every interval is a class-level bootstrap, **seeds quantify training stochasticity only**, and
**split construction** and **family specification** are the other two uncertainties, each bounded on its own
(§3.3, Appendix AL). Four sources, each with a measured magnitude and an appendix.

**§13**, in our own voice and not yours (tenth consecutive round we have declined to paste a reviewer's
sentence): *"each 𝓕ₜ is declared, **as is the level hierarchy above it**, so what the audit can measure bounds
Theorem 1's `s` from below, never above."* The audit does not claim S1–S3 is the uniquely correct
decomposition. It measures how far a verdict moves under expansion: `≤ +0.038` by hand, `+0.1584` by search,
and now unchanged out of sample.

---

## 4. Your §15/§17 on density: measured again, and the italic was the problem this time

Round 42 answered the same complaint by grepping its own markup and cutting `\textbf` 206 → 98. So we grepped
again, and the mass had moved:

| | round 42 before | round 44 (what you read) | now |
|---|---|---|---|
| `\textbf` | 206 | 102 | **102** |
| `\emph` | 229 | 240 | **187** |
| body words | 6,541 | 6,228 | 6,228 |
| one emphasis every | 15.0 words | 18.2 words | **21.6 words** |

Across the two rounds: **435 → 289 emphasis spans, a 34% cut, with nothing removed.** Not one word, number,
scoping clause or caveat was deleted. That is provable rather than asserted: strip every `\emph{}` wrapper from
the six body files before and after, and all six are byte-identical.

The rule was mechanical and is stated in the tool that applied it: keep the **first** italicised instance of
each argument, convert later repeats, and never touch a per-sentence logical operator (`every`, `not`, `no`,
`only`, `all`, `both`) or a contrast pair.

**We did not reach the 150–170 we were aiming for, and the reason is worth stating.** 61 spans converted, then
**8 restored** after reading the rendered pages, because the remaining spans are singletons, protected
operators, or contrast pairs, and cutting further removes a distinction rather than a decoration. The eight:

- **`(i)`/`(ii)`/`(iii)` inside Theorem 1.** In a `theorem` environment the whole body is italic, so `\emph`
  renders these **upright**, and that upright/italic flip is the only thing separating three clauses in a wall
  of italic. In the *source* they look like decoration, which is exactly why the pass took them. **No gate in
  this repo can see this**; it was caught by reading page 5 as an image. A comment now pins them.
- **`novel *arrangement* far cheaper than novel *inventory*`** and **`a *failure* is conclusive, a *pass* only
  family-relative`** and the conclusion's **`the *direction* is forced; *which* family we declare is the
  choice`** — three contrast pairs where a first-use rule strips the italic *at the site where the contrast
  does the work*, because an earlier incidental use claimed the first instance.

Net-zero on every page, verified: identical slack profile, identical placements, identical line counts.

---

## 5. Four asks the paper already answers: by line number

| your point | where it already is |
|---|---|
| **§18**, *"make the conventional-report-vs-audit table central"* | **Table 2 already is that table**, page 5, 18 rows, columns *Claim audited · Level · Strongest admissible control · Reported · Verdict*. All six rows you sketch are in it. §4.3 carries a second one, per modality, on page 9. |
| **§12**, *"move Boolean8 into the main narrative"* | It is in the body: `experiments.tex` ×5, and `methodology.tex:176` prints the readout-closure near-miss; one of **our own** passes left unproved by `0.0027` at `boolean8 K=50` (`0.8706` against a bound of `0.8733`). *"the polynomial setting for the coverage mechanism"* is a literal pinned at exactly one occurrence in our gate script, so the mechanism is already scoped as polynomial-specific in the body. |
| **§26.1**, *"distinguish 𝓐_P from 𝓕"* | Stated at `methodology.tex:127(ii)` and in Appendix AN(c); §2 above gives it a display and a page-6 home. |
| **Q3/Q4** (no exact twin exists; approximate invariance) | The twin's exactness is Prop. 4; every other rung is explicitly the lower-bound reading. The asymmetry §2 prints is the general answer: an approximate member weakens a *pass*, never a *failure*. |

---

## 6. Three declines, each with its reason

**Your §26.3 / Q5: one truly non-symbolic modern case study. Declined, and named as the first item of future
work in your own term (Generality).** The paper's scope sentence, which you quote approvingly, is *portability,
not general validation*. What the existing ports establish is that the audit **fires** in three modalities, and
the code result you call *"essentially a negative result"* is the method working correctly: **our own** claimed
inversion does not replicate there, and we print that. A vision or language audit built inside one review round
could not carry the preregistered docstring, provenance tag and verifier assertions that every other run in this
paper carries. Shipping one that could not would contradict the paper's own argument. **We would rather score 6
on Generality than ship an audited claim we could not audit.**

**A caption and float number on §3.3's inline tabular. Declined again**, for page mechanics rather than
principle: a caption is ~3 lines there, and 3 lines at that point lands on a bistable page boundary that moves
~14 lines in one step. The lead-in states the inferential difference instead.

**§17's *"move the audit trail to the supplement"*. Partly declined.** Round 43's reviewer moved the audit
ledger **into** the body on the significance axis, and round 44 confirmed it. Compressing it two rounds after
promoting it would re-create a defect we were told to fix. What §4 does instead is reduce the machinery's
**voice** without removing any of it.

---

## 7. The bookkeeping, including a self-check that was wrong

- **`verify_claims.py`: 2353 → 2366**, exit 0 in all three copies. `statements.tex` prints the new total.
- **`REPRODUCE.md`'s index count: 44 → 76**, and *the 32 it gained are not new runs*. The self-check derived its
  list by **reading its own source** for load sites with a *literal* string argument, so whole families
  addressed by a computed name (five class partitions × three scripts, four replicate runs) were being
  asserted against while invisible to the check that exists to prove they are indexed. It now records stems as
  they are loaded. This is bookkeeping, not evidence, and `statements.tex` says so.
- **The same blind spot, in a second script.** `check_reviewer_map.py` resolves each map tag to exactly one
  `load_log()` call site. The moment `r82_ladder71` was loaded literally (the join reads it to check two
  scripts' intervals agree), the script reported it as tagged in no appendix, while Appendix AL *does* name it,
  as the glob `r82_ladder*`. The glob is now honoured rather than the failure silenced.
- **A new gate: `check_holdout_join()`.** It reads Table 36 and the five-partition sweep out of the source and
  asserts the shared bag agrees split by split, that exactly split 70 is marked seen-by-the-search, that each
  printed margin equals `encoder − composite`, that the intervals are disjoint, that the mean±sd row recomputes
  over the **four unseen** rows only, and that the three ranges in the prose (`+0.16`–`+0.27`, `+0.1635`–
  `+0.2670`, `+0.07`–`+0.15`) recompute from the cells. `--control` now fires **6** FAILs, up from 5.
- Two of its assertions exist because they caught this round's own near-misses: a dispersion quoted at the wrong
  **individuation** (the sweep's sd over *five* partitions where the comparison is over *four*), and a gap
  quoted across a **rounding boundary**.
- 0 errors · 0 undefined references · exactly 2 overfull boxes, both pre-existing · 0 floats too large · body
  ends page 9 · Figure 1 p3, Table 1 p4, Table 2 p5, Figure 2 p8, all unmoved · every rewritten `\ref` resolved
  against the `.aux`.

---

## 8. What we think is still open, in your terms

Generality, and we agree with your framing of it. The audit is a **family-relative falsification** instrument;
it has been ported three times, and one of those ports returns a negative result about our own earlier claim.
What it has not been shown to do is validate a representation-level claim about a modern large model on a task
nobody chose for it. That is the next paper, and it needs the same provenance discipline as this one, which is
why it is not in this one.
