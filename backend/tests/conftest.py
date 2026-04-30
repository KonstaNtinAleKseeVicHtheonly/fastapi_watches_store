# tests/conftest.py
from typing import AsyncGenerator

from httpx import AsyncClient
import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.core.db.database import Base
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
#
from backend.core.config import project_settings
from backend.core.dependencies import get_db_session
#
import asyncio

# Тестовая БД (отдельная БД для тестов)
TEST_DATABASE_URL = project_settings.DATABASE_URL + "_test"
test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestingAsyncSessionLocal = async_sessionmaker(test_engine, expire_on_commit=False, class_=AsyncSession)


@pytest.fixture(scope="session")
def event_loop():
    """Создает event loop для всей сессии тестов"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


async def create_test_database():
    """Создает тестовую БД и таблицы"""
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_test_database():
    """Удаляет тестовую БД и таблицы"""
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await test_engine.dispose()


@pytest.fixture(scope="session")
async def setup_test_database():
    """Настройка тестовой БД (один раз на сессию)"""
    await create_test_database()
    yield
    await drop_test_database()


@pytest.fixture
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """Фикстура сессии БД для каждого теста (откат в конце)"""
    
    # Создаём новую сессию
    async with TestingAsyncSessionLocal() as session:
        # Начинаем транзакцию
        async with session.begin():
            # Подменяем зависимость
            async def override_get_db():
                yield session
            
            app.dependency_overrides[get_db_session] = override_get_db
            
            yield session
            
            # После теста откатываем
            await session.rollback()
        
        app.dependency_overrides.clear()


@pytest.fixture
async def client(db_session) -> AsyncGenerator[AsyncClient, None]:
    """Фикстура HTTP клиента (асинхронный)"""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture
async def test_category(db_session):
    """Создает тестовую категорию"""
    from backend.modules.categories.models import CategoryModel
    
    category = CategoryModel(name="Test Category", slug="test-category")
    db_session.add(category)
    await db_session.commit()
    await db_session.refresh(category)
    return category


@pytest.fixture
async def auth_headers(test_user):
    """Возвращает заголовки с JWT токеном для авторизации"""
    # Логинимся и получаем токен
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/users/token",
            data={
                "username": test_user.email,
                "password": "testpass123"
            }
        )
        token = response.json()["access_token"]
    
    return {"Authorization": f"Bearer {token}"}


# @pytest.fixture
# async def test_product(db_session, test_category):
#     """Создает тестовый продукт"""
#     from backend.modules.products.models import ProductModel
    
#     product = ProductModel(
#         name="Test Product",
#         slug="test-product",
#         price=100.0,
#         category_id=test_category.id,
#         stock=10,
#         movement_type="mechanical"
#     )
#     db_session.add(product)
#     await db_session.commit()
#     await db_session.refresh(product)
#     return product

# @pytest.mark.asyncio
# async def test_get_product_by_id_manual_create(
#     client: AsyncClient, 
#     db_session, 
#     test_category
# ):
#     """Тест с ручным созданием продукта в тесте"""
#     from backend.modules.products.models import ProductModel
    
#     # Создаём продукт специально для этого теста
#     product = ProductModel(
#         name="Manual Test Product",
#         slug="manual-test-product",
#         price=150.0,
#         category_id=test_category.id,
#         stock=5,
#         movement_type="quartz"
#     )
#     db_session.add(product)
#     await db_session.commit()
#     await db_session.refresh(product)
    
#     # Тестируем эндпоинт
#     response = await client.get(f"/api/products/{product.id}")
    
#     assert response.status_code == 200
#     assert response.json()["name"] == "Manual Test Product"
#     assert response.json()["price"] == 150.0