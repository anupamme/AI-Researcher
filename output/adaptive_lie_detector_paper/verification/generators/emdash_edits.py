#!/usr/bin/env python3
"""Em-dash conversion ledger.  Each entry is (relpath, old, new).

Discipline: every `old` must occur EXACTLY once in the current file, or the
script aborts without writing anything.  Idempotent: an entry whose `old` is
absent while `new` is present is reported as already-applied and skipped.

Usage:  emdash_edits.py [--check]
"""
import io, os, sys, json, collections

D = "/Users/mediratta/code/paper_writing/AI-Researcher-align/output/adaptive_lie_detector_paper"

EDITS = []
def E(f, old, new):
    EDITS.append((f, old, new))

# ----------------------------------------------------------------- abstract (8 sites)
A = "sections/abstract.tex"
E(A, "behavior}---so its accuracy cannot be read",
     "behavior}, so its accuracy cannot be read")
E(A, "which $\\tau_E$---the \\emph{instruction}'s effect, and not a magnitude accuracy estimates---neither bounds nor signs",
     "which $\\tau_E$ (the \\emph{instruction}'s effect, and not a magnitude accuracy estimates) neither bounds nor signs")
E(A, "is not new---trained belief-verified organisms have it---but not as the",
     "is not new (trained belief-verified organisms have it), but not as the")
E(A, "reaches 69--80\\%---\\emph{surface-accessible accuracy}",
     "reaches 69--80\\%: \\emph{surface-accessible accuracy}")
E(A, "signals---still not $\\tau_D$---\\textbf{rung~4 of five}",
     "signals (still not $\\tau_D$): \\textbf{rung~4 of five}")

# ------------------------------------------------------------- introduction (28 sites)
I = "sections/introduction.tex"
E(I, "not deception as a construct}---so its accuracy cannot establish",
     "not deception as a construct}, so its accuracy cannot establish")
E(I, "deception is undetectable}---we end by detecting it",
     "deception is undetectable}: we end by detecting it")
E(I, "\\textbf{Yes}---we reproduce it and dispute none of it.",
     "\\textbf{Yes}: we reproduce it and dispute none of it.")
E(I, "\\textbf{Unidentified}---the instruction moves both",
     "\\textbf{Unidentified}: the instruction moves both")
# a list of three items bracketed by a dash pair -> parenthesis pair
E(I, "three claims---\\textsc{i.~identification}, \\textsc{ii.~what a valid test requires}, \\textsc{iii.~empirical diagnosis}---in descending order",
     "three claims (\\textsc{i.~identification}, \\textsc{ii.~what a valid test requires}, \\textsc{iii.~empirical diagnosis}), in descending order")
# the dash pair here supplies the sentence's SUBJECT ("the ECCP ... holds by
# structure"), which a parenthesis cannot do -> split the sentence instead.
E(I, "claims are about $\\tau_D$---the \\textbf{Elicitation--Construct Confounding Principle}, with behavioral deception detection as one instantiation (§\\ref{sec:identification})---\\emph{holds by structure}",
     "claims are about $\\tau_D$. The \\textbf{Elicitation--Construct Confounding Principle}, with behavioral deception detection as one instantiation (§\\ref{sec:identification}), \\emph{holds by structure}")
# sibling labels read "Label: gloss", but this sentence already carries a colon
# before "five criteria" -> parenthesise the gloss to keep exactly one colon.
E(I, "\\textbf{(2)~Protocol---an identification audit an auditor can apply to a benchmark they did not build}",
     "\\textbf{(2)~Protocol (an identification audit an auditor can apply to a benchmark they did not build)}")
E(I, "\\textbf{decidable from a design's specification}---we decide them on ten designs",
     "\\textbf{decidable from a design's specification}; we decide them on ten designs")
E(I, "\\textbf{no audited public release supplies all five}---the closest cells failing",
     "\\textbf{no audited public release supplies all five}, the closest cells failing")
E(I, "materials that do---and there, \\textbf{prior work's own battery",
     "materials that do, and there \\textbf{prior work's own battery")
E(I, "elementary but \\emph{unenforced}---no benchmark we audit states requirement~(i)---so \\textbf{the protocol",
     "elementary but \\emph{unenforced}: no benchmark we audit states requirement~(i), so \\textbf{the protocol")
