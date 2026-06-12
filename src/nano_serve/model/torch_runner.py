"""Torch model runner placeholder."""

from __future__ import annotations

from nano_serve.engine.batch import BatchPlan
from nano_serve.model.runner import ModelOutput


class TorchModelRunner:
    def execute(self, batch: BatchPlan) -> ModelOutput:
        del batch
        raise NotImplementedError("Torch model runner is not implemented yet.")

