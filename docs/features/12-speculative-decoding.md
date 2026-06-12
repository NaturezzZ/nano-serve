# Speculative Decoding

## Goal

Use draft/verify algorithms to reduce target model decode steps.

## Why It Exists

Autoregressive decode runs the target model once per token. Speculative
decoding can accept multiple tokens per target verification step when the draft
is accurate enough.

## Dependencies

- Robust request state machine.
- KV append for multiple tokens.
- Streaming that can emit multiple accepted tokens per iteration.
- Metrics that separate draft overhead from target savings.

## Interfaces

- `SpeculativeDecoder`
- `DraftModel`
- `Verifier`
- acceptance accounting
- KV rollback/update helpers

## Metrics

- draft tokens proposed,
- accepted tokens,
- acceptance length,
- target calls per output token,
- draft overhead,
- TPOT and E2E change,
- hostile/friendly workload split.

## Tests

- greedy draft/verify correctness,
- rejection path correctness,
- KV update after accepted tokens,
- sampling distribution test,
- batched requests with different accepted lengths.

## Benchmarks

- friendly workload,
- hostile workload,
- gamma sweep,
- draft size sweep,
- batch size interaction.

## Exit Criteria

- Benchmarks show where speculation helps and where it hurts.
- Output distribution rules are documented for greedy vs sampling modes.

## References

- Speculative Decoding.
- Speculative Sampling.
- Medusa.
- EAGLE.

