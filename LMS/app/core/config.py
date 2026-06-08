from pydantic_settings import BaseSettings, SettingsConfigDict
from motor.motor_asyncio import AsyncIOMotorClient

class Settings(BaseSettings):
    MONGODB_URL: str
    DATABASE_NAME: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

# Initialize the async MongoDB client
client = AsyncIOMotorClient(settings.MONGODB_URL)
database = client[settings.DATABASE_NAME]