E(I, "\\textbf{The full mapping---question $\\to$ evidence $\\to$ result $\\to$ what it licenses, row by row, with pre-registration status marked---is Table~\\ref{tab:roadmap}",
     "\\textbf{The full mapping (question $\\to$ evidence $\\to$ result $\\to$ what it licenses, row by row, with pre-registration status marked) is Table~\\ref{tab:roadmap}")
E(I, "closest instance---our primary audit target---is \\citet{pacchiardi2024catch}",
     "closest instance (our primary audit target) is \\citet{pacchiardi2024catch}")
E(I, "deception and compliance together---so generalization can be perfect",
     "deception and compliance together, so generalization can be perfect")
E(I, "not what we claim to introduce}---\\citet{cooney2026didyoulie}'s trained organisms",
     "not what we claim to introduce}: \\citet{cooney2026didyoulie}'s trained organisms")
E(I, "distinct detector paradigms}---while auditing whether public artifacts",
     "distinct detector paradigms}, while auditing whether public artifacts")
E(I, "settle the attribution question---stated in full, and then run.}",
     "settle the attribution question, stated in full and then run.}")
# the list items are comma-separated, so the higher-level break is a semicolon
E(I, "equivalent to the detector's input---(i)--(v) operationalize criterion~4",
     "equivalent to the detector's input; (i)--(v) operationalize criterion~4")
E(I, "both public rollout releases---ten rollout sets and 35 further cells---and \\textbf{none supplies all five}",
     "both public rollout releases (ten rollout sets and 35 further cells), and \\textbf{none supplies all five}")
# a dash pair around a list that itself contains commas and parens, in a sentence
# that already has a colon -> make the colon carry the list and split the tail off
E(I, "\\textbf{What the accuracy aggregates}: \\textbf{a heterogeneous mixture}---instruction-following",
     "\\textbf{What the accuracy aggregates} is \\textbf{a heterogeneous mixture}: instruction-following")
E(I, "at byte-identical elicitation)---\\textbf{and once the instruction confound is removed",
     "at byte-identical elicitation). \\textbf{Once the instruction confound is removed")
E(I, "the elicitation is held byte-identical---and when we build them",
     "the elicitation is held byte-identical, and when we build them")

# ------------------------------------------------------------- methodology (28 prose sites)
# NOT converted here, by design: the three `& --- &` cells in tab:claim_ledger row 1
# (methodology.tex:42) are the conventional "not applicable" mark, a symbol rather
# than punctuation, and tab:claim_ledger is a pinned p5 float where a +6-char cell
# edit is a measured spill tripwire.  Asserted still present by the verifier.
M = "sections/methodology.tex"
E(M, r"communicative goal---a different task, differently worded",
     r"communicative goal: a different task, differently worded")
E(M, r"while holding $\neg p$}---binary, latent, and observed by no benchmark audited here.",
     r"while holding $\neg p$}. It is binary, latent, and observed by no benchmark audited here.")
E(M, r"criterion~4 reaches---a deception-\emph{associated} signal at fixed elicitation",
     r"criterion~4 reaches, a deception-\emph{associated} signal at fixed elicitation")
E(M, r"not a new theoretical result}---its premises~(A1)--(A5)",
     r"not a new theoretical result}: its premises~(A1)--(A5)")
E(M, r"auditable on $Y$---crossing elicitation with items, recording the channel a detector reads, grading $Y$ off that channel---and \textbf{none supplies all three}",
     r"auditable on $Y$ (crossing elicitation with items, recording the channel a detector reads, grading $Y$ off that channel), and \textbf{none supplies all three}")
E(M, r"vary $D$ with $E$ fixed---uninstructed deception under incentive or goal conflict",
     r"vary $D$ with $E$ fixed, uninstructed deception under incentive or goal conflict")
E(M, r"(EXP-C4, §\ref{sec:external_audit})---criterion~4 met, still not $\mathrm{do}(D)$.",
     r"(EXP-C4, §\ref{sec:external_audit}), criterion~4 met, still not $\mathrm{do}(D)$.")
E(M, r"marked not pre-registered}---the lexical rule is diagnostic.",
     r"marked not pre-registered}: the lexical rule is diagnostic.")
