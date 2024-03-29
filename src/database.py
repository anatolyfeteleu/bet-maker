from pydantic import PostgresDsn
from sqlalchemy import create_engine as create_sync_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.config import SETTINGS

ASYNC_DATABASE_URL: PostgresDsn = (
    f"postgresql+asyncpg://"
    f"{SETTINGS.DB_USERNAME}:{SETTINGS.DB_PASSWORD}"
    f"@{SETTINGS.DB_HOSTNAME}"
    f"/{SETTINGS.DB_NAME}"
)

DATABASE_URL: PostgresDsn = (
    f"postgresql://"
    f"{SETTINGS.DB_USERNAME}:{SETTINGS.DB_PASSWORD}"
    f"@{SETTINGS.DB_HOSTNAME}"
    f"/{SETTINGS.DB_NAME}"
)

Base = declarative_base()

async_engine = create_async_engine(ASYNC_DATABASE_URL, echo=True)
async_session = sessionmaker(  # NOQA
    async_engine, class_=AsyncSession, expire_on_commit=False
)

engine = create_sync_engine(DATABASE_URL, echo=True)
session = sessionmaker(engine)
