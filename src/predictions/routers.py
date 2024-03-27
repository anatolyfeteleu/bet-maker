from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.events.enums import EventResultEnum
from src.events.services import get_event
from src.extensions.dependencies import get_async_session
from src.predictions import serializers, services

router = APIRouter()


@router.get(
    "/",
    description="List of bets",
    response_description="Return list of bets",
    response_model=List[serializers.PredictionListSerializer],
)
async def get_bets(session: AsyncSession = Depends(get_async_session)):
    return await services.get_predictions(session)


@router.post(
    path="/",
    description="Place a bet",
    response_description="Placed bet information",
    response_model=serializers.PredictionDetailSerializer,
)
async def place_a_bet(
    bet: serializers.PredictionCreateSerializer,
    session: AsyncSession = Depends(dependency=get_async_session),
):
    event = await get_event(session, bet.event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if event.result != EventResultEnum.PENDING:
        raise HTTPException(status_code=403, detail="Event is already completed")
    return await services.place_a_prediction(session, bet)
