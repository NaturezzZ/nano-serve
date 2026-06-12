"""Scheduler protocol."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from nano_serve.engine.batch import BatchPlan
from nano_serve.engine.request import RequestState


@dataclass(frozen=True)
class ScheduleBudget:
    max_num_seqs: int
    max_num_batched_tokens: int
    max_prefill_tokens: int | None = None
    max_decode_tokens: int | None = None


class Scheduler(Protocol):
    def schedule(
        self,
        waiting: list[RequestState],
        running: list[RequestState],
        kv_cache: object,
        budget: ScheduleBudget,
    ) -> BatchPlan:
        """Build the next batch plan."""

