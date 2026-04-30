from sqlalchemy.ext.asyncio import  AsyncSession
from backend.core.logging.logging_conf import project_logger
from typing import AsyncGenerator
from backend.core.db.database import AsyncSessionLocal
# from backend.modules.users.service import UserService
# from backend.modules.users.dependencies import get_user_service



# SECRET_KEY = project_settings.SECRET_KEY
# ALGORITHM = project_settings.ALGORITHM
# ACCESS_TOKEN_EXPIRE_MINUTES = project_settings.ACCESS_TOKEN_EXPIRE_MINUTES
# REFRESH_TOKEN_EXPIRE_DAYS = project_settings.REFRESH_TOKEN_EXPIRE_DAYS

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/token")




async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency that provides database session.
    Сессия автоматически создается для каждого запроса и закрывается после ответа.
    """
    async with AsyncSessionLocal() as session:
        project_logger.debug({'event':'запуск зависимости асинхронной сессии'})
        yield session
    # ЗАКРЫТИЕ СЕССИИ
    project_logger.debug({'event':'ЗАкрытие асинхронной сессии'})
    
    
