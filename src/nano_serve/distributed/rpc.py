"""RPC placeholder."""

from __future__ import annotations


class RPCClient:
    def call(self, *args, **kwargs):
        raise NotImplementedError("RPC client is not implemented yet.")


class RPCServer:
    def serve(self) -> None:
        raise NotImplementedError("RPC server is not implemented yet.")

