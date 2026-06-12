# Quantization, LoRA, and Structured Output

## Goal

Add mature serving features after the scheduler, KV cache, and benchmark stack
are stable.

## Why It Exists

Quantization reduces memory/bandwidth pressure. LoRA and structured output are
common production serving features. They should be implemented as measurable
experiments, not as hidden complexity in early milestones.

## Dependencies

- Model runner abstraction.
- Attention/KV metrics.
- Quality/correctness regression tests.

## Interfaces

- quantized weight loader,
- KV quantization backend,
- LoRA adapter registry,
- multi-LoRA batching metadata,
- grammar/structured output decoder.

## Metrics

- memory saved,
- TPOT/E2E impact,
- quality/correctness deltas,
- adapter switch overhead,
- structured decoding overhead.

## Tests

- quantized output tolerance,
- KV quant decode stability,
- LoRA adapter correctness,
- multi-LoRA batching isolation,
- grammar acceptance/rejection.

## Benchmarks

- memory-constrained workloads,
- long-context KV quant,
- multi-adapter mixed workload,
- JSON/grammar constrained decoding.

## Exit Criteria

- Each feature has a quality and performance tradeoff report.
- Features remain optional through config flags.

## References

- vLLM feature docs.
- SGLang feature docs.
- TensorRT-LLM optimization docs.

