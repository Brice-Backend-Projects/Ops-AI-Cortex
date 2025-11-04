"""tests/test_smoke.py"""

import pytest
from httpx import AsyncClient, ASGITransport
from ops_ai_cortex.main import create_app


@pytest.mark.asyncio
async def test_health_check():
    """Simple smoke test to confirm FastAPI app responds with 200 OK."""
    app = create_app()  # ✅ instantiate the FastAPI app
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

