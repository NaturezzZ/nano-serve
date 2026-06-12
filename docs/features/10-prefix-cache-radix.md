# Prefix Cache and Radix Cache

## Goal

Reuse KV cache for requests sharing prompt prefixes.

## Why It Exists

Multi-turn chat, RAG, and agent workloads often reuse system prompts, tool
definitions, or retrieved context. Prefix cache reduces duplicate prefill work
and improves TTFT.

## Dependencies

- Paged KV cache.
- Tokenizer-stable prompts.
- Block ref counts.

## Interfaces

- block-level prefix hash cache,
- radix tree cache,
- cache lookup/insert/evict,
- copy-on-write for shared blocks.

## Metrics

- prefix hit tokens,
- prefix hit rate,
- saved prefill tokens,
- TTFT improvement,
- cache memory bytes,
- matching CPU overhead.

## Tests

- exact token prefix matching,
- partial block behavior,
- ref count correctness,
- LRU eviction,
- copy-on-write on divergence,
- tokenizer template stability.

## Benchmarks

- shared system prompt,
- multi-turn chat,
- RAG with common documents,
- cache size sweep,
- eviction stress.

## Exit Criteria

- Prefix cache improves TTFT on shared-prefix workloads.
- No incorrect reuse occurs under token/template changes.

## References

- SGLang / RadixAttention.
- PagedAttention KV sharing.

