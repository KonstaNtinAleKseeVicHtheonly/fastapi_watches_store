from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
import jwt
# конфмгруация
from backend.core.config import project_settings
#зависимости
# модели
#лоигрование
from backend.core.logging.logging_conf import project_logger


# Создаём контекст для хеширования с использованием bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = project_settings.SECRET_KEY
ALGORITHM = project_settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = project_settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS = project_settings.REFRESH_TOKEN_EXPIRE_DAYS

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/users/token")



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
        project_logger.info(f"Начало создание jwt токена доступа юзера с данными {data}")
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
        project_logger.info(f"Начало создание refresh токена доступа юзера с данными {data}")
        to_encode = data.copy() #  Создаёт копию входного словаря data, чтобы избежать изменения оригинала
        expire = datetime.now(timezone.utc) + timedelta(minutes=cls.REFRESH_TOKEN_EXPIRE_DAYS) # время жизни токена
        to_encode.update({"exp": expire,
                        'token_type' : 'refresh'})
        return jwt.encode(to_encode, cls.SECRET_KEY, algorithm=cls.ALGORITHM) # кодируем данные от юзера



