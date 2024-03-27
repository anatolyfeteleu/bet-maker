from sqlalchemy import create_engine as create_sync_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.config import SETTINGS

DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{SETTINGS.DB_USERNAME}:{SETTINGS.DB_PASSWORD}"
    f"@{SETTINGS.DB_HOSTNAME}"
    f"/{SETTINGS.DB_NAME}"
)


Base = declarative_base()

async_engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(  # NOQA
    async_engine, class_=AsyncSession, expire_on_commit=False
)

sync_engine = create_sync_engine(DATABASE_URL, echo=True)
sync_session = sessionmaker(sync_engine)
