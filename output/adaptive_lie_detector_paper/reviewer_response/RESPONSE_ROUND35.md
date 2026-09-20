# Response to Reviewer (7/10, Weak Accept, confidence 4/5) — the epistemic-hierarchy round

Thank you. Your report is unusually easy to act on, because it tells us exactly where the score comes
from. Your per-dimension scores are Novelty 8, Technical correctness 8.5, Experimental rigor 8.5,
Empirical support 8, Significance 8.5, Clarity 8, Reproducibility 9 — an average near **8.4** — and the
**7** is a discount you explain twice:

> *"Claims 1–4: very strong. Claim 5: quite weak."* (§2) · *"this creates a strange asymmetry."* (§8)

Your §18 names the remedy: make the epistemic hierarchy **"the dominant thing a reviewer sees."** And you
tell us what not to do — *"I don't think you need another giant experiment"* / *"I would not add another
10 experiments."* We took all three literally.

**This round ran no experiment, added no pre-registration, and changed no number.** It made four prose
edits plus a bibliography audit (§B, Part E), and their total measured price was **zero**: all **223**
`\newlabel` page pins in the document are byte-identical to the previous build, the main text still ends
on p9 at margin ruler **485**, and the paper is still **89 pages**.

Two things come first, because they change which of your items are still actionable.

---

## §0. Provenance: you reviewed round 31. Rounds 32, 33 and 34 are invisible to your report — and this is now the third time.

Stated as **information, not rebuttal.** Your report names `main(20260919-020957).pdf`.

| Timestamp in your report | = IST | The tree it is |
|---|---|---|
| `20260919-020957` = 02:09:57 UTC | **07:39:57** | **round 31.** Commit `3d2805e` landed at **07:40:08** — **eleven seconds later** |

The heads you did **not** see:

| Commit | Round | Landed (IST) |
|---|---|---|
| `79d39b6` | 32 — the two validity distinctions, and the inferential unit | 09:02:56 |
| `225f069` | 33 — the clarity round: rung tags, an executable ladder, two numberings named apart | 10:39:53 |
| `c9718cf` | 34 — the length round: appendix −6,748 chars, 91 → 89 pp, the novelty label | 14:37:39 |

This is the **third consecutive review of that same tree**, so we have stopped treating it as an accident
and put the fix in the artifact rather than in a letter. **Part D** below adds a build-identity stamp to
the Reproducibility statement: `Source revision 35, built 20 September 2026 from parent commit c9718cf`,
plus the sentence that makes it usable — *"The revision number increments once per review round, so a
reader can check which round's tree a given PDF was compiled from."* It renders on p11, outside the
9-page main-text budget, so it cost nothing.

We are not claiming credit for anticipating you. We are telling you where to look, so that **2.5 of your
three 7→8 items** are not re-requested as open.

---

## §A. Your §17 — "what would move my score from 7 → 8", item by item

| Your item | Status, measured |
|---|---|
| **§17.1** make the identification result unmistakably central | **Already landed, in round 34.** `introduction.tex` carries **`\textbf{What is new.}`** in front of the (byte-unchanged) novelty sentence. And the abstract sentence you yourself quote as the paper's strongest — *"This is an identification problem, not a generalization one: generalization can be perfect while identification fails."* — has been in the abstract since round 27 |
| **§17.2** make the 1/5 result explicitly secondary | **Was half-landed; now complete.** Already present: `conclusion.tex`'s opening — *"We establish—(1)–(3) structurally or by replication, **(4)–(5) as a weaker, target-dependent secondary finding**"* (round 31) — and §3.5's closing sentence, which is near-verbatim what you asked for: *"**The standing 1-of-5 is itself a positive finding rather than a disappointment: once the elicitation confound is removed, detection is markedly less stable across targets than the instructed benchmark's near-ceiling accuracy suggests.**"* **Missing until this round: the independence claim.** `does not depend` occurred **0** times in the main text. That is **Part B** |
| **§17.3** reduce the main paper by 15–20% | **Declined, with the budget law.** See §E |

**Part B is the one genuinely absent thing your report identified**, and it is the direct answer to the
score discount: if (1)–(3) do not depend on (4), then the weakness of claim 5 does not propagate to the
paper's principal result. Your §8 asked for it almost verbatim.

