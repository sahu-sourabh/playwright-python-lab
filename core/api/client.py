import httpx
import logging
from configs.settings import config
from data.models import BookingRequest

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
    
    async def put(self, endpoint: str, data: dict = None, headers: dict = None):
        """Asynchronous PUT request wrapper"""
        logger.info(f"PUT request to: {endpoint} | Data: {data}")
        response = await self.client.put(endpoint, json=data, headers=headers)
        self._log_response(response)
        return response
    
    async def delete(self, endpoint: str, headers: dict = None):
        """Asynchronous DELETE request wrapper"""
        logger.info(f"DELETE request to: {endpoint}")
        response = await self.client.delete(endpoint, headers=headers)
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
        auth_data = {"username": config.booker_api_username, "password": config.booker_api_password}
        response = await self.post("/auth", data=auth_data)
        if response.status_code == 200:
            token = response.json().get("token")
            logger.info("Token generated successfully")
            return token
        else:
            raise Exception(f"Failed to get token: {response.status_code}")

    async def create_booking(self, booking_data: BookingRequest):
        """Create a new booking and returns the response object"""
        # Convert Pydantic model to dictionary for the API call
        payload = booking_data.model_dump()
        response = await self.post("/booking", data=payload)
        return response

    async def update_booking(self, booking_id: int, booking_data: BookingRequest, token: str):
        """Update an existing booking using a Token (PUT)"""
        payload = booking_data.model_dump()

        # Adding the Authentication Cookie
        headers = {"Cookie": f"token={token}"}

        url = f"/booking/{booking_id}"
        response = await self.put(url, data=payload, headers=headers)
        return response

    async def delete_booking(self, booking_id: int, token: str):
        """Deletes a booking using a Token (DELETE)"""
        headers = {"Cookie": f"token={token}"}
        url = f"/booking/{booking_id}"
        response = await self.delete(url, headers=headers)
        return response

    async def close(self):
        """Close the session"""
        await self.client.aclose()