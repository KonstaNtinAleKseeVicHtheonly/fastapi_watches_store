
from sqlalchemy.ext.asyncio import  AsyncSession
from loguru import logger
from typing import AsyncGenerator
from db.database import AsyncSessionLocal




async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency that provides database session.
    Сессия автоматически создается для каждого запроса и закрывается после ответа.
    """
    async with AsyncSessionLocal() as session:
        logger.debug("🔌 Database session created")
        yield session
    # ЗАКРЫТИЕ СЕССИИ
    logger.debug("🔌 Database session closed")