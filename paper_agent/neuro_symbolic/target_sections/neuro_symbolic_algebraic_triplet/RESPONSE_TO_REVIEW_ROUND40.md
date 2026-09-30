# Response to the round-40 review

**Zero new experiments, zero new runs, zero new floats, no net body lines. 90 pages, body still ends on
page 9.** This is the fifth consecutive review to say the paper does not need more evidence, and the first
to say precisely what it needs instead.

## 0. The build you read, once, with timestamps, and why it changes nothing below

Your review cites a PDF timestamped **03:20:34**. The previous revision's final build was **07:58:35**,
4h38m later, and the file you read is no longer on disk. From your own quotations that build **did**
contain the corrected Figure 1 label (`0.276`), §3.3's five-rung chain (you quote `0.517`), the Definition 1
rename and the Theorem 1 retitle. It **probably did not** contain the last two changes of that round: your
R2 says the paper has *"too much Feynman material before reaching its strongest experiment"* and treats the
twin *"as just another result"*, which is not consistent with a page-2 paragraph headed *"The sharpest form
of the test, and the result we would put first"* and an abstract paragraph 3 that opens on the twin. Both
were in the 07:58:35 build.

We are not arguing from that. We spent the staleness card last round and every ask below is answered as if
it were made against the current text, because two of your three Requests turned out to be answerable
**from the render**, which is a stronger response than a re-edit, and because the third turned out to
identify a real presentation failure that the newer build did not fix either.

---

## 1. §14: the one sentence, installed in three places, with one word added

You wrote: *"I don't think you need more experiments to turn this into an 8. You need to make the
contribution more obviously novel."* And: *"Baseline comparison estimates relative performance.
Admissibility auditing estimates the maximum performance compatible with an alternative explanation. These
are fundamentally different inferential objects. That is your paper. Everything else should demonstrate
it."*

We agree that this is the paper, and we did not have it stated as an *object* anywhere. It is now in three
places, and it is the first thing after the problem statement in both the abstract and §1.

- **Abstract ¶2's opening sentence** (page 1, slots 017–019), previously *"Admissibility auditing therefore
  evaluates…"*:

  > **A baseline comparison estimates *relative performance*; *admissibility auditing* estimates the best
  > score the *declared* alternatives can reach — a different inferential object.**

- **§1 ¶2** (page 2, slots 062–064), where the ceiling is defined:

  > **A baseline comparison estimates *relative performance*; this estimates the *best score the declared
  > alternatives can reach* — a different inferential object, not a stronger baseline, and *no* published
  > evaluation reports it.**

- **§3.3's contrast table lead-in** (page 6, slots 322–323); see §3 below.

