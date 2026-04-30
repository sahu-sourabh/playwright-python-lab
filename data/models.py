from pydantic import BaseModel

class AuthRequest(BaseModel):
    username: str = "admin"
    password: str = "password123"

class AuthResponse(BaseModel):
    token: str