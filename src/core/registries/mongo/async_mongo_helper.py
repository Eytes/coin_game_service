from typing import AsyncGenerator

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorClientSession,
)

from src.core.config import settings
from ..abstract_db_helper import AsyncDBHelper


class AsyncMongoDBHelper(AsyncDBHelper):
    def __init__(self, client_url: str, database_name: str) -> None:
        self.__mongo_client = AsyncIOMotorClient(
            client_url,
            uuidRepresentation="standard",
        )
        self.__mongo_database = self.__mongo_client[database_name]

    def get_database(self) -> AsyncIOMotorDatabase:
        return self.__mongo_database

    async def get_session(self) -> AsyncGenerator[AsyncIOMotorClientSession, None]:
        """Создается новая сессия. После окончания операций автоматически завершается"""
        async with await self.__mongo_client.start_session() as session:
            yield session
            await session.end_session()


mongo_helper = AsyncMongoDBHelper(
    client_url=settings.mongodb.url,
    database_name=settings.mongodb.database_name,
)
