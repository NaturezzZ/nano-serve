"""Torch SDPA attention placeholder."""

from __future__ import annotations


class TorchSDPAAttention:
    def forward_prefill(self, *args, **kwargs):
        raise NotImplementedError("Torch SDPA prefill attention is not implemented yet.")

    def forward_decode(self, *args, **kwargs):
        raise NotImplementedError("Torch SDPA decode attention is not implemented yet.")

