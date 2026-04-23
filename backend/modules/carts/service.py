# services/cart_service.py
from typing import Dict, Optional

from fastapi import HTTPException, status
from backend.modules.carts.repo import CartRepository
from backend.modules.carts.models import CartItemModel, CartModel
from backend.modules.carts.repo import CartRepository, CartItemRepository
from backend.modules.products.repo import ProductRepository
from backend.core.service.base_service import BaseService
from sqlalchemy.ext.asyncio import  AsyncSession

from backend.modules.carts.schemas import CartItemUpdateSchema

class CartService(BaseService):
    

        
    def __init__(self, main_cart_repo: CartRepository, cart_item_repository: CartItemRepository, product_repository:ProductRepository, db_session: AsyncSession):
        # Передаем основной репозиторий в BaseService
        super().__init__(main_cart_repo, db_session)
        # Добавляем дополнительный репозиторий
        self.cart_item_repository = cart_item_repository
        self.product_repository = product_repository
    
    async def get_user_cart(self, user_id:int):
        current_user_cart = await self.main_repo.get_by_params(self.session, user_id= user_id)
        return current_user_cart
    
    async def check_user_cart(self, user_id:int)->CartModel|bool:
        '''проверяет сущесвтует ли общая корзина юзера'''
        current_user_cart = await self.get_user_cart(user_id=user_id)
        if not current_user_cart:
            return False
        return current_user_cart
    
    async def add_to_cart(self, user_id: int, product_id: int, quantity: int):
        """Добавить товар в корзину : принимаем Id товара и его количество """
        # 1. Проверяем, существует ли товар
        product = await self.product_repository.get_by_id(product_id)
        if not product:
            raise HTTPException(404, "Product not found")
        
        if product.stock < quantity:
            raise HTTPException(400, "Not enough stock")

        # 2. Получаем или создаем корзину пользователя 
        user_cart = await self.get_user_cart(user_id)
        if not user_cart:
            user_cart = await self.main_repo.create(self.session,{'user_id':user_id})
            await self.session.flush()
        # 3. Добавляем или обновляем позицию в корзине
        existing_item = await self.cart_item_repository.get_by_params(self.session, 
                                                    {'cart_id':user_cart.id,'product_id':product_id})
        if existing_item:
            new_quantity = existing_item.quantity + quantity
            if new_quantity > product.stock:
                raise HTTPException(400, "Total quantity exceeds stock")
            updated_cart_item = await self.cart_item_repository.update_patch(self.session,
                                                         find_by={'id':existing_item.id},
                                                         update_data={'quantity':new_quantity})
            await self.session.commit()
            return updated_cart_item
        else:
            new_item_data = {'cart_id':user_cart.id,
                             'product_id' : product_id,
                             'quantity' : quantity,
                             'price' : product.price
                             }
            new_cart_item = await self.cart_item_repository.create(self.session, new_item_data)
            if new_cart_item:
                await self.session.commit()
                return new_cart_item
            raise HTTPException(status_code=404, detail='неверные данные')
    # async def add_to_cart_via_session(self, cart_data: Dict[int, int], item: CartItemCreate) -> Dict[int, int]:
    #     product = self.product_repository.get_by_id(item.product_id)
    #     if not product:
    #         raise HTTPException(
    #             status_code=status.HTTP_404_NOT_FOUND,
    #             detail=f'Product with id {item.product_id} not found'
    #         )

    #     if item.product_id in cart_data:
    #         cart_data[item.product_id] += item.quantity
    #     else:
    #         cart_data[item.product_id] = item.quantity

    #     return cart_data
    
    async def update_cart_item_via_session(self, cart_data: Dict[int, int], item: CartItemUpdateSchema) -> Dict[int, int]:
        '''cart_data - ключи это id итема в значение - его количества'''
        if item.product_id not in cart_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {item.product_id} not found in cart"
            )

        cart_data[item.product_id] = item.quantity
        return cart_data
    
    # метод с разнесенной лоигкой на обнволение текущей позиции
    async def update_cart_item_quantity(
    self, 
    user_id: int, 
    item_id: int, 
    quantity: int) -> Optional[CartItemModel]:
            """Установить конкретное количество товара в корзине"""
            
            # 1. Находим позицию
            cart_item = await self.cart_item_repository.get_by_id(self.session, item_id)
            if not cart_item:
                raise HTTPException(404, "Cart item not found")
            
            # 2. Проверяем соответстие корзины - юзеру
            cart = await self.main_repo.get_by_id(self.session, cart_item.cart_id)
            if not cart:
                raise HTTPException(404, "У юзера еще нет общей корзины")
            if cart.user_id != user_id:
                raise HTTPException(403, "Permission denied")
            
            # 3. Если количество 0 - удаляем
            if quantity <= 0:
                await self.cart_item_repository.delete(self.session, item_id)
                await self.session.commit()
                return None
            # 4. Проверяем наличие на складе
            product = await self.product_repository.get_by_id(cart_item.product_id)
            # если на складе менте чем юзер хочет добавить
            if quantity > product.stock:
                raise HTTPException(400, f"Max available: {product.stock}")
            
            # 5. Обновляем количество
            cart_item.quantity = quantity
            await self.session.commit()
            
            return cart_item
        
    async def remove_item(self, user_id: int, product_id: int):
        """Удалить товар из корзины"""
        user_cart = await self.get_user_cart(user_id)
        if not user_cart:
            raise HTTPException('у юзера еще нет общей корзины')
        current_item = await self.cart_item_repository.get_by_params(self.session,
                                                                     cart_id=user_cart.id,
                                                                     product_id=product_id)
        if not current_item:
            raise HTTPException(status_code=404, detail='такой позиции нет в корзине')
        
        removing_result = await self.cart_item_repository.remove_item(self.session, current_item)
        return removing_result
    
    
    
    async def clear_cart(self, user_id: int):
        """Очистить всю корзину"""
        cart = await self.main_repo.get_user_cart(user_id)
        if not cart:
            raise HTTPException('нет такой корзины')
        try:
            await self.main_repo.clear_cart(cart.id)
            return True
        except Exception:
            return False
        
        
    async def get_cart_details(self, cart_data: Dict[int, int]):
        '''по id продуктов из cart_data вернет инфу о них
        Принимает на вход словарь с id продуктов и их количество'''
        if not cart_data:
            return []

        product_ids = list(cart_data.keys())
        products = self.product_repository.get_multiple_by_ids(product_ids)
        # берем id продуктов из корзины
        products_dict = {product.id: product for product in products}

        cart_items = []
        total_price = 0.0
        total_items = 0

        for product_id, quantity in cart_data.items():
            if product_id in products_dict:
                product = products_dict[product_id]
                subtotal = product.price * quantity

                cart_item = CartItemModel(product_id=product.id, name=product.name,
                    price=product.price, quantity=quantity, subtotal=subtotal,
                    image_url=product.image_url)

                cart_items.append(cart_item)
                total_price += subtotal
                total_items += quantity

        return cart_items