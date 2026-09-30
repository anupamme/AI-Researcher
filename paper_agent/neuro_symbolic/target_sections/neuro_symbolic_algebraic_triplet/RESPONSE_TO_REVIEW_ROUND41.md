# Response to the round-41 review

**One new experiment (the one you asked for) one new proposition, and no net body lines. 93 pages (+3,
all of it the new appendix section), body still ends on page 9.** You asked for a single decisive addition
rather than twenty more experiments. This is that addition, plus the result it produced, **which went
against us and is printed in the body anyway**.

The headline, before anything else: **the adversarial search you asked for beat the strongest control we had
published.** It did not beat the encoder. Our margin at the cell in question falls from `+0.3398` to
**`+0.1814`**, the ratio from `1.7×` to **`1.3×`**, and **the body now prints the searched number where it
used to print the catalogued one**.

---

## 0. The build you read, with timestamps: stated once, then not used

Your review cites `iclr2027_conference(20260910-045255).pdf`, **04:52:55**. That sits *between* round 40's
reviewed build (**03:20:34**) and round 39's final build (**07:58:35**), so it is an intermediate build from
the round-39 session, and round 40's changes are not in it. Three internal markers confirm it: §17 praises
abstract ¶1 and never mentions ¶2's new opener; §3's six-item list maps onto the **six**-row version of
§3.3's tabular, before a 7th row was added; and nothing anywhere objects to the word "complete", which round
40 removed from Definition 1.

**We spent the staleness card two rounds ago and are not spending it again.** Every ask below is answered as
if made against the current text. Where an ask is already satisfied, we say which page it is on rather than
adding a sentence, and where it is not, we changed the paper.

---

## 1. §19: the adversarial family challenge, run; and the rung where it was already answered by proof

You wrote that if we add one experiment it should be the adversarial expansion of F3, because it attacks
*"You only ruled out the explanations you decided in advance to include."* Two things are now true, and they
are different things.

### 1a. At the shape-matched twin that objection has **no force at all**, and the paper now says so (Prop. 4)

Theorem 1 was always quantified over the unrestricted class: *"let A_P be **every** representation
invariant to P"*. The twin pairs a held-out form with a sibling-swapped partner carrying the **identical**
variable multiset, operator/arity multiset and bounded local shape, differing in arrangement alone. So for
every `g ∈ A_P`: `g(T) = g(T')`, hence equal distance to any centroid, hence a tie on every trial; under the
label-blind tie rule (implemented, disclosed and separately audited, tag `r78`) every tie scores exactly
`0.500`. Therefore

> `s = sup{M(g) : g ∈ A_P} = 0.500`, **exactly and attained** — not lower-bounded — and by Prop. 1
> unchanged by post-composition with **any** readout `f`, including a trained one at any capacity.

**At this rung `sup F_3 = s`.** The declared family is not a stand-in for anything; it computes the
unenumerable class's supremum exactly, and `M(h) = 0.994 > s` meets Theorem 1(ii) with no family
relativisation to carry. Your requested search, run *here*, is a maximisation and could therefore only
**lower**-bound a value that is already an equality.

**The paper had every ingredient and never assembled them.** `A_P` appeared in exactly seven places, none of
them in a twin section, and `experiments.tex` contained the word "invariant" zero times. Every statement of
the twin result was family-relative. That is now fixed in five places:

