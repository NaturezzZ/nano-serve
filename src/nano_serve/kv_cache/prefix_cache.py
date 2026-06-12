"""Prefix cache placeholder."""

from __future__ import annotations


class PrefixCache:
    def lookup(self, token_ids: list[int]) -> int:
        del token_ids
        return 0

    def insert(self, token_ids: list[int], block_ids: list[int]) -> None:
        del token_ids, block_ids

