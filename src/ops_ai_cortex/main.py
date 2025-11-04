"""
main.py
-------
Main application factory.
"""

from fastapi import FastAPI

def create_app() -> FastAPI:
    """Factory to create and configure the FastAPI app."""
    app = FastAPI(
        title="OpsAICortex",
        version="0.1.0",
        description="AI-Driven Operational Intelligence Platform",
    )

    @app.get("/health")
    def health_check() -> dict[str, str]:
        """Simple health check endpoint for CI/CD smoke tests."""
        return {"status": "ok"}

    return app

