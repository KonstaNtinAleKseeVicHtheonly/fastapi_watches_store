from fastapi import HTTPException, status
from backend.core.logging.logging_conf import project_logger
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
        existed_product = await self.main_repo.get_by_params(self.session,name = product_data.name)
        if existed_product:
            raise HTTPException(400, f"Product '{product_data.name}' already exists")
        new_product_data = product_data.model_dump()
        new_product = await self.main_repo.create(self.session, new_product_data)
        if new_product:
            await self.session.commit()
            return new_product
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid data for product {product_data}")
        
    async def delete_current_product(self, product_id:int)->bool|HTTPException:
        
        current_product = await self.main_repo.get_by_id(self.session, product_id)
        
        if not current_product:
            raise HTTPException(status_code=404, detail=f'продукта с id : {product_id}, не сущетсвует')
        if not current_product.is_active:
            raise HTTPException(status_code=404, detail=f'продукта с id : {product_id} уже удален')
        try:
             await self.main_repo.soft_deleting_by_id(self.session, product_id)
             await self.session.commit()
             return True
        except Exception as err:
            project_logger.error({'step':f'мягкое удаление товара с id {product_id}',
                                  'case' : f'ошибка произошла : {err}'})
            return HTTPException(status_code=500, detail='внутренняя ошибка сервера при удалении товара, повторите позже')