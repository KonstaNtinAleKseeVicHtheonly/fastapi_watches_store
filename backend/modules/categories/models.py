# app/models.py
from sqlalchemy import String, Integer, Float, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from backend.core.db.database import Base

class CategoryModel(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("categories.id"), nullable=True)
    
    # Отношения
    parent: Mapped[Optional["CategoryModel"]] = relationship("CategoryModel", remote_side='CategoryModel.id', back_populates="children")
    children: Mapped[List["CategoryModel"]] = relationship("CategoryModel", back_populates="parent")
    products: Mapped[List["ProductModel"]] = relationship("ProductModel", back_populates="category")




