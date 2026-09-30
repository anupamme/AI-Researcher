# Response to the round-33 review

*Not part of the paper.*

**Summary: you told us we did not need another ten experiments, we needed one conceptual upgrade,
and you were right, so this round is almost entirely that upgrade.** The paper now reads in the order
you specified: a **general principle** for evaluating representation-level claims, symbolic
mathematics as the **detailed case study**, and SCAN and Python code as **two ports** that show the
procedure travels. Three measurements made the diagnosis undeniable: `case study`, `instantiat`,
`general principle` and `general framework` appeared **zero times** across all six body files, our
non-symbolic evidence sat in **three fragments** under a subsection titled *Does Clearing Every Bag
Make a Score Evidence of Composition?*, and the code port stopped at S2. All three are fixed.

We also did the one thing that was genuinely missing rather than merely mispositioned: **`r99`
finishes the code ladder to S3**, no training and no download, and it returns a **fourth distinct
verdict**, the family already attains the corpus maximum, so no score on Type-2 clones is evidence
about structure above S3. That is the sharpest available demonstration that the audit
**discriminates domains instead of rubber-stamping them**, and it is billed as a verdict of the
method, not as a win.

On your reason (1), the theorem being definitional: **we had already conceded exactly that, in our
own words, in §3.4**: *"billed as scoping rather than as theoretical contributions … a reader who
finds the theorem close to a restatement of what an admissible family means is not disagreeing with
us"*, and you replied *"I agree."* We have not re-litigated it and we did not touch it. On reason
(2), family-relativity is inherent and the paper says so in three places. So we spent the round on
reason (3).

Assertion count **2219 → 2250** (+31). One new run (`r99`), on a corpus already in the paper.

---

## 1. The upgrade: general principle → case study → two ports

Stated in our own words, once, in **three positions**, because the lesson from round 30 is that
redundancy is not salience, position and form are:

- **Abstract ¶2 tail:** *"The levels name cues, not algebra, so symbolic-expression encoders are this
  paper's case study, not its scope."*
- **§1 contribution (3) lead:** *"symbolic-expression encoders are this paper's detailed case study,
  and SCAN and Python code are two ports where the same code instantiates the same ladder, billed as
  evidence the procedure is usable and travels, not as the thesis."*
- **A new §4.3, *The Same Audit Outside Symbolic Mathematics***, its first sentence: *"S1–S3 name
  cues, not algebra: everything above is the detailed case study, and a new modality needs only a
  parser and a level assignment."*

Each of the three states the **limit in the same breath**: *portability, not general validation*,
never prevalence in those literatures. We would rather under-claim the ports than have you find the
gap for us.

**§4.3 is consolidation, not addition.** `r95` was a sub-clause of §4.1's *Two encoders we did not
build*; `r96` was a clause inside §4.2 ¶3; `r97` was §4.2 ¶6. Same evidence, one visible block, and
it costs the page budget a heading rather than a paragraph. Protocol-disagreement is now §4.4 and
coverage/LOSO §4.5.

## 2. `r99`: your program-representations bullet, finished to S3

Your §24 bullet was *identifier inventory / API inventory / local AST fragments*. We had the first
two. `r99` adds the third:

- **Corpus reused verbatim** from `r95`: seed 95, 300 Type-2 clone classes × 4 members, 40–400 AST
  nodes, drawn from **1003 real Python stdlib functions** on the local machine. No download, and
  `r95` was neither re-run nor altered.
- **The only new code is an adapter**, exactly as for SCAN: Python `ast` → our `Node`. Because
  `structural_baselines._children` reads only `.left`/`.right`, **the right-fold of n-ary children is
  ours**, and that is disclosed in the same sentence as the mapping: the corpus is now
  *constructed* twice over (clone relation and tree shape), so no prevalence claim follows from it.
- **No new measurement code.** `phi_d_bagger`, `wl_subtree_bagger_stable`,
  `canonical_tree_bagger(ordered=True)` and `bag_classifier_accuracy` all consume `Node` unchanged.
  No twin machinery is needed: φ_d is order-blind by construction, so Corollary 1 applies directly,
  and only the ordered completion is an extension, labelled as one.
