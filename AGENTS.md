# AGENTS.md

This repository is an agent-friendly learning project for an LLM serving engine
called `nano-serve`.

## Non-Negotiable Project Rules

1. Every feature must have a design document under `docs/features/`.
2. If you add a new feature, create or update its design document before coding.
3. If you change a feature's behavior, update its design document in the same
   change.
4. If you add a roadmap item in `README.md` or `TODO.md`, add a matching
   `docs/features/<feature>.md` document.
5. A feature is not complete until it has:
   - a config flag,
   - correctness tests,
   - a microbenchmark or benchmark plan,
   - metrics wired into JSONL events,
   - an ablation path against the previous baseline.
6. README content must stay bilingual. `README.md` is the default English
   version and `README.zh.md` is the Chinese version. If one changes, update the
   other in the same change.
7. README visuals must stay synchronized across languages. If a README image,
   diagram, caption, or alt text changes in one language, update the other
   README in the same change.

## Current Scope

This repo starts as a skeleton. Prefer narrow, staged implementation:

1. benchmark infrastructure,
2. torch single-request forwarding,
3. KV cache and prefill/decode split,
4. static batching,
5. continuous batching,
6. paged KV,
7. torch paged-attention reference,
8. TileLang paged decode attention,
9. chunked prefill,
10. prefix cache,
11. speculative decoding,
12. distributed serving,
13. PD disaggregation,
14. AF disaggregation.

Do not jump directly to distributed serving, custom GEMM, or AF
disaggregation before the scheduler, KV cache, benchmark, and metrics layers are
usable.

## Documentation Contract

Human-facing documentation:

- `README.md`: default English project overview, high-level roadmap, and
  readable TODO list.
- `README.zh.md`: Chinese version of `README.md`; keep the same structure,
  roadmap, links, diagrams, and TODO state.
- `TODO.md`: operational implementation checklist.
- `docs/roadmap.md`: milestone dependencies and completion criteria.
- `docs/architecture.md`: system boundaries and core abstractions.
- `docs/benchmarking.md`: benchmark metric definitions and workload design.
- `docs/features/*.md`: one design doc per feature.

Agent-facing documentation:

- This `AGENTS.md` is the main source of coding constraints.
- Feature documents are the source of truth for each feature's goal, interfaces,
  tests, benchmarks, and exit criteria.

When creating a new feature document, include:

```text
# Feature Name

## Goal
## Why It Exists
## Dependencies
## Interfaces
## Metrics
## Tests
## Benchmarks
## Exit Criteria
## References
```

## Code Ownership Boundaries

- `engine/`: request lifecycle, state transitions, batch plans, and engine loop.
- `scheduler/`: admission and batch construction policy only.
- `kv_cache/`: KV allocation, block tables, ownership, ref counts, and eviction.
- `attention/`: attention backend interfaces and PyTorch/TileLang attention
  implementations.
- `model/`: model loading and execution. Do not hide serving logic inside model
  code.
- `sampling/`: token sampling and penalties.
- `speculative/`: draft/verify algorithms and acceptance accounting.
- `benchmark/`: workloads, metrics, reports, profiling, and comparisons.
- `distributed/`: worker processes, RPC, parallelism, KV transfer, PD, AF.
- `observability/`: runtime events, tracing, Prometheus, and dashboard hooks.

Keep these boundaries strict. For example, scheduler code may ask the KV manager
whether capacity exists, but it should not mutate block tables directly.

## Feature Flag Contract

All feature behavior should be selectable through `EngineConfig` and
`FeatureFlags`. Avoid hidden environment-variable behavior unless the feature
doc explicitly says it is a temporary profiling hook.

Preferred flag dimensions:

```yaml
engine:
  scheduler: single | static_batch | continuous | chunked_prefill
  kv_cache: none | contiguous | paged | paged_prefix | offload
  attention_backend: torch_naive | torch_sdpa | torch_gather_paged | tile_paged
  sampler: greedy | topk_topp | beam
  spec_decode: none | draft_model | ngram | medusa | eagle
  graph: none | torch_compile | cuda_graph
  parallel:
    mode: none | dp | tp | pp | ep | pd | af
benchmark:
  enable_nvtx: true
  enable_ncu: false
  log_iteration_trace: true
```

## Benchmark Contract

Every benchmark run must record enough metadata to reproduce the result:

- git commit,
- command,
- model id/path,
- dtype,
- GPU name/count,
- CUDA/PyTorch/TileLang versions when available,
- engine config,
- workload config,
- random seed,
- start/end timestamps.

Required request metrics:

- arrival timestamp,
- first scheduled timestamp,
- prefill start/end,
- first token timestamp,
- last token timestamp,
- TTFT,
- TPOT/ITL,
- E2E latency,
- queueing time,
- input/output tokens.

Required iteration metrics:

- iteration id,
- batch size,
- prefill tokens,
- decode tokens,
- running/waiting request counts,
- KV blocks used/free,
- KV fragmentation,
- prefix cache hit tokens,
- GPU time,
- CPU scheduling time.

Required system metrics:

- output tokens/s,
- total tokens/s,
- requests/s,
- goodput under SLO,
- GPU memory peak,
- prefill/decode MFU,
- SM Active / SM Activity,
- HBM bandwidth utilization.

## README Visual Assets

- For deterministic technical diagrams with exact labels, prefer Mermaid or
  repo-native SVG because they are easier to review and keep bilingual.
- When a README needs a polished raster visual, agents may use GPT image2
  through the `imagegen` skill.
- Project-bound generated images must be copied into the workspace, preferably
  under `docs/assets/`, before being referenced from README files.
- Never reference an image that only exists under a temporary or Codex generated
  images directory.
- Do not rely on generated image text for exact technical labels. Put exact
  labels in Markdown, Mermaid, SVG, or captions instead.
- Any image referenced by `README.md` should also be referenced by
  `README.zh.md` at the same relative path unless there is a clear reason to
  localize the asset.

## Testing Rules

- Start with import and pure-Python unit tests.
- Any model-level change must have a small correctness test against a reference.
- Any KV cache change must include allocator and logits-consistency tests.
- Any scheduler change must include deterministic queue/state transition tests.
- Any benchmark change must include schema tests for emitted JSONL.

## Implementation Style

- Keep code small and explicit.
- Prefer dataclasses and protocol interfaces for early skeletons.
- Do not introduce a broad framework before the feature needs it.
- Keep model support narrow until the serving abstractions are stable.
- Add comments only when they clarify non-obvious state transitions or ownership.
- Use `rg` for searching.

## Important Pitfalls

- Do not treat tokens/s as the only success metric.
- Do not combine TTFT and TPOT into one latency number when evaluating serving
  features.
- Do not write custom kernels before the PyTorch reference and benchmark exist.
- Do not implement paged attention before paged KV correctness is stable.
- Do not implement speculative decoding before request state and KV append logic
  are robust.
- Do not implement PD/AF disaggregation before distributed metrics and KV
  transfer accounting exist.
