# app/models.py
from sqlalchemy import String, Integer, Float, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from typing import Optional, List
from backend.core.db.database import Base
from slugify import slugify



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

    @validates('name')
    def generate_slug(self, key, value):
        if value:
            self.slug = slugify(value)
        return value
    def __repr__(self):
        return f"PRoduct : id{self.id} | name {self.name}, price {self.price}, brand {self.brand}, at stock {self.stock}"



