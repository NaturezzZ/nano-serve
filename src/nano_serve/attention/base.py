"""Attention backend protocol."""

from __future__ import annotations

from typing import Any, Protocol


class AttentionBackend(Protocol):
    def forward_prefill(
        self,
        q: Any,
        k: Any,
        v: Any,
        mask: Any,
        kv_cache: Any,
        metadata: dict[str, Any],
    ) -> Any:
        ...

    def forward_decode(
        self,
        q: Any,
        kv_cache: Any,
        block_table: Any,
        seq_lens: Any,
        metadata: dict[str, Any],
    ) -> Any:
        ...

