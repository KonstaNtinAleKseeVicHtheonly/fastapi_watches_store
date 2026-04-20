# app/models.py
from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Integer, Float, ForeignKey, Text, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.core.db.database import Base


class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class OrderModel(Base):
    '''Общий заказ юзера с статусом датой создания'''
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    status: Mapped[OrderStatus] = mapped_column(String(20), default=OrderStatus.PENDING)
    total_amount: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Данные для доставки (денормализовано)
    shipping_address: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    contact_phone: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)

    # Отношения
    user: Mapped["UserModel"] = relationship("UserModel", back_populates="orders")
    items: Mapped[List["OrderItemModel"]] = relationship("OrderItemModel", back_populates="order", cascade="all, delete-orphan")

class OrderItemModel(Base):
    '''детальная позиция товара в заказе '''
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price_at_order: Mapped[float] = mapped_column(Float, nullable=False)  # цена на момент заказа
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)  # цена на момент заказа) # ценка за одну ед. товара на момент формирования заказа(для статистики)

    # Отношения
    order: Mapped["OrderModel"] = relationship("OrderModel", back_populates="items")
    product: Mapped["ProductModel"] = relationship("ProductModel", back_populates="order_items")