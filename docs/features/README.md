# Feature Design Index

Every roadmap feature has a design document here. When adding or changing a
feature, update the matching file before coding.

| Phase | Feature | Design |
| --- | --- | --- |
| 0 | Infrastructure | [00-infrastructure.md](00-infrastructure.md) |
| 1 | Torch forwarding | [01-torch-forwarding.md](01-torch-forwarding.md) |
| 1 | Tokenizer, sampling, streaming | [02-tokenizer-sampling-streaming.md](02-tokenizer-sampling-streaming.md) |
| 2 | KV cache and prefill/decode split | [03-kv-cache-prefill-decode.md](03-kv-cache-prefill-decode.md) |
| 3 | Static batching | [04-static-batching.md](04-static-batching.md) |
| 4 | Continuous batching | [05-continuous-batching.md](05-continuous-batching.md) |
| 5 | Paged KV cache | [06-paged-kv-cache.md](06-paged-kv-cache.md) |
| 6 | Paged attention reference | [07-paged-attention-reference.md](07-paged-attention-reference.md) |
| 7 | TileLang kernels | [08-tilelang-kernels.md](08-tilelang-kernels.md) |
| 8 | Chunked prefill | [09-chunked-prefill.md](09-chunked-prefill.md) |
| 9 | Prefix/Radix cache | [10-prefix-cache-radix.md](10-prefix-cache-radix.md) |
| 10 | CPU/GPU overlap and graphs | [11-overlap-graphs.md](11-overlap-graphs.md) |
| 11 | Speculative decoding | [12-speculative-decoding.md](12-speculative-decoding.md) |
| 12 | Quantization, LoRA, structured output | [13-quantization-lora-structured.md](13-quantization-lora-structured.md) |
| 13 | Single-node distributed | [14-single-node-distributed.md](14-single-node-distributed.md) |
| 14 | Multi-node distributed | [15-multi-node-distributed.md](15-multi-node-distributed.md) |
| 15 | Prefill-decode disaggregation | [16-pd-disaggregation.md](16-pd-disaggregation.md) |
| 16 | Attention-FFN disaggregation | [17-af-disaggregation.md](17-af-disaggregation.md) |
| 17 | Production-like observability | [18-observability-production.md](18-observability-production.md) |

