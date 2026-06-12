"""KV offload placeholder."""

from __future__ import annotations


class KVOffloadManager:
    def offload(self, request_id: str) -> None:
        raise NotImplementedError("KV offload is not implemented yet.")

    def restore(self, request_id: str) -> None:
        raise NotImplementedError("KV restore is not implemented yet.")

