from typing import Annotated
from uuid import UUID

from fastapi import Path

from .exceptions import CoinNotFoundHTTPException
from ..core.services import coin_service
from ..schemes import CoinHash


async def create_coin() -> UUID:
    coin_id = await coin_service.create_coin()
    if coin_id:
        return coin_id
    raise CoinNotFoundHTTPException()


async def get_coin_hash(coin_id: Annotated[UUID, Path]) -> CoinHash:
    coin = await coin_service.get_coin_hash(coin_id)
    if coin:
        return coin
    raise CoinNotFoundHTTPException()
