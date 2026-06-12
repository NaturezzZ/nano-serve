# Production-Like Observability

## Goal

Add production-style metrics, traces, dashboards, and regression benchmark
artifacts.

## Why It Exists

The project is educational, but mature serving features are hard to reason
about without observability. Tail latency, queue depth, KV pressure, and worker
utilization must be visible.

## Dependencies

- Benchmark event schema.
- Engine metrics.
- Distributed metrics for later stages.

## Interfaces

- Prometheus exporter,
- request trace id,
- per-iteration timeline dump,
- profiler artifact registry,
- benchmark archive,
- dashboard config.

## Metrics

- request latency histograms,
- queue depth,
- running/waiting requests,
- KV usage,
- prefix cache stats,
- speculative stats,
- worker health,
- error counts.

## Tests

- metrics endpoint schema,
- trace id propagation,
- event timeline ordering,
- benchmark archive metadata,
- dashboard JSON validation.

## Benchmarks

- observability overhead,
- Prometheus scrape overhead,
- tracing enabled vs disabled,
- regression benchmark CI.

## Exit Criteria

- Local runs expose enough metrics to debug feature regressions.
- Observability can be disabled for clean performance measurement.

## References

- vLLM production metrics.
- SGLang production metrics.
- OpenTelemetry concepts where adopted.

