from pydantic import BaseModel, Field, ConfigDict, field_validator, EmailStr
from datetime import datetime
from typing import Optional



class UserBaseSchema(BaseModel):
    '''базовая схема с общей инфой о товаре'''
    email: EmailStr = Field(..., min_length=5, max_length=200, description="user's email")
    password: str = Field(min_length=8, description="Пароль (от 8 символов)")
    fullname: str = Field(min_length=4, description='полное имя юзера')
    
    @field_validator('password')
    @classmethod
    def check_password(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return None
    
    
    @field_validator('fullname')
    @classmethod
    def check_username(cls, value:str):
        current_name = value.strip()
        if current_name in ('vip', 'admin'):
            raise ValueError('имя юзера не должно содержать vip или admin')
        if not current_name.isalnum():
            raise ValueError('Имя пользователя должно содержать только буквы и цифры')
        return current_name
    
    
class UserCreateSchema(UserBaseSchema):
    pass

class UserUpdateSchema(UserBaseSchema):
    pass

class UserPatchSchema(BaseModel):
    """Схема для частичного обновления пользователя (PATCH)"""
    email: Optional[EmailStr] = Field(
        None,
        min_length=5,
        max_length=200,
        description="user's email"
    )
    password: Optional[str] = Field(
        None,
        min_length=8,
        description="Пароль (от 8 символов)"
    )
    fullname: Optional[str] = Field(
        None,
        min_length=4,
        description='полное имя юзера'
    )
    @field_validator('password')
    @classmethod
    def check_password(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return None

    
    @field_validator('fullname')
    @classmethod
    def check_username(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return None  # Если поле не передано - не валидируем
        
        current_name = value.strip()
        if current_name in ('vip', 'admin'):
            raise ValueError('имя юзера не должно содержать vip или admin')
        if not current_name.isalnum():
            raise ValueError('Имя пользователя должно содержать только буквы и цифры')
        return current_name


class UserResponseSchema(UserBaseSchema):
    id: int = Field(..., description="User id")
    is_active: bool = Field(..., description="актуален ли юзер")
    is_superuser: bool = Field(..., description="Полномочия админа")
    created_at: datetime = Field(..., description="Когда юзер был зареган")
    


    class Config:
        from_attributes = True

