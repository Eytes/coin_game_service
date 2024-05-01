from pydantic import BaseModel

from .coin import CoinSide


class Player(BaseModel):
    id: int
    bet: float
    coin_side: CoinSide
