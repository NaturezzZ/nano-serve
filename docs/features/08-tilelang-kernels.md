# TileLang Kernels

## Goal

Replace selected PyTorch operators with TileLang kernels, starting from simple
ops and paged decode attention.

## Why It Exists

The project should eventually teach kernel-level tradeoffs, but only after
system-level benchmarks can explain end-to-end impact.

## Dependencies

- Torch references.
- Paged attention reference.
- Benchmark and profiler infrastructure.

## Interfaces

- `kernels.tilelang`
- `TilePagedAttention`
- kernel microbenchmark registry
- correctness tolerance helpers

## Metrics

- kernel latency,
- achieved bandwidth,
- estimated FLOPs/s,
- SM activity,
- HBM bandwidth,
- occupancy,
- end-to-end TPOT impact.

## Tests

- RMSNorm vs torch,
- RoPE vs torch,
- SiLU-mul vs torch,
- paged decode attention vs torch gather reference,
- dtype tolerance.

## Benchmarks

- shape sweep,
- dtype sweep,
- block size sweep,
- NCU profile,
- end-to-end ablation.

## Exit Criteria

- The first TileLang paged decode attention kernel beats the torch gather
  reference for at least one documented shape.
- Correctness and profiler artifacts are checked in as benchmark outputs or
  reproducible instructions.

## References

- TileLang docs.
- FlashAttention.
- Nsight Compute.

