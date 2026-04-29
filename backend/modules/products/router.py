from typing import List
from fastapi import APIRouter, Body, File, Path, Query, Depends, status, HTTPException, UploadFile
# схемы
from backend.modules.products.schemas import ProductCreateSchema, ProductResponseSchema, ProductPatchSchema, ProductListResponseSchema
#сервисы БД
from backend.modules.products.service import ProductService
from backend.modules.categories.service import CategoryService
#depends
from backend.modules.products.dependencies import get_product_service
from backend.modules.categories.dependencies import get_category_service



# # конфиги для записи фоток продуктов в папку проекта
# BASE_DIR = SYSTEM_PATH(__file__).resolve().parent.parent.parent # Абсолютный путь к корню проекта. Нужен, чтобы в дальнейшем можно было найти файл по относительному пути. 
# MEDIA_ROOT = BASE_DIR / "media" / "products"
# MEDIA_ROOT.mkdir(parents=True, exist_ok=True)
# ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp"}
# MAX_IMAGE_SIZE = 2 * 1024 * 1024  # 2 097 152 байт


product_api_router = APIRouter(prefix="/api/products", tags=['products'])



@product_api_router.get('/', response_model=ProductListResponseSchema, status_code=status.HTTP_200_OK)
async def get_all_products(
                             product_service:ProductService = Depends(get_product_service)):
    '''из базы берет все доступные продукты'''
    try:
        
        all_products = await product_service.get_all_objects()
        return ProductListResponseSchema(
                products=all_products,  # [] если пусто
                total=len(all_products),
                page=1,
                page_size=20
            )
    except Exception as err:
         raise HTTPException(
            status_code=500,
            detail=str(err))  # общая ошибка 

@product_api_router.get("/{product_id}", response_model=ProductResponseSchema, status_code=status.HTTP_200_OK)
async def get_product_by_id_route(
    product_id: int=Path(ge=1, description='id продукта'),
    product_service:ProductService = Depends(get_product_service),
):
    """Получить продукт по ID."""
    try:
        current_product = await product_service.get_object_by_id(product_id)
        
        return ProductResponseSchema.model_validate(current_product)
    except Exception as err:
         raise HTTPException(
            status_code=500,
            detail=str(err))  # общая ошибка 
         
@product_api_router.get("/category/{category_id}", response_model=ProductListResponseSchema, status_code=status.HTTP_200_OK)
async def get_products_by_category(
    category_id: int=Path(ge=1, description='id категории для вывода продуктов из нее'),
    product_service:ProductService = Depends(get_product_service),
    page: int = 1,
    page_size: int = 20):
    """Получить развернутую инфу по продуктам по указанной Id категории"""
    try:
        products_by_category = await product_service.get_products_by_category(category_id)

        return ProductListResponseSchema(
                                        products = products_by_category,
                                        page = page,
                                        page_size=page_size,
                                        total = len(products_by_category))
    except Exception as err:
         raise HTTPException(
            status_code=500,
            detail=str(err)) from err # общая ошибка 
         


