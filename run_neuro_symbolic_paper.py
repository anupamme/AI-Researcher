"""End-to-end driver for the ICLR 2027 neuro-symbolic paper.

Stage 1: research-agent run (`Detailed Idea Description` mode).
    Implements the algebraic-constraint satisfaction classifier with the three
    encoder backbones inside the AI-Researcher Docker workplace and produces
    `workplace_paper/task_<instance>_<model>/workplace/project/`.

Stage 2: paper-writing run (`Paper Generation Agent` mode).
    Composes the LaTeX sections using the writing templates we seeded and
    compiles
    ``paper_agent/neuro_symbolic/target_sections/<instance>/iclr2025_conference.pdf``.

The two stages are gated by `--stage` (`research`, `paper`, or `all`).
Set the required environment variables in `.env` first (Bedrock model IDs,
AWS_REGION_NAME, GITHUB_AI_TOKEN, ...). Run from the repo root::

    uv venv --python 3.11 && source .venv/bin/activate
    uv pip install -e . && playwright install
    docker pull tjbtech1/airesearcher:v1   # only needed for stage 1
    python run_neuro_symbolic_paper.py --stage all
"""

from __future__ import annotations

import argparse
import os
import sys
from textwrap import dedent

# `main_ai_researcher` mutates the working directory; make sure imports below
# run from the repo root regardless of where the user invoked us.
REPO_ROOT = os.path.dirname(os.path.realpath(__file__))
os.chdir(REPO_ROOT)
sys.path.insert(0, REPO_ROOT)

# Some modules under research_agent/inno/ import their siblings as bare
# `inno.X` rather than the fully-qualified `research_agent.inno.X`. Add
# research_agent/ to sys.path AND alias the two names to the same module
# object so import bookkeeping stays consistent.
_RA_DIR = os.path.join(REPO_ROOT, "research_agent")
if _RA_DIR not in sys.path:
    sys.path.insert(0, _RA_DIR)
import importlib
sys.modules.setdefault("inno", importlib.import_module("research_agent.inno"))

IDEA = dedent(
    """\
    Combining Neuro-Symbolic approaches with Neural Networks is a long-standing
    challenge for the ML community. We address one concrete instance: expressing
    algebraic constraints with real-valued random variables over the outputs of
    a neural network. An example setting is the motion of a physical object in
    a constrained environment (n-body gravitational motion, spring simulation).

    We train a classifier that, given an algebraic expression and a sampled
    assignment, returns true if the expression is satisfied and false otherwise.
    What we care about is the *latent representation* of the algebraic
    expressions: distance in that latent space is used as a regularising term
    in downstream prediction losses.

    Training data is generated programmatically:
      1. Sample algebraic expressions as trees (trees are the natural inductive
         bias). Leaves are real-valued random variables and small numeric
         constants; binary operators are {+, -, *, /}; unary operators are
         {sin, cos, exp, log, sqrt}; the whole tree is wrapped in a relation
         drawn from {<, <=, =, >=, >}.
      2. Sample values for each variable with a mixture of random sampling and
         hard-negative sampling so the (expression, assignment, label) triples
         are well distributed.

    The encoder is trained with a triplet-loss objective (FaceNet-style
    semi-hard online mining) on the expression embeddings, jointly with a
    binary satisfaction-classification head. We use Tree Neural Networks as
    the natural backbone and compare against Graph Neural Networks and
    Transformers over a linearised tree. The resulting latent distance is
    then evaluated as a regulariser on the n-body and spring-system
    benchmarks of Cranmer et al. (2019).
    """
)

REFERENCES = dedent(
    """\
    1. Lample, Guillaume, and Francois Charton. "Deep learning for symbolic
       mathematics." arXiv:1912.01412 (2019).
    2. Xie, Yaqi, et al. "Embedding Symbolic Knowledge into Deep Networks."
       NeurIPS 2019.
    3. Stewart, Russell, and Stefano Ermon. "Label-free supervision of neural
       networks with physics and domain knowledge." AAAI 2017.
    4. Cranmer, Miles D., et al. "Learning Symbolic Physics with Graph
       Networks." arXiv:1909.05862 (2019).
    5. Schroff, Florian, Dmitry Kalenichenko, and James Philbin. "FaceNet: A
       Unified Embedding for Face Recognition and Clustering." CVPR 2015.
       (Standing in for the triplet-loss tutorial cited in the original idea.)
    """
)


def _require_env(*names: str) -> None:
    missing = [n for n in names if not os.environ.get(n)]
    if missing:
        sys.exit(
            f"ERROR: missing required env vars: {', '.join(missing)}. "
            f"Populate .env (loaded automatically by main_ai_researcher)."
        )


def run_research_stage() -> None:
    print("=" * 72)
    print("Stage 1/2: research agent (Detailed Idea Description)")
    print("=" * 72)
    import global_state  # noqa: F401  -- initialises INIT_FLAG
    from main_ai_researcher import main_ai_researcher

    # main_ai_researcher calls argparse.parse_args() internally on sys.argv,
    # which would choke on our own --stage flag. Feed it an empty argv.
    saved_argv = sys.argv[:]
    sys.argv = [sys.argv[0]]
    try:
        main_ai_researcher(IDEA, REFERENCES, mode="Detailed Idea Description")
    finally:
        sys.argv = saved_argv


def run_paper_stage() -> None:
    print("=" * 72)
    print("Stage 2/2: paper-writing agent (Paper Generation Agent)")
    print("=" * 72)
    # Run from repo root so the writing pipeline's relative paths
    # (`paper_agent/neuro_symbolic/target_sections/...`) resolve correctly.
    os.chdir(REPO_ROOT)
    sys.path.insert(0, REPO_ROOT)
    import asyncio
    from paper_agent import writing

    # Same argparse guard as run_research_stage() — the writing entry point
    # eventually reads argparse from sys.argv too.
    saved_argv = sys.argv[:]
    sys.argv = [sys.argv[0]]
    try:
        research_field = os.environ.get("CATEGORY", "neuro_symbolic")
        instance_id = os.environ.get("INSTANCE_ID", "neuro_symbolic_algebraic_triplet")
        asyncio.run(writing.writing(research_field, instance_id))
    finally:
        sys.argv = saved_argv


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--stage",
        choices=("research", "paper", "all"),
        default="all",
        help="Which stage(s) to run. Default: all.",
    )
    args = parser.parse_args()

    from dotenv import load_dotenv

    load_dotenv()

    _require_env(
        "COMPLETION_MODEL",
        "CHEEP_MODEL",
        "CATEGORY",
        "INSTANCE_ID",
        "CONTAINER_NAME",
        "WORKPLACE_NAME",
        "CACHE_PATH",
        "PORT",
        "MAX_ITER_TIMES",
    )

    if args.stage in ("research", "all"):
        run_research_stage()
    if args.stage in ("paper", "all"):
        run_paper_stage()
    print("done.")


if __name__ == "__main__":
    main()
