from fastapi.params import Depends
from sqlalchemy.ext.asyncio import  AsyncSession
from loguru import logger
from typing import AsyncGenerator
from backend.modules.categories.repo import CategoryRepository
from backend.modules.categories.service import CategoryService
from backend.modules.categories.models import CategoryModel
from backend.core.dependencies import get_db_session




def get_category_repository():
     return CategoryRepository(CategoryModel)
 
 
def get_category_service(session:AsyncSession = Depends(get_db_session), 
                        category_repo : CategoryRepository=Depends(get_category_repository)):

        return CategoryService(category_repo=category_repo, db_session=session)