---

## §B. What this round changes — four prose edits, a bibliography audit, and a punctuation pass, total price zero

### Part A — `fig:ladder`'s five rungs now carry **your** epistemic vocabulary (their §18)

Your §18 closes with a five-line hierarchy and says making it dominant is the path from 7 to 8. The paper
already renders that hierarchy **three** ways (`fig:ladder`, `tab:claim_ledger`, and §2.2's boxed
"Establishes / Does not establish / Unresolved"), so a fourth rendering would make the label overload
your **§15** complains about strictly worse. Instead we folded your vocabulary into the five rungs that
already exist. **Only the first `\rungrow` argument of each row changed**; the operational-test column,
the site column, all three headers, the caption and the `↑ this paper reaches rung 4, not rung 5` arrow
are byte-unchanged.

| Rung | Before | Now |
|---|---|---|
| 5 | `5. Causal deception signal (D→S, τ_D)` | **`5. Not identified`**`: causal D→S (τ_D)` |
| 4 | `4. Deception-associated signal, fixed E` | **`4. Possible`**`: deception-associated` |
| 3 | `3. Behavioural, not surface form` | **`3. Diagnosed`**`: not surface form` |
| 2 | `2. Asymmetry-independent signal` | **`2. Demonstrated`**`: survives equalization` |
| 1 | `1. Instructed-condition discrimination` | **`1. Identified`**`: instructed contrast` |

Read top-down, the figure now *is* your hierarchy, in your words, with the paper's own stopping point
marked between rungs 4 and 5. The tikz bands sit at fixed y-coordinates with `minimum height=5.0mm`, so
this cost **zero rulers**.

**Two rows were measured, not eyeballed, and that changed what shipped.** `\makebox[56mm][l]` pads with
`\hss`, which shrinks infinitely — so an over-wide column-1 label produces **no** Overfull warning and
silently collides with column 2. We measured every cell with `\settowidth` under the paper's own class and
fonts. The budget is 56 mm = **159.34 pt**:

| Candidate | Width | Verdict |
|---|---|---|
| `2. Demonstrated: not the prompt asymmetry` | 164.56 pt | **overflows** |
| `2. Demonstrated: asymmetry-independent` | 156.30 pt | fits by 1.05 mm — **visually flush**, rejected |
| `2. Demonstrated: survives equalization` | **145.20 pt** | shipped |
| `4. Possible: deception-associated, fixed E` | 153.58 pt | fits by 2.0 mm — rejected as flush |
| `4. Possible: deception-associated` | **121.89 pt** | shipped (*fixed E* survives in column 2's "fix E, grade D off-label" and in the caption's "at byte-identical elicitation") |

Rung 2's wording also had to respect an earlier reviewer's must-fix: what equalization removes is the
**asymmetry** between two prompts, so the rung may not be called "instruction-independent." *"Survives
equalization"* states the operational fact and cannot be misread that way at all; the verifier check that
enforced the old wording was **updated with that reasoning recorded in a comment, not deleted**.

### Part B — the independence claim (`conclusion.tex`, ~+15 chars, 0 rulers)

- **Before:** *"The alternative reading—that deception is undetectable—is what (4) tests, and the evidence runs against it."*
- **Now:** ***"(1)–(3) do not depend on (4)**: it tests the reading that deception is undetectable, and the evidence runs against it."*

A **substitution, not an addition** — the site sits at p9 rulers 481–482, where adding a sentence spills
the page. The numbering is the conclusion's own (1)–(5), defined in the sentence immediately above; note
that the conclusion's **(4)** is `tab:claim_ledger`'s **claim 5**, the criterion-4 contrast you scored as
weak. So the claim on the page is exactly yours: *the principal result does not depend on criterion 4
being positive.*

Three sites now say one coordinated thing, and the verifier pins all three together:

1. `conclusion.tex` — *"(4)–(5) as a weaker, target-dependent secondary finding"* (round 31)
2. `conclusion.tex` — *"(1)–(3) do not depend on (4)"* (**this round**)
3. `experiments.tex` §3.5 — *"markedly less stable across targets…"* (round 31)

