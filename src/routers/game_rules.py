from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, status, Body

from .dependencies import distribution
from ..schemes import Player, Distribution

router = APIRouter(
    prefix="/rules",
    tags=["Rules"],
)


@router.post(
    path="/winners_and_losers",
    response_model=Distribution,
    status_code=status.HTTP_200_OK,
)
async def get_players_distribution(
    coin_id: Annotated[UUID, Body],
    players: Annotated[list[Player], Body],
):
    """
    Распределить средства между игроками
    :param coin_id: id монетки
    :param players: массив игроков
    :return: два массива - победители и проигравшие
    """
    return await distribution(
        coin_id=coin_id,
        players=players,
    )
