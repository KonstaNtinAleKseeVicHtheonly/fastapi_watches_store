from fastapi import HTTPException, status
from backend.core.logging.logging_conf import project_logger
from backend.core.service.base_service import BaseService
from sqlalchemy.ext.asyncio import  AsyncSession
#модели
from backend.modules.categories.models import CategoryModel
# репозитории
from backend.modules.categories.repo import CategoryRepository
from backend.modules.products.repo import ProductRepository
# схемы
from backend.modules.categories.schemas import CategoryCreateSchema, CategoryResponseSchema, CategoryResponseSchema





class CategoryService(BaseService):
    
    def __init__(self, category_repo: CategoryRepository, db_session: AsyncSession):
        # Передаем основной репозиторий в BaseService
        super().__init__(category_repo, db_session)

    async def create_category_by_schema(self, category_data: CategoryCreateSchema) -> CategoryResponseSchema:
        project_logger.info({'event' : f'создание новой категории с параметрами {category_data}'})
        new_category_data = category_data.model_dump()
        existed_category = await self.main_repo.get_by_params(self.session, **new_category_data)
        if existed_category:
            project_logger.error({'event' : f'создание новой категории с параметрами {category_data}',
                                  'step' : 'проверка на существование категории',
                                  'case' : 'данная категория уже существует в БД'})
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Category with data {new_category_data} already exists"
            )
        new_category = await self.main_repo.create(self.session, new_category_data)
        if new_category:
            await self.session.commit()
            project_logger.info({'event' : f'создание новой категории с параметрами {category_data}',
                                  'case' : 'СОздана успешно'})
            return new_category
        project_logger.info({'event' : f'создание новой категории с параметрами {category_data}',
                             'case' : 'ДАнные категории не валидны'})
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid data for product {category_data}")

    async def get_category_by_id(self,category_id:int) -> CategoryModel:
        '''если по заданому id есть категория - вренет ее иначе ошибку поднимет'''
        project_logger.info({'event' : f'поиск категории по ее id {category_id}'})
        current_category = await self.main_repo.get_by_id(self.session, category_id)
        if not current_category:
            project_logger.error({'event' : f'поиск категории по ее id {category_id}',
                                 'case' : 'данная категория не найдена в БД'})
            raise HTTPException(status_code=404, detail="категория по заданному id не найдена")
        return current_category
    
    async def delete_current_category(self, category_id:int)->bool|HTTPException:
        
        current_category = await self.main_repo.get_by_id(self.session, category_id)
        
        if not current_category:
            raise HTTPException(status_code=404, detail=f'категории с id : {category_id}, не сущетсвует')
        if not current_category.is_active:
            raise HTTPException(status_code=404, detail=f'категории с id : {category_id} уже удален')
        try:
             await self.main_repo.soft_deleting_by_id(self.session, category_id)
             await self.session.commit()
             return True
        except Exception as err:
            project_logger.error({'step':f'мягкое удаление категории с id {category_id}',
                                  'case' : f'ошибка произошла : {err}'})
            return HTTPException(status_code=500, detail='внутренняя ошибка сервера при удалении категории, повторите позже')