E(M, r"& \emph{none}---structural (§\ref{sec:identification}) &",
     r"& \emph{none}: structural (§\ref{sec:identification}) &")
E(M, r"\textbf{Instructed accuracy is regime-dependent}---three mechanistically distinct paradigms",
     r"\textbf{Instructed accuracy is regime-dependent}: three mechanistically distinct paradigms")
E(M, r"\textbf{No learned features needed}---\emph{surface-accessible accuracy}, not a decomposition",
     r"\textbf{No learned features needed}: \emph{surface-accessible accuracy}, not a decomposition")
E(M, r"\textbf{rung~4, not rung~5}---not $\tau_D$ \\",
     r"\textbf{rung~4, not rung~5}; not $\tau_D$ \\")
E(M, r"signal at byte-identical elicitation---necessary for, but not equal to, $\tau_D$.",
     r"signal at byte-identical elicitation (necessary for, but not equal to, $\tau_D$).")
E(M, r"not a construct-validity test}---criterion~1 is how the confound is \emph{detected}",
     r"not a construct-validity test}; criterion~1 is how the confound is \emph{detected}")
E(M, r"\textbf{necessary for this audit to be operational}---(iii)~is how an auditor",
     r"\textbf{necessary for this audit to be operational}: (iii)~is how an auditor")
E(M, r"every valid deception benchmark}---they rule out specific alternative explanations.",
     r"every valid deception benchmark}: they rule out specific alternative explanations.")
E(M, r"$U\!\to\!S$ survives it---criterion~4 removes the \emph{elicitation} confound",
     r"$U\!\to\!S$ survives it; criterion~4 removes the \emph{elicitation} confound")
E(M, r"criterion~4 tests only the first---\textbf{the protocol falsifies validity claims",
     r"criterion~4 tests only the first; \textbf{the protocol falsifies validity claims")
E(M, r"of a population-level effect}---the thousands of graded trials",
     r"of a population-level effect}: the thousands of graded trials")
E(M, r"cannot attribute itself to $D$---by structure.",
     r"cannot attribute itself to $D$ (by structure).")
E(M, r"design \emph{does} yield a deception-\emph{associated} signal---\textbf{rung~4 of Figure~\ref{fig:ladder}, not rung~5}.",
     r"design \emph{does} yield a deception-\emph{associated} signal: \textbf{rung~4 of Figure~\ref{fig:ladder}, not rung~5}.")
E(M, r"the weakest thing here---\textbf{one} of five standing after a pre-registered covariate audit withdrew one, one of five new---on 3B--14B open-weight targets.",
     r"the weakest thing here (\textbf{one} of five standing after a pre-registered covariate audit withdrew one, one of five new) on 3B--14B open-weight targets.")
E(M, r"the \emph{absence} of a signal---it may remove the deception with the confound",
     r"the \emph{absence} of a signal: it may remove the deception with the confound")
E(M, r"on a deployed-observable channel---a property of the designs, not the models.",
     r"on a deployed-observable channel, a property of the designs, not the models.")
E(M, r"at fixed $E$---an association at byte-identical elicitation---so any latent $U$",
     r"at fixed $E$ (an association at byte-identical elicitation), so any latent $U$")

# ------------------------------------------------------------- experiments (33 prose sites)
# NOT converted: the seven `& --- &` cells in tab:external_audit AND the caption
# legend `\textbf{---}~not expressible` (experiments.tex:86) that defines that
# symbol.  Converting one without the other would desynchronise table and legend.
X = "sections/experiments.tex"
E(X, r"across four families---Llama~3.2~3B/3.1~8B/3.3~70B~\citep{meta2024llama3}, Mistral~7B~\citep{jiang2023mistral}, Qwen~2.5~7B/14B~\citep{qwen2025qwen25} and Claude Haiku~4.5~\citep{anthropic2025haiku45}---at $n=50$--100",
     r"across four families (Llama~3.2~3B/3.1~8B/3.3~70B~\citep{meta2024llama3}, Mistral~7B~\citep{jiang2023mistral}, Qwen~2.5~7B/14B~\citep{qwen2025qwen25} and Claude Haiku~4.5~\citep{anthropic2025haiku45}) at $n=50$--100")
