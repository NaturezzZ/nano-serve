# Multi-Node Distributed

## Goal

Run model workers across multiple machines.

## Why It Exists

Multi-node serving introduces topology, failure, and network bottlenecks that
are invisible in single-node experiments.

## Dependencies

- Single-node distributed.
- Distributed metric collection.
- Worker lifecycle management.

## Interfaces

- multi-node launcher,
- rank/topology config,
- worker discovery,
- heartbeat,
- distributed event collector,
- network profiler hooks.

## Metrics

- network bandwidth,
- network latency,
- collective time,
- per-node queue depth,
- worker heartbeat age,
- p99 request latency.

## Tests

- rank mapping,
- worker join/leave,
- heartbeat timeout,
- distributed event merge,
- basic failure detection.

## Benchmarks

- cross-node TP,
- cross-node PP,
- topology comparison,
- failure injection,
- network saturation.

## Exit Criteria

- Multi-node runs produce one merged benchmark artifact.
- Network overhead is quantified separately from model compute.

## References

- TensorRT-LLM multi-node docs.
- vLLM and SGLang distributed serving docs.

