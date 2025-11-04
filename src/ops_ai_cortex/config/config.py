"""
Core configuration loader for OpsAICortex
-----------------------------------------
Combines .env secrets, YAML structured config, and pydantic validation.
"""

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Temporary minimal configuration for development and type checking."""

    APP_NAME: str = Field(default="OpsAICortex")
    DEBUG: bool = Field(default=True)
    DATABASE_URL: str = Field(default="postgresql://user:pass@localhost/placeholder_db")
    JWT_SECRET_KEY: str = Field(default="dev-secret-key")

    class Config:
        env_file = ".env"
        extra = "ignore"


# Instantiate settings for global import
settings = Settings()

# temporary assignment in pre-development
yaml_config: dict = {}
