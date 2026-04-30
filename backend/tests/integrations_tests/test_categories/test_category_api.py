import pytest
from httpx import AsyncClient
from backend.modules.products.models import ProductModel




# ===== ТЕСТЫ =====
@pytest.mark.asyncio
async def test_get_all_categories(client: AsyncClient, test_category):
    response = await client.get("/api/categories")
    assert response.status_code == 200
    assert len(response.json()["items"]) == 1


@pytest.mark.asyncio
async def test_get_category_by_id(client: AsyncClient, test_category):
    """GET /products/{id} - успешное получение"""
    response = await client.get(f"/api/categories/{test_category.id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Category"



@pytest.mark.asyncio
async def test_get_category_not_found(client: AsyncClient):
    """указывает несущестующий id категории"""
    response = await client.get("/api/categories/999")
    assert response.status_code == 404


# @pytest.mark.asyncio
# async def test_delete_category_by_id(client: AsyncClient, test_category):
#     """указывает несущестующий id категории"""
#     response = await client.delete(f"/api/categories/{test_category.id}")
#     assert response.status_code == 200
#     assert response.json()["message"] == f"Категория  с id {test_category.id} стала неактивна"


    

    
@pytest.mark.asyncio
async def test_delete_category_by_id(client: AsyncClient, db_session, test_category):
    """Тест успешного мягкого удаления продукта по ID"""
    
    response = await client.delete(f"/api/categories/{test_category.id}")
    
    assert response.status_code == 200
    
    #  Проверяем, что продукт стал неактивным
    from backend.modules.categories.models import CategoryModel
    
    deleted_category = await db_session.get(CategoryModel, test_category.id)
    assert deleted_category.id == test_category.id  # запись осталась
    assert  not deleted_category.is_active  # мягкое удаление
