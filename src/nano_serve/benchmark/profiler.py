"""Profiler hooks."""

from __future__ import annotations

from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def nvtx_range(name: str) -> Iterator[None]:
    """Placeholder NVTX range.

    The real implementation should call torch.cuda.nvtx or nvtx when available.
    """

    del name
    yield

