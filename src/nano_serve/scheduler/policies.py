"""Scheduling policy names and small helpers."""

from __future__ import annotations

from enum import StrEnum


class SchedulerPolicy(StrEnum):
    FCFS = "fcfs"
    DECODE_FIRST = "decode_first"
    PREFILL_FIRST = "prefill_first"
    SLO_AWARE = "slo_aware"

