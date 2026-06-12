"""Runtime event schema."""

from __future__ import annotations

from dataclasses import dataclass, field
from time import time_ns


@dataclass(frozen=True)
class Event:
    name: str
    timestamp_ns: int = field(default_factory=time_ns)
    fields: dict[str, object] = field(default_factory=dict)