**We added one word to your sentence: *declared*.** Your wording (*"the maximum performance compatible
with an alternative explanation"*) is a bound over *all* alternative explanations, which is exactly the
claim your own §6 tells us to stop making, and which Corollary 3 and §3.2's clause (iii) exist in order to
deny (*"it does not establish that $\mathcal{F}_3$ contains all $P$-invariant explanations"*). The ceiling
is a supremum over an **enumerated, prespecified** family. With *declared* in it your sentence is true of
this paper and still names a different inferential object; without it, it is the overclaim you attack two
sections later. This is the fifth consecutive round in which a reviewer's proposed sentence would have been
false about the paper as written, and we mention it only because the pattern is now informative: the
distance between what the framework sounds like and what it licenses is small enough to cross by accident,
which is itself an argument for the paper.

---

## 2. W1: the theorem's concession is now a claim, and we did not delete the concession

You call Theorem 1 *"almost immediate from the definition of the supremum"* and quote the paper's own *"a
simple formal justification"* and *"billed as scoping"* back at us. Both of those phrases were **added at
an earlier reviewer's request**, and `billed as scoping` is pinned at exactly one occurrence by
`check_protected_claims.py`, so removing them is not available to us, and would in any case be the wrong
move. We agree with your reading of Theorem 1. What was missing was the counterweight in the same breath.
§3.2 now reads:

> These numbered results are billed as *scoping*, not as theoretical contributions — they fall out of the
> definition below — **but what follows *from* them is not definitional**: closure puts a *trained* readout
> *inside* the family (Prop. 1), and the ceiling is then measured *non-monotone* in resolution (Cor. 2) —
> neither of which is a property of suprema, and every ceiling here had to be re-measured.

Those are the two consequences that a definition does not give you. Proposition 1's closure under
post-composition is what makes the statistic a supremum over **trained readouts** rather than over feature
maps; it is why an 80M-parameter encoder can be *inadmissible* and a zero-parameter bag *admissible*, and
it is a property of the family's construction, not of suprema. Corollary 2's non-monotonicity in resolution
is an **empirical** finding: no definition predicts that raising $d$ can lower the ceiling, and every
ceiling in the paper had to be measured rather than derived. We are not claiming the theorem is deep. We
are claiming the theorem is not where the theoretical content is, and the text now says which corollary
carries it.

---

## 3. R1: the practice-vs-paper contrast existed, one row short, and was unfindable

You asked for *"a compact subsection: 'Why this is not merely a stronger-baseline recipe'"* with a
seven-row existing-practice/this-paper table, and added *"Table 1 already contains most of this, but the
prose needs to make the novelty argument much sharper."*

We measured before editing. **Six of your seven rows already existed**, as an unnumbered inline `tabular`
in §3.3 on page 6, no caption, no float number, no list-of-tables entry. You credited Table 1 on page 4
and asked for the contrast anyway, which is the correct behaviour and tells us the object did not register.
We accept this as a presentation failure, not a content gap. Two changes:

**(a) The lead-in was modesty; it is now the novelty argument.** It read *"The ingredients are old; what is
new is that each one becomes measured, not judged:"*. It now reads:

> **Left column: estimate *relative performance*. Right column: estimate the *ceiling* the declared
> alternatives cannot pass — measured, not judged:**

Same honest second clause, but the first clause now says what changes *inferentially* rather than
apologising that the ingredients are old.

**(b) Your seventh axis is now a row.** Mapping your seven axes onto the current six rows:

| your axis | where it is |
|---|---|
| baseline → *invariant* baseline | row 1, `a strong baseline ⇒ admissible`, with Thm 1(iii) |
| one baseline → a *family* | row 3, `a matched control ⇒ a declared family and its ceiling` |
| point estimate → *ceiling* | row 3, closing on `which no member replaces` (Prop. 1, Cor. 2) |
| assume invariance → *test* it | row 2, `a control task ⇒ invariance tested per instance, by a twin` |
| fixed readout → optimise over readouts | row 5, extended this round: *the ceiling is a supremum over readouts too, and we measure it* |
| higher score → *exceed the ceiling* | row 4, `a good score ⇒ read only above that ceiling` |
| OOD → explicit novelty axes | **new row 6**, added this round |

The new row reads: `"out-of-distribution"` ⇒ **five separately costed axes**: novel *arrangement* far
cheaper than novel *inventory* (Fig. 2). Your §8 calls the novelty-axis decomposition the paper's
second-most-publishable idea and it was the one axis of yours with no row at all.

**We did not promote the tabular to a numbered float.** A caption costs ~3 rendered lines and adds a float
to the section with the least slack in the paper (§3's pages measure `-1.0` and `-1.9` points against the
text-block bound, and `placeins [section]` means §3 cannot borrow float pressure from anywhere else). It
sits immediately under a bold lead-in that now states the claim, in the subsection titled *"Why a single
invariant baseline is not enough"*, which is your requested subsection, under a different name, already
cross-referenced from §2's *"What is new, given all of that"* paragraph on page 3.

---

## 4. R2: the twin, with page numbers

You asked us to *"move the shape-matched twin to the absolute center of the paper"* and proposed five
figures. Measured against the current build, the twin is now:

- **Page 1, abstract ¶3's opening sentence**: *"The strongest test holds every lower-level cue fixed…
  every admissible order-blind control is pinned at exactly $0.500$ by proof, and a Tree-LSTM reaches
  0.994."*
- **Page 2, §1 ¶4**, a dedicated paragraph headed *"The sharpest form of the test, and the result we would
  put first"*, carrying `0.500` by construction (a *trained* readout over an order-blind map included at
  any capacity), `0.994`, and tree-edit distance at `0.723` as the strongest order-*sensitive*
  **non**-member.
- **Page 3, Figure 1**: rung 4 of the inference diagram, *and* the caption's **first** sentence as of this
  round. It previously reached the twin in sentence two, behind the bar-shading legend, so the paper's
  entry-point figure opened on a rendering note. The reorder is character-identical: a caption that grows
  from four to seven lines repacks five pages of floats.
- **Page 7, §4.2**, retitled *"The shape-matched twin: a ceiling known by proof"*.
- **Page 5, Table 2**, row *"Our `poly8`, across protocols … matched construction; twin"*.

