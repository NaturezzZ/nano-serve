"""Contiguous KV cache placeholder."""

from __future__ import annotations

from nano_serve.kv_cache.base import KVHandle


class ContiguousKVCache:
    def __init__(self) -> None:
        self._handles: dict[str, KVHandle] = {}

    def allocate_prefill(self, request_id: str, n_tokens: int) -> KVHandle:
        handle = KVHandle(request_id=request_id, num_tokens=n_tokens)
        self._handles[request_id] = handle
        return handle

    def allocate_decode_slot(self, request_id: str) -> KVHandle:
        handle = self._handles.setdefault(request_id, KVHandle(request_id=request_id))
        handle.num_tokens += 1
        return handle

    def free(self, request_id: str) -> None:
        self._handles.pop(request_id, None)

    def get_block_table(self, request_id: str) -> list[int]:
        del request_id
        return []

