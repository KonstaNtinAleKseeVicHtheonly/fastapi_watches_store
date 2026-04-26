from fastapi import HTTPException, status
from loguru import logger
from backend.core.service.base_service import BaseService
from sqlalchemy.ext.asyncio import  AsyncSession
from backend.modules.categories.repo import CategoryRepository
from backend.modules.products.models import ProductModel
from backend.modules.products.repo import ProductRepository
from backend.modules.products.schemas import ProductCreateSchema, ProductListResponseSchema, ProductResponseSchema





class ProductService(BaseService):
    
    def __init__(self, product_repo: ProductRepository, category_repo: CategoryRepository, db_session: AsyncSession):
        # Передаем основной репозиторий в BaseService
        super().__init__(product_repo, db_session)
        # Добавляем дополнительный репозиторий
        self.category_repo = category_repo
    
    async def get_products_by_category(self, category_id: int) -> list[ProductModel]:
        current_category = await self.category_repo.get_by_id(self.session, category_id)
        if not current_category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {category_id} not found")
            
        products = await self.main_repo.get_products_by_category(self.session, category_id)

        return products
    
    async def create_product_by_schema(self, product_data: ProductCreateSchema) -> ProductResponseSchema:
        '''по принятым их схемы валидации данным проверяе т и создает нвоый продукт'''
        category = await self.category_repo.get_by_id(self.session, product_data.category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Category with id {product_data.category_id} does not exist"
            )
        existed_product = await self.main_repo.get_by_params(self.session,product_data.name)
        if existed_product:
            raise HTTPException(400, f"Product '{product_data.name}' already exists")
        new_product_data = product_data.model_dump()
        new_product = await self.main_repo.create(self.session, new_product_data)
        if new_product:
            await self.session.refresh()
            return new_product
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid data for product {product_data}")

  