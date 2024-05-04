from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel


class AsyncRegistry(ABC):
    @abstractmethod
    async def get_by_id(self, item_id: Any) -> dict[str, Any] | None: ...

    @abstractmethod
    async def create(self, item_data: BaseModel, session: Any | None = None) -> Any: ...

    @abstractmethod
    async def delete_by_id(self, item_id: Any, session: Any | None = None) -> None: ...
