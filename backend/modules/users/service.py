from fastapi import HTTPException, status
from backend.core.logging.logging_conf import project_logger
from backend.core.service.base_service import BaseService
from sqlalchemy.ext.asyncio import  AsyncSession
from backend.modules.categories.repo import CategoryRepository
from backend.modules.products.models import ProductModel
from backend.modules.users.repo import UserRepository
from backend.modules.products.schemas import ProductCreateSchema, ProductListResponseSchema, ProductResponseSchema
#токенизация jwt
from backend.core.security import TokenService, verify_password





class UserService(BaseService):
    
    def __init__(self, user_repo: UserRepository, token_service: TokenService, db_session: AsyncSession):
        # Передаем основной репозиторий в BaseService
        super().__init__(user_repo, db_session)
        
        self.token_service = token_service # логика с токенизацией у нас отдельно
        
    async def get_user_by_info(self,email:str, full_name:str):
        '''используется при выводе юзера или проверке на существоавание при создании юзера'''
        current_user = await self.main_repo.get_by_params(self.session, 
                                                          email=email,
                                                          full_name=full_name, is_active=True)
        return current_user
    
    def generate_access_token_for_user(self,user_data:dict):
        user_access_token = self.token_service.create_access_token(data=user_data)
        return user_access_token
    
    def generate_refresh_token_for_user(self,user_data:dict):
        user_refresh_token = self.token_service.create_refresh_token(data=user_data)
        return user_refresh_token
    
    def generate_tokens_for_user(self, user_data:dict) -> dict:
        '''по валидным данным от новго юзера генерирует ему токены'''
        user_refresh_token = self.generate_refresh_token_for_user(user_data=user_data)
        user_access_token = self.generate_access_token_for_user(user_data=user_data)
        return {'access_token' : user_access_token, 'refresh_token' : user_refresh_token, 'token_type' : 'bearer'}
    
    
    
    async def login_user(self, email: str, password: str):
            """Полная аутентификация + создание токенов"""
            current_user = await self.get_object_by_params(email=email, is_active=True)
            
            if not current_user or not verify_password(password, current_user.hashed_password):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect email or password",
                    headers={"WWW-Authenticate": "Bearer"})
            user_data = {
                'sub': current_user.email,
                'full_name': current_user.full_name,
                'id': current_user.id
            }
            
            return self.generate_tokens_for_user(user_data)  # ← возвращает готовый dict
        
