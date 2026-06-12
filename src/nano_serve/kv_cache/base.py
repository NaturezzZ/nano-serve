"""KV cache protocol."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


@dataclass
class KVHandle:
    request_id: str
    num_tokens: int = 0
    block_ids: list[int] = field(default_factory=list)


class KVCacheManager(Protocol):
    def allocate_prefill(self, request_id: str, n_tokens: int) -> KVHandle:
        ...

    def allocate_decode_slot(self, request_id: str) -> KVHandle:
        ...

    def free(self, request_id: str) -> None:
        ...

    def get_block_table(self, request_id: str) -> list[int]:
        ...

