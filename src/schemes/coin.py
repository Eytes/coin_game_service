from datetime import datetime, UTC
from enum import Enum
from uuid import uuid4

from Crypto.Random import random
from pydantic import (
    BaseModel,
    Field,
    model_validator,
    StrictBool,
    UUID4,
    PositiveInt,
)
from typing_extensions import Self

from .utils import get_hash_sha256


class CoinSide(str, Enum):
    HEAD: str = "ОРЕЛ"
    TAIL: str = "РЕШКА"


class CoinHash(BaseModel):
    id: UUID4
    hash: str
    is_live: StrictBool


class Coin(BaseModel):
    id: UUID4 = Field(alias="_id", default_factory=uuid4)
    timestamp: PositiveInt = Field(
        default_factory=lambda: int(datetime.now(UTC).timestamp())
    )
    hash: str = ""
    salt: str = ""
    is_live: StrictBool = True
    side: CoinSide = Field(
        default_factory=lambda: random.choice([CoinSide.TAIL, CoinSide.HEAD])
    )

    @model_validator(mode="after")
    def calculate_hash_and_salt(self) -> Self:
        self.hash, self.salt = get_hash_sha256(self.side.value)
        return self
