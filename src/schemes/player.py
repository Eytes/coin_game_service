from pydantic import BaseModel, PositiveInt

from .coin import CoinSide


class Player(BaseModel):
    id: PositiveInt
    coin_side: CoinSide
