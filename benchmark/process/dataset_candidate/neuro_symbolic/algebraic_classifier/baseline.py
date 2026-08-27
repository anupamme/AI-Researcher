"""Tiny bag-of-operators logistic-regression baseline.

This is intentionally trivial: the ML agent should treat it as a sanity check,
not as a real model. It exists so that `run_demo.py` can prove the full
pipeline (data, features, training, evaluation) is functional.
"""

from __future__ import annotations

import math
import random
from typing import Iterable, List, Sequence

from generator import (
    BINARY_OPS,
    LabelledExample,
    RELATIONS,
    UNARY_OPS,
    serialise_expression,
)

FEATURE_VOCAB: List[str] = list(BINARY_OPS) + list(UNARY_OPS) + list(RELATIONS)


def featurise(example: LabelledExample) -> List[float]:
    tokens = serialise_expression(example.expression).split()
    counts = [float(tokens.count(tok)) for tok in FEATURE_VOCAB]
    counts.append(float(len(tokens)))
    counts.extend(example.assignment)
    return counts


class BagOfOperatorsLogistic:
    def __init__(self, dim: int, lr: float = 0.05, seed: int = 0) -> None:
        rng = random.Random(seed)
        self.weights = [rng.gauss(0.0, 0.1) for _ in range(dim)]
        self.bias = 0.0
        self.lr = lr

    @staticmethod
    def _sigmoid(z: float) -> float:
        if z >= 0:
            ez = math.exp(-z)
            return 1.0 / (1.0 + ez)
        ez = math.exp(z)
        return ez / (1.0 + ez)

    def predict_proba(self, features: Sequence[float]) -> float:
        z = self.bias + sum(w * x for w, x in zip(self.weights, features))
        return self._sigmoid(z)

    def predict(self, features: Sequence[float]) -> int:
        return 1 if self.predict_proba(features) >= 0.5 else 0

    def step(self, features: Sequence[float], label: int) -> float:
        prob = self.predict_proba(features)
        error = prob - label
        for i, x in enumerate(features):
            self.weights[i] -= self.lr * error * x
        self.bias -= self.lr * error
        return -(label * math.log(max(prob, 1e-9)) + (1 - label) * math.log(max(1.0 - prob, 1e-9)))


def evaluate(model: BagOfOperatorsLogistic, examples: Iterable[LabelledExample]) -> float:
    correct = 0
    total = 0
    for ex in examples:
        if model.predict(featurise(ex)) == int(ex.label):
            correct += 1
        total += 1
    return correct / max(total, 1)
