from fastapi.params import Depends
from sqlalchemy.ext.asyncio import  AsyncSession
from loguru import logger
from typing import AsyncGenerator
from backend.modules.users.repo import UserRepository
from backend.modules.users.service import UserService
from backend.modules.users.models import UserModel
from backend.core.dependencies import get_db_session
from backend.core.security import TokenService



# дописать репозиторий и сервис юзера
def get_user_repository():
     return UserRepository(UserModel)

def get_token_service():
     return TokenService()
 
 
def get_user_service(session:AsyncSession = Depends(get_db_session), 
                        user_repo : UserRepository=Depends(get_user_repository),
                        token_service : TokenService=Depends(get_token_service)):

        return UserService(user_repo==user_repo, token_service=token_service, db_session=session)


