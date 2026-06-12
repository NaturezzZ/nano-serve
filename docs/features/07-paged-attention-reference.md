# Paged Attention Reference

## Goal

Implement a torch gather-based paged attention backend as the correctness
reference for custom kernels.

## Why It Exists

Paged KV changes memory layout. Before writing TileLang kernels, the project
needs a slow but trustworthy reference that reads block tables correctly.

## Dependencies

- Paged KV cache.

## Interfaces

- `AttentionBackend`
- `TorchGatherPagedAttention`
- block-table gather helper

## Metrics

- gather time,
- attention time,
- temporary memory,
- context length,
- block size,
- TPOT impact.

## Tests

- output vs contiguous attention,
- block boundary cases,
- GQA/MQA cases,
- long context,
- mixed sequence lengths.

## Benchmarks

- block size sweep,
- context length sweep,
- batch size sweep,
- gather overhead isolation.

## Exit Criteria

- Correctness is stable across shapes needed by TileLang kernels.
- The overhead baseline is recorded for future speedup claims.

## References

- PagedAttention.
- FlashAttention IO-awareness for later kernel design.

