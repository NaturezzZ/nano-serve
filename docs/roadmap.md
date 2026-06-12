# Roadmap

The roadmap is dependency-ordered. Later features rely on earlier state,
metrics, and correctness infrastructure.

## Feature Dependency Chain

```text
benchmark infra
  -> torch forwarding
  -> prefill/decode split + KV cache
  -> static batching
  -> continuous batching
  -> paged KV
  -> paged attention reference
  -> TileLang paged decode attention
  -> chunked prefill
  -> prefix cache
  -> overlap/graphs
  -> speculative decoding
  -> quantization/LoRA/structured outputs
  -> single-node distributed
  -> multi-node distributed
  -> PD disaggregation
  -> AF disaggregation
  -> production observability
```

## Why This Order

- Benchmark infrastructure comes first because every feature is an ablation.
- Torch forwarding comes before kernels because correctness must be easy to
  reason about.
- KV cache comes before batching because decode state is the main serving
  primitive.
- Static batching comes before continuous batching so the waste is measurable.
- Paged KV comes before paged attention because memory ownership must be
  correct before writing kernels against block tables.
- TileLang kernels come after torch references.
- PD and AF disaggregation come after distributed metrics and KV transfer
  accounting.

## Completion Criteria

A milestone is complete only when:

- the implementation is behind a config flag,
- tests cover correctness and edge cases,
- benchmarks can compare it with the previous milestone,
- docs describe design, metrics, and known tradeoffs,
- TODO/README checkboxes are updated.

