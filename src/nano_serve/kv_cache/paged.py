"""Paged KV allocator skeleton."""

from __future__ import annotations

from dataclasses import dataclass

from nano_serve.kv_cache.base import KVHandle
from nano_serve.kv_cache.block_table import BlockTable, KVBlock


@dataclass(frozen=True)
class PagedKVStats:
    num_blocks: int
    free_blocks: int
    used_tokens: int


class PagedKVCache:
    def __init__(self, num_blocks: int, block_size: int) -> None:
        self.num_blocks = num_blocks
        self.block_size = block_size
        self.blocks = [KVBlock(block_id=i) for i in range(num_blocks)]
        self.free_blocks: list[int] = list(range(num_blocks))
        self.tables: dict[str, BlockTable] = {}

    def allocate_prefill(self, request_id: str, n_tokens: int) -> KVHandle:
        table = self.tables.setdefault(request_id, BlockTable(request_id=request_id))
        needed = (n_tokens + self.block_size - 1) // self.block_size
        while len(table.block_ids) < needed:
            table.block_ids.append(self._alloc_block())
        table.seq_len = n_tokens
        return KVHandle(request_id=request_id, num_tokens=n_tokens, block_ids=table.block_ids)

    def allocate_decode_slot(self, request_id: str) -> KVHandle:
        table = self.tables.setdefault(request_id, BlockTable(request_id=request_id))
        if table.seq_len % self.block_size == 0:
            table.block_ids.append(self._alloc_block())
        table.seq_len += 1
        return KVHandle(
            request_id=request_id,
            num_tokens=table.seq_len,
            block_ids=list(table.block_ids),
        )

    def free(self, request_id: str) -> None:
        table = self.tables.pop(request_id, None)
        if table is None:
            return
        for block_id in table.block_ids:
            self.blocks[block_id].ref_count = 0
            self.blocks[block_id].used_tokens = 0
            self.free_blocks.append(block_id)

    def get_block_table(self, request_id: str) -> list[int]:
        table = self.tables.get(request_id)
        return [] if table is None else list(table.block_ids)

    def stats(self) -> PagedKVStats:
        used_tokens = sum(table.seq_len for table in self.tables.values())
        return PagedKVStats(
            num_blocks=self.num_blocks,
            free_blocks=len(self.free_blocks),
            used_tokens=used_tokens,
        )

    def _alloc_block(self) -> int:
        if not self.free_blocks:
            raise MemoryError("paged KV cache is out of blocks")
        block_id = self.free_blocks.pop()
        self.blocks[block_id].ref_count = 1
        return block_id