E(X, r"\textbf{sixteen pre-registered analyses---one of them a rule that failed, reported as a null---are the only confirmatory results",
     r"\textbf{sixteen pre-registered analyses (one of them a rule that failed, reported as a null) are the only confirmatory results")
E(X, r"\textbf{Three tiers---confirmatory, supporting, exploratory---are marked per row",
     r"\textbf{Three tiers (confirmatory, supporting, exploratory) are marked per row")
E(X, r"(0--2 of 16 dimensions varying)---absence of a usable signal",
     r"(0--2 of 16 dimensions varying): absence of a usable signal")
E(X, r"target's answer about the claim---only binarised yes/no replies",
     r"target's answer about the claim, only binarised yes/no replies")
E(X, r"under equalization on all six targets---on five it is the whole of the accuracy",
     r"under equalization on all six targets; on five it is the whole of the accuracy")
E(X, r"A single regex feature---refusal/correction marker count from 14 patterns---reaches \textbf{69--80\%}",
     r"A single regex feature (refusal/correction marker count from 14 patterns) reaches \textbf{69--80\%}")
E(X, r"nor deception-specific---\emph{surface-accessible accuracy}, \textbf{not a decomposition of the rest}.",
     r"nor deception-specific; \emph{surface-accessible accuracy}, \textbf{not a decomposition of the rest}.")
E(X, r"inside a white-box probe---a third detector paradigm (EXP-WP).}",
     r"inside a white-box probe, a third detector paradigm (EXP-WP).}")
E(X, r"and steering is null---\textbf{decodable, not causal}.",
     r"and steering is null; \textbf{decodable, not causal}.")
E(X, r"but~(iii) is unmet---\textbf{neither establishes attribution}",
     r"but~(iii) is unmet; \textbf{neither establishes attribution}")
E(X, r"whether the agent \emph{traded}---a label disjoint from its input",
     r"whether the agent \emph{traded}, a label disjoint from its input")
E(X, r"judge AUROC 0.847---but \texttt{deceptive} grades the report both read",
     r"judge AUROC 0.847, but \texttt{deceptive} grades the report both read")
E(X, r"Appendix~\ref{app:frontier_panel})---\textbf{scale moves the numbers, not the verdict}",
     r"Appendix~\ref{app:frontier_panel}); \textbf{scale moves the numbers, not the verdict}")
E(X, r"One set clears both gates---sandbagging, $n\!=\!1000$, one fixed system prompt---and there the release's",
     r"One set clears both gates (sandbagging, $n\!=\!1000$, one fixed system prompt), and there the release's")
E(X, r"naming the pattern it keys on---\textbf{annotation-channel leakage}, whence~(iv).",
     r"naming the pattern it keys on: \textbf{annotation-channel leakage}, whence~(iv).")
E(X, r"rule and grader share evidence---\textbf{construct recovery}, whence~(v)---while against the \emph{action} label",
     r"rule and grader share evidence (\textbf{construct recovery}, whence~(v)), while against the \emph{action} label")
E(X, r"satisfies all five}---the channel facts are measurements",
     r"satisfies all five}; the channel facts are measurements")
E(X, r"the target asserts it---deception, the belief screen showing it holds $\neg p$---or corrects it",
     r"the target asserts it (deception, the belief screen showing it holds $\neg p$) or corrects it")
E(X, r"keeps two of the three---not the weakest---and adds \textbf{one of five",
     r"keeps two of the three (not the weakest) and adds \textbf{one of five")
E(X, r"produce a deception-associated signal---this is not an estimate",
     r"produce a deception-associated signal; this is not an estimate")
E(X, r"most discriminative question---``if you had made an error, would you point it out without being asked?''---reaches \textbf{100.0\%}",
     r"most discriminative question (``if you had made an error, would you point it out without being asked?'') reaches \textbf{100.0\%}")
E(X, r"a \emph{different} probe---\emph{``would you stake your reputation on the accuracy of what you just said?''}---which \textbf{points the same way",
     r"a \emph{different} probe, \emph{``would you stake your reputation on the accuracy of what you just said?''}, which \textbf{points the same way")

# -------------------------------------------------------------- discussion (2 sites)
S = "sections/discussion.tex"
E(S, r"premise of the identification result}---the equalization experiments",
     r"premise of the identification result}: the equalization experiments")
