from sqlalchemy import Boolean, Index, Numeric, String, Integer, Float, ForeignKey, Text, text, Computed
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from typing import Optional, List
from backend.core.db.database import Base
from sqlalchemy.dialects.postgresql import TSVECTOR
#модели с других модулеуй
from backend.modules.orders.models import OrderItemModel
#
from slugify import slugify

class ProductModel(Base):
    __tablename__ = "products"
    
    # Создаем индекс для ускорения поиска
    __table_args__ = (
        Index('idx_watch_models_tsv', 'tsv', postgresql_using='gin'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    slug: Mapped[str] = mapped_column(String(220), unique=True, index=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    brand : Mapped[Optional[str]] = mapped_column(String(40), nullable=True)
    sex : Mapped[str] = mapped_column(String(40), default='male', server_default='male') 
    # Внешний ключ категории
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete='SET NULL'), index=True, nullable=False)
    
    # Характеристики часов
    material_case: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)   # материал корпуса (сталь, титан, керамика)
    battery_type: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)    # тип батарейки (CR2032, SR626SW и т.д.) – актуально для кварцевых
    movement_type: Mapped[str] = mapped_column(String(20), nullable=False)            # 'quartz' или 'mechanical'
    water_resistance: Mapped[Optional[str]] = mapped_column(String(30), nullable=True) # водозащита (30m, 50m, 100m)
    glass_type: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)       # стекло (минеральное, сапфировое)
    dial_color : Mapped[Optional[str]] = mapped_column(String(30), nullable=True) 
    # параметры в магазине
    image_url: Mapped[str | None] = mapped_column(String(200), nullable=True)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    rating: Mapped[float] = mapped_column(
        Numeric(2, 1),          
        nullable=False,
        server_default=text('0.0'),
        default=0.0)
    
    # Отношения
    category: Mapped["CategoryModel"] = relationship("CategoryModel", back_populates="products")
    cart_items: Mapped[List["CartItemModel"]] = relationship("CartItemModel", back_populates="product")
    order_items: Mapped[List["OrderItemModel"]] = relationship("OrderItemModel", back_populates="product")
    
    # Полнотекстовый индекс
    tsv: Mapped[TSVECTOR] = mapped_column(
        TSVECTOR,
        Computed(
            """
            setweight(to_tsvector('russian', coalesce(name, '')), 'A') ||
            setweight(to_tsvector('english', coalesce(name, '')), 'A') ||
            setweight(to_tsvector('russian', coalesce(description, '')), 'B') ||
            setweight(to_tsvector('english', coalesce(description, '')), 'B')
            """,
            persisted=True
        ),
        nullable=False
    )
    
    @validates('name')
    def generate_slug(self, key, value):
        if value:
            self.slug = slugify(value)
        return value
    def __repr__(self):
        return f"PRoduct : id{self.id} | name {self.name}, price {self.price}, brand {self.brand}, at stock {self.stock}"