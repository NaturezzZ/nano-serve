"""Model runner protocol."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

from nano_serve.engine.batch import BatchPlan


@dataclass
class ModelOutput:
    logits: Any
    metadata: dict[str, Any]


class ModelRunner(Protocol):
    def execute(self, batch: BatchPlan) -> ModelOutput:
        ...

