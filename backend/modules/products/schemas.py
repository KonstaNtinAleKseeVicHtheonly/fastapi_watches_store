from pydantic import BaseModel, Field, ConfigDict, field_validator
from datetime import datetime
from typing import Optional
from backend.modules.categories.schemas import CategoryResponseSchema



class ProductBaseSchema(BaseModel):
    '''базовая схема с общей инфой о товаре'''
    name: str = Field(..., min_length=5, max_length=200,
                            description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., gt=0,
                            description="Product price(must be greater than 0")
    brand: Optional[str] = Field(None, description="Product brand")
    sex: str = Field(default='male', description="Product gender preferences (male/female/unisex)")
    category_id: int = Field(..., description='Category ID')
    material_case: Optional[str] = Field(None, description='material of case')   # материал корпуса (сталь, титан, керамика)
    battery_type: Optional[str] = Field(None, description='type of battery')    # тип батарейки (CR2032, SR626SW и т.д.) – актуально для кварцевых
    movement_type: str = Field(..., description='quartz|mechanical')            # 'quartz' или 'mechanical'
    water_resistance: Optional[str] = Field(None, description='30m, 50m...')  # водозащита (30m, 50m, 100m)
    glass_type: Optional[str] = Field(None, description='mineral|saphire')       # стекло (минеральное, сапфировое)
    dial_color : Optional[str] = Field(None, description='color as orange, red ...') 
    image_url: Optional[str] = Field(None, description='Product image URL')
    stock: int = Field(...,ge=1, description='product number at store')
    rating: Optional[float] = Field(default=0.0, ge=0, le=5)
    
    field_validator('movement_type')
    @classmethod
    def validate_movement_type(cls, v: str) -> str:
        allowed = ['quartz', 'mechanical']
        if v.lower() not in allowed:
            raise ValueError(f'Movement type must be one of: {allowed}')
        return v.lower()
    
    @field_validator('sex')
    @classmethod
    def validate_sex(cls, v: str) -> str:
        allowed = ['male', 'female', 'unisex']
        if v.lower() not in allowed:
            raise ValueError(f'Sex must be one of: {allowed}')
        return v.lower()
    
class ProductCreateSchema(ProductBaseSchema):
    pass

class ProductUpdateSchema(ProductBaseSchema):
    pass

class ProductPatchSchema(BaseModel):
    """Схема для частичного обновления товара (PATCH)"""
    name: Optional[str] = Field(None, min_length=5, max_length=200, description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: Optional[float] = Field(None, gt=0, description="Product price")
    brand: Optional[str] = Field(None, description="Product brand")
    sex: str = Field(default='male', description="Product gender preferences (male/female/unisex)")
    category_id: Optional[int] = Field(None, gt=0, description='Category ID')
    material_case: Optional[str] = Field(None, description='material of case')
    battery_type: Optional[str] = Field(None, description='type of battery')
    movement_type: Optional[str] = Field(None, description='quartz|mechanical')
    water_resistance: Optional[str] = Field(None, description='30m, 50m...')
    glass_type: Optional[str] = Field(None, description='mineral|sapphire')
    dial_color: Optional[str] = Field(None, description='color as orange, red ...')
    image_url: Optional[str] = Field(None, description='Product image URL')
    stock: Optional[int] = Field(None, ge=1, description='product number at store')
    rating: Optional[float] = Field(None, ge=0, le=5, description='Product rating')
    
    field_validator('movement_type')
    @classmethod
    def validate_movement_type(cls, v: str) -> str:
        allowed = ['quartz', 'mechanical']
        if v.lower() not in allowed:
            raise ValueError(f'Movement type must be one of: {allowed}')
        return v.lower()
    
    @field_validator('sex')
    @classmethod
    def validate_sex(cls, v: str) -> str:
        allowed = ['male', 'female', 'unisex']
        if v.lower() not in allowed:
            raise ValueError(f'Sex must be one of: {allowed}')
        return v.lower()


class ProductResponseSchema(ProductBaseSchema):
    id: int = Field(..., description="Unique product ID")
    slug: str = Field(min_length=5, max_length=200, description="Product slug")
    is_active: bool
    category: CategoryResponseSchema = Field(..., description="Product category details")

    class Config:
        from_attributes = True

class ProductListResponseSchema(BaseModel):
    products: list[ProductResponseSchema]
    total: int = Field(..., description='Total number of products')
    page: int = Field(ge=1, description="Номер текущей страницы")
    page_size: int = Field(ge=1, description="Количество элементов на странице") # используется как лимит товаров на странице
    
    model_config = ConfigDict(from_attributes=True)
