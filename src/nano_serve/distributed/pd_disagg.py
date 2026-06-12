"""Prefill-decode disaggregation placeholders."""

from __future__ import annotations


class PrefillWorker:
    def prefill(self, *args, **kwargs):
        raise NotImplementedError("Prefill worker is not implemented yet.")


class DecodeWorker:
    def decode(self, *args, **kwargs):
        raise NotImplementedError("Decode worker is not implemented yet.")

