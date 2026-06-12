"""Speculative verification data structures."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class VerificationResult:
    accepted_token_ids: list[int]
    rejected_token_id: int | None = None
    target_calls: int = 1


class Verifier:
    def verify(self, *args, **kwargs) -> VerificationResult:
        raise NotImplementedError("Speculative verification is not implemented yet.")

