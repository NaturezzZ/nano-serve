"""Single-request scheduler baseline."""

from __future__ import annotations

from nano_serve.engine.batch import BatchKind, BatchPlan
from nano_serve.engine.request import RequestState
from nano_serve.scheduler.base import ScheduleBudget


class SingleRequestScheduler:
    def schedule(
        self,
        waiting: list[RequestState],
        running: list[RequestState],
        kv_cache: object,
        budget: ScheduleBudget,
    ) -> BatchPlan:
        del kv_cache, budget
        candidates = running or waiting
        if not candidates:
            return BatchPlan(kind=BatchKind.DECODE, request_ids=[], input_token_ids=[])
        req = candidates[0]
        return BatchPlan(
            kind=BatchKind.PREFILL,
            request_ids=[req.request_id],
            input_token_ids=[req.prompt_token_ids],
            num_prefill_tokens=len(req.prompt_token_ids),
        )

