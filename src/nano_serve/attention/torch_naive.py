"""Naive torch attention placeholder."""

from __future__ import annotations


class TorchNaiveAttention:
    def forward_prefill(self, *args, **kwargs):
        raise NotImplementedError("Naive torch prefill attention is not implemented yet.")

    def forward_decode(self, *args, **kwargs):
        raise NotImplementedError("Naive torch decode attention is not implemented yet.")