- **The prediction was pre-registered in the docstring before the full run**, and it held:
  identifier bag alone **0.770** (chance 0.0033), S2 **0.987**, and **every** F₃ member attains
  **0.990**: *exactly the maximum this corpus admits*.

**The verdict is a boundary, and we prefer it to a replication.** A clone detector's accuracy on this
corpus cannot be evidence about structure above S3, because the audit's own controls already saturate
it. That is a fourth distinct verdict alongside *exposed* (AI Feynman), *entitlement, not defect*
(Lample–Charton), and *upheld* (the 14-corpus leaderboard), and it has its own row in Table 2,
saying so plainly.

## 3. Your §16 was already in the paper, in the wrong position: the fourteenth time

You asked for the prespecified-vs-descriptive statement to be prominent in §4. It existed, at the
**tail of a §3 paragraph about Figure 4**, four pages before the experiments it governs. It is now
the second sentence of §4, and **deleted from §3 in the same edit**; this paper's own recorded
lesson is that leaving both copies is redundancy, not salience.

This is the fourteenth instance in this paper's revision history of *"already there, wrong position
or wrong format."* We record it as such because the pattern is now the single most reliable predictor
of what a reviewer will say we did not do.

## 4. Your §17 was already satisfied in the body, so we fixed what actually caused the impression

Measured, not assumed: `verify_claims`, `assertions` and the assertion count appear **zero times** in
the numbered body. The infrastructure lives in the page-limit-exempt statements and Appendix A–K,
whose reading map already tells a reader who wants the science and not the bookkeeping to skip A–K.

What created the impression was **one 25-clause mega-sentence** in the Reproducibility Statement. It
is now a short lead plus correct pointers, and it ends with the sentence that was missing:
*"This is bookkeeping, not evidence: it establishes that the numbers in the paper are the numbers the
runs produced, and nothing about whether the audit is the right test."* Zero cost to the body. The
count, the `42`-run claim and the five *not recorded* cells are unchanged; all three are gated by
`check_reproduce_index()`, which derives its list from the verifier's own `load_log()` call sites.

Rewriting that sentence is also what exposed the round's fourth caught defect, below: it had pointed
twice at **Appendix A** for things Appendix A does not contain.

## 5. §18, §12, §14 and the title

- **§18, intuition before Definition 1.** Genuinely absent *at that position*; it existed in §1's box
  and the `x+y` example, four pages earlier. Added in **our** vocabulary rather than yours: your
  proposed text conflated the *control* (a representation) with the *twin* (a form pair), and
  reviewer-supplied prose has been false about this paper in five of the last seven rounds. **Funded
  by absorption**: §3's *"What passing establishes, stated once"* is folded into the new paragraph
  and deleted, so the intuition now arrives *before* the formalism and §3 nets ≈ 0 lines.
- **§12.** `systematic` appeared **zero times** in the body. The conclusion's (3) now reads *"does not
  establish systematic compositional reasoning"*, paired explicitly with *bounded structural **and
  lexical** alternatives*.
- **§14.** Agreed, and this is what funded the round. The `65,527/65,528` enumeration is **de-billed
  from the abstract and from §1(2)**, keeping its own §4.2 paragraph and its Table 2 row: two
  statements, in the two places that earn them. The abstract is **390 words** of source, down from
  449.
- **The title.** We kept the previous reviewer's hook and sharpened the subtitle to name the scope:
  ***When Stronger Baselines Mislead: Admissibility Auditing for Representation-Level Claims***.
- **§15.** Measured: the token-bag story is already appendix-only in the body. No edit.

## 6. Where you and the previous reviewer disagree, and how we resolved it

Round 32's reviewer called *an evaluation protocol is itself a hypothesis about what generalization
means* *"potentially more profound — I would elevate this"*, and elevated it we did. Your three
messages have **no slot for it**.

