# services/cart_service.py
from typing import Dict, Optional

from fastapi import HTTPException, status
from backend.modules.carts.repo import CartRepository
from backend.modules.carts.models import CartItemModel, CartModel
from backend.modules.carts.repo import CartRepository, CartItemRepository
from backend.modules.products.repo import ProductRepository
from backend.core.service.base_service import BaseService
from sqlalchemy.ext.asyncio import  AsyncSession

from backend.core.logging.logging_conf import project_logger
from backend.modules.carts.schemas import CartItemUpdateSchema

class CartService(BaseService):
    

        
    def __init__(self, main_cart_repo: CartRepository, cart_item_repository: CartItemRepository, product_repository:ProductRepository, db_session: AsyncSession):
        # Передаем основной репозиторий в BaseService
        super().__init__(main_cart_repo, db_session)
        # Добавляем дополнительный репозиторий
        self.cart_item_repository = cart_item_repository
        self.product_repository = product_repository
        
        

    
    async def get_user_cart_short(self, user_id:int)->CartModel|None:
        project_logger.info({'event' : 'Вывод общей корзины юзера',
                     'user_id' : user_id })
        
        current_user_cart = await self.main_repo.get_by_user_id(self.session, user_id= user_id)
        if not current_user_cart:
            return None
        return current_user_cart
    
    async def get_user_cart_detailed(self, user_id:int)->CartModel|None:
        '''развернутая инфа о корзине юзера с связьж=ю с продуктами'''
        
        current_user_cart = await self.main_repo.get_cart_with_items(self.session, user_id=user_id)
        if not current_user_cart:
            return None
        return current_user_cart
        
    async def check_user_cart(self, user_id:int)->CartModel|bool:
        '''проверяет сущесвтует ли общая корзина юзера'''
        current_user_cart = await self.get_user_cart_short(user_id=user_id)
        if not current_user_cart:
            return False
        return current_user_cart
    
    async def add_to_cart(self, user_id: int, product_id: int, quantity: int)->CartItemModel|HTTPException:
        """Добавить товар в корзину : принимаем Id товара и его количество """
        project_logger.info({'event' : 'добавление продукта в корзину',
                     'product_id' : product_id,
                     'quantity' : quantity})
        # 1. Проверяем, существует ли товар
        product = await self.product_repository.get_by_id(self.session, product_id)
        if not product:
            raise HTTPException(404, "Product not found")
        
        if product.stock < quantity:
            raise HTTPException(400, "Not enough stock")

        # 2. Получаем или создаем корзину пользователя 
        user_cart = await self.get_user_cart_short(user_id)
        project_logger.info({'event' : 'добавление продукта в корзину',
                     'step' : 'проверка наличия общей корзины юзера'})
        if not user_cart:
            project_logger.info({'event' : 'добавление продукта в корзину',
                     'step' : 'у юзера нет общей корзины, создаем ее'})
            user_cart = await self.main_repo.create(self.session,{'user_id':user_id})
            await self.session.flush()
        # 3. Добавляем или обновляем позицию в корзине
        existing_item = await self.cart_item_repository.get_by_params(self.session, 
                                                    cart_id = user_cart.id,
                                                    product_id = product_id)
        if existing_item:
            project_logger.warning({'event' : 'добавление продукта в корзину',
                         'case' : 'текущая позиция уже есть в корзине'})
            updated_item = await self.update_cart_item_quantity(user_id, existing_item.id, quantity)
            return updated_item
            #провери есть ли такая позиция в корзине
            # new_quantity = existing_item.quantity + quantity
            # if new_quantity > product.stock:
            #     raise HTTPException(400, "Total quantity exceeds stock")
            # updated_cart_item = await self.cart_item_repository.update_patch(self.session,
            #                                              find_by={'id':existing_item.id},
            #                                              update_data={'quantity':new_quantity})
            # await self.session.commit()
            # return updated_cart_item
        else:
            project_logger.info({'event' : 'добавление продукта в корзину',
                     'step' : 'товара еще не было в корзине, добвим его'})
            new_item_data = {'cart_id':user_cart.id,
                             'product_id' : product_id,
                             'quantity' : quantity,
                             'price' : product.price
                             }
            new_cart_item = await self.cart_item_repository.create(self.session, new_item_data)
            if new_cart_item:
                await self.session.commit()
                return new_cart_item
            project_logger.error({'event' : 'добавление продукта в корзину',
                     'step' : 'товара еще не было в корзине, добвим его',
                     'case' : 'ошибка при добавлении товара в корзину'})
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
    
    async def update_cart_item_via_session(self, 
                                           cart_data: Dict[int, int], 
                                           item: CartItemUpdateSchema) -> Dict[int, int]:
        '''cart_data - ключи это id итема в значение - его количества'''
        if item.product_id not in cart_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {item.product_id} not found in cart"
            )

        cart_data[item.product_id] = item.quantity
        return cart_data
    
    # метод с разнесенной лоигкой на обнволение текущей позиции
    async def update_cart_item_quantity(self, 
                                        user_id: int, 
                                        product_id: int, 
                                        quantity: int) -> str | HTTPException | CartItemModel:
            """Установить конкретное количество товара в корзине"""
            
            project_logger.info({'event' : 'обновление товара в корзине',
                         'item_id' : product_id,
                         'quantity' : quantity, 
                          'step' : 'прверка присутствия товара в корзине'})
            
            # 1. Проверяем наличие общей корзины
            user_cart = await self.get_user_cart_short(user_id)
            if not user_cart:
                project_logger.error({'event' : 'обновление товара в корзине',
                     'step' : 'прверка существования общей корзины',
                     'case' : 'ее не сущесвтует бля'})
                raise HTTPException(404, "У юзера еще нет общей корзины")
            # 2. Находим позицию, по Id общей корзины юзера из бщей корзины
            cart_item = await self.cart_item_repository.get_by_params(self.session, 
                                                                      cart_id=user_cart.id,
                                                                      product_id=product_id)
            if not cart_item:
                project_logger.error({'event' : 'обновление товара в корзине',
                     'step' : 'прверка присутствия товара в корзине',
                     'case' : f'такого товара в корзине нет по параметрам user_id: {user_cart.user_id}, product_id {product_id}'})
                raise HTTPException(404, "Cart item not found")

            # 3. Если количество 0 - удаляем
            if quantity <= 0:
                deleting_result = await self.cart_item_repository.remove_item(self.session, cart_item)
                if not deleting_result:
                        project_logger.error({'event' : 'обновление товара в корзине',
                        'step' : f'удаление позиции из корзины т.к quantity был указан {quantity}',
                        'case' : f'такого товара в корзине нет по параметрам user_id: {user_cart.user_id}, product_id {product_id}'})
                        raise HTTPException(500, "Deleting has failed, try again later")
                await self.session.commit()
                project_logger.info({'event' : 'обновление товара в корзине',
                          'step' : 'заданное количество меньше нуля - значит удалаяем позицию из корзины'})
                return "product was deleted"
            # 4. Проверяем наличие на складе
            product = await self.product_repository.get_by_id(self.session, cart_item.product_id)
            # если на складе менте чем юзер хочет добавить
            if quantity > product.stock:
                project_logger.error({'event' : 'обновление товара в корзине',
                          'step' : 'прверка присутствия товара на складе',
                          'case' : f'указанное юзером количество превышает количество товара на складе юзер указал {quantity}, на складе {product.stock}'})
                raise HTTPException(400, f"Max available: {product.stock}")
            # 5. Обновляем количество
            cart_item.quantity = quantity
            project_logger.info({'event' : 'обновление товара в корзине',
                          'step' : f'обновим количество товара в корзине на {quantity}'})
            await self.session.commit()
            
            return cart_item
        
    async def remove_item_from_cart(self, user_id: int, product_id: int)->str|HTTPException:
        """Удалить товар из корзины"""
        project_logger.info({'event' : 'Удаление товара из корзины',
                         'user_id' : user_id,
                         'product_id' : product_id})
        #ищем общую корзину юзера
        user_cart = await self.get_user_cart_short(user_id)
        if not user_cart:
            project_logger.error({'event' : 'Удаление товара из корзины',
                         'step' : 'проверка существования общей корзины юзера',
                         'case' : 'ее не сущесвтует'})
            raise HTTPException('у юзера еще нет общей корзины')
        project_logger.info({'event' : 'Удаление товара из корзины',
                         'step' : 'проверка существования данного item в корзине юзера',
                         'product_id' : product_id})
        current_item = await self.cart_item_repository.get_by_params(self.session,
                                                                     cart_id=user_cart.id,
                                                                     product_id=product_id)
        if not current_item:
            project_logger.error({'event' : 'Удаление товара из корзины',
                         'step' : 'проверка существования данного item в корзине юзера',
                         'case' : 'данной позиции нет в корзине юзера'})
            raise HTTPException(status_code=404, detail='такой позиции нет в корзине')
        
        removing_result = await self.cart_item_repository.remove_item(self.session, current_item)
        if removing_result:# в случае успешного удаления
            project_logger.info({'event' : 'Удаление товара из корзины',
                         'step' : 'удаление позиции из корзины завершено успешно'})
            return "product has been deleted from cart"
        else: # если ошибка при удалении была
            raise HTTPException(status_code=500, detail='Ошибка при удалении позиции из корзины на стороне сервера, повторите запрос позже')

    async def _clear_user_cart(self, user_id: int) -> bool|HTTPException:
            """Очистить всю корзину пользователя"""

            # Находим корзину
            user_cart = await self.get_user_cart_short(user_id)
            if not user_cart:
                    project_logger.error({'event' : 'Очистка корзины юзера от позиций',
                    'step' : 'проверка существования общей корзины юзера',
                    'case' : 'ее не сущесвтует'})
                    raise HTTPException(status_code=404, detail='Нет корзины у данного юзера что бы ее очистить')
            try:
                 await self.main_repo.clear_cart(self.session, user_cart.id)
            except Exception as err:
                project_logger.error({'event' : 'Очистка корзины юзера от позиций',
                    'step' : 'удаление позииций из корзины',
                    'case' : f'ошибка {err}'})
                await self.session.rollback()
                raise HTTPException(status_code=500, detail='Ошибка при очистке на стороне сервера, повторите запрос позже')
            else:
                project_logger.info({'event' : 'Очистка корзины юзера от позиций',
                         'step' : 'удаление позиции из корзины завершено успешно'})
                await self.session.commit()
                return True
                            
    async def get_cart_details(self, cart_data: Dict[int, int]):
        '''по id продуктов из cart_data вернет инфу о них
        Принимает на вход словарь с id продуктов и их количество'''
        if not cart_data:
            return []

        product_ids = list(cart_data.keys())
        products = await self.product_repository.get_multiple_by_ids(self.session, product_ids)
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
        return {'cart_items' : cart_items,
                'total_price' : total_price,
                'total_items' : total_items}