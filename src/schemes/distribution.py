from pydantic import BaseModel, ConfigDict

from .player import Player


class Distribution(BaseModel):
    model_config = ConfigDict(frozen=True)
    winners: list[Player]
    losers: list[Player]
