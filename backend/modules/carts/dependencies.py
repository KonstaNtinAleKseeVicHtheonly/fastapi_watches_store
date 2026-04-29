from fastapi.params import Depends
from sqlalchemy.ext.asyncio import  AsyncSession
from backend.core.logging.logging_conf import project_logger
from typing import AsyncGenerator
from backend.modules.carts.repo import CartRepository, CartItemRepository
from backend.modules.products.repo import ProductRepository
from backend.modules.carts.service import CartService
from backend.modules.carts.models import CartModel, CartItemModel
from backend.core.dependencies import get_db_session
from backend.modules.products.dependencies import get_product_repository





def get_cart_repository():
     return CartRepository(CartModel)
 
def get_cart_item_repository():
    return CartItemRepository(CartItemModel)
 
def get_cart_service(session:AsyncSession = Depends(get_db_session), 
                        cart_repo : CartRepository=Depends(get_cart_repository),
                        cart_item_repo : CartItemRepository=Depends(get_cart_item_repository),
                        product_repo : ProductRepository=Depends(get_product_repository)):

        return CartService(main_cart_repo=cart_repo, cart_item_repository=cart_item_repo,product_repository=product_repo, db_session=session)
