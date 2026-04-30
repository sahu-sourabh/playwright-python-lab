import httpx
import logging
from configs.settings import config

logger = logging.getLogger(__name__)

class AsyncAPIClient:
    # constructor
    def __init__(self):
        self.base_url = config.booker_api_url
        # we use a context-managed client for connection pooling
        self.client = httpx.AsyncClient(base_url=self.base_url, timeout=10.0)

    async def post(self, endpoint: str, data: dict = None, headers: dict = None):
        """Asynchronous POST request wrapper"""
        logger.info(f"POST request to: {endpoint} | Data: {data}")
        response = await self.client.post(endpoint, json=data, headers=headers)
        self._log_response(response)
        return response
    
    async def get(self, endpoint: str, params: dict = None):
        """Asynchronous GET request wrapper"""
        logger.info(f"GET request to: {endpoint}")
        response = await self.client.get(endpoint, params=params)
        self._log_response(response)
        return response
    
    def _log_response(self, response: httpx.Response):
        """Internal helper to log status codes"""
        if response.is_success:
            logger.info(f"Response Success: {response.status_code}")
            # This print ensures it shows up in 'pytest -s'
            print(f"\n[API LOG] {response.status_code} <- {response.text}")
        else:
            logger.error(f"Response Failed: {response.status_code} | Body: {response.text}")
    
    async def get_token(self):
        """Fetch a token from /auth and returns it"""
        auth_data = {"username": "admin", "password": "password123"}
        response = await self.post("/auth", data=auth_data)
        if response.status_code == 200:
            token = response.json().get("token")
            logger.info("Token generated successfully")
            return token
        else:
            raise Exception(f"Failed to get token: {response.status_code}")

    async def close(self):
        """Close the session"""
        await self.client.aclose()