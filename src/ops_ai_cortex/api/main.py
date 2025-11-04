"""src/ops_ai_cortex/api/main.py"""

from fastapi import APIRouter

# app = FastAPI(
#     title="OpsAICortex",
#     version="0.1.0",
#     description="AI-driven operational intelligence platform for DevOps teams.",
# )

def get_api_router() -> APIRouter:
    router = APIRouter()
    # ... add routes here later ...
    return router

# @app.get("/health", tags=["system"])
# async def health_check():
#     """
#     Lightweight endpoint for system health verification.
#     Used by CI/CD smoke tests and uptime monitors.
#     """
#     return {"status": "ok"}

