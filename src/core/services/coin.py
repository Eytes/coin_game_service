from src.schemes import Coin, CoinHash
from ..registries.abstract_registry import AsyncRegistry


class CoinService:
    def __init__(self, registry: AsyncRegistry):
        self.registry = registry

    async def get_coin(self, coin_id: str) -> Coin | None:
        coin = await self.registry.get_by_id(coin_id)
        return Coin(**coin) if coin else None

    async def get_coin_hash(self, coin_id: str) -> CoinHash | None:
        coin = await self.get_coin(coin_id)
        return CoinHash(**coin.model_dump()) if coin else None

    async def create_coin(self) -> str:
        coin_id = await self.registry.create(item_data=Coin())
        return coin_id

    async def delete_coin(self, coin_id: str) -> None:
        await self.registry.delete_by_id(coin_id)
