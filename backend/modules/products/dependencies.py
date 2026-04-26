from fastapi.params import Depends
from sqlalchemy.ext.asyncio import  AsyncSession
from loguru import logger
from typing import AsyncGenerator
from backend.modules.products.repo import ProductRepository
from backend.modules.categories.repo import CategoryRepository
from backend.modules.products.service import ProductService
from backend.modules.products.models import ProductModel

from backend.modules.categories.dependencies import get_category_repository
from backend.core.dependencies import get_db_session




def get_product_repository():
     return ProductRepository(ProductModel)
 
 

def get_product_service(session:AsyncSession = Depends(get_db_session), 
                        product_repo : ProductRepository=Depends(get_product_repository),
                        category_repo : CategoryRepository = Depends(get_category_repository)):

        return ProductService(product_repo=product_repo, category_repo=category_repo, db_session=session)
