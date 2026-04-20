from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from backend.core.config import project_settings





engine = create_async_engine(project_settings.DATABASE_URL)

# 2. Создаем фабрику сессий
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)
# 3. Базовый класс для моделей
class Base(DeclarativeBase):  # общая таблица для моделей проекта связыающая их мжеду собой и с СУБД
    pass


      