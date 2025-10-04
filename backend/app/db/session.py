from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
from app.core.config import settings

# Именование для ограничений — важно для Alembic
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)

class Base(DeclarativeBase):
    metadata = metadata

# Создаём асинхронный движок
engine = create_async_engine(settings.database_url, echo=False, pool_pre_ping=True, future=True)

# Фабрика для сессий
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
