"""Engine loop skeleton."""

from __future__ import annotations

import time
import uuid

from nano_serve.engine.config import EngineConfig
from nano_serve.engine.request import RequestMetrics, RequestState
from nano_serve.sampling.base import SamplingParams


class Engine:
    """Minimal engine shell.

    The real implementation will wire scheduler, KV cache, model runner, and
    sampler according to `EngineConfig`.
    """

    def __init__(self, config: EngineConfig | None = None) -> None:
        self.config = config or EngineConfig()
        self.waiting: list[RequestState] = []
        self.running: list[RequestState] = []
        self.finished: list[RequestState] = []

    def add_request(
        self,
        prompt_token_ids: list[int],
        sampling_params: SamplingParams | None = None,
        request_id: str | None = None,
    ) -> str:
        request_id = request_id or str(uuid.uuid4())
        sampling_params = sampling_params or SamplingParams()
        state = RequestState(
            request_id=request_id,
            prompt_token_ids=prompt_token_ids,
            sampling_params=sampling_params,
            max_new_tokens=sampling_params.max_tokens,
            metrics=RequestMetrics(arrival_time_ns=time.monotonic_ns()),
        )
        self.waiting.append(state)
        return request_id

    def step(self) -> None:
        raise NotImplementedError("Engine.step is implemented in the scheduler milestones.")

    def generate(self, prompt_token_ids: list[int]) -> list[int]:
        self.add_request(prompt_token_ids)
        raise NotImplementedError("Offline generation is not implemented yet.")

