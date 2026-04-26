from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
import jwt
# конфмгруация
from backend.core.config import project_settings
#зависимости
# модели
#лоигрование
from loguru import logger


# Создаём контекст для хеширования с использованием bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = project_settings.SECRET_KEY
ALGORITHM = project_settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = project_settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS = project_settings.REFRESH_TOKEN_EXPIRE_DAYS

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/token")



# перенесено в users/dependenices
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


def hash_password(password: str) -> str:
 """
 Преобразует пароль в хеш с использованием bcrypt.
 """
 return pwd_context.hash(password)



def verify_password(plain_password: str, hashed_password: str) -> bool:
 """
 Проверяет, соответствует ли введённый пароль сохранённому хешу.
 """
 return pwd_context.verify(plain_password, hashed_password)


class TokenService:
    
    SECRET_KEY = project_settings.SECRET_KEY
    ALGORITHM = project_settings.ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES = project_settings.ACCESS_TOKEN_EXPIRE_MINUTES
    REFRESH_TOKEN_EXPIRE_DAYS = project_settings.REFRESH_TOKEN_EXPIRE_DAYS
        
    @classmethod
    def create_access_token(cls, data: dict): # прнимает инфу о юзере для payload в jwt
        """
        Создаёт JWT с payload (sub, role, id, exp).
        функия применяеься в post эндпионте после успешной аутентификации
        """
        logger.info(f"Начало создание jwt токена доступа юзера с данными {data}")
        to_encode = data.copy() #  Создаёт копию входного словаря data, чтобы избежать изменения оригинала
        expire = datetime.now(timezone.utc) + timedelta(minutes=cls.ACCESS_TOKEN_EXPIRE_MINUTES) # время жизни токена
        to_encode.update({"exp": expire,
                        'token_type' : 'access'})
        return jwt.encode(to_encode, cls.SECRET_KEY, algorithm=cls.ALGORITHM) # кодируем данные от юзера

    @classmethod
    def create_refresh_token(cls, data: dict): # прнимает инфу о юзере для payload в jwt
        """
        Создаёт refresh-токен с длительным сроком действия и token_type="refresh".
        """
        logger.info(f"Начало создание refresh токена доступа юзера с данными {data}")
        to_encode = data.copy() #  Создаёт копию входного словаря data, чтобы избежать изменения оригинала
        expire = datetime.now(timezone.utc) + timedelta(minutes=cls.REFRESH_TOKEN_EXPIRE_DAYS) # время жизни токена
        to_encode.update({"exp": expire,
                        'token_type' : 'refresh'})
        return jwt.encode(to_encode, cls.SECRET_KEY, algorithm=cls.ALGORITHM) # кодируем данные от юзера



