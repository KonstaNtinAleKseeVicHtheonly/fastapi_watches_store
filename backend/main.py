from backend.core.logging.logging_conf import setup_logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
setup_logging()
from loguru import logger
# # кофнигурация и  БД
from backend.core.db.database import engine
from backend.core.config import project_settings
# роутеры(доделать модуль orders и все орутеры сервисы, репо к немк)
from backend.modules.products.router import product_api_router
from backend.modules.categories.router import category_api_router
from backend.modules.users.router import user_api_router
from backend.modules.carts.router import cart_api_router

# # для подгрузки стетических файлов
# from fastapi.staticfiles import StaticFiles
# from starlette.middleware.sessions import SessionMiddleware
# from fastapi.middleware.cors import CORSMiddleware
# логирование модулей проекта по уровням


@asynccontextmanager
async def lifespan(app:FastAPI):# не забыть передать в параметры нашего app саму функцию
    logger.warning("Начало работы приложения")
    yield
    logger.warning("🛑 Конец работы приложения") # почему то от уровня warning и выше выводится инфа в треминал, а уровень info не выводится
 
    await engine.dispose()
#основное прилжение
app = FastAPI(title='Интернет магазин', lifespan=lifespan)
#включаем роутеры
app.include_router(product_api_router)
app.include_router(category_api_router)
app.include_router(user_api_router)
app.include_router(cart_api_router)


