import os

from pydantic import PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict


class MongoSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    username: str = os.getenv("MONGO_USERNAME")  # type: ignore
    password: str = os.getenv("MONGO_PASSWORD")  # type: ignore
    host: str = os.getenv("MONGO_HOST") or "localhost"
    port: PositiveInt = int(os.getenv("MONGO_PORT") or 27017)
    database_name: str = os.getenv("MONGO_DATABASE_NAME") or "coin_database"
    url: str = f"mongodb://{username}:{password}@{host}:{port}/"


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    mongodb: MongoSettings = MongoSettings()


settings = Settings()
