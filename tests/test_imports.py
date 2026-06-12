from __future__ import annotations

from pathlib import Path

from nano_serve import Engine, EngineConfig, FeatureFlags, SamplingParams
from nano_serve.kv_cache.paged import PagedKVCache
from nano_serve.sampling.greedy import GreedySampler


def test_public_imports() -> None:
    config = EngineConfig()
    flags = FeatureFlags.from_config(config)
    engine = Engine(config)

    assert config.scheduler == "single"
    assert flags.use_kv_cache is False
    assert engine.config is config


def test_greedy_sampler() -> None:
    token_id = GreedySampler().sample([0.1, 3.0, 2.0], SamplingParams())

    assert token_id == 1


def test_paged_kv_allocator_smoke() -> None:
    cache = PagedKVCache(num_blocks=4, block_size=2)
    handle = cache.allocate_prefill("req", 3)

    assert handle.block_ids
    assert cache.get_block_table("req") == handle.block_ids

    cache.allocate_decode_slot("req")
    cache.free("req")

    assert cache.get_block_table("req") == []


def test_every_feature_doc_exists() -> None:
    feature_dir = Path(__file__).resolve().parents[1] / "docs" / "features"
    expected = {
        "00-infrastructure.md",
        "01-torch-forwarding.md",
        "02-tokenizer-sampling-streaming.md",
        "03-kv-cache-prefill-decode.md",
        "04-static-batching.md",
        "05-continuous-batching.md",
        "06-paged-kv-cache.md",
        "07-paged-attention-reference.md",
        "08-tilelang-kernels.md",
        "09-chunked-prefill.md",
        "10-prefix-cache-radix.md",
        "11-overlap-graphs.md",
        "12-speculative-decoding.md",
        "13-quantization-lora-structured.md",
        "14-single-node-distributed.md",
        "15-multi-node-distributed.md",
        "16-pd-disaggregation.md",
        "17-af-disaggregation.md",
        "18-observability-production.md",
    }

    assert expected.issubset({path.name for path in feature_dir.glob("*.md")})


def test_bilingual_readmes_exist() -> None:
    root = Path(__file__).resolve().parents[1]

    assert (root / "README.md").exists()
    assert (root / "README.zh.md").exists()
    assert "README.zh.md" in (root / "README.md").read_text()
    assert "README.md" in (root / "README.zh.md").read_text()
