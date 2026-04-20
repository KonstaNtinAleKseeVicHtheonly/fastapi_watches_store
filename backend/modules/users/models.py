from datetime import datetime

from sqlalchemy import Boolean, DateTime, Index, Numeric, String, Integer, Float, ForeignKey, Text, text, Computed
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from backend.core.db.database import Base

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(200), nullable=False)
    full_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Отношения
    cart: Mapped["CartModel"] = relationship("CartModel", back_populates="user", uselist=False)  # one-to-one
    orders: Mapped[List["OrderModel"]] = relationship("OrderModel", back_populates="user")
