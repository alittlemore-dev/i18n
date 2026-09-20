from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from infra.config.constants import constants


class ProjectBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=constants.path.env_file, extra="ignore")


class AppSettings(ProjectBaseSettings):
    model_config = SettingsConfigDict(env_prefix="APP_")

    debug: bool
    use_cache: bool


class ValkeySettings(ProjectBaseSettings):
    model_config = SettingsConfigDict(env_prefix="VALKEY_")

    host: str = Field(min_length=1)
    port: int = Field(gt=0, le=65535)

    @property
    def url(self) -> str:
        return f"valkey://{self.host}:{self.port}/{constants.valkey.database}"


class SentrySettings(ProjectBaseSettings):
    model_config = SettingsConfigDict(env_prefix="SENTRY_")

    use: bool
    dsn: SecretStr


class Settings:
    def __init__(self) -> None:
        self.app = AppSettings()
        self.valkey = ValkeySettings()
        self.sentry = SentrySettings()


settings = Settings()
