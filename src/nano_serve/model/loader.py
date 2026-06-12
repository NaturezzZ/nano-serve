"""Model loader placeholder."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ModelSpec:
    model_path: Path
    dtype: str = "bfloat16"
    max_model_len: int | None = None


class ModelLoader:
    def load(self, spec: ModelSpec):
        raise NotImplementedError("Model loading is not implemented yet.")

