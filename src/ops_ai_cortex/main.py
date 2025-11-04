# src/ops_ai_cortex/main.py
from fastapi import FastAPI
from ops_ai_cortex.config.config import settings, yaml_config

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

@app.get("/health")
def health_check():
    return {
        "app": settings.APP_NAME,
        "environment": settings.ENVIRONMENT,
        "ai_default": yaml_config.get("ai", {}).get("default_provider"),
    }
