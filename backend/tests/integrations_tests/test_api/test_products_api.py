import pytest
from httpx import AsyncClient
from backend.modules.products.models import ProductModel


# ===== ФИКСТУРЫ (только для этого файла) =====
@pytest.mark.asyncio
async def test_product(db_session, test_category):
    """Создает тестовый продукт (общий для многих тестов)"""
    product = ProductModel(
        name="Test Product",
        slug="test-product",
        price=100.0,
        category_id=test_category.id,
        stock=10,
        movement_type="mechanical"
    )
    db_session.add(product)
    await db_session.commit()
    await db_session.refresh(product)
    return product


# ===== ТЕСТЫ =====
@pytest.mark.asyncio
async def test_get_all_products(client: AsyncClient, test_product):# test_product Нун в параметрах даже если не используется
    """GET /products - список продуктов"""
    response = await client.get("/api/products")
    assert response.status_code == 200
    assert len(response.json()["items"]) == 1


@pytest.mark.asyncio
async def test_get_product_by_id(client: AsyncClient, test_product):
    """GET /products/{id} - успешное получение"""
    response = await client.get(f"/api/products/{test_product.id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"



@pytest.mark.asyncio
async def test_get_product_not_found(client: AsyncClient):
    """GET /products/{id} - продукт не найден"""
    response = await client.get("/api/products/99999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_create_product(client: AsyncClient, test_category, auth_headers):
    """POST /products - создание продукта"""
    product_data = {
        "name": "New Product",
        "price": 200.0,
        "category_id": test_category.id,
        "stock": 3,
        "movement_type": "mechanical"
    }
    
    response = await client.post(
        "/api/products",
        json=product_data,
        headers=auth_headers
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == product_data["name"]
    assert data["price"] == product_data["price"]
    
@pytest.mark.asyncio
async def test_delete_product_by_id(client: AsyncClient, db_session, test_product):
    """Тест успешного мягкого удаления продукта по ID"""
    
    response = await client.delete(f"/api/products/{test_product.id}")
    
    assert response.status_code == 200
    
    #  Проверяем, что продукт стал неактивным
    from backend.modules.products.models import ProductModel
    
    deleted_product = await db_session.get(ProductModel, test_product.id)
    assert deleted_product.id == test_product.id  # запись осталась
    assert not deleted_product.is_active # мягкое удаление
    