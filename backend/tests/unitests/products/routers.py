from fastapi.testclient import TestClient
from main import app
import unittest



class TestProductAPI(unittest.TestCase):


 def setUp(self):
  self.client = TestClient(app) # обернули приложение в TestClient объект что бы эмулировать запросы к эндпоинтам и для удобной работы с резульатами запросов
 
 
 def test_get_all_products(self):
    response = self.client.get("/api/products/")
    self.assertEqual(response.status_code, 200)
   #  self.assertEqual(response.json(), {"id": 1, "name": "Laptop", "price": 999.99})
    self.assertEqual(response.headers["content-type"], "application/json")
    
def test_get_current_product(self):
    response = self.client.get("/api/products/1")
    self.assertEqual(response.status_code, 200)
   #  self.assertEqual(response.json(), {"id": 1, "name": "Laptop", "price": 999.99})
    self.assertEqual(response.headers["content-type"], "application/json")


def test_get_item_not_found(self):
    response = self.client.get("/items/999")
    self.assertEqual(response.status_code, 404)
    self.assertEqual(response.json(), {"detail": "указанного id Нет в базе"})
    self.assertIn("application/json", response.headers["content-type"])
    
if __name__ == '__main__':
 unittest.main()