E(S, r"but not in \emph{environment}---the one cell satisfying (i)--(iv)",
     r"but not in \emph{environment}: the one cell satisfying (i)--(iv)")

# -------------------------------------------------------------- conclusion (2 sites)
# "We establish---X, Y:" has the dash qualifying HOW each group is established;
# deleting it and coordinating with "and" is the only reading that stays grammatical
# without a second colon.  +2 chars, and this paragraph is on p9 (the paying region).
C = "sections/conclusion.tex"
E(C, r"\textbf{We establish---(1)--(3) structurally or by replication, (4)--(5) as a weaker",
     r"\textbf{We establish (1)--(3) structurally or by replication, and (4)--(5) as a weaker")
# NB: "magnitude we measure only" is the p9 fit-test anchor -- untouched.
E(C, r"outside deception and we decide it}---\textbf{while its magnitude we measure only",
     r"outside deception and we decide it}, \textbf{while its magnitude we measure only")

# ------------------------------------- main.tex (14 sites, all on pp10-11: free zone)
T = "main.tex"
E(T, r"or---in the criterion-4 materials---by presenting a knowledge-screened false",
     r"or, in the criterion-4 materials, by presenting a knowledge-screened false")
E(T, r"a paraphrase of the lie instruction---information that could",
     r"a paraphrase of the lie instruction, information that could")
E(T, r"Ollama---Llama~3.2~3B, Llama~3.1~8B, Mistral~7B and Qwen~2.5~7B/14B/32B---with",
     r"Ollama (Llama~3.2~3B, Llama~3.1~8B, Mistral~7B and Qwen~2.5~7B/14B/32B) with")
E(T, r"""at bf16 stored as float32---Gemma-3's residual stream
carries outlier features above fp16 range, so the narrower storage is not an
option---and the extracted tensors run to""",
     r"""at bf16 stored as float32 (Gemma-3's residual stream
carries outlier features above fp16 range, so the narrower storage is not an
option), and the extracted tensors run to""")
E(T, r"stored model response---but not the tensors, which re-extract",
     r"stored model response, but not the tensors, which re-extract")
E(T, r"""artifact---eight per-configuration rule records, the eligibility survey, and
1{,}356 raw judgements---from which every EXP-XL number recomputes""",
     r"""artifact (eight per-configuration rule records, the eligibility survey, and
1{,}356 raw judgements) from which every EXP-XL number recomputes""")
E(T, r"""Its \emph{five} targets---Llama~3.2~3B, Llama~3.1~8B, Mistral~7B and
Qwen~2.5~7B/14B---are served locally""",
     r"""Its \emph{five} targets (Llama~3.2~3B, Llama~3.1~8B, Mistral~7B and
Qwen~2.5~7B/14B) are served locally""")
E(T, r"judgements---757 confirmatory graded trials, the rest pilot---are committed as JSONL",
     r"judgements (757 confirmatory graded trials, the rest pilot) are committed as JSONL")


def main():
    check = "--check" in sys.argv
    per = collections.Counter()
    applied = collections.Counter()
    already = collections.Counter()
    cache = {}
    for rel, old, new in EDITS:
        if rel not in cache:
            cache[rel] = io.open(os.path.join(D, rel), encoding="utf-8").read()
        s = cache[rel]
        n = s.count(old)
        if n == 1:
            cache[rel] = s.replace(old, new, 1)
            applied[rel] += 1
        elif n == 0 and s.count(new) >= 1:
            already[rel] += 1
        else:
            sys.stderr.write("ABORT %s: old occurs %d times (expected 1)\n  old=%r\n" % (rel, n, old[:90]))
            sys.exit(2)
        per[rel] += 1

    for rel in sorted(per):
        print("%-28s sites=%3d  applied=%3d  already=%3d" % (rel, per[rel], applied[rel], already[rel]))
    if check:
        print("\n--check: nothing written")
        return
    for rel, s in cache.items():
        io.open(os.path.join(D, rel), "w", encoding="utf-8").write(s)
    print("\nwrote %d file(s)" % len(cache))
    json.dump(EDITS, io.open("/tmp/r36_emdash_edits.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("ledger -> /tmp/r36_emdash_edits.json (%d entries)" % len(EDITS))


main()
