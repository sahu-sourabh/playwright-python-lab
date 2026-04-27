from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # API Target
    booker_api_url: str

    # UI Targets
    booker_base_url: str
    sauce_base_url: str

    model_config = SettingsConfigDict(env_file=".evn", extra="ignore")

# class object
config = Settings()