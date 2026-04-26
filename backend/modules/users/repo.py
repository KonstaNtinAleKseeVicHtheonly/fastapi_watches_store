from typing import List

from sqlalchemy.orm import joinedload, selectinload

from backend.core.repo.base_repo import BaseRepository
from backend.modules.users.models import UserModel
from sqlalchemy import (
    select,        # для создания SELECT запросов
    insert,        # для INSERT
    update,        # для UPDATE
    delete,        # для DELETE
    and_,          # логическое И
    or_,           # логическое ИЛИ
    not_,          # логическое НЕ
    desc,          # сортировка по убыванию
    asc,           # сортировка по возрастанию
    func,          # SQL функции (count, sum, avg, etc.)
    between,       # BETWEEN оператор
    distinct,      # DISTINCT
    text,          # для сырых SQL запросов
)
from sqlalchemy.ext.asyncio import AsyncSession



class UserRepository(BaseRepository):
    '''репозиторий для CRUD Операций с модель ProductModel'''
    
    def __init__(self, user_db_model : UserModel):
                super().__init__(user_db_model)