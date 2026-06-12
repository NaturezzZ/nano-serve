"""No-cache baseline."""

from __future__ import annotations

from nano_serve.kv_cache.base import KVHandle


class NoKVCache:
    def allocate_prefill(self, request_id: str, n_tokens: int) -> KVHandle:
        return KVHandle(request_id=request_id, num_tokens=n_tokens)

    def allocate_decode_slot(self, request_id: str) -> KVHandle:
        return KVHandle(request_id=request_id, num_tokens=1)

    def free(self, request_id: str) -> None:
        del request_id

    def get_block_table(self, request_id: str) -> list[int]:
        del request_id
        return []

