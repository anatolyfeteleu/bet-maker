from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.events import serializers, services
from src.events.enums import EventResultEnum
from src.extensions.dependencies import get_async_session

router = APIRouter(tags=["Events"])


@router.get(
    "/",
    description="List of events",
    response_description="Return list of events",
    response_model=List[serializers.EventListSerializer],
)
async def get_events(session: AsyncSession = Depends(get_async_session)):
    return await services.get_events(session)


@router.put(
    path="/{event_id}",
    description="Updates the selected one event",
    response_description="Returns the new status and id",
    response_model=serializers.EventShortSerializer,
)
async def update_event(
    event_id: int,
    data: serializers.EventUpdateSerializer,
    session: AsyncSession = Depends(dependency=get_async_session),
):
    event = await services.get_event(session, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if event.result != EventResultEnum.PENDING:
        raise HTTPException(
            status_code=403, detail="Event is already completed"
        )
    return await services.update_event(
        session=session, event_id=event_id, data=data
    )
