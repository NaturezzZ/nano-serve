"""Benchmark workload descriptors."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WorkloadSpec:
    name: str
    input_tokens: int
    output_tokens: int
    description: str = ""


STANDARD_WORKLOADS: dict[str, WorkloadSpec] = {
    "single_short": WorkloadSpec("single_short", 128, 128),
    "single_long_prefill": WorkloadSpec("single_long_prefill", 8192, 128),
    "decode_long": WorkloadSpec("decode_long", 128, 2048),
}

