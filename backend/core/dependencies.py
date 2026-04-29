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



# async def get_verified_user(token: str = Depends(oauth2_scheme),
#       user_service: UserService=Depends(get_user_service)):
#     """
#     Проверяет JWT и возвращает пользователя из базы.
#     """
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#         )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         email: str = payload.get("sub")
#         if email is None:
#              raise credentials_exception
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Token has expired",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     except jwt.PyJWTError:
#         raise credentials_exception
#     current_user = await user_service.get_object_by_params(email=email, is_active=True)

#     if current_user is None:
#          raise credentials_exception
#     return current_user



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
    
    
