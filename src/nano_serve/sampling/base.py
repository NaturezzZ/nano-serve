"""Sampling protocol and params."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class SamplingParams:
    max_tokens: int = 16
    temperature: float = 1.0
    top_k: int | None = None
    top_p: float | None = None
    stop_token_ids: tuple[int, ...] = ()


class Sampler(Protocol):
    def sample(self, logits: Any, params: SamplingParams) -> int:
        ...

