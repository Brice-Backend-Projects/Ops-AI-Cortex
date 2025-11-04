"""
main.py
-------
Main application factory.
"""

from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(
        title="OpsAICortex",
        version="0.1.0",
        description="AI-Driven Operational Intelligence Platform",
    )
    return app
