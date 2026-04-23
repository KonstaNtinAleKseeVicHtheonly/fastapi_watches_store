from pydantic import BaseModel, Field, ConfigDict, field_validator, model_serializer, model_validator
from datetime import datetime
from typing import List, Optional
from backend.modules.products.schemas import ProductResponseSchema

from sqlalchemy import Float, Integer
from sqlalchemy.orm import Mapped
        
class CartItemBaseSchema(BaseModel):
    product_id: int = Field(..., gt=0, description="Product ID to add to cart")
    quantity: Mapped[int] = Field(Integer, nullable=False, default=1)
    
class CartItemCreateSchema(CartItemBaseSchema):
    ...
    
class CartItemResponseSchema(BaseModel):
    """Ответ с позицией корзины"""
    cart_id: int
    quantity: Mapped[int] = Field(Integer, nullable=False, default=1, description='количество товара в корзине')
    product: Optional["ProductResponseSchema"] = None  # вложенный продукт
    price : float = Field(Float, gt=0.0, description='цена товара на момент добавления в корзину')
    
    model_config = ConfigDict(from_attributes=True)
    
    @model_validator(mode='after')
    def calculate_subtotal(self):
        self.subtotal = self.price * self.quantity
        return self
    
class CartItemUpdateSchema(CartItemBaseSchema):
    ...
    
class CartItemPatchSchema(BaseModel):
    quantity: int = Field(..., ge=0, le=99, description="New quantity")
    

class CartBaseSchema(BaseModel):
    """Базовая схема корзины"""
    pass  # корзина не имеет отдельных полей для создания
    
class CartResponseSchema(BaseModel):
    """Ответ с корзиной (список позиций)"""
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    items: List[CartItemResponseSchema] = Field(default_factory=list, description="Cart items")
    
    @property
    def total_items(self) -> int:
        return sum(item.quantity for item in self.items)
    
    @property
    def total_price(self) -> float:
        return sum(item.price * item.quantity for item in self.items)
    
    @model_serializer
    def serialize_model(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'items': [item.model_dump() for item in self.items],
            'total_items': self.total_items,
            'total_price': self.total_price
        }
    model_config = ConfigDict(from_attributes=True)    
    
# Для добавления товара в корзину (request body)
class AddToCartRequestSchema(BaseModel):
    """Запрос на добавление товара в корзину"""
    product_id: int = Field(..., gt=0, description="Product ID")
    quantity: int = Field(default=1, ge=1, le=99, description="Quantity")

# Для обновления количества товара
class UpdateCartItemRequestSchema(BaseModel):
    """Запрос на обновление количества товара в корзине"""
    quantity: int = Field(..., ge=0, le=99, description="New quantity (0 to remove)")
