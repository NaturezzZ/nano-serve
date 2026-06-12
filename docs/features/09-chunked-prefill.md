# Chunked Prefill

## Goal

Split long prompts into prefill chunks and mix prefill chunks with decode work.

## Why It Exists

Long prefill can stall ongoing decode requests and damage TPOT tail latency.
Chunked prefill exposes a controllable TTFT/TPOT tradeoff.

## Dependencies

- Continuous batching.
- KV cache.
- BatchPlan that can represent mixed prefill/decode work.

## Interfaces

- `prefill_cursor` in `RequestState`
- `ChunkedPrefillScheduler`
- max prefill chunk size
- decode-maximal policy

## Metrics

- prefill chunk size,
- decode stall time,
- TTFT p90/p99,
- TPOT p90/p99,
- prefill waiting time,
- mixed batch token counts.

## Tests

- cursor advancement,
- chunk boundary correctness,
- mixed batch state transitions,
- cancellation during partial prefill,
- logits consistency vs unchunked prefill.

## Benchmarks

- long prefill plus ongoing decode,
- chunk size sweep,
- RPS sweep,
- throughput-latency frontier.

## Exit Criteria

- Long prompt arrivals no longer catastrophically stall existing decode.
- The chunk size tradeoff is visible in benchmark reports.

## References

- Sarathi-Serve.

