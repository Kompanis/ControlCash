import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from app.db.session import Base
from app.db import base as models  # <-- ВАЖНО: импортируем модели, чтобы они попали в metadata
from app.core.config import settings

async def main():
    engine = create_async_engine(settings.database_url, echo=True, future=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
    print("DB schema created.")

if __name__ == "__main__":
    asyncio.run(main())
