from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from fastapi.staticfiles import StaticFiles
# логер
from backend.core.logging.logging_conf import project_logger
# кофнигурация и  БД
from backend.core.db.database import engine
from backend.core.config import project_settings
# роутеры(доделать модуль orders и все орутеры сервисы, репо к немк)
from backend.modules.products.router import product_api_router
from backend.modules.categories.router import category_api_router
from backend.modules.users.router import user_api_router
from backend.modules.carts.router import cart_api_router
# Мидлвари
from backend.core.middlewares.base_middleware import setup_cors
#

# # для подгрузки стетических файлов
# from fastapi.staticfiles import StaticFiles
# from starlette.middleware.sessions import SessionMiddleware
# from fastapi.middleware.cors import CORSMiddleware
# логирование модулей проекта по уровням


@asynccontextmanager
async def lifespan(app:FastAPI):# не забыть передать в параметры нашего app саму функцию
    project_logger.warning({'event' : 'Запуск работы сервера'})
    yield
    project_logger.warning({'event' : 'Запуск работы сервера'}) # почему то от уровня warning и выше выводится инфа в треминал, а уровень info не выводится
 
    await engine.dispose()
    
#основное прилжение
app = FastAPI(title=project_settings.APP_NAME, lifespan=lifespan)
# Настройка middleware
setup_cors(app)
# путь до медиа и статик файлов
app.mount("/media", StaticFiles(directory=project_settings.STATIC_DIR), name="static")

#включаем роутеры
app.include_router(product_api_router)
app.include_router(category_api_router)
app.include_router(user_api_router)
app.include_router(cart_api_router)


@app.get('/')
async def greetings():
    return {'message' : 'Добро пожаловать в наш магазин'}

@app.get('/health')
async def health_check():
    """Метод для проверки работы сервера"""
    return {'status': 'ok', 'message': 'Server is running'}