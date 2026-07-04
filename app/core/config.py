from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    app_name: str = "Ecommerce AI"
    app_version: str = "0.1.0"

    # Environment
    environment: str = "development"
    debug: bool = True

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # API
    api_prefix: str = "/api/v1"

    # Logging
    log_level: str = "INFO"

    # Backend Service
    backend_url: str = "http://backend:8000"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()