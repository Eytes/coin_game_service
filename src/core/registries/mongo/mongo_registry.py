from typing import Any

from motor.motor_asyncio import (
    AsyncIOMotorCollection,
    AsyncIOMotorClientSession,
    AsyncIOMotorDatabase,
)
from pydantic import BaseModel

from src.core.registries.abstract_registry import AsyncRegistry


class AsyncMongoRegistry(AsyncRegistry):
    def __init__(self, collection: AsyncIOMotorCollection) -> None:
        self.__collection = collection

    async def get_by_id(self, item_id: Any) -> dict[str, Any] | None:
        """
        Получить запись из БД по id
        :param item_id: id записи
        :return: запись из БД, а если не нашлась, тогда None
        """
        return await self.__collection.find_one({"_id": item_id})

    async def create(
        self,
        item_data: BaseModel,
        session: AsyncIOMotorClientSession | None = None,
    ) -> Any:
        """
        Создание записи в БД
        :param item_data: модель данных pydantic
        :param session:
        :return: id новой записи
        """
        result = await self.__collection.insert_one(item_data.model_dump(by_alias=True))
        return result.inserted_id

    async def delete_by_id(
        self,
        item_id: Any,
        session: AsyncIOMotorClientSession | None = None,
    ) -> None:
        """Удаление записи из БД"""
        await self.__collection.find_one_and_delete({"_id": item_id})


class AsyncMongoRegistryFactory:
    def __init__(self, database: AsyncIOMotorDatabase):
        self.__database = database

    def get_registry(self, collection_name: str) -> AsyncMongoRegistry:
        return AsyncMongoRegistry(self.__database[collection_name])