| where | now reads |
|---|---|
| abstract ¶3 (**p1**) | *every arrangement-invariant representation, **declared or not**, is pinned at exactly 0.500 by proof* |
| §1 ¶4 (**p2**) | *Every representation invariant to arrangement (**not** only the declared family's members) is pinned at exactly 0.500, chance, by proof, a trained readout over one included at any capacity* |
| §4.2 | same quantifier, with the `\ref` to Prop. 4 |
| Figure 1, rung 4 (**p3**) | *clears, and here the ceiling **is a theorem**: **any** arrangement-invariant map is pinned at chance* |
| Appendix, **Proposition 4** + proof | stated, proved, and placed immediately after Prop. 3 as its complement |

All five are net-zero or free; the Figure 1 change was measured for width before it was made (see §9).

### 1b. At the rung where the ceiling **is** empirical, we ran your search, and it beat us

New run, tag **`r101_adversarial_family`**, Appendix **BB**, `run_r101_adversarial_family.py`, ~10 min 27 s,
**CPU only, nothing trained anywhere in the run**.

**Three advantages handed to the adversary deliberately**, because an adversary that loses without them
establishes nothing: it may **compose** descriptors rather than pick from a list; it gets **oracle access to
the very split we report**; and it starts from the strongest control the paper publishes.

- **Search space:** 28 order-blind primitives (the seven declared, `φ_d` at d ∈ {3,5,6,7}, `WL_h` at
  h ∈ {4,5,6}, the full-token / variable-blind / variable-only / tree-local bags, the canonical unordered
  tree bag, graphlet bags at orders 3, 4, 3–4, 3–5, a root-to-leaf path bag, Laplacian-spectrum bags at 1–4
  eigenvalues). Candidates are weighted unions of ≤6 primitives; greedy forward selection then weight
  climbing, from the strongest singleton and from three random size-3 restarts. **706 distinct composites
  scored in 46 ladder calls**, each by the shipped `r71` ladder with the bagger registry swapped; no
  scoring code is new.
- **Admissibility gate, verbatim from `r92`:** the per-instance twin test on the published K=500 swap split,
  348 classes, and **a member must be pinned at exactly 0.500 on every instance, not on average**. Positive
  control `bag_tree_local` pins at `0.500`; negative control `bag_token_ngram` reads `0.681034` and is
  excluded as an extension X. **Both controls behaved.** All 28 primitives were admitted; **the two
  discovered winners were re-gated after the search and pinned at exactly 0.500.**
- **Three reference lines separated *before* the search**, because the paper prints two different numbers:
  **L1** = sup over the seven maps Definition 1 enumerates, `0.2763`; **L2** = sup over weighted *unions* of
  those seven; **L3** = sup over every order-blind descriptor the twin test admits, published value
  `0.5174` (the full-token bag): the line §4.2's ratio is read against and the one your objection means.
  **This resolved the open question we flagged before writing any "no admissible descriptor beats X"
  sentence.**

**Two pre-registered predictions, written into the docstring before the run and not renegotiated after:**

- **Track 1 held, and it strengthens a printed number.** All 67 candidates: every union, every reweighting,
  four independent local optima: read exactly `0.2763`. So **L2 = L1**, and the printed `0.276` is the
  supremum not merely over Definition 1's enumeration but over **every weighted union of it**. The
  readout-closed bound `0.2962` is undisturbed.
- **Track 2 did *not* hold, and that is the result.** Registered: the search would not materially exceed
  `0.5174`. **It did.** Best composite `0.6758`, class bootstrap `[0.6096, 0.7351]` (**`+0.1584` over the
  strongest control we had published**) namely
  `bag[φ_{d=6} + 8·tok_full + tok_varblind + 16·tok_varonly + WL_1 + WL_4]`, six components. **Not one lucky
  basin**: unrelated restarts reached `0.6577` and `0.6523`, the greedy run `0.6635`. **And not an artifact
  of the selected split, in the direction that is worse for us**: re-scored on a partition the search never
  saw (`shuffle_seed 71`) it reads `0.7395` `[0.6770, 0.7937]` against the full-token bag's `0.5498`. We
  report that as a robustness check on the *search*, **not** as a new ceiling; there is no trained row on
  that partition, and a ceiling from one split against an encoder from another is the cross-split error this
  paper flags elsewhere.
- **The mechanism is not mysterious, and naming it matters:** every gain comes from up-weighting descriptors
  that read the **variable identity** `φ_d` anonymises away, which is exactly why the full-token bag
  outscored `sup F_3` in the first place. **The search found more of a cue the paper had already
  identified, not a new kind of explanation.**
- **Nor is the ordering at that cell an artifact of `k=5`, the other quantity it could have been fitted to.**
  The ladder logs every candidate at every `k` it sweeps, so the winner's own sweep needed no further run:
  the searched composite reads `0.8208 / 0.7469 / 0.6758 / 0.5354` at `k = 1/3/5/10` against the encoder's
  `1.000 / 0.965 / 0.894 / 0.710`. **The encoder leads the *searched* baseline at every `k`, by between
  `+0.17` and `+0.22`**: flat in `k`, not largest at the value the body quotes. Track 1's supremum is not
  `k=5`-specific either (`0.2955 / 0.2841 / 0.2763 / 0.2524`). This is a stronger statement than the
  twenty-cell one in the k-tie appendix, which concerns *catalogued* baselines, and it is available at
  `K=500` alone, where the search ran; both are now stated with that distinction in print.

**What it cost us, in the body, not in a footnote:** §4.2's ratio at K=500 was `0.894` vs `0.517`, `1.7×`;
against the searched control it is **`1.3×`**. Against the encoder's published class-level lower bound
`0.8572` the margin falls from `+0.3398` to **`+0.1814`**. §3.3's measured chain now ends *"0.517 — **0.676**
once such bags may be composed"*, and its five apparent margins are `+0.874 / +0.618 / +0.598 / +0.377 /
+0.218` according to which control is called "the invariant baseline". **The verdict holds; the margin is
narrower; the body prints the narrower one.**

---

## 2. §12: the biggest weakness, answered rung by rung rather than in general

You put it exactly right: the paper established *"exceeds the declared family"*, not *"exceeds every
possible P-invariant explanation"*. Our answer is not that the distinction is unimportant. It is that
**the distinction is rung-indexed, and the paper was stating it as if it were uniform**:

- **At the twin: the gap is zero, by proof.** Prop. 4, §1a above.
- **At UnseenEqClass, AI Feynman, every level below S3: the gap is real, and it is now *searched* rather
  than argued about.** §1b. It cost us `0.1584`.
- **The honest residual is not *which representation*: every invariant one is covered by proof, but
  *which perturbation class* a twin realises.** And that residual was already **measured**: the nested
  probe ladder shows that **one rung looser** than the twin the body reports, the test admits a control
  scoring **`0.909`** on the very perturbation membership requires it not to see, while at the **strictly
  most-matched** rung all three bags are pinned and the encoder gap stays positive; and on the rotation twin
  the same bags reach `0.889`–`0.901`, which is why rotation is reported as the weaker probe. **That is a
  narrower limitation than family-relativity, and a quantified one.**

**Three blanket concessions that actively denied what the paper proves are now rung-indexed rather than
deleted.** The appendix's *"no realisable instrument is it"* now reads *"no **generally** realisable
instrument is it"* followed by the exception and its proof reference. §3.3's close still says **"And the
family is incomplete by construction: the audit falsifies within F_3, never outside it — the standing
limitation of the method"** and now adds *"at every rung but the twin, where sup F_3 = s exactly"*. Clause
(iii) (*"it does not establish that F_3 contains all P-invariant explanations"*) **survives verbatim**; it
is pinned at ==1 by a gate and we qualified around it rather than through it.

**And the conflation the fix is stated to remove is separated in print.** The appendix records that a
baseline *observed* at exactly `0.500` on all 348 classes is admitted under an **operational** definition and
that this is a membership test, not a proof of global invariance. That caveat governs
*observation ⇒ invariance* and **stands unchanged**. Prop. 4 runs the other way,
*invariance ⇒ 0.500*, a deduction from the hypothesis that needs no test. A paragraph says exactly this,
because reading Prop. 4 as weakening the caveat is the error it exists to prevent.

**Your warning is taken literally.** You wrote that drift toward *"therefore the model understands
structure"* moves 7 → 5/6. Every installation of Prop. 4 carries, in the same breath, that removing the
ambiguity is **not** certification, and cites Prop. 3. The proposition's scope note ends: **"The
proposition's content is that the incompleteness objection has no force at this one rung — not that the
encoder is shown to compose."** The conclusion still ends *"The audit falsifies; it certifies nothing."*

---

## 3. §13 and §24 weakness 6: the theoretical contribution, named

You wrote that F3 is hand-designed, so the result is family-relative evidence; and that *"the theoretical
results are largely formal consequences of the ceiling definition."* We accept that reading of Theorem 1:
the paper itself now says a reader who finds it close to a restatement is **not disagreeing with us**, and
presents it as scoping.

**Proposition 4 is not of that kind.** It is not a consequence of what "admissible family" means; it is a
property of a **construction**: that the shape-matched twin protocol makes the supremum over an
unenumerable class *computable*, exactly, and closed under trained readouts at any capacity. It has four
stated scope conditions, all of them limiting: (a) P is the arrangement a *given* twin realises, not all of
S3; (b) it rests on the label-blind tie rule; (c) `M` reads only the representation, so an order-exploiting
rule is outside `A_P` by construction; (d) it licenses nothing about mechanism.

**Prop. 3 does not contradict it and is cited beside it.** Prop. 3 bounds *licensing* (no admissible family
certifies, for every admissible family); Prop. 4 concerns whether `sup F_t = s` at a rung. They are
complements, which is why Prop. 4 sits immediately after Prop. 3's proof.

---

## 4. §14 and §21: what is already there, and the one gap we concede

**§21 is already in the paper, on p1 and p9.** On `boolean8` at K=190 one set of trained **GIN** weights
reads **`.881`** on UnseenEqClass and **`.511`** on the shape-matched twin against chance `.500`, and *"of
the three, only the Tree-LSTM clears both"* (§4.4). Three architectures are trained. **The method
distinguishes architectures; it does not merely validate a Tree-LSTM.**

**Four of the audited results are other people's**, including a released **80M-parameter** integration
encoder scoring `0.872` where a zero-parameter operator/arity bag scores `0.941`: an S2 task correctly
identified, and a 14-corpus leaderboard audited the same way and **upheld**.

**The gap, conceded in print rather than argued away** (new paragraph, Appendix AR): both external audits
stop at **S2**. **No pretrained model has been run on the shape-matched twin**: the one rung whose ceiling
is known by proof and the rung our constructive claim rests on. Building twins for an integration benchmark
needs an equivalence oracle for that benchmark. **It is the single largest piece of coverage this paper does
not have**, and it is stated as an open gap, not a footnote. It is in the appendix because p9 is full to
`0.07pt` and we will not buy body space by deleting a self-limiting clause.

---

## 5. §16 and §17: the four-object critical path is now in the body

The fifteen-minute path existed, correctly, at the head of the appendix; i.e. **page 11+**, which for a
reader deciding what to read is nowhere. It is now mirrored into **§1 ¶2, page 2**, funded by an equal cut
inside §1: *"**four objects are the critical path**: Figure 1, the test, each step carrying the published
result that settles it; Table 2, every claim, its evidence and its verdict on one page; §4.2's twin; and
§3.3."* It lands one sentence after the *"different inferential object"* framing and one before *"What it
refutes is an **evidential** interpretation, not the hypothesis of compositional reasoning."*

On §16's "too much machinery": no machinery was added to the body this round. The body is **net +1 rendered
character**, measured, not estimated.

---

## 6. A defect we found and are reporting against ourselves

The caption of the stronger-baselines table printed tree-edit distance at **`0.733`**: a value this paper
**retracted**, documents as a fixed defect, and whose correction *runs in our favour*. **Its own table row,
directly beneath it, printed `0.723`.** A second stale site printed it too. Both are corrected.

`check_figure_provenance.py` pinned `0.723` in the *figure*; **nothing checked a caption against the tabular
it captions**. There is now a gate that does: `check_caption_rows.py`, 34 caption literals across 35 floats
with tabulars, 19 via a declared allowance. Run against the pre-fix text **it fires on exactly this
defect**; that is its positive control.

**And the round's own result is now in the ledger it belongs in.** The table of *what running the audit
changes* had recorded eight already-published results and omitted the one this round narrowed; its `poly8`
row now reads *"restated: passes F₃ at K≥200, over what is tested; margin 1.7× falls to 1.3× under a search
of ours"*. It is **not** an eighth entry in the incident ledger, and Appendix BB now says why in print:
**no published number of ours was wrong**; what was too weak was the *instrument*, a list where a search was
available. The two tables count different things and the paper now distinguishes them where a reader meets
both on the same page.

---

## 7. What we decline, and why

- **§22's do-not-add list is honoured in full**: no more AI Feynman equations, no more seeds, no more E3
  variants, no more tiny synthetic datasets, no additional baseline, **no further proof of Theorem 1**.
  `r101` is none of these, and Prop. 4 is a proposition about a *construction*.
- **§6** the compositional-generalization claim is the most vulnerable claim we make; it is already scoped in
  print as *"calling that composition-of-known-transformations generalization is an interpretation"*, and the
  conclusion says *"not systematic compositional reasoning"*. No edit.
- **§7** SCAN is *"useful but dangerous"*; it is already billed as **portability, not general validation**,
  and nothing in the thesis leans on it. No edit.
- **§15** symbolic strong / SCAN partial / code negative is already the paper's own framing.
- **§11** the revision history stays.
- **We did not widen Prop. 4 to "structure".** Exactness holds for the arrangement difference a twin
  realises. Claiming invariance-class exactness for S3 as a whole would be this round's overclaim and would
  contradict the membership caveat, which stays.
- **We do not present tree-edit distance as bounding `s`.** It is order-**sensitive**, hence not in `A_P`,
  and our own Theorem 1(iii) says it bounds `s` at no value. Its `0.723` is a fortiori evidence only.

---

## 8. Verification

`err 0`, `undef 0`, `0 Float too large`, **exactly 2** overfull (`6.4211pt` vbox, `3.509pt` hbox, both
pre-existing), 0 real bibtex warnings, **93 pages**, abstract ends **p1**, **body ends p9** (read from p10's
first *body* line: the Ethics heading), References **p11**, so **pages 1–90 are structurally unchanged and
the +3 is Appendix BB, pp. 91–93**, outside the page limit. The page-count gate was re-pinned 90 → 93 once,
deliberately, with the increase fully attributed; no script or `.tex` hardcodes it.

All **thirteen** body headings on their pre-round pages (§1 p1 · §2 p3 · §3 p4 · §3.1 p4 · §3.2 p4 · §3.3 p6
· §3.4 p7 · §4 p7 · §4.1 p7 · §4.2 p7 · §4.3 p9 · §4.4 p9 · §5 p9), all four body floats on theirs
(**Fig 1 p3 · Table 1 p4 · Table 2 p5 · Fig 2 p8**), and the per-page slack profile **byte-identical** to the
pre-round baseline (p4 `+0.736`, p6 `+0.070`, p9 `+0.070`, every other page `0.000`). The bistable p8/§4.3
boundary landed in its canonical state.

Gates: `check_protected_claims.py` **PASS** (19 claims, 4 absences over 6+5 files, 3 document-wide, run
after each rewrite, including the abstract's three ==1 literals and clause (iii)'s). `check_reviewer_map.py`
**PASS** (17 rows, 285 checks, 44 tags, 54 letters): one row's Claim cell was rejected as not a verbatim
body quote and was corrected to the body's wording, which is the check working.
`check_figure_provenance.py` **PASS** on 10 values, control fires 2 FAILs. `check_caption_rows.py` **PASS**,
control fires 1 FAIL. `verify_claims.py` **2336/2336, exit 0, in all three copies**: 32 new assertions for
`r101`, including that both admissibility controls behaved, that Track 2's prediction **failed**, that
`F_3` is unchanged, that the per-`k` margins against the searched composite are read from **both** logs rather
than typed, and that the run's text log is shipped so the per-restart scores are checkable at all.
`REPRODUCE.md` carries `r101` with its command and runtime; the verifier checks that index against its own
`load_log()` call sites and pins the count at **44**.

A final adversarial readiness pass over the built PDF found four things, all closed. One appendix sentence
still called `1.7×` *"the published ratio"* after the body moved to `1.3×`, and its five-partition robustness
sweep does not cover the searched line; both now said explicitly. The audit-changes ledger omitted this
round's own narrowing (above). The searched composite's logged `k`-sweep had never been printed (§1b). And
three per-restart scores the appendix quotes live only in the run's **text** log, which the shipping
supplement had never received; it is synced, redacted, and a positive control confirms that removing it
**fails** the verifier rather than skipping. **Figure 1 was examined and deliberately left unchanged:** its
rung-3 bars are the two reference lines the tables carry across all five `K`, and its verdict is a scaling
claim about those rows, whereas the searched composite exists at `K=500` only; the searched number is printed
in §3.3's chain and §4.2's ratio instead.

Pages **1, 2, 3, 6 and 9** were read as rendered images. The `\resizebox` in Figure 1 scales by **width**, so
the widened verdict cell was measured before it was written: the binding maximum is rung 3's line at
`97.75pt` and the two new lines are `89.71pt` and `93.44pt`, so the bounding box, the scale factor and every
page below are provably untouched.
