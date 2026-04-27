import pytest
from core.api.client import AsyncAPIClient

@pytest.mark.asyncio
async def test_api_health_check():
    # 1. Initialize our high-performance client
    # class object creation
    api = AsyncAPIClient()

    # 2. Hit the "Ping" endpoint of Restful Booker
    # Endpoint: https://restful-booker.herokuapp.com/ping
    response = await api.get("/ping")

    # 3. Assertions
    assert response.status_code == 201, f"Expected 201 Created, got {response.status_code}"
    print("\n✅ API Engine is ROARING!")

    # 4. Clean up
    await api.close()