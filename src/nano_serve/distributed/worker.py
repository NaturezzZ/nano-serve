"""Worker process placeholder."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WorkerInfo:
    worker_id: str
    rank: int
    world_size: int
    role: str = "model"


class Worker:
    def __init__(self, info: WorkerInfo) -> None:
        self.info = info

    def run(self) -> None:
        raise NotImplementedError("Distributed worker loop is not implemented yet.")

