# Single-Node Distributed

## Goal

Scale from one GPU to multiple GPUs on one machine.

## Why It Exists

Larger models require sharding or replication. Single-node distributed is the
lowest-risk path to learn DP, TP, PP, and EP before multi-node deployment.

## Dependencies

- Stable model runner.
- KV cache ownership.
- Benchmark and metrics.

## Interfaces

- worker process,
- local RPC/control plane,
- data-parallel router,
- tensor parallel runner,
- pipeline parallel runner,
- expert parallel runner.

## Metrics

- per-rank latency,
- NCCL time,
- all-reduce bytes,
- all-to-all bytes,
- pipeline bubble,
- per-GPU memory,
- TPOT p99.

## Tests

- single-rank vs multi-rank logits,
- tensor parallel shard correctness,
- pipeline stage ordering,
- EP token dispatch/combine,
- worker startup/shutdown.

## Benchmarks

- TP degree sweep,
- PP split sweep,
- DP replica throughput,
- EP MoE load balance.

## Exit Criteria

- One model can run with at least one multi-GPU strategy.
- Communication overhead is visible in reports.

## References

- TensorRT-LLM parallelism docs.
- vLLM distributed docs.
- SGLang distributed docs.

