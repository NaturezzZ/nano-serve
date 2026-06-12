# Infrastructure

## Goal

Create the project skeleton, config system, benchmark event schema, and report
pipeline before implementing model execution.

## Why It Exists

The project is an ablation platform. Without reproducible benchmark artifacts,
later features cannot be compared fairly.

## Dependencies

None.

## Interfaces

- `EngineConfig`
- `FeatureFlags`
- `RequestMetrics`
- `IterationMetrics`
- `BenchmarkRunConfig`
- JSONL event writer
- report and compare commands

## Metrics

- request-level timestamps,
- iteration batch statistics,
- system throughput,
- GPU memory placeholders,
- profiler artifact paths.

## Tests

- config serialization round trip,
- event schema validation,
- report generation from a tiny synthetic event file,
- import smoke test.

## Benchmarks

Start with a dummy workload that emits deterministic events without running a
model. The benchmark harness should work before the engine works.

## Exit Criteria

- `nano-serve bench dummy` design is documented.
- A run emits `run_config.json`, `events.jsonl`, `summary.json`, and `report.md`.
- Future feature flags can be represented in config.

## References

- NVIDIA GenAI-Perf metrics.
- vLLM metrics design.
- SGLang production metrics.

