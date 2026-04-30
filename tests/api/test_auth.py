import pytest
from core.api.client import AsyncAPIClient
from data.models import AuthResponse

@pytest.mark.asyncio
async def test_successful_authentication():
    # 1. Arrange: Setup class object
    api = AsyncAPIClient()

    # 2. Action: Call the new get_method
    token = await api.get_token()

    # 3. Assertions & Validation
    assert token is not None, "Token is empty"
    assert isinstance(token, str), "Token should be a string"

    # Validation using Pydantic model
    # This proves the response matches our expected schema
    auth_obj = AuthResponse(token=token)
    print(f"\n🔑 Validated Token: {auth_obj.token}")

    # 4. Cleanup
    await api.close()