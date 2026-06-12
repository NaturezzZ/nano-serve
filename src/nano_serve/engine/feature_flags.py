"""Feature flag helpers."""

from __future__ import annotations

from dataclasses import dataclass

from nano_serve.engine.config import EngineConfig


@dataclass(frozen=True)
class FeatureFlags:
    use_kv_cache: bool
    use_paged_kv: bool
    use_prefix_cache: bool
    use_spec_decode: bool
    use_distributed: bool
    use_pd_disagg: bool
    use_af_disagg: bool

    @classmethod
    def from_config(cls, config: EngineConfig) -> "FeatureFlags":
        return cls(
            use_kv_cache=config.kv_cache != "none",
            use_paged_kv=config.kv_cache in {"paged", "paged_prefix", "offload"},
            use_prefix_cache=config.kv_cache == "paged_prefix",
            use_spec_decode=config.spec_decode != "none",
            use_distributed=config.parallel.mode in {"dp", "tp", "pp", "ep", "pd", "af"},
            use_pd_disagg=config.parallel.mode == "pd",
            use_af_disagg=config.parallel.mode == "af",
        )

