from typing import List

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.events.enums import EventResultEnum
from src.events.models import Event
from src.events.serializers import EventUpdateSerializer
from src.predictions.services import update_predictions


async def get_event(session: AsyncSession, event_id: int) -> Event | None:
    statement = select(Event).filter(Event.id == event_id)
    result = await session.execute(statement)
    return result.scalar_one_or_none()


async def get_events(session: AsyncSession) -> List[Event]:
    result = await session.execute(select(Event))
    return result.scalars().all()


async def update_event(
    session: AsyncSession, event_id: int, data: EventUpdateSerializer
) -> Event | None:
    async def update_row(event_id: int, result: EventResultEnum):
        statement = (
            update(Event).where(Event.id == event_id).values(result=result)
        )
        await session.execute(statement)
        await session.commit()

    instance = await session.get(Event, event_id)
    if not instance:
        return

    await update_row(event_id, data.result)
    await update_predictions(event=instance)
    return instance
