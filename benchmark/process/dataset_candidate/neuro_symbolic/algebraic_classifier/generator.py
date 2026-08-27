"""Procedural generator for algebraic-constraint satisfaction data.

Produces (expression_tree, assignment, label) triples and (anchor, positive,
negative) triplets for metric learning. Domain guards on division, log, and
sqrt are enforced during sampling.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import Callable, List, Optional, Sequence, Tuple

BINARY_OPS = ("+", "-", "*", "/")
UNARY_OPS = ("sin", "cos", "exp", "log", "sqrt")
RELATIONS = ("<", "<=", "=", ">=", ">")

_EQUAL_TOL = 1e-3


@dataclass
class Node:
    kind: str  # "binary" | "unary" | "var" | "const"
    op: Optional[str] = None
    value: Optional[float] = None
    var_index: Optional[int] = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def serialise(self) -> List[str]:
        if self.kind == "var":
            return [f"x{self.var_index}"]
        if self.kind == "const":
            return [f"{self.value:.3g}"]
        if self.kind == "unary":
            return ["(", self.op, *self.left.serialise(), ")"]
        return ["(", *self.left.serialise(), self.op, *self.right.serialise(), ")"]


@dataclass
class Expression:
    tree: Node
    relation: str
    threshold: float

    def serialise(self) -> List[str]:
        return [*self.tree.serialise(), self.relation, f"{self.threshold:.3g}"]


def _safe_eval(node: Node, assignment: Sequence[float]) -> float:
    if node.kind == "var":
        return assignment[node.var_index]
    if node.kind == "const":
        return float(node.value)
    if node.kind == "unary":
        x = _safe_eval(node.left, assignment)
        op = node.op
        if op == "sin":
            return math.sin(x)
        if op == "cos":
            return math.cos(x)
        if op == "exp":
            return math.exp(min(max(x, -20.0), 20.0))
        if op == "log":
            return math.log(abs(x) + 1e-6)
        if op == "sqrt":
            return math.sqrt(abs(x))
        raise ValueError(f"unknown unary op {op}")
    # binary
    a = _safe_eval(node.left, assignment)
    b = _safe_eval(node.right, assignment)
    op = node.op
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / (b if abs(b) > 1e-6 else math.copysign(1e-6, b))
    raise ValueError(f"unknown binary op {op}")


def _evaluates(expr: Expression, assignment: Sequence[float]) -> bool:
    try:
        val = _safe_eval(expr.tree, assignment)
    except (OverflowError, ValueError):
        return False
    if not math.isfinite(val):
        return False
    t = expr.threshold
    if expr.relation == "<":
        return val < t
    if expr.relation == "<=":
        return val <= t
    if expr.relation == "=":
        return abs(val - t) < _EQUAL_TOL
    if expr.relation == ">=":
        return val >= t
    if expr.relation == ">":
        return val > t
    raise ValueError(expr.relation)


class ExpressionGenerator:
    """Samples algebraic-constraint expression trees."""

    def __init__(
        self,
        num_variables: int = 4,
        min_depth: int = 2,
        max_depth: int = 6,
        const_bank: Sequence[float] = (-2.0, -1.0, -0.5, 0.5, 1.0, 2.0, 3.0),
        seed: int = 0,
    ) -> None:
        self.num_variables = num_variables
        self.min_depth = min_depth
        self.max_depth = max_depth
        self.const_bank = tuple(const_bank)
        self.rng = random.Random(seed)

    def _leaf(self) -> Node:
        if self.rng.random() < 0.7:
            return Node(kind="var", var_index=self.rng.randrange(self.num_variables))
        return Node(kind="const", value=self.rng.choice(self.const_bank))

    def _grow(self, depth_budget: int) -> Node:
        if depth_budget == 0:
            return self._leaf()
        r = self.rng.random()
        if r < 0.2:
            return self._leaf()
        if r < 0.5:
            return Node(
                kind="unary",
                op=self.rng.choice(UNARY_OPS),
                left=self._grow(depth_budget - 1),
            )
        return Node(
            kind="binary",
            op=self.rng.choice(BINARY_OPS),
            left=self._grow(depth_budget - 1),
            right=self._grow(depth_budget - 1),
        )

    def sample(self) -> Expression:
        depth = self.rng.randint(self.min_depth, self.max_depth)
        tree = self._grow(depth)
        relation = self.rng.choice(RELATIONS)
        threshold = self.rng.choice(self.const_bank)
        return Expression(tree=tree, relation=relation, threshold=float(threshold))


class AssignmentSampler:
    """Samples satisfying and non-satisfying assignments for an expression."""

    def __init__(
        self,
        n_pos: int = 5,
        n_neg: int = 5,
        negative_ratio: float = 0.5,
        var_range: Tuple[float, float] = (-3.0, 3.0),
        max_retries: int = 64,
        seed: int = 0,
    ) -> None:
        self.n_pos = n_pos
        self.n_neg = n_neg
        self.negative_ratio = negative_ratio
        self.var_range = var_range
        self.max_retries = max_retries
        self.rng = random.Random(seed)

    def _random_assignment(self, num_variables: int) -> List[float]:
        lo, hi = self.var_range
        return [self.rng.uniform(lo, hi) for _ in range(num_variables)]

    def _perturb(self, assignment: Sequence[float]) -> List[float]:
        out = list(assignment)
        idx = self.rng.randrange(len(out))
        out[idx] += self.rng.gauss(0.0, 0.5)
        return out

    def sample(
        self, expr: Expression, num_variables: int
    ) -> Optional[List[Tuple[List[float], bool]]]:
        pos: List[List[float]] = []
        neg: List[List[float]] = []
        retries = 0
        while (len(pos) < self.n_pos or len(neg) < self.n_neg) and retries < self.max_retries * (
            self.n_pos + self.n_neg
        ):
            assignment = self._random_assignment(num_variables)
            label = _evaluates(expr, assignment)
            if label and len(pos) < self.n_pos:
                pos.append(assignment)
            elif (not label) and len(neg) < self.n_neg:
                neg.append(assignment)
            retries += 1
        if len(pos) < self.n_pos or len(neg) < self.n_neg:
            return None
        # Hard negatives: perturb a satisfying assignment until the label flips.
        n_hard_neg = int(round(self.negative_ratio * self.n_neg))
        for slot in range(min(n_hard_neg, len(neg))):
            seed = pos[slot % len(pos)]
            for _ in range(self.max_retries):
                candidate = self._perturb(seed)
                if not _evaluates(expr, candidate):
                    neg[slot] = candidate
                    break
        out: List[Tuple[List[float], bool]] = [(a, True) for a in pos] + [
            (a, False) for a in neg
        ]
        self.rng.shuffle(out)
        return out


@dataclass
class LabelledExample:
    expression: Expression
    assignment: List[float]
    label: bool


@dataclass
class TripletDataset:
    """A small in-memory dataset that yields labelled examples and triplets."""

    generator: ExpressionGenerator
    sampler: AssignmentSampler
    num_expressions: int = 2000
    triplet_seed: int = 0
    _examples: List[LabelledExample] = field(default_factory=list, init=False)
    _by_label: dict = field(default_factory=dict, init=False)
    _rng: random.Random = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._rng = random.Random(self.triplet_seed)
        for _ in range(self.num_expressions):
            expr = self.generator.sample()
            samples = self.sampler.sample(expr, self.generator.num_variables)
            if samples is None:
                continue
            for assignment, label in samples:
                self._examples.append(
                    LabelledExample(expression=expr, assignment=assignment, label=label)
                )
        for idx, ex in enumerate(self._examples):
            self._by_label.setdefault(ex.label, []).append(idx)

    def __len__(self) -> int:
        return len(self._examples)

    def __getitem__(self, idx: int):
        anchor = self._examples[idx]
        positives = self._by_label.get(anchor.label, [])
        negatives = self._by_label.get(not anchor.label, [])
        positive_idx = self._rng.choice(positives) if positives else idx
        negative_idx = self._rng.choice(negatives) if negatives else idx
        return {
            "anchor": anchor,
            "positive": self._examples[positive_idx],
            "negative": self._examples[negative_idx],
        }

    def labelled_examples(self) -> List[LabelledExample]:
        return list(self._examples)


def serialise_expression(expr: Expression) -> str:
    return " ".join(expr.serialise())
