# repositories/cart_repository.py
from typing import List, Optional
from fastapi import HTTPException

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from backend.core.repo.base_repo import BaseRepository
from backend.modules.carts.models import CartModel, CartItemModel

class CartRepository(BaseRepository):

    
    def __init__(self, cart_db_model : CartModel):
                super().__init__(cart_db_model)

    async def get_by_user_id(self, session:AsyncSession, user_id: int) -> Optional[CartModel]:
        '''вернет неразвернутый объекь корзины юзера'''
        stmt = select(self.model).where(self.model.user_id == user_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def clear_cart(self, session:AsyncSession, cart_id: int) -> None:
        # Удаляем все позиции корзины
            stmt = delete(CartItemModel).where(CartItemModel.cart_id == cart_id)
            await session.execute(stmt)
            
    async def get_cart_with_items(self, user_id: int) -> CartModel | None:
        '''по Id юзера дает развернутый ответ по корзине юзера'''
        # stmt = (
        #     select(CartModel)
        #     .where(CartModel.user_id == user_id)
        #     .options(selectinload(CartModel.items))  # ← загружаем все CartItem
        # )
        # развернутая инфа о проуктах в позициях корзины
        stmt = (
            select(CartModel)
            .where(CartModel.user_id == user_id)
            .options(selectinload(CartModel.items).selectinload(CartItemModel.product))
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
    
    
    
    def __init__(self, cart_item_db_model : CartItemModel):
                super().__init__(cart_item_db_model)

    
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
            raise ValueError(f'ошибка при удалении позиции из корзины : {err}')
    
