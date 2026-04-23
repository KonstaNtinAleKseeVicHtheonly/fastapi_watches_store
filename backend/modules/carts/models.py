from datetime import datetime

from sqlalchemy import Boolean, DateTime, Index, Numeric, String, Integer, Float, ForeignKey, Text, text, Computed
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from backend.core.db.database import Base

class CartModel(Base):
    '''Общая корзина юзера - создается один раз для юзера при регистрации'''
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Отношения
    user: Mapped["UserModel"] = relationship("UserModel", back_populates="cart")
    items: Mapped[List["CartItemModel"]] = relationship("CartItemModel", back_populates="cart", cascade="all, delete-orphan")

class CartItemModel(Base):
    '''текущая позиция с товаром в корзине юзера с количеством и ценой'''
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    price: Mapped[float] = mapped_column(Float, nullable=False)  # ← цена на момент добавления

    # Отношения
    cart: Mapped["CartModel"] = relationship("CartModel", back_populates="items")
    product: Mapped["ProductModel"] = relationship("ProductModel", back_populates="cart_items")
    
    @property
    def subtotal(self) -> float:
        """Сумма по позиции"""
        return self.price * self.quantity