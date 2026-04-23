
from typing import Any, Sequence
from sqlalchemy.ext.asyncio import  AsyncSession
from core.repo.base_repo import BaseRepository
from fastapi import HTTPException
from loguru import logger
from abc import ABC, abstractmethod


class BaseService(ABC):
  def __init__(self, main_repo:BaseRepository, db_session: AsyncSession):
    self.main_repo = main_repo
    self.session = db_session

async def get_object_by_id(self, object_id:int):
    current_object = await self.main_repo.get_by_id(self.session, object_id)
    if current_object is None:
            raise HTTPException(status_code=404, detail=f"Object {object_id} not found")    
    return current_object

async def get_object_by_params(self, **filters)->object|None:
        '''ищет строку в табице по заданным параметрам если не находит - вернет None'''
        if not filters:
            logger.info("пожалуйста введите значения при поиске по параметрам")
            return False
        current_object = await self.main_repo.get_by_params(self.session, **filters)
        if current_object is None:
            raise HTTPException(status_code=404, detail=f"Object with params  {filters} not found")    
        return current_object
    
async def get_objectS_by_params(self, **params):
        if not params:
            return None
        current_objects = await self.main_repo.get_objects_by_params(self.session, **params)
        return current_objects

async def object_is_active(self, object_id:int)->bool:
        '''Если у объекта статус активен вернет True Иначе вернет False'''

        current_object = await self.get_object_by_id(object_id)

        return current_object.is_active
            
async def get_all_objects(self, skip: int = 0, limit: int = 100) -> Sequence[object]:  
    all_objects = await self.main_repo.get_all(skip=skip, limit=limit)
    return all_objects

async def create_object(self, new_object_data:dict) -> object | None:
    existing_object = await self.main_repo.get_by_params(new_object_data)
    if existing_object:
      raise ValueError(f"объекта с параметрами : {new_object_data}  уже существует")
    new_object = await self.main_repo.create(self.session, new_object_data)
    await self.session.commit()
    return new_object

async def delete_object_softly(self, object_id:int):
    current_object = await self.get_object_by_id(object_id)
    result = await self.basse_repo.soft_deleting_by_id(self.session, object_id)
    await self.session.commit()
    return result
    
async def delete_object_hard(self, object_id:int):
    current_object = await self.get_object_by_id(object_id)
    result = await self.basse_repo.delete_by_id(self.session, object_id)
    await self.session.commit()
    return result
    
async def update_put(self, session: AsyncSession,  object_id:int ,update_data: dict[str, Any]):
    '''по методу put полностью обновляем строку'''
    logger.info(f"НАчало put обновления строки с id {object_id} у модели {self.model.__name__}")
    updated_obj = await self.get_object_by_id(session, object_id)
    updated_result = await self.main_repo(self.session, object_id, update_data)
    # # Объект тот же самый, ID тот же # не нужно т.к объект до этого добалвне в сессию и его изменения
    # session.add(updated_obj)
    await self.session.commit()
    return updated_result