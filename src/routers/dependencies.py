from typing import Annotated

from fastapi import Path
from pydantic import UUID4

from .exceptions import CoinNotFoundHTTPException
from ..core.services import coin_service
from ..schemes import CoinHash, Coin, Player, Distribution


async def create_coin() -> UUID4:
    coin_id = await coin_service.create_coin()
    if coin_id:
        return coin_id
    raise CoinNotFoundHTTPException()


async def get_coin_hash(coin_id: Annotated[UUID4, Path]) -> CoinHash:
    coin = await coin_service.get_coin_hash(coin_id)
    if coin:
        return coin
    raise CoinNotFoundHTTPException()


async def get_coin(coin_id: Annotated[UUID4, Path]) -> Coin:
    coin = await coin_service.get_coin(coin_id)
    if coin:
        return coin
    raise CoinNotFoundHTTPException()


async def distribution(
    coin_id: UUID4,
    players: list[Player],
) -> Distribution:

    coin = await get_coin(coin_id)
    winners, losers = [], []
    for player in players:
        if player.coin_side == coin.side:
            winners.append(player)
        else:
            losers.append(player)

    return Distribution(winners=winners, losers=losers)
