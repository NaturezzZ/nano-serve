"""Torch gather-based paged attention reference placeholder."""

from __future__ import annotations


class TorchGatherPagedAttention:
    def gather_kv(self, *args, **kwargs):
        raise NotImplementedError("Paged KV gather is not implemented yet.")

    def forward_prefill(self, *args, **kwargs):
        raise NotImplementedError("Paged prefill reference is not implemented yet.")

    def forward_decode(self, *args, **kwargs):
        raise NotImplementedError("Paged decode reference is not implemented yet.")