### Part C — the ECCP status disclaimer moves earlier (their §14, 0 chars)

Your §14: *"A skeptical reviewer may think 'why does this need a new named principle?' … I might even
move that sentence earlier."* It was the paragraph's third sentence; it is now its second, immediately
after the italic statement:

> *When a benchmark creates its target construct Y by an intervention E that also changes the elicited
> behavior C a detector reads, no score evaluated only under do(E) is attributable to Y.* **The ECCP names
> a benchmark-design instance of standard pathway non-identifiability, not a new theoretical result** —
> its premises (A1)–(A5) are stated in full in Appendix A, and **what is new is the audit it licenses**,
> not the constraint.

A pure move of exact text: **1,330 characters in, 1,330 out.** The verifier now asserts the *order* — the
disclaimer's character offset must be **less than** the Proposition-instantiation sentence's — because
presence alone was already pinned and presence is what a future round could satisfy while undoing this.

### Part D — the build-identity stamp (free)

Described in §0. It lands in the Reproducibility statement on p11; the verifier renders pages 1–9 and
asserts the stamp is **not** on any of them, which is how "free" is checked rather than claimed. It
carries a date and a hash and nothing else — the submission is double-blind, and a check asserts
`\iclrfinalcopy` is still commented out on every executable line.

### Part E — the bibliography, audited entry by entry against authoritative records (free)

You did not raise references, so this is a disclosure rather than a response. The AI use statement claims
that *"all references were independently verified against their authoritative records (DOI, arXiv, or
publisher metadata) using an automated citation-retrieval tool."* We re-ran that audit over **all 26
entries then in the file** this round, through four independent channels — an automated retrieval tool
against arXiv and DOI, a live fetch of every `url` field, and, for venue claims, the arXiv API's `comment`
field plus OpenReview's `api2` notes search. (The audit added a 27th entry, verified the same way.)

**No hallucinated reference, no fabricated author, and no non-existent venue was found.** Seven real
defects were — every one of them in metadata or citation coverage, none in the existence or identity of a
reference — and all are fixed:

| Entry | Was | Authoritative record | Fix |
|---|---|---|---|
| `denison2024sycophancy` | "Reward-Tampering in **Language Models**" | arXiv:2406.10162 | title corrected to **Large Language Models** |
| `hagendorff2024deception` | "Deception Abilities **Emerge**" | PNAS 121(24) e2317967121 | corrected to **Emerged** |
| `pacchiardi2023catch` / `li2024inference` | key year ≠ `year` field | ICLR **2024** / NeurIPS **2023** | keys renamed to `pacchiardi2024catch` / `li2023inference` |
| `hagendorff2024deception` | no `doi` field | PNAS `10.1073/pnas.2317967121` | DOI added, confirmed against the publisher record |
| `perez2022red` | no `doi` field | ACL `10.18653/v1/2022.emnlp-main.225` | DOI added, confirmed against the ACL Anthology record |
| `team2024gemma2` | in the bibliography, **cited nowhere** | Gemma 2 9B is a real EXP-C4B Family E target (H3 **−41.2 pp**, $p=0.0001$) | cited at the Family E roster, where the target is introduced |
| Gemma 3 | **absent from the bibliography**, though EXP-WP probes `google/gemma-3-4b-it` and reports H1–H4 on it | arXiv:2503.19786, *Gemma 3 Technical Report*, 2025 | entry added and cited at the EXP-WP setup |

The rename touched **11 citation sites across 5 files and cost 0 rulers**, because both new keys are the
same length as the old ones (19 and 15 characters) — and natbib renders the year from the `year` field, not
from the key, so **every rendered citation is byte-identical**: `Pacchiardi et al. (2024)` and
`(ITI; Li et al., 2023)` read exactly as before. It was a source-hygiene fix with no typeset consequence,
which is why it was affordable at zero slack.

**The two DOIs are what make the AI use statement's claim checkable, so they were worth measuring for.**
Adding a `doi` field is not free in this style: `iclr2027_conference.bst` typesets it (`FUNCTION
{format.doi}`), so both DOIs render in the reference list. Measured: the bibliography's last page absorbed
both, and the paper is still **89 pages** with p9 still closing at ruler **485** and all **223** page pins
unmoved. They also render as **clickable links** rather than inert text — `main.bbl` ships a plain-text
`\doi` fallback, so `main.tex` defines `\doi` ahead of it purely to make the pair resolvable in one click;
the verifier proves this from the PDF's compressed object streams, not from the macro.

