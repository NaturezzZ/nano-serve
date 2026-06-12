"""Greedy sampler."""

from __future__ import annotations

from collections.abc import Sequence

from nano_serve.sampling.base import SamplingParams


class GreedySampler:
    def sample(self, logits: Sequence[float], params: SamplingParams | None = None) -> int:
        del params
        if not logits:
            raise ValueError("logits must not be empty")
        return max(range(len(logits)), key=lambda idx: logits[idx])

