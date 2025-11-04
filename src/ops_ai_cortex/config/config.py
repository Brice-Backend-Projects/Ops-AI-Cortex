"""
Core configuration loader for OpsAICortex
-----------------------------------------
Combines .env secrets, YAML structured config, and pydantic validation.
"""

from pathlib import Path


import yaml
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict # type: ignore[import]


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or .env file.
    """

    app_name: str = Field(default="OpsAICortex", description="Application name")
    environment: str = Field(default="development", description="Environment name")
    database_url: str = Field(default="postgresql://user:pass@localhost/db", description="Database connection URL")

    model_config = SettingsConfigModel = SettingsConfigDict(env_file=".env", extra="ignore")


def load_yaml_config(file_path: str = "src/ops_ai_cortex/config/config.yaml") -> dict:
    """
    Load YAML configuration file safely.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


settings = Settings()
yaml_config = load_yaml_config()