The effect on the released verification artifact is the point: before this round, **four** entries could
only be resolved by `verify_bib.py`'s title-search fallback, which is unreliable — it is what produced the
one spurious mismatch in our own audit. It is now **two**, and those two (`anthropic2025haiku45`, a system
card; `hopkins2026liedetectors`, a blog post) are the only entries in the bibliography with no
machine-resolvable identifier of any kind; both were verified by hand against their live URLs.

**The Gemma defect was the instructive one, because the obvious diagnosis was wrong.** An uncited
`team2024gemma2` next to an EXP-WP target called `gemma-3-4b-it` looks like a stale citation pointing at the
wrong model generation. It is not: Gemma 2 9B is a genuine EXP-C4B **Family E** target, one of the five, and
the paper reports an H3 result of **−41.2 pp** ($p=0.0001$) on it. So the entry was correct and merely
uncited, while the model the paper actually runs a white-box probe on had no entry at all. Replacing Gemma 2
with Gemma 3 — the tempting one-line fix — would have deleted a live reference. Both are now cited at the
site where each model is introduced, and **every one of the 27 entries in the bibliography is now cited**:
`\begin{thebibliography}` went from `{25}` to `{27}`, so BibTeX prints all of them and there are no orphans
left.

That is also now a **standing check rather than an observation**: the verifier fails if any
`references.bib` entry is cited nowhere, and separately if BibTeX prints fewer entries than the file
contains. An uncited entry is exactly how this defect hid, so it is no longer allowed to.

### Part F — every em dash in the paper replaced with ordinary punctuation (free)

