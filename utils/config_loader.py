import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    USERNAME = os.getenv("SAUCE_USERNAME")
    LOCKED_OUT_USERNAME = os.getenv("SAUCE_LOCKED_OUT_USERNAME")
    PASSWORD = os.getenv("SAUCE_PASSWORD")
    SAUCE_BASE_URL = os.getenv("SAUCE_BASE_URL")
