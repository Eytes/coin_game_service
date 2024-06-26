from fastapi import APIRouter

from .coin import router as coin_router
from .game_rules import router as rules_router
from ..core.config import settings

router_v1 = APIRouter(prefix=settings.api_v1_prefix)
router_v1.include_router(coin_router)
router_v1.include_router(rules_router)
