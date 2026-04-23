# repositories/cart_repository.py
from typing import List, Optional
from fastapi import HTTPException

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from backend.core.repo.base_repo import BaseRepository
from backend.modules.carts.models import CartModel, CartItemModel

class CartRepository(BaseRepository):

    async def get_by_user_id(self, user_id: int) -> Optional[CartModel]:
        stmt = select(self.model).where(self.model.user_id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def clear_cart(self, cart_id: int) -> None:
        # Удаляем все позиции корзины
            stmt = delete(CartItemModel).where(CartItemModel.cart_id == cart_id)
            await self.session.execute(stmt)
    
    async def get_cart_with_items(self, cart_id: int) -> Optional[CartModel]:
        stmt = select(self.model).where(
            self.model.id == cart_id
        ).options(
            selectinload(self.model.items).selectinload(CartItemModel.product)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_or_create_cart(self, session: AsyncSession, user_id:int):
        stmt = select(self.model).where(self.model.user_id == user_id)
        current_cart = await session.execute(stmt)
        result = current_cart.scalar_one_or_none()
        if  result:
            return result
        new_cart = await self.create(session, {'user_id':user_id})
        await session.flush() 
        return new_cart
    

        
    
    
class CartItemRepository(BaseRepository):
    # шляпа для макет функциоанл не проверен
    async def get_by_cart_and_product(self, cart_id: int, product_id: int) -> Optional[CartItemModel]:
        stmt = select(self.model).where(
            self.model.cart_id == cart_id,
            self.model.product_id == product_id
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    # async def get_all_by_cart(self, session: AsyncSession, cart_id: int) -> List[CartItemModel]:
    #     stmt = select(self.model).where(
    #         self.model.cart_id == cart_id
    #     ).options(selectinload(self.model.product))
    #     result = await self.session.execute(stmt)
    #     return result.scalars().all()
    
    async def update_quantity(self, item_id: int, quantity: int) -> Optional[CartItemModel]:
        item = await self.get_by_id(item_id)
        if item:
            item.quantity = quantity
            return item
        return None
    async def remove_item(self, session:AsyncSession, current_item:CartItemModel)->bool:
        '''удалет сам объект что бы лишний а=запрос по Id в базу  не отправляьб'''
        try:
            await session.delete(current_item)
            return True
        except Exception as err:
            return False
    