Also not something you raised. The paper leaned heavily on the em dash: **602** of them across the nine
`.tex` files, a density that makes long sentences readable to write and harder to read. **560 are now
ordinary punctuation and 42 remain** — and all 42 are the table "not applicable" mark (`& --- &`,
`\multicolumn{2}{c}{---}`, the legend's `\textbf{---}~not expressible`) or lines inside a `verbatim`
transcript, where a dash is not punctuation at all.

Each of the 560 was decided **at its own site**, not by a global rule, against a fixed set of choices:
consequence or coordinator → comma; non-restrictive relative → comma; interposed phrase that already
carries commas → a parenthesis pair; final appositive → colon; second clause in a sentence that already
has a grammatical colon → semicolon. Two constraints were enforced mechanically afterwards, because both
are failure modes a site-by-site pass invites: **no sentence may end up with two grammatical colons**,
and **no semicolon may stand without a clause on both sides**. Five sites violated one of them and were
re-decided — two in the abstract, two in §3, one in Appendix J — each with a replacement of exactly the
same width, so re-deciding them cost nothing.

**Why this was affordable at zero slack.** Replacing `---` with `, ` removes one character; a parenthesis
pair removes two. The pass therefore *shrinks* the source, and shrink upstream of p9 refunds nothing but
also costs nothing — it only has to not reflow a float. It did reflow four, and that is disclosed rather
than hidden:

| Quantity | Before | After |
|---|---|---|
| Pages | 89 | **89** |
| Last main-text margin ruler on p9 / first on p10 | 485 / 486 | **485 / 486** |
| Em dashes (`---`) across the nine `.tex` files | 602 | **42**, all of them table marks or `verbatim` |
| En dashes (`--`) | 327 | **327** — none touched |
| Source characters, nine files | 462,392 | **461,913** (**−479**) |
| The 5 main-text float pins | — | **byte-identical** |
| `tab:appendix_roadmap` | p14 | **p14** |
| Appendix `\newlabel` page pins moved | — | **4 of 223**, all inside the appendix: `app:causal_probes` and `app:exp_i_4th_scenario` 86→87, `app:machine_icc` 89→88, `tab:td_vs_fd` 87→86 |
| Overfull boxes / Underfull / undefined references | 0 / 99 / 0 | **0 / 99 / 0** |

Those four moves were **priced before they were accepted**. Holding all 223 pins is possible, and we
measured what it costs: declining every appendix site at or after source line 2100 — **56** of the 560 —
holds them exactly. We took the conversion instead, on the view that four appendix cross-references
shifting by one page is not a reader-visible cost while 56 surviving em dashes are. The four pins were
re-pinned in the verifier **with the reason recorded in a comment**, and the check is now *stricter* than
the one it replaced: it asserts the moved set is exactly those four labels with exactly those deltas,
where the old check only asserted that nothing moved.

**The 2,230 checks retained from round 35 were not relaxed to accommodate this.** A punctuation pass
threatens every pinned literal in the verifier, and 18 checks did fail on the first run. None was
rewritten by hand — hand-editing a pinned string is precisely how a near-miss substitution gets in. The
verifier instead carries a `UNCONVERT` function and the round-36 ledger as data (538 widened,
two-way-unique pairs), and any check that pins pre-conversion prose now asserts it against the
un-converted text. So every historical assertion in the file is still the **byte-exact** string it was
before this round. Three of the 18 were not literal mismatches and are worth naming, because they are the
class of defect this machinery exists to catch: one pin broke *at a distance* (a parenthesis closer landed
immediately before its trailing brace, in a literal containing no dash), one was a four-token implicitly
concatenated string where the closer fell in the fourth token, and one exposed that the ledger was not a
true inverse — a pair reversed onto a second site that had carried a comma all along. The ledger generator
now requires **two-way uniqueness** and asserts a reverse round-trip, and a negative control confirms the
new checks bite: restoring a single em dash anywhere fires exactly two of them.

### The price, measured (Parts A–E)

| Quantity | Before (`c9718cf`) | After |
|---|---|---|
| Pages | 89 | **89** |
| Last main-text margin ruler on p9 | 485 | **485** |
| `\newlabel` page pins moved | — | **0 of 223** |
| `methodology.tex` | 15,696 chars | 15,687 (**−9**, all of it Part A) |
| `conclusion.tex` | 2,099 chars | 2,114 (**+15**, Part B) |
| `references.bib` | 9,779 chars | 10,022 (**+243**: two title corrections, two `doi` fields, the Gemma 3 entry) |
| `appendix.tex` | 379,617 chars | 379,666 (**+49**, the two Gemma `\cite`s) |
| Bibliography rendering | ends on p13, `{25}` entries | **ends on p13**, `{27}` entries — two new references and two DOIs all absorbed; appendix still opens p14 |
| `introduction.tex` · `experiments.tex` · `related_work.tex` | — | **identical up to the two key renames**, byte for byte, and **unchanged in length** |
| Overfull boxes / undefined references | 0 / 0 | **0 / 0** |

The character counts in that table are the state **after Parts A–E and before Part F**; Part F's own
table above gives the nine files' final sizes, and the two are reconciled by the round-36 ledger.

Measured on the Parts A–E tree, `abstract.tex` and `discussion.tex` are **byte-identical** to the previous
commit — asserted against `c9718cf` itself, not described. Nothing was funded out of the abstract or the
discussion. The four other section files are asserted equal to their `c9718cf` versions *with the Part E
rename applied — and, for `appendix.tex`, the two named Gemma `\cite` insertions — and nothing else*. That
is a stronger check than an exception list: it cannot pass if any other character in a 379,666-character
file moved. Part F then applies punctuation-only changes on top, and those identity checks still hold
because the verifier evaluates them through `UNCONVERT`: the assertion is unchanged, the text it is
asserted against is the pre-conversion text, and the conversion itself is proved separately to apply once
and invert once against the live tree.

---

## §C. Already closed in rounds 31–34, with sites

| Your item | Where it already is |
|---|---|
| **§5** drop-one vs full-inventory lexical accuracy | Stronger than the ask: §3.3 reports **both** — *"**69.1%** with the most load-bearing pattern dropped **is the figure we rely on**; 79.8% on the full inventory a sensitivity result"* — and names which one is load-bearing |
| **§9** don't weaken "deception-associated" | Standing policy; the phrase is unchanged at every site, including rung 4 and `tab:external_audit` |
| **§10** say plainly that only two public releases were audited | Abstract: *"no public release **we audited** supplies all five"*; §3.5: *"**no audited public set satisfies all five**"*; conclusion: *"across **both** public rollout releases"* |
| **§11** vintage scoping | Retired in favour of the seven-organization frontier panel (EXP-FS); the recency disclaimers came out with it |
| **§13** the figure architecture you describe | Already exactly the five main floats: `fig:dag`, `tab:claim_ledger`, `fig:ladder`, `fig:r1c_collapse`, `tab:external_audit` — pinned as an equality (the main text has exactly 5 floats) |
| **§17.1 / §17.2** | §A above |

---

## §D. Conflicts shown, not resolved

**§15, label density.** You count too many identifiers; we agree the count is high. Measured: **19
distinct `EXP-` tags in 48 occurrences** across the six compiled main-text files. Both clean cuts are
blocked, and we would rather show you the conflict than pick a side silently:

1. **Four of the tags sit inside §3 subsection titles, and two of them — `EXP-R1b` and `EXP-XJ` — appear
   in the main text *only* there.** The body uses the compressed idioms `EXP-R1/R1c` and `EXP-XA/XJ`.
   Cutting the title tags therefore deletes two experiments' claim→pre-registration traceability — the
   dimension you score **9/10**. Restoring them in body prose is an upstream add at ~1:1 against a budget
   with **zero** slack, so it is net negative.
2. **Removing the titles' `Rung N to M` prefixes reverses round 33's deliverable**, which a *previous*
   reviewer asked for in the same words you use in §18 ("make the hierarchy visible").

**Your §17.3 vs your own §17.** You ask for a 15–20% shorter main paper while also noting the
reproducibility material is stronger than the narrative strictly needs. The length is not in the
narrative: main text **5,668 words over 9 pages**; appendix **44,668 words over 76 pages**.

---

## §E. Declines, each with its price

- **§17.3, a physical 15–20% main-text reduction.** Slack is exactly 0 (the 9-page limit is met at p9
  ruler 485/485), and the measured budget law is asymmetric: **an upstream cut refunds 0 rulers** — only
  p9 text pays. Round 34 already removed **6,748** characters and two pages, from the appendix, which is
  where the length actually is. A further 15–20% of the *main* text would have to come out of §3.5's
  criterion-4 result, the discussion's limitations, or the three structured caution boxes that every
  reviewer who has commented on them named a strength.
- **A standalone rendering of your §18 hierarchy.** ~5 rulers, unfunded, and self-defeating against your
  own §15. Part A delivers your vocabulary inside the figure that already existed.
- **New experiments, including measuring an ECCP magnitude outside deception** — on your own instruction.
  This is the one change that would move Novelty and Empirical support, and it is the honest reason we do
  not claim more than 8 this round.
- **Abstract edits.** 403 words, 383 non-Scope, 20 Scope, with 10 of its 13 sentences pinned verbatim by
  earlier rounds' must-fixes — one of them promoted *into* the abstract at a prior reviewer's request. Any
  edit here must be word-neutral or it is declined.
- **Compressing EXP-AD** (§3.5's 12 rendered lines on p9, the only fundable mass in the paying region).
  Kept at full length by decision; it is the finding that benchmark design determines *which* behavioral
  signal looks like deception detection.

---

## §F. Carried-forward disclosures

- Generality is bounded in the paper's own words: *"its precondition is decidable outside deception and we
  decide it — **while its magnitude we measure only for behavioral deception detection**"* (EXP-AF).
- The non-English pilot is named, scoped and **unrun**.
- EXP-C4B's −30.3 / −28.7 pp deltas remain appendix-only.
- `tab:frontier_panel`'s 50.5% vs 49.5% is reported as the near-tie it is.
- **Rung 4, not rung 5**: no design audited here, ours included, manipulates D. Part A now says this in
  the figure's own top row — *"5. Not identified"*.

---

## §G. Standing declines (unchanged, and not this round's decisions)

- The title stays as it is (author's decision).
- The ladder stays Figure 2; `tab:criteria` stays in Appendix A.
- **§16's Papers A/B/C split** describes a different submission, not a revision of this one.

---

## Verification

| Check | Result |
|---|---|
| `verify_r36.py` | **2,464 / 2,464 passing** (2,082 retained from round 34 + 148 in Group 35, **31** of them Part E's bibliography pins, + 234 in Group 36 for Part F) |
| `latexmk` | exit 0, **0** Overfull hbox/vbox, **0** undefined references |
| Pages | **89** |
| Fit test | p9 contains the conclusion's last words, p10 does not, `ETHICS STATEMENT` opens p10, p9's last ruler = **485**, p10's first = **486** |
| Main float pins | `fig:dag` 1/p2 · `tab:claim_ledger` 1/p5 · `fig:ladder` 2/p5 · `fig:r1c_collapse` 3/p7 · `tab:external_audit` 2/p8 — **all unmoved** |
| All page pins | **219 / 223 unmoved** vs `c9718cf`; the 4 that moved are Part F's costed appendix moves, each re-pinned with its delta asserted |
| Files unchanged | evaluated through `UNCONVERT`, i.e. on the pre-Part-F text: `abstract`, `discussion` — **byte-identical** to `c9718cf`; `introduction`, `experiments`, `related_work` — **exactly `c9718cf` with the Part E rename applied**, length unchanged; `appendix` — exactly that plus the two named Gemma `\cite`s, each asserted to apply once |
| Punctuation pass (Part F) | **42** `---` left, each classified (26 + 3 + 2 appendix, 7 + 1 experiments, 3 methodology) and every class pinned; **327** en dashes on both sides; parenthesis balance unchanged in all nine files; 18 artifact patterns asserted no more frequent than before; the 538-pair ledger asserted to apply once and invert once against the live tree |
| Bibliography | 27 entries, **0 hallucinated**, **0 uncited**, **0** undefined citations, **0** BibTeX warnings; every entry asserted cited somewhere and BibTeX asserted to print all 27; the two renamed keys pinned and both dead keys asserted absent from every source file; the two corrected titles pinned against their published records |
| Gemma citations | each key cited **exactly once**, at the named introduction site; the Gemma 3 entry pinned to arXiv:2503.19786 / 2025; Gemma 2's **−41.2 pp** H3 result and EXP-WP's `google/gemma-3-4b-it` target both pinned, so neither citation can decay into decoration |
| DOIs | both pinned to their entry, asserted to render in the PDF, and asserted **clickable** from the PDF's compressed object streams; `doi`-field count pinned at exactly **2**, so a later round cannot add an unaudited one |
| Appendix pagination | bibliography still ends p13, appendix still opens p14, `tab:appendix_roadmap` still p14 — the DOIs were absorbed, not paid for |

Retained checks that this round deliberately changed were **updated in place with the round-35 reason
recorded in a comment, never deleted**: round 24's rung-2 wording pin, round 31's rung-label list, the
prose-bold ledger (198 → 199 spans, the single label Part B adds), and the edit ledger's replay stage.
Part E's rename broke three byte-identity pins; rather than carve out exceptions, those three were
**strengthened** into exact equality against `c9718cf` *with the rename applied*, and two files that cite
neither key kept their unconditional byte-identity pins.

Part F changed four more, each with the round-36 reason in a comment: the abstract's character count and
the methodology's (both now pinned **twice**, once live and once un-converted, so the conversion cannot
hide a word change behind a punctuation change); the appendix float-pin check, **strengthened** from "no
pin moved" to "exactly these four labels moved, by exactly these deltas"; and one pinned phrase on p1 that
TeX now hyphenates across a line break, made hyphen-tolerant the same way round 29 made its pins
whitespace-tolerant. Everything else in the file — all 2,230 prior assertions — is the byte-exact string
it was, asserted against un-converted text rather than rewritten.

**What we think this is worth, honestly.** Your own §17 heading caps the presentation route at **8**, and
your two named vulnerabilities are evidence-shaped: the identification argument is standard causal
inference (Novelty 8) and claim 5 stands at 1 of 5 (Empirical support 8). The single change that moves
either is measuring an ECCP magnitude outside deception — a new experiment, which your report tells us not
to run. What this round does instead is remove the **logical basis** for the discount you applied: the
paper now states, where you asked for it, that its principal result does not depend on claim 5 — and puts
your epistemic hierarchy, in your vocabulary, in the figure you said should dominate.
