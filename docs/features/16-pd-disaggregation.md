# Prefill-Decode Disaggregation

## Goal

Split prefill and decode onto separate worker pools.

## Why It Exists

Prefill and decode have different resource profiles. PD disaggregation can
reduce interference and optimize TTFT/TPOT SLOs separately, but KV transfer can
erase the gains.

## Dependencies

- Multi-node worker model.
- KV transfer accounting.
- Distributed metrics.
- Chunked prefill and continuous batching understanding.

## Interfaces

- `PrefillWorker`
- `DecodeWorker`
- `KVTransferManager`
- `KVLocationRegistry`
- router with phase transition
- TTFT-aware and TPOT-aware queues

## Metrics

- prefill queue time,
- decode queue time,
- KV transfer time,
- KV transfer bytes,
- goodput under TTFT/TPOT SLO,
- prefill/decode pool utilization,
- decode starvation.

## Tests

- KV handoff correctness,
- same-node transfer,
- cross-node transfer,
- request state transition across pools,
- decode worker takeover and streaming.

## Benchmarks

- colocated vs PD,
- long-prefill-heavy workload,
- short-prompt workload,
- pool ratio sweep,
- transfer bandwidth sensitivity.

## Exit Criteria

- PD helps on long-prefill-heavy workloads.
- Reports also show workloads where PD is not worth the transfer overhead.

## References

- Splitwise.
- DistServe.

