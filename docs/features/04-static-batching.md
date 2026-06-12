# Static Batching

## Goal

Run a fixed group of requests together through prefill and decode.

## Why It Exists

Static batching is a simple baseline that reveals padding waste and inactive
slot waste. That waste is the motivation for continuous batching.

## Dependencies

- KV cache and prefill/decode split.

## Interfaces

- `StaticBatchScheduler`
- batch padding metadata
- inactive slot tracking

## Metrics

- batch size,
- padding tokens,
- inactive slots,
- effective tokens/s,
- per-request TTFT/TPOT.

## Tests

- same-length batch correctness,
- mixed-length batch correctness,
- finished request masking,
- stop conditions per request.

## Benchmarks

- equal prompt/output lengths,
- mixed prompt/output lengths,
- batch size sweep,
- inactive slot waste.

## Exit Criteria

- Batch shape stays fixed during generation.
- Waste metrics clearly show why static batching is insufficient.

## References

- Orca motivation for iteration-level scheduling.

