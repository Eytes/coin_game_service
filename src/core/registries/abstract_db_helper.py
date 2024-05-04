from abc import ABC, abstractmethod
from typing import AsyncGenerator, Any


class AsyncDBHelper(ABC):

    @abstractmethod
    def get_database(self) -> Any: ...

    @abstractmethod
    async def get_session(self) -> AsyncGenerator[Any, None]:
        yield None
