from typing import List
from fastapi import APIRouter, Body, File, Path, Query, Depends, status, HTTPException, UploadFile
# схемы
from backend.modules.carts.schemas import CartResponseSchema, AddToCartRequestSchema, UpdateCartItemRequestSchema, \
 RemoveFromCartRequest
#сервсиы
from backend.modules.carts.service import CartService
#модели
from backend.modules.users.models import UserModel
#depends
from backend.modules.carts.dependencies import get_cart_service
from backend.core.security import get_verified_user







cart_api_router = APIRouter(prefix="/api/carts", tags=['carts'])



@cart_api_router.get('/', response_model=CartResponseSchema, status_code=status.HTTP_200_OK)
async def get_user_main_cart(
                             cart_service:CartService = Depends(get_cart_service),
                             current_user:UserModel = Depends(get_verified_user)):
    '''выводит корзину юзера со всеми позициями в ней'''
    try:
        
        user_cart_short = await cart_service.get_user_cart_short(current_user.id)
        return user_cart_short
    except Exception as err:
         raise HTTPException(
            status_code=500,
            detail=str(err))  # общая ошибка 

@cart_api_router.get('/detailed', response_model=CartResponseSchema, status_code=status.HTTP_200_OK)
async def get_user_main_cart_detailed_info(
                             cart_service:CartService = Depends(get_cart_service),
                             current_user:UserModel = Depends(get_verified_user)):
    '''выводит корзину юзера со всеми позициями в ней'''
    try:
        
        user_cart_detailed = await cart_service.get_user_cart_detailed(current_user.id)
        return user_cart_detailed
    except Exception as err:
         raise HTTPException(
            status_code=500,
            detail=str(err))  # общая ошибка 
         

         
@cart_api_router.post("/add", status_code=status.HTTP_200_OK)
async def add_product_to_cart(new_item_data: AddToCartRequestSchema,
                        cart_service:CartService = Depends(get_cart_service),
                        current_user:UserModel = Depends(get_verified_user)):
    # проверка на существование продукта, позиции в корзине и т.д уже в методе сервиса
    new_item_in_cart = await cart_service.add_to_cart(user_id=current_user.id,
                                                      product_id=new_item_data.product_id,
                                                      quantity=new_item_data.quantity)
    return new_item_in_cart



@cart_api_router.put("/update", status_code=status.HTTP_200_OK)
async def update_cart_item(updated_item_data: UpdateCartItemRequestSchema,
                        cart_service:CartService = Depends(get_cart_service),
                        current_user:UserModel = Depends(get_verified_user)):

    updated_cart_item = await cart_service.update_cart_item_quantity(user_id=current_user.id,
                                                                     item_id=updated_item_data.product_id,
                                                                     quantity=updated_item_data.quantity)
    return updated_cart_item

@cart_api_router.delete("/remove/{product_id}", status_code=status.HTTP_200_OK)
async def remove_item_from_cart(current_item_data: RemoveFromCartRequest,
                        cart_service:CartService = Depends(get_cart_service),
                        current_user:UserModel = Depends(get_verified_user)):
    # метд сервиса включает в себя проверку на существование корзины зера, позиции в ней, вернт либо ошибку либо инфу об успешном удалении
    item_deliting_result = await cart_service.remove_item_from_cart(user_id=current_user.id,
                                                                    product_id=current_item_data.product_id)

    return {"message": item_deliting_result}

@cart_api_router.delete("/clear_cart", status_code=status.HTTP_200_OK)
async def clear_user_cart(cart_service:CartService = Depends(get_cart_service),
                        current_user:UserModel = Depends(get_verified_user)):
    '''очищает всю корзину юзера от позиций'''
    # метд сервиса включает в себя проверку на существование корзины зера, позиции в ней, вернт либо ошибку либо инфу об успешном удалении
    item_deliting_result = await cart_service._clear_user_cart(user_id = current_user.id)
    if item_deliting_result:
         return {"message": "Cart cleared successfully", "success": True}