"""API schema placeholders.

Keep these lightweight until FastAPI/Pydantic schemas are needed by the server
milestone.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class GenerateRequest:
    prompt: str
    max_tokens: int = 16
    stream: bool = False
    extra: dict[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class GenerateResponse:
    text: str
    request_id: str
    finish_reason: str | None = None

