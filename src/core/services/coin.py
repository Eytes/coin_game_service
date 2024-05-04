from pydantic import UUID4

from src.schemes import Coin, CoinHash
from ..registries.abstract_registry import AsyncRegistry


class CoinService:
    def __init__(self, registry: AsyncRegistry):
        self.registry = registry

    async def get_coin(self, coin_id: UUID4) -> Coin | None:
        coin = await self.registry.get_by_id(coin_id)
        return Coin(**coin) if coin else None

    async def get_coin_hash(self, coin_id: UUID4) -> CoinHash | None:
        coin = await self.get_coin(coin_id)
        return CoinHash(**coin.model_dump()) if coin else None

    async def create_coin(self) -> UUID4:
        coin_id: UUID4 = await self.registry.create(item_data=Coin())
        return coin_id

    async def delete_coin(self, coin_id: UUID4) -> None:
        await self.registry.delete_by_id(coin_id)
