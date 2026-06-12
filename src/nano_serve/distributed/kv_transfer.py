"""KV transfer placeholders for PD disaggregation."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class KVLocation:
    worker_id: str
    device: str
    request_id: str


class KVTransferManager:
    def transfer(self, *args, **kwargs):
        raise NotImplementedError("KV transfer is not implemented yet.")


class KVLocationRegistry:
    def lookup(self, request_id: str) -> KVLocation | None:
        del request_id
        return None

