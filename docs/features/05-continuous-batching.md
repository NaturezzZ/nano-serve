# Continuous Batching

## Goal

Use iteration-level scheduling so finished requests leave and new requests enter
while other requests are decoding.

## Why It Exists

Serving workloads have variable prompt and output lengths. Continuous batching
keeps the GPU busier and reduces inactive slot waste.

## Dependencies

- Static batching.
- Request state machine.
- KV cache manager.

## Interfaces

- `ContinuousScheduler`
- `ScheduleBudget`
- `BatchPlan`
- waiting/running/finished queues
- `Engine.step()`

## Metrics

- running request count,
- waiting request count,
- batch size timeline,
- scheduler CPU time,
- TTFT and TPOT under RPS sweep,
- GPU idle gaps.

## Tests

- deterministic FCFS admission,
- new request admission during decode,
- finished request removal,
- capacity limits,
- cancellation behavior.

## Benchmarks

- static vs continuous batching,
- variable output lengths,
- Poisson RPS sweep,
- burst workload,
- p99 TTFT/TPOT.

## Exit Criteria

- New requests can enter without restarting the batch.
- Finished requests release KV immediately.
- Mixed-length workload improves over static batching.

## References

- Orca: iteration-level scheduling.
- vLLM and SGLang runtime docs.

