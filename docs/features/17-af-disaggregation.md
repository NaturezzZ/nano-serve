# Attention-FFN Disaggregation

## Goal

Explore splitting Attention and FFN/MoE computation into separate resource
pools.

## Why It Exists

Attention is state-heavy because it owns KV cache. FFN/MoE is more
compute-heavy and can be stateless. AF disaggregation may help some MoE serving
scenarios but is sensitive to activation traffic, synchronization, and network
jitter.

## Dependencies

- PD disaggregation.
- Distributed tracing.
- KV and activation transfer accounting.
- MoE/EP support for meaningful experiments.

## Interfaces

- AF simulator,
- attention worker,
- FFN/MoE worker,
- activation transfer manager,
- per-step synchronization protocol.

## Metrics

- attention latency,
- FFN latency,
- activation transfer bytes,
- pipeline bubble,
- A/F ratio,
- FFN utilization,
- TPOT p99,
- network jitter sensitivity.

## Tests

- simulator sanity checks,
- single-layer split correctness,
- colocated vs split logits,
- activation shape and dtype checks,
- MoE routing correctness.

## Benchmarks

- A/F ratio sweep,
- dense vs MoE model,
- network bandwidth sweep,
- microbatch size sweep,
- pipeline bubble report.

## Exit Criteria

- Simulator comes before distributed prototype.
- Prototype documents when AF is worse than colocated execution.
- MoE-first path is evaluated before dense-only claims.

## References

- Attention-FFN disaggregation ratio analysis.
- MoE AFD design-space exploration.
- vLLM AFD RFCs, if used as implementation background.

