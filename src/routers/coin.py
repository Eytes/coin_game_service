from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, status, Depends

from .dependencies import create_coin, get_coin_hash
from ..schemes import CoinHash

router = APIRouter(
    prefix="/coins",
    tags=["Coins"],
)


@router.post(
    path="/new",
    status_code=status.HTTP_201_CREATED,
    response_model=UUID,
)
async def new_coin(coin_id: Annotated[UUID, Depends(create_coin)]):
    """Запросить новую монетку для новой партии"""
    return coin_id


@router.get(
    path="/{coin_id}",
    status_code=status.HTTP_200_OK,
    response_model=CoinHash,
)
async def get_coin_hash(coin_hash: Annotated[CoinHash, Depends(get_coin_hash)]):
    return coin_hash
