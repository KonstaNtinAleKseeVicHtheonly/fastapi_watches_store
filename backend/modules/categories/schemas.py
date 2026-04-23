from pydantic import BaseModel, Field, ConfigDict, field_validator
from datetime import datetime
from typing import Optional



class CategoryBaseSchema(BaseModel):
    '''базовая схема с общей инфой о товаре'''
    
    name : str = Field(min_length=1, max_length=50, description='НАзвание категории')
    parent_id : int | None = Field(default=None, description='Id родительской категории если есть')

    
    
class CategoryCreateSchema(CategoryBaseSchema):
    pass

class CategoryUpdateSchema(CategoryBaseSchema):
    pass

class CategoryPatchSchema(BaseModel):
    name : Optional[str] = Field(min_length=1, max_length=50, description='НАзвание категории', default=None)
    parent_id : Optional[int] = Field(default=None, description='Id родительской категории если есть')



class CategoryResponseSchema(CategoryBaseSchema):
    
    id: int = Field(..., description="Unique category ID")
    slug: str = Field(min_length=5, max_length=200, description="Category slug")

    class Config:
        from_attributes = True
