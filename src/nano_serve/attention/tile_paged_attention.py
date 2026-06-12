"""TileLang paged attention placeholder."""

from __future__ import annotations


class TilePagedAttention:
    def forward_decode(self, *args, **kwargs):
        raise NotImplementedError("TileLang paged decode attention is not implemented yet.")

    def forward_prefill(self, *args, **kwargs):
        raise NotImplementedError("TileLang paged prefill attention is not implemented yet.")

