from abc import ABC, abstractmethod
from typing import AsyncGenerator

from .base_types import T


class AsyncDBHelper(ABC):

    @abstractmethod
    def get_database(self) -> T: ...

    @abstractmethod
    async def get_session(self) -> AsyncGenerator[T, None]:
        yield
