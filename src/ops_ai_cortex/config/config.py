"""
Core configuration loader for OpsAICortex
-----------------------------------------
Combines .env secrets, YAML structured config, and pydantic validation.
"""

from pathlib import Path
from typing import Any, Dict, Optional
from pydantic import BaseSettings, Field
import yaml


class Settings(BaseSettings):
    """Type-safe environment configuration."""
    APP_NAME: str = "OpsAICortex"
    DEBUG: bool = True
    ENVIRONMENT: str = Field("development", env="ENVIRONMENT")

    # Database / Redis
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    REDIS_URL: str = Field(..., env="REDIS_URL")

    # AI providers
    AI_PROVIDER: str = Field("claude", env="AI_PROVIDER")
    CLAUDE_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None

    # Integrations
    SLACK_WEBHOOK_URL: Optional[str] = None
    GITHUB_TOKEN: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def load_yaml_config(path: str = "src/ops_ai_cortex/core/config.yaml") -> Dict[str, Any]:
    """Load structured YAML configuration (non-secrets)."""
    yaml_path = Path(path)
    if not yaml_path.exists():
        raise FileNotFoundError(f"Missing YAML config: {yaml_path}")
    with open(yaml_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# Instantiate settings and merge layers
settings = Settings()
yaml_config = load_yaml_config()

# Optional merged accessor
def get_config() -> Dict[str, Any]:
    """
    Merge YAML + env settings into one dict.
    Environment variables override YAML where conflicts occur.
    """
    merged = {**yaml_config, **settings.dict()}
    return merged


# Example usage:
# from core.config import settings, yaml_config, get_config
# print(settings.DATABASE_URL)