@product_api_router.post("/", response_model=ProductResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_product_route(
    product_data: ProductCreateSchema, # FastAPI валидирует Pydantic-схему
    product_service: ProductService = Depends(get_product_service) # Внедряем сервис
):
    """Создать новую категорию."""
    try:
        
        new_product = await product_service.create_product_by_schema(product_data)
        return ProductResponseSchema.model_validate(new_product)
    except ValueError as e: # Обрабатываем бизнес-ошибки из сервиса
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    except Exception as e: # Общая обработка других ошибок
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An unexpected error occurred: {e}")




# # вариант для фильтрации и паигнации
# @product_api_router.get('/', response_model = ProductListResponseSchema)
# async def get_all_products(session : AsyncSession = Depends(get_db_session),
#                            page : int = Query(1, ge=1),
#                            page_size : int = Query(20,ge=1, le=100),
#                             category_id: int | None = Query(
#                                 None, description="ID категории для фильтрации"),
#                             min_price: float | None = Query(
#                                 None, ge=0, description="Минимальная цена товара"),
#                             max_price: float | None = Query(
#                                 None, ge=0, description="Максимальная цена товара"),
#                             in_stock: bool | None = Query(
#                                 None, description="true — только товары в наличии, false — только без остатка"),
#                             rating: float | None = Query(None, ge= 1, description='рейтинг товара'),
#                             seller_id: int | None = Query(
#                                 None, description="ID продавца для фильтрации"),
#                             search: str | None = Query(None, min_length=1, description="Поиск по названию товара"),
#                            repo : ProductRepository = Depends(get_product_repository),
#                            )->ProductList:
#     '''из базы берет все доступные категории с пагинацией'''
#     try:
#         task = high_priority_task.delay()
#         # Проверка логики min_price <= max_price
#         if min_price is not None and max_price is not None and min_price > max_price:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="min_price не может быть больше max_price",
#             )
#         # Формируем список фильтров
#         filters = [ProductModel.is_active == True]
#         if category_id is not None: # ограничение выборки указанной категорией
#             filters.append(ProductModel.category_id == category_id)
#         if min_price is not None:# Ограничение по цене
#             filters.append(ProductModel.price >= min_price)
#         if max_price is not None:
#             filters.append(ProductModel.price <= max_price)
#         if in_stock is not None:# ограничение по количеству на складе
#             filters.append(ProductModel.stock > 0 if in_stock else ProductModel.stock == 0)
#         if rating is not None:
#             filters.append(ProductModel.rating >= rating)
#         if seller_id is not None: # если продавец есть то его товары выводим иначе все выводим
#             filters.append(ProductModel.seller_id == seller_id) 
#         rank_col = None # критерий ранжирование
#         if search:# критерий поиска по словам
#             search_value = search.strip()
#             if search_value:
#                 ts_query_eng = func.websearch_to_tsquery('english', search_value) # реобразует обычный поисковый запрос в объект типа tsquery, подходящий для PostgreSQL.
#                 ts_query_rus = func.websearch_to_tsquery('russian', search_value)
#                 filters.append(ProductModel.tsv.op('@@')(ts_query_eng))# Добавляем full-text фильтр @@ в атрибут tsv(токенизация слов из запроса(search))
#                 filters.append(ProductModel.tsv.op('@@')(ts_query_rus))
#                 rank_col = func.greatest(
#                             func.ts_rank_cd(ProductModel.tsv, ts_query_eng),# алгоритм ранжирования -Учитывает плотность покрытия ключевых слов, учитывает вес слова
#                             func.ts_rank_cd(ProductModel.tsv, ts_query_rus)
#                         ).label("rank")
   
#         # поиск товаров в бд по условиям от юзера(фильтрация) и вывод общего количества найденных товаров
#         items_and_total:dict[str,any] = await repo.get_objects_for_offset_pagination_by_params(session,filters, page=page, page_size=page_size, rank_col=rank_col)
        
#         return {'items' : items_and_total['items'],
#                 'total' : items_and_total['total'],
#                 'page' : page,
#                 'page_size' : page_size}
#     except Exception as err:
#                  raise HTTPException(
#             status_code=500,
#             detail=str(err))  # общая ошибка 
        

# @product_api_router.get('/{product_id}', response_model=ProductSchema)
# async def get_current_product(product_id : int = Path(ge=0),
#                              session : AsyncSession = Depends(get_db_session),
#                              repo : ProductRepository = Depends(get_product_repository),
#                               ) -> ProductSchema:
#     '''Выводит инфу о продукте через id'''
#     try:
#         task = low_priority_task.delay()
#         current_product = await repo.get_by_params(session, id=product_id, is_active=True)
#         if not current_product:
#             raise HTTPException(status_code=400, detail="Product doesn't exist or inactive")
#         return current_product
#     except ValueError as err:
#         raise HTTPException(
#             status_code=400,
#             detail=str(err) )
#     except Exception as err:
#                  raise HTTPException(
#             status_code=500,
#             detail=str(err))  
                 
                 
# @product_api_router.get('/{product_id}/reviews', response_model=List[ReviewSchema])
# async def get_product_reviews(product_id : int = Path(ge=0),
#                              session : AsyncSession = Depends(get_db_session),
#                              product_repo : ProductRepository = Depends(get_product_repository),
#                              review_repo : ReviewRepository = Depends(get_review_repository),
#                               ) ->List[ReviewSchema]:
#     '''По Id товара выводит все отзывы по нему. Доступно не аутентифицированным юзерам'''
#     try:
#         current_product = await product_repo.get_by_params(session, id=product_id, is_active=True)
#         if not current_product:
#               raise HTTPException(
#             status_code=404)
#         product_reviews = await review_repo.get_objects_by_params(session, product_id=product_id, is_active=True)
#         return product_reviews
#     except ValueError as err: # если юзер шляпу отправил какую то
#         raise HTTPException(
#             status_code=400,
#             detail=str(err))
#     except Exception as err:
#                  raise HTTPException(
#             status_code=500, 
#             detail=str(err))  # общая ошибка на стороне сервера
                 

# @product_api_router.get('/category/{category_id}', response_model=List[ProductSchema])
# async def get_category_products(category_id : int = Path(ge=0),
#                                 session : AsyncSession = Depends(get_db_session),
#                              category_repo : CategoryRepository = Depends(get_category_repository)):
#     '''По id категории вывожит все вхоящие в нее продукты'''
#     try:
#         category_products = await category_repo.get_category_products_by_id(session, category_id)
#         return category_products
#     except ValueError as err:
#         raise HTTPException(
#             status_code=400,
#             detail=str(err))
#     except Exception as err:
#         raise HTTPException(
#         status_code=500,
#         detail=str(err))  




# @product_api_router.post('/', response_model=ProductSchema, status_code = 201)
# async def create_product(new_product_info:ProductCreateSchema = Depends(ProductCreateSchema.as_form),
#                          new_product_image : UploadFile | None = File(None),
#                          session : AsyncSession = Depends(get_db_session),
#                              product_repo : ProductRepository = Depends(get_product_repository),
#                              category_repo : CategoryRepository = Depends(get_category_repository),
#                              current_user: UserModel = Depends(get_current_seller)):
#         try:
#             existed_category = await category_repo.get_by_params(session , id=new_product_info.category_id, is_active = True)
#             if existed_category is None : # если категории нет или она неактивно
#                      raise HTTPException(status_code=400, detail="Category doesn't exist")
                 
#             # Сохранение изображения (если есть) Иначе None 
#             image_url = await save_product_image(file=new_product_image, media_root=MEDIA_ROOT) if new_product_image else None
#             # создание нового товара
#             new_product_validated_data = new_product_info.model_dump()
#             new_product_validated_data['seller_id'] = current_user.id
#             new_product_validated_data['image_url'] = image_url
#             new_product = await product_repo.create(session, new_product_validated_data) # проверка на существование самого продукта внутри метода репозитория
#             await session.commit()
#             await session.refresh(new_product)
#             return new_product
#         except Exception as err:
#                                      raise HTTPException(
#             status_code=500,
#             detail=str(err))
                                     
                                    
    
    
# @product_api_router.put('/{product_id}', response_model=ProductSchema)
# async def update_product(update_info : ProductCreateSchema = Depends(ProductCreateSchema.as_form),
#                         current_product_image : UploadFile | None = File(None),
#                         product_id : int = Path(ge=0),
#                          session : AsyncSession = Depends(get_db_session),
#                         product_repo : ProductRepository = Depends(get_product_repository),
#                         category_repo : CategoryRepository = Depends(get_category_repository),
#                         current_user: UserModel = Depends(get_current_seller)):
#         try:
#             current_product =   await product_repo.get_by_params(session, id=product_id, is_active=True)
#             if not current_product:
#                 raise HTTPException(status_code=400, detail=f"Product with id : {product_id} doesn't exist or inactive")
#             if current_product.seller_id != current_user.id:
#                 raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only update your own products")
#             category_is_active  = await category_repo.object_is_active(session , update_info.category_id)
#             if not category_is_active:
#                      raise HTTPException(status_code=400, detail=f"Category with id {update_info.category_id} doesn't exist or inactive")
#             current_product_updated_info = update_info.model_dump()
#             if current_product_image:# если юзер захотел фотку изменить
#                 remove_product_image(media_root=MEDIA_ROOT, file_url = current_product.image_url)# удаляем старую фотку
#                 current_product_image_url = await save_product_image(file=current_product_image, media_root=MEDIA_ROOT) # записываем новую
#                 current_product_updated_info['image_url'] = current_product_image_url# добавляем путь до новой фотки в инфу для обновления товара
#             updated_product = await product_repo.update_put(session,current_product.id, current_product_updated_info)
            
#             await session.commit()
#             await session.refresh(updated_product)
#             return updated_product
#         except Exception as err:
#                     raise HTTPException(
#             status_code=500,
#             detail=str(err))  




# @product_api_router.delete('/{product_id}',  status_code=status.HTTP_200_OK)
# async def delete_product(product_id : int = Path(ge=0),
#                         session : AsyncSession = Depends(get_db_session),
#                         repo : ProductRepository = Depends(get_product_repository),
#                         current_user: UserModel = Depends(get_current_seller)):
#     try:
#         current_product = await repo.get_by_params(session, id=product_id, is_active=True)
#         current_product_url = current_product.image_url # для удаления фотки товара
#         if not current_product:
#             raise HTTPException(status_code=400, detail=f"Product with id : {product_id} doesn't exist or inactive")
#         if current_product.seller_id != current_user.id:
#             raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only delete your own products")
#         # deleted_product = await repo.soft_deleting_by_id(session, product_id)
#         deleted_product = await repo.update_put(session, product_id, {'is_active' : False, 'image_url' : 'None'})
#         # при удалении(даже мягком) удаляем фотку товара хранящуюся в папке media в проекте
#         remove_product_image(media_root=MEDIA_ROOT, file_url =current_product_url)  # удаляем также ссылку на фотку в папке проекта
#         await session.commit()
#         await session.refresh(deleted_product)

        
#         return {'message' : f"продукт с id {product_id} стал неактивен"}
#     except Exception as err:
#                          raise HTTPException(
#             status_code=500,
#             detail=str(err))  