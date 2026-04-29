from typing import List

from sqlalchemy.orm import joinedload, selectinload

from backend.core.repo.base_repo import BaseRepository
from backend.modules.products.models import ProductModel
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
from backend.modules.products.schemas import ProductCreateSchema


class ProductRepository(BaseRepository):
    '''репозиторий для CRUD Операций с модель ProductModel'''
    
    
    def __init__(self, product_db_model : ProductModel):
                super().__init__(product_db_model)
    
    
    # async def get_products_by_category(self, session:AsyncSession, category_id:int)->list[ProductModel]:
    #     '''по id категории выводит все продукты из нее'''
    #     stmt = select(self.model).where(self.model.category_id==category_id)
    #     result = await session.execute(stmt)
    #     return result.scalars().all()
        
    async def get_multiple_by_ids(self, session:AsyncSession, product_ids: List[int]) -> List[ProductModel]:
        '''по указанным списку id продуктов вернет развернутую инфу по ним '''
        stmt = select(self.model).where(
            self.model.id.in_(product_ids)
        ).options(selectinload(self.model.category))  # selectinload вместо joinedload для async
        
        result = await session.execute(stmt)
        return result.scalars().all()
    
    # async def create_product_by_schema(self, session:AsyncSession, product_data: ProductCreateSchema)->ProductModel:
    #     new_product = ProductModel(**product_data.model_dump())
    #     session.add(new_product)
    #     return new_product
    
    async def get_products_by_category(self,session:AsyncSession,  category_id: int) -> List[ProductModel]:
        '''выводит все продукты с развернутой инфой по указанной id категори'''
        stmt = select(self.model).options(joinedload(self.model.category)).filter(self.model.category_id == category_id)
        
        query = await session.execute(stmt)
        
        products_by_category = query.scalars().all()
        return products_by_category
        
  