from pydantic_settings import BaseSettings
from dotenv import find_dotenv


class Settings(BaseSettings):
    azure_storage_account_key: str
    steam_api_key: str
    steam_id: str

    class Config:
        env_file = find_dotenv(".env")
        env_file_encoding = "utf-8"
        extra = "ignore"
        case_sensitive = False


settings = Settings()
