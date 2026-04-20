from core.logging.logging_conf import setup_logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
setup_logging()
from loguru import logger
# # кофнигурация БД
from backend.core.db.database import engine

# # роутеры
# # для подгрузки стетических файлов
# from fastapi.staticfiles import StaticFiles
# from starlette.middleware.sessions import SessionMiddleware
# from fastapi.middleware.cors import CORSMiddleware
# логирование модулей проекта по уровням


@asynccontextmanager
async def lifespan(app:FastAPI):# не забыть передать в параметры наш app
    logger.warning("Начало работы приложения")
    yield
    logger.warning("🛑 Конец работы приложения") # почему то от уровня warning и выше выводится инфа в треминал, а уровень info не выводится
 
    await engine.dispose()

app = FastAPI(title='Интернет магазин', lifespan=lifespan)
