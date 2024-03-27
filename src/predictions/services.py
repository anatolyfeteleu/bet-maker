from typing import TYPE_CHECKING, List
from uuid import uuid4

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.extensions.dependencies import get_async_session
from src.predictions.enums import (
    EventPredictionBetResultMapper,
    PredictionBetEnum,
)
from src.predictions.models import Prediction
from src.predictions.serializers import PredictionCreateSerializer

if TYPE_CHECKING:
    from src.events.models import Event


async def get_predictions(session: AsyncSession) -> List[Prediction]:
    result = await session.execute(select(Prediction))
    return result.scalars().all()


async def place_a_prediction(
    session: AsyncSession, prediction: PredictionCreateSerializer
) -> Prediction:
    instance = Prediction(
        uuid=uuid4(),
        amount=prediction.amount,
        event_id=prediction.event_id,
        bet=prediction.bet,
    )
    session.add(instance)
    await session.commit()
    await session.refresh(instance)
    return instance


async def update_predictions(event: "Event"):
    session = await get_async_session().__anext__()
    predicted_result = EventPredictionBetResultMapper[event.result]

    win_statement = (
        update(Prediction)
        .where(
            Prediction.event_id == event.id, Prediction.bet == predicted_result
        )
        .values(status=PredictionBetEnum.WIN)
    )
    lose_statement = (
        update(Prediction)
        .where(
            Prediction.event_id == event.id, Prediction.bet != predicted_result
        )
        .values(status=PredictionBetEnum.LOSE)
    )

    await session.execute(win_statement)
    await session.execute(lose_statement)

    await session.commit()
