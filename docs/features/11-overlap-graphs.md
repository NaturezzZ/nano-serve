# CPU/GPU Overlap and Graphs

## Goal

Reduce CPU scheduler/tokenizer/sampler overhead and kernel launch overhead.

## Why It Exists

Once batching and KV cache are stable, small-batch decode can be limited by CPU
gaps and launch overhead. Overlap and CUDA graphs should make those gaps
measurable and smaller.

## Dependencies

- Continuous batching.
- Benchmark profiler infrastructure.
- Stable batch metadata.

## Interfaces

- tokenizer worker,
- async scheduler preparation,
- double-buffered batch metadata,
- `torch.compile` experiment,
- CUDA graph capture with shape buckets.

## Metrics

- CPU scheduling time,
- tokenizer time,
- GPU idle gaps,
- kernel launch count,
- graph replay count,
- TPOT tail.

## Tests

- shape bucket selection,
- graph fallback behavior,
- event order under async scheduling,
- correctness with and without graph mode.

## Benchmarks

- small batch decode,
- stable-shape decode,
- nsys timeline comparison,
- CPU-heavy online workload.

## Exit Criteria

- Profiler timeline shows reduced GPU idle gap for a documented workload.
- Graph mode is optional and has safe fallback.

## References

- vLLM and SGLang runtime docs.
- Nsight Systems/Nsight Compute.

