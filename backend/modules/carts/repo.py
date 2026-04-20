# repositories/cart_repository.py
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.core.repo.base_repo import BaseRepository
from backend.modules.carts.models import CartModel, CartItemModel

class CartRepository(BaseRepository):
    
    

                
    async def get_or_create_cart(self, user_id: int) -> CartModel:
        """Получить корзину пользователя или создать новую"""
        stmt = select(CartModel).where(CartModel.user_id == user_id)
        result = await self.session.execute(stmt)
        cart = result.scalar_one_or_none()
        
        if not cart:
            cart = CartModel(user_id=user_id)
            self.session.add(cart)
            await self.session.flush()
        
        return cart
    
    async def get_cart_item(self, cart_id: int, product_id: int) -> CartItemModel | None:
        """Найти позицию товара в корзине"""
        stmt = select(CartItemModel).where(
            CartItemModel.cart_id == cart_id,
            CartItemModel.product_id == product_id
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def add_or_update_cart_item(self, cart_id: int, product_id: int, quantity: int) -> CartItemModel:
        """Добавить или обновить позицию в корзине"""
        existing = await self.get_cart_item(cart_id, product_id)
        
        if existing:
            existing.quantity += quantity
            item = existing
        else:
            item = CartItemModel(
                cart_id=cart_id,
                product_id=product_id,
                quantity=quantity
            )
            self.session.add(item)
        
        await self.session.flush()
        return item
    
    async def remove_cart_item(self, cart_id: int, product_id: int) -> bool:
        """Удалить позицию из корзины"""
        item = await self.get_cart_item(cart_id, product_id)
        if item:
            await self.session.delete(item)
            await self.session.flush()
            return True
        return False
    
    async def clear_cart(self, cart_id: int):
        """Очистить всю корзину"""
        stmt = select(CartItemModel).where(CartItemModel.cart_id == cart_id)
        result = await self.session.execute(stmt)
        items = result.scalars().all()
        
        for item in items:
            await self.session.delete(item)
        
        await self.session.flush()