**We resolved this additively rather than picking a side, and we are telling you so rather than
deciding it quietly.** Your M2 (that the statistic is a **family-level ceiling**, and that *"beat
the strongest available baseline"* is not a valid evidential principle for a representation-level
claim) is now explicit inside contribution **(1)**, where it belongs. Contribution **(2)** remains
protocol-as-hypothesis. The cost is a clause; both asks are satisfied; neither reviewer's point was
silently dropped.

## 7. Verification, and four defects our own gates caught

1. **A cut that *declined* something was load-bearing.** §4.2's `6.1×` aside exists to say we are
   **not** quoting the flattering ratio, and Appendix AY's consistency argument cites it. Cutting it
   as surplus would have removed the paper's own act of refusal. Restored. **A sentence whose content
   is a refusal is not surplus prose.**
2. **The heading-placement gate gave a false green.** `p9: CONCLUSION` and `p10: ETHICS` were both
   correct (exactly what the gate tested), while the conclusion's *prose* spilled four lines onto
   page 10. Heading placement proves where a section starts, never where the body ends. The gate now
   reads **page 10's first body line** as well.
3. **A page-limit failure can be *packing* rather than *volume*.** Pages 1–9 held **573** body text
   lines against the previous build's **581**: eight lines *shorter* in total text, and still
   spilling. Cause: p7 carries five heading blocks and p8 four paragraph breaks, and LaTeX was
   stretching **seven slots** of glue there because §4.3's `\subsection` heading plus its two
   required following lines could not land at p8's bottom, so every cut aimed at those pages was
   absorbed. Fixed by cutting **only from page 9** and shortening §4.3's framing paragraph so the
   heading had a clean break to take. No finding was removed to make the page.
4. **A cross-reference is a claim, and two of ours were false.** The Reproducibility Statement said
   *"Appendix A lists the tags"* and *"Appendix A lists what it checks"*. Appendix A is *Provenance,
   Pipeline, and Domain Guards*: the tag table is **Appendix K**, and **no appendix lists what the
   verifier checks**. The same sentence also claimed *"all tables derive from a single frozen run
   family"*, which Appendix A's own text contradicts; it records that two of them do not. Fixed to
   point at `\ref{app:provenance}`, `REPRODUCE.md` and Appendix A's actual content. Found by
   resolving **every** hardcoded appendix letter in the body against the built letters, because the
   appendix letters here are hand-written in `\subsection*` and pinned with `\applabel`, so a
   pointer typed as a letter is unverified prose. The other nine resolved correctly.
   **Consequence for the verifier:** making the second sentence true required closing the one
   `load_log()` call site of 69 that *printed and returned* on a missing log instead of failing
   (`r74_probe_matrix`); the silent-skip class this repo has fixed twice before.

**Verifier.** Four new assertion groups, each added because a body literal did not trace to a log:
`r99`'s corpus and class counts (`1003` appeared in **no log**, so the runner now records
`n_functions_pool`); `boolean8`'s twin margin `+0.299` **and** the claim that it is *wider* than
`poly8`'s, asserted as the comparison the paper actually makes rather than as two loose numbers; and
`poly8`'s `1102` classes. Two loopholes surfaced in the process: the `poly8` comparison **silently
skipped** on a wrong dict key and returned one assertion where two were expected (a missing operand
now **FAILs**), and the survey selector `endswith("poly8")` matched **two** rows, the second being
`EQNET simplepoly8`; the corpus the paper names as the *weak* one, so it is now an exact match.

**Gates on the final build:** `0` errors · `0` undefined references or citations · `0` `Float too
large` · exactly **2** overfull boxes, both pre-existing · **87 pages** · abstract ends page 1, body
ends page 9, page 10's first body line is the Ethics Statement · all thirteen body section headings
on the same page as the round-32 baseline (§1 p1, §2 p3, §3 p4, §4 p7, §5 p9, Ethics p10) ·
`check_protected_claims.py` PASS at 19 protected claims and 2 required absences, with both controls
firing · `verify_claims.py` exit `0` at **2250/2250 in all three shipped code copies** · pages 1, 8
and 9 read as rendered images, which is what caught a sentence fragment every automated gate passed.
