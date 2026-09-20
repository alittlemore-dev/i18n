from pathlib import Path


class PathConstants:
    root_dir: Path = Path(__file__).resolve().parents[3]
    env_file: Path = root_dir / ".env"


class ValkeyConstants:
    database: int = 0
    namespace: str = "I18N_LITESTAR"
    store_name: str = "litestar_cache"
    timeout_seconds: float = 2.0


class ResponseCacheConstants:
    default_ttl_seconds: int = 86_400


class MonitoringConstants:
    interval_seconds: float = 1.0
    lag_threshold_seconds: float = 1.0


class Constants:
    path: PathConstants = PathConstants()
    response_cache: ResponseCacheConstants = ResponseCacheConstants()
    valkey: ValkeyConstants = ValkeyConstants()
    monitoring: MonitoringConstants = MonitoringConstants()


constants = Constants()
