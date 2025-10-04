import asyncio, asyncpg
from app.core.config import settings
async def main():
    conn = await asyncpg.connect(
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        database=settings.POSTGRES_DB,
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
    )
    v = await conn.fetchval('select 1')
    print('PG_OK:', v)
    await conn.close()
asyncio.run(main())
