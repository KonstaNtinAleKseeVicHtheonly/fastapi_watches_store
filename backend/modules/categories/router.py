from fastapi import APIRouter, Body, Path, Query, HTTPException, status
from typing import List
#схемы
from backend.modules.categories.schemas import CategoryCreateSchema, CategoryPatchSchema, CategoryResponseSchema
# depends
from fastapi import Depends
from backend.modules.categories.dependencies import get_category_service
from backend.modules.users.dependencies import check_user_for_admin
# сервисы
from backend.modules.categories.service import CategoryService
from backend.modules.users.models import UserModel



category_api_router = APIRouter(prefix="/api/categories", tags=['categories'])





@category_api_router.get('/', response_model=List[CategoryResponseSchema], status_code=status.HTTP_200_OK)
async def get_all_categories(
                             category_service:CategoryService = Depends(get_category_service)):
    '''из базы берет все доступные категории'''
    try:
        
        all_categories = await category_service.get_all_objects()
        return all_categories
    except Exception as err:
         raise HTTPException(
            status_code=500,
            detail=str(err))  # общая ошибка 

@category_api_router.get("/{category_id}", response_model=CategoryResponseSchema, status_code=status.HTTP_200_OK)
async def get_category_by_id(
    category_id: int=Path(ge=1, description='id категории'),
    category_service: CategoryService = Depends(get_category_service)
):
    """Получить категорию по ID."""
    try:
        current_category = await category_service.get_category_by_id(category_id) # если категория не найдется то исключение из сервиса подинмется
        return CategoryResponseSchema.model_validate(current_category)
    except HTTPException:
        raise
    except Exception as err:
         raise HTTPException(
            status_code=500,
            detail=str(err))  # общая ошибка 


@category_api_router.post("/", response_model=CategoryResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_new_category(
    category_data: CategoryCreateSchema, # FastAPI валидирует Pydantic-схему
    category_service: CategoryService = Depends(get_category_service) # Внедряем сервис
):
    """Создать новую категорию."""
    try:
        # првоерка на существоавание категории уже в методе сервиса
        new_category = await category_service.create_category_by_schema(category_data)
        return CategoryResponseSchema.model_validate(new_category)
    except ValueError as e: # Обрабатываем бизнес-ошибки из сервиса
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    except Exception as e: # Общая обработка других ошибок
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An unexpected error occurred: {e}")


@category_api_router.delete('/{category_id}', status_code=status.HTTP_200_OK)
async def delete_category(category_id : int = Path(ge=0), 
                         category_service: CategoryService = Depends(get_category_service),
                         admin_user: UserModel = Depends(check_user_for_admin)):

        deleting_result = await category_service.delete_current_category(category_id)
        if deleting_result:
            return {"message" : f"Категория  с id {category_id} стала неактивна"}
        return{"message" : "произошла непредвиденна ситуация"}





# @category_api_router.get('/{category_id}', response_model=CategorySchena)
# async def get_current_category(category_id : int = Path(ge=1), 
#                                session : AsyncSession = Depends(get_db_session),
#                                repo : CategoryRepository = Depends(get_category_repository)):
#     '''вывод категории по id'''
#     try:
#         current_category = await repo.get_by_id(session, category_id)
#         return current_category
#     except ValueError as err:
#                  raise HTTPException(
#             status_code=400,
#             detail=str(err)  
#         )
#     except Exception as err:
#          raise HTTPException(
#             status_code=500,
#             detail=str(err)  # общая ошибка 
#         )




# @category_api_router.post('/', response_model=CategorySchena)
# async def create_category(new_category_info : CategoryCreateSchema, 
#                           session : AsyncSession= Depends(get_db_session), 
#                           repo:CategoryRepository= Depends(get_category_repository)):
#     try:
#         # Проверка существования parent_id, если указан
#         if new_category_info.parent_id is not None:
#             parent = await repo.get_by_params(session, id = new_category_info.parent_id, is_active = True)
#             if parent is None: # значит нет в базе родителя по id указанного в запросе
#                 raise HTTPException(status_code=400, detail="Parent category not found")
#         # процесс создания новой категории
#         new_category = await repo.create(session, new_category_info.model_dump())
#         await session.commit()
#         await session.refresh(new_category)
#         return new_category
#     except ValueError as err:
#          raise HTTPException(
#             status_code=400,
#             detail=str(err)  # "Категория 'Test' уже существует"
#         )
#     except Exception as err:
#          raise HTTPException(
#             status_code=500,
#             detail=str(err)  # общая ошибка 
#         )



# @category_api_router.put('/{category_id}', response_model=CategorySchena)
# async def update_category(update_data : CategoryCreateSchema,
#                           category_id : int = Path(ge=0), 
#                           session : AsyncSession = Depends(get_db_session),
#                           repo:CategoryRepository = Depends(get_category_repository)):
#     try:
#         #проверямем наличие и валидность родительского id категории
#         if update_data.parent_id is not None:
#             parent = await repo.get_by_params(session, id = update_data.parent_id, is_active = True)
#             if parent is None:
#                 raise HTTPException(status_code=400, detail="Parent category not found") 
#         updated_result = await repo.update_put(session,category_id, update_data.model_dump())
#         await session.commit()
#         await session.refresh(updated_result)
#         return updated_result
        
#     except HTTPException as err:
#         raise HTTPException(
#                 status_code=400,
#                 detail=str(err)  # неверный id родителя 
#             )
#     except Exception as err:
#             raise HTTPException(
#                 status_code=500,
#                 detail=str(err)  # общая ошибка 
#             )

