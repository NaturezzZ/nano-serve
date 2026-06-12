# Paged KV Cache

## Goal

Manage KV cache as fixed-size blocks with per-request block tables.

## Why It Exists

Contiguous KV allocation wastes memory under variable sequence lengths and
dynamic request lifetimes. Paged KV improves memory utilization and enables
prefix sharing.

## Dependencies

- KV cache.
- Continuous batching.

## Interfaces

- `PagedKVCacheManager`
- `KVBlock`
- `BlockTable`
- free block allocator
- ref-counted blocks

## Metrics

- allocated blocks,
- free blocks,
- used tokens,
- internal fragmentation,
- OOM count,
- max resident requests.

## Tests

- randomized allocate/free,
- block table sequence length invariants,
- append-token allocation,
- OOM behavior,
- logits consistency vs contiguous KV.

## Benchmarks

- contiguous vs paged KV,
- high concurrency,
- long output,
- mixed length,
- block size sweep.

## Exit Criteria

- Paged KV matches contiguous KV correctness.
- Fragmentation and OOM behavior are measurable.
- Block table is stable enough for paged attention.

## References

- PagedAttention / vLLM paper.

