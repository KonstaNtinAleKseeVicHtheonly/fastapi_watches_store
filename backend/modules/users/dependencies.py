from fastapi import HTTPException, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import  AsyncSession
from backend.core.logging.logging_conf import project_logger
from typing import AsyncGenerator
from backend.modules.users.repo import UserRepository
from backend.modules.users.service import UserService
from backend.modules.users.models import UserModel
from backend.core.dependencies import get_db_session
from backend.core.security import TokenService
#конфигурация
from backend.core.config import project_settings
#
from fastapi.security import OAuth2PasswordBearer
import jwt



SECRET_KEY = project_settings.SECRET_KEY
ALGORITHM = project_settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = project_settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS = project_settings.REFRESH_TOKEN_EXPIRE_DAYS

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/users/token") # путь ведущий на эндпоинт аутентифификации


# дописать репозиторий и сервис юзера
def get_user_repository():
     return UserRepository(UserModel)

def get_token_service():
     return TokenService()
 
 
def get_user_service(session:AsyncSession = Depends(get_db_session), 
                        user_repo : UserRepository=Depends(get_user_repository),
                        token_service : TokenService=Depends(get_token_service)):

        return UserService(user_repo=user_repo, token_service=token_service, db_session=session)




async def get_verified_user(token: str = Depends(oauth2_scheme),
      user_service: UserService=Depends(get_user_service))->UserModel|HTTPException:
    """
    Проверяет JWT и возвращает пользователя из базы.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
             raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token has expired",
        headers={"WWW-Authenticate": "Bearer"},
    )
    except jwt.PyJWTError:
        raise credentials_exception
    current_user = await user_service.get_object_by_params(email=email, is_active=True)

    if current_user is None:
         raise credentials_exception
    return current_user

