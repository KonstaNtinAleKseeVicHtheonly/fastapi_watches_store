# services/cart_service.py
from fastapi import HTTPException
from backend.modules.carts.repo import CartRepository
from backend.modules.products.repo import ProductRepository

class CartService:
    def __init__(self, cart_repo: CartRepository, product_repo: ProductRepository):
        self.cart_repo = cart_repo
        self.product_repo = product_repo
    
    async def add_to_cart(self, user_id: int, product_id: int, quantity: int):
        """Добавить товар в корзину"""
        # 1. Проверяем, существует ли товар
        product = await self.product_repo.get_by_id(product_id)
        if not product:
            raise HTTPException(404, "Product not found")
        
        if product.stock < quantity:
            raise HTTPException(400, "Not enough stock")
        
        # 2. Получаем или создаем корзину пользователя
        cart = await self.cart_repo.get_or_create_cart(user_id)
        
        # 3. Добавляем или обновляем позицию в корзине
        cart_item = await self.cart_repo.add_or_update_cart_item(
            cart_id=cart.id,
            product_id=product_id,
            quantity=quantity
        )
        
        return {
            "cart_id": cart.id,
            "item_id": cart_item.id,
            "product_id": product_id,
            "quantity": cart_item.quantity,
            "product_name": product.name,
            "price": product.price,
            "subtotal": product.price * cart_item.quantity
        }
    
    async def get_cart(self, user_id: int):
        """Получить корзину пользователя"""
        cart = await self.cart_repo.get_or_create_cart(user_id)
        
        # Загружаем все позиции с продуктами
        items = []
        for item in cart.items:
            items.append({
                "id": item.id,
                "product_id": item.product_id,
                "product_name": item.product.name,
                "price": item.product.price,
                "quantity": item.quantity,
                "subtotal": item.product.price * item.quantity
            })
        
        total = sum(item["subtotal"] for item in items)
        
        return {
            "cart_id": cart.id,
            "user_id": user_id,
            "items": items,
            "total": total
        }
    
    async def update_quantity(self, user_id: int, product_id: int, quantity: int):
        """Изменить количество товара в корзине"""
        if quantity < 0:
            raise HTTPException(400, "Quantity cannot be negative")
        
        cart = await self.cart_repo.get_or_create_cart(user_id)
        
        if quantity == 0:
            # Удаляем позицию
            await self.cart_repo.remove_cart_item(cart.id, product_id)
            return {"message": "Item removed"}
        else:
            # Обновляем количество
            item = await self.cart_repo.add_or_update_cart_item(cart.id, product_id, 0)
            item.quantity = quantity
            await self.cart_repo.session.flush()
            return {"message": "Quantity updated"}
    
    async def remove_item(self, user_id: int, product_id: int):
        """Удалить товар из корзины"""
        cart = await self.cart_repo.get_or_create_cart(user_id)
        await self.cart_repo.remove_cart_item(cart.id, product_id)
        return {"message": "Item removed"}
    
    async def clear_cart(self, user_id: int):
        """Очистить всю корзину"""
        cart = await self.cart_repo.get_or_create_cart(user_id)
        await self.cart_repo.clear_cart(cart.id)
        return {"message": "Cart cleared"}