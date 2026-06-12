"""Batch plan dataclasses."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class BatchKind(StrEnum):
    PREFILL = "PREFILL"
    DECODE = "DECODE"
    MIXED = "MIXED"


@dataclass(frozen=True)
class BatchPlan:
    kind: BatchKind
    request_ids: list[str]
    input_token_ids: list[list[int]]
    num_prefill_tokens: int = 0
    num_decode_tokens: int = 0
    metadata: dict[str, object] = field(default_factory=dict)

    @property
    def batch_size(self) -> int:
        return len(self.request_ids)