**We did not swap §4.1 and §4.2.** Three reasons, in order of weight: (i) Figure 1 is an S1→S2→S3→twin
ladder and §4's order is the figure's order (the twin is the *sharpest* rung because every lower-level cue
is held fixed, which only reads as sharpening if the reader has met the lower levels; (ii) §4.1 is where
*"two encoders we did not build"* lives, and moving it later buries the strongest answer to *"is this just
your own benchmark?"*; (iii) the §4.3/page-8 boundary is bistable) roughly one net body line anywhere in
§1–§3 relocates a ~14-slot block and pushes the conclusion off page 9, and a section swap across it burned
three recovery attempts in an earlier round. Of your five proposed figures, four exist (the inference chain
is Figure 1, the novelty-axis cost is Figure 2, the twin's ceiling is Figure 1's rung 4 and §4.2's table,
the entitlement map is Table 2); the fifth, a schematic of the twin construction, is the one we would add
first if a page limit ever permitted, and it is in Appendix AC's prose today.

---

## 5. R3; this is already the title

You asked us to sell the paper as *auditing whether representation-level claims are supported by their
controls*, rather than as a framework for compositional reasoning. The title is:

> **When Stronger Baselines Mislead: Admissibility Auditing for Representation-Level Claims**

and the abstract already carries *"The levels name **cues**, not algebra, so symbolic-expression encoders
are this paper's **case study**, not its scope"* and closes on *"That is not compositional reasoning: four
primitives are not a library."* The conclusion's clause (3) is a scope *narrowing*, not a claim. We added
one sentence to the appendix reading path so that a reader entering from the back gets the same framing:
**what is being audited throughout is whether a representation-level claim is supported by its controls,
not whether a model reasons compositionally, which this paper does not claim to settle.**

---

## 6. §6: "complete" is gone from the predicate, and deliberately kept in two other senses

You wrote: *"'Complete' is dangerous… The safest alternative: 'passes the $\mathcal{F}$-relative
admissibility test.'"* Agreed, and the previous round's relativisation did not go far enough. Definition 1
is now:

> **Definition 1** (Passing the $\mathcal{F}$-relative admissibility audit through level S$T$, and
> coverage-gated)

with the body reading *"An evaluation of $h$ under $M$ **passes the $\mathcal{F}$-relative admissibility
audit through level S$T$**"*. Nine sites were renamed: three in §3.2 and six in the appendix, including the
proposition formerly titled *"What completeness licenses"*. This converges on language the paper already
used: *"we say it **passes the $\mathcal{F}_3$ audit**, so the family travels in the name"*, so it is
convergence rather than churn, and the rendered definition title still occupies one line on page 5.

**The word survives in two other senses, on purpose, and a blind substitution would have destroyed both.**

1. **Descriptor completeness**, a mathematical fact about $\phi_d$: *"$\phi_{d\geq4}$ is **the complete
   order-blind fingerprint** and no finer member exists"*. Five sites, untouched. This is what makes the
   depth ladder terminate rather than being a tunable hyperparameter.
2. **Absolute completeness, the standing concession**; §3.2's clause *(iv) open: completeness is
   unreachable* and §4's *"robustness of the verdict to family specification, **not completeness** — which
   is not claimed and cannot be"*. Untouched. These are the sentences that already answer your §6 and your
   W2, and deleting them to tidy the vocabulary would have handed the next reviewer the overclaim.

---

## 7. W5 and §5's cognitive-load list: the measurement, which is the most useful thing in this response

You ask of the E3m result: *"Why is this result occupying so much conceptual space?"* And §5 lists ~20 terms
as cognitive load. We grepped all eight body and float `.tex` files (the nine-page body) for every term
on both lists:

| term | body lines | appendix lines |
|---|---|---|
| `skyline` (random-encoder skyline) | **0** | 32 |
| `E3m` and its numbers (`0.053`, `-0.686`, `0.41`, `Doppler`, `Spring`) | **0** | 28 |
| leakage index / $\ell'$ | **0** | 4 / 83 |
| correction histories | **0** | 26 |
| `WL` · axis C | 2 · 2 | 38 · 6 |
| twin · protocol · coverage | 22 · 23 · 13 | 72 · 107 · 24 |

**E3m occupies zero lines of the nine-page body.** So does the skyline, so do the leakage indices, so do the
correction histories. The complaint is about the appendix, and cutting body content in response would have
cut the wrong thing, which is why this round's body edits go the other way: sharpen the central claim so
the machinery reads as support rather than as a list.

We also agree with the substance of W5 and fixed it where it lives. The appendix **already** conceded it:
*"it should not be interpreted as a coherent 'intermediate regime' but rather as an unstable probe"*,
*"carries high per-equation instability that prevents claims about the functional form"*, *"The robust claim
is the **two-point** E3/E3b contrast"*, but that paragraph sat **150 lines after** the first place `0.41`
was printed. Redundancy is not salience; position is. The caveat now travels with the number:

- the E3m bullet where `0.41` **first** appears now reads *"aggregate $\ell'=0.41$: **an unstable probe
  rather than an intermediate regime, and no claim in the body rests on it**: the four per-equation values
  are $0.053$, clipped $>1$, $-0.686$ and undefined. **The robust result here is the two-point E3/E3b
  contrast.**"*
- the table that prints the row gained the same caveat in its caption.

Both edits are outside the nine-page limit and therefore free.

---

## 8. W6, and what we are declining in print

W6 says the paper reads as eight competing identities. We fixed the half of this that was ours to fix:
**§1 ¶6**, the ~20-line contribution paragraph carrying the method name, three numbered consequences, eight
results, five axes and eleven cross-references, is thinner by roughly two lines; the SCAN numbers (which
are in the abstract and in §4.4), a restatement of the two ports, and four cross-references. **No content
and no self-limitation was removed**, and the two clauses that had to survive did: the reviewer-map quote
*"admissibility is a property of the comparator's **input pipeline**, not of its strength"*, and *"which
admissible family we declared cannot manufacture a pass"*, which is your own §8 rebuttal, in print, at
Corollary 3.

**We are not thinning the abstract further, and you should know that as a decision rather than an
oversight.** Page 1 still asserts the audit of other people's results, the protocol-disagreement finding,
the novelty axes and the two ports. Each was added at an earlier reviewer's request, three are pinned at
exactly one occurrence by our claim gate (`eight already-published results`, `Four of the audited`,
`portability, not general validation`), and one previous reviewer called ¶1 *"excellent"*. What we have done
instead is make the ordering unambiguous: ¶1 is the problem, **¶2's first sentence is now the inferential
object**, and everything after it is demonstration. If the identity count still reads as high, we would
rather be told which claim to *drop* than trade a protected concession for concision.

**W2** ($\mathcal{F}_3$ necessarily incomplete) you name as inherent, and we agree: §3.2 clause (iv) and
§4's *"not completeness — which is not claimed and cannot be"* are the standing statements, and Appendix AT
enumerates all 8,191 subfamilies to show the verdict does not depend on which one we picked. Your §8 states
our best rebuttal better than we did: the ceiling is monotone under family inclusion, so declaring a
*narrower* family is strictly against our own interest. That is Corollary 3, and it is quoted in the
conclusion.

**W3** (S3 hand-designed); you write *"I would therefore not call this a flaw"*, and the depth ladder
terminates at $\phi_{d\geq4}$ for the descriptor-completeness reason in §6 above, so there is no free
parameter to tune in our favour at the top of the ladder.

**W4** (small symbolic worlds, four primitives); this is the honest limit and the abstract states it in the
strongest form available to us: *"That is not compositional reasoning: four primitives are not a library."*
The 23-corpus survey, the two systems we did not build, the SCAN port and the code-clone port (where **our
own** inversion does not replicate, and we report it) are what we have; we agree they do not make the
symbolic worlds large.

---

## 9. §7's trusted-evidence tiers: accepted as written

Your tiering is: the twin > `poly8` `0.894`/`0.517` > the protocol disagreement `0.881`→`0.511` > the
Feynman leakage $\ell'$ `0.17`→`0.88` > SCAN and the code clones. We accept it and note that **nothing in
the body rests on the tiers you distrust**: the SCAN and clone ports are billed as *portability, not general
validation*, the clone result is a **non-replication of our own** prediction, and the Feynman leakage index
is appendix-only (0 body lines, per §7 above). The three claims the conclusion actually makes are the top
three of your list.

---

## 10. Verification of this revision

- **Build:** `pdflatex → bibtex → pdflatex ×2`. 0 errors · 0 undefined references or citations · 0 *Float
  too large* · exactly **2** overfull boxes, both pre-existing (`6.4211pt` vbox, `3.509pt` hbox) · 0 real
  BibTeX warnings.
- **Length:** **90 pages**, abstract ends page 1, **body ends page 9**. All four body floats on their
  previous pages: Figure 1 page 3 · Table 1 page 4 · Table 2 page 5 · Figure 2 page 8.
- **Gates:** `check_protected_claims.py` PASS (19 pinned claims, 4 body absences, 3 document-wide, controls
  firing) · `check_reviewer_map.py` PASS (16 rows, 272 checks, 43 log tags, 53 appendix letters) ·
  `check_figure_provenance.py` PASS on 10 values, positive control firing 2 FAILs; this is the gate that
  proves Figure 1's `0.276` still traces to its appendix source row rather than to its own bar.
- **Code:** `verify_claims.py` **2304/2304, exit 0**, in all three copies (`artifact/audit-sym`,
  `artifact/iclr-supplementary`, and the workplace project). The shipping copy is clean: 541 files, 0
  absolute-home-path hits, 0 author-name hits.
- **Rendered pages read as images:** pages 1, 2, 3, 5, 6, 7, the three claim installations, the renamed
  definition, Theorem 1's counterweight, the reframed contrast with its new row, and Figure 1's reordered
  caption, all verified visually rather than by grep.
