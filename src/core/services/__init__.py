from .coin import CoinService
from ..registries import CoinMongoRegistry

coin_service = CoinService(CoinMongoRegistry)
