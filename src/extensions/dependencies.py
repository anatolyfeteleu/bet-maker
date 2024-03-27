from typing import Any, Generator

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.database import async_session, sync_session


async def get_async_session() -> Generator[AsyncSession, Any, None]:
    async with async_session() as session:
        yield session


def get_sync_session() -> Generator[Session, Any, None]:
    with sync_session() as session:
        yield session
