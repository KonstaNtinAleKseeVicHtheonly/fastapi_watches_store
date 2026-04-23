from fastapi import HTTPException, status
from loguru import logger
from backend.core.service.base_service import BaseService
from sqlalchemy.ext.asyncio import  AsyncSession
from backend.modules.categories.repo import CategoryRepository
from backend.modules.products.repo import ProductRepository
from backend.modules.categories.schemas import CategoryCreateSchema, CategoryResponseSchema, CategoryResponseSchemaa





class CategoryService(BaseService):
    
    def __init__(self, category_repo: CategoryRepository, db_session: AsyncSession):
        # Передаем основной репозиторий в BaseService
        super().__init__(category_repo, db_session)

    async def create_category_by_schema(self, category_data: CategoryCreateSchema) -> CategoryResponseSchema:
        new_category_data = category_data.model_dump()
        existed_category = await self.main_repo.get_by_params(self.session, new_category_data)
        if existed_category:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Category with data {new_category_data} already exists"
            )
            
        new_category = await self.main_repo.create(self.session, new_category_data)
        if new_category:
            await self.session.refresh()
            return new_category
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid data for product {category_data}")

      
