from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, status, Depends

from .dependencies import create_coin, get_coin_hash, get_coin
from .exceptions import HTTPExceptionResponseSchema
from ..schemes import CoinHash, Coin

router = APIRouter(
    prefix="/coins",
    tags=["Coins"],
)


@router.post(
    path="/new",
    response_model=UUID,
    status_code=status.HTTP_201_CREATED,
)
async def new_coin(coin_id: Annotated[UUID, Depends(create_coin)]):
    """Запросить новую монетку для новой партии"""
    return coin_id


@router.get(
    path="/{coin_id}/hash",
    response_model=CoinHash,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": HTTPExceptionResponseSchema},
    },
)
async def get_coin_hash(coin_hash: Annotated[CoinHash, Depends(get_coin_hash)]):
    return coin_hash


@router.get(
    path="/{coin_id}",
    response_model=Coin,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": HTTPExceptionResponseSchema},
    },
)
async def get_coin(coin: Annotated[Coin, Depends(get_coin)]):
    return coin
