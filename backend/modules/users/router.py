from fastapi import APIRouter, Body, Path, Query, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
# схемы
from backend.modules.users.schemas import RefreshTokenRequestSchema, UserResponseSchema, UserCreateSchema, UserPatchSchema, UserUpdateSchema
#сервисы
from backend.modules.users.service import UserService
#depends
from backend.modules.users.dependencies import get_user_service, get_verified_user
from backend.core.security import  hash_password
# jwt, авторизация аутентификация
import jwt
#конфигурация 
from backend.core.config import project_settings
#Модели
from backend.modules.users.models import UserModel
# from app.config import SECRET_KEY, ALGORITHM
# from fastapi.security import OAuth2PasswordRequestForm


user_api_router = APIRouter(prefix="/api/users", tags=['users'])


@user_api_router.get('/', response_model=UserResponseSchema)
async def get_user_info(current_user : UserModel = Depends(get_verified_user)):
    '''просто покажет юзеру инфу о нем  в БД'''
        
    return current_user

    
    
@user_api_router.get('/{user_id}', response_model=UserResponseSchema)
async def find_user_by_id(user_id:int = Path(ge=1),
                         current_user : UserModel = Depends(get_verified_user)
                         ):
    '''Доступно только для админов или юзеру владеющему данным id в БД
    выводит инфу о юзере по его id'''
    if current_user.id == user_id or (current_user.is_superuser and current_user.is_active):
        return current_user
    raise HTTPException(status_code=404, detail='вы ввели не свйо id либо не обладает достаточными полномочиями')

@user_api_router.post('/', response_model=UserResponseSchema,  status_code=status.HTTP_201_CREATED)
async def create_new_user(new_user_info:UserCreateSchema,
                         user_service : UserService = Depends(get_user_service)):
        '''регистрация юзера с выдачей ему jw токена'''
        try:
            existed_user = await user_service.get_user_by_info(email = new_user_info.email,
                                                                full_name=new_user_info.full_name)
            if existed_user: # если такой юзер уже существует
                        raise HTTPException(status_code=409, detail=" such a User has already been registered")
                    
            new_user_validated_data = {"email" : new_user_info.email,
                                        "full_name" : new_user_info.full_name,
                                        "hashed_password":hash_password(new_user_info.password)}
            new_user = await user_service.create_object(new_user_validated_data)
            return new_user
        except Exception as err:
                                     raise HTTPException(
            status_code=500,
            detail=str(err))  
                            
@user_api_router.post('/token')
async def login_user(form_data:OAuth2PasswordRequestForm = Depends(),
                        user_service : UserService = Depends(get_user_service)):
    '''аутентифицирует юзера и вовзвращает jwt токен с почтой ролью и id
    url путть эндпоинрта должен совпадать с url путем в oauth2_scheme !!! '''
    try:

        login_result = await user_service.login_user(email=form_data.username, password=form_data.password)
        return login_result
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Внутрення ошибка на сервере : {err}, повторите запрос позже") 
        
    
@user_api_router.post('/refresh_token')
async def refresh_token(body:RefreshTokenRequestSchema,
                     user_service : UserService = Depends(get_user_service)):# без зависимости get_verified_user, т. к этому времени еще не юзер еше не авторизовался в системе и будет ошибка
    """
    Обновляет refresh-токен, принимая старый refresh-токен в теле запроса.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate refresh token",
        headers={"WWW-Authenticate": "Bearer"})
    old_refresh_token = body.refresh_token
    
    try:
        payload = jwt.decode(old_refresh_token, project_settings.SECRET_KEY, algorithms=[project_settings.ALGORITHM])
        user_email: str | None = payload.get("sub")
        token_type: str | None = payload.get("token_type")
        # если не подходят условия или не тот тип токена(access)
        if user_email is None or token_type != "refresh":
            raise credentials_exception
    except jwt.ExpiredSignatureError:
        # refresh-токен истёк
        raise credentials_exception
    except jwt.PyJWTError:
        # подпись неверна или токен повреждён
        raise credentials_exception
    current_user = await user_service.get_object_by_params(email=user_email, is_active=True)
    if current_user is None:
        raise credentials_exception
    user_validated_data = {"sub": current_user.email, "full_name" : current_user.full_name, "id": current_user.id}
    # если все ок создае новый рефреш токен
    new_refresh_token = user_service.generate_refresh_token_for_user(user_data=user_validated_data)
    return {
        "refresh_token": new_refresh_token,
        "token_type": "bearer"}
    


@user_api_router.post('/access_token')
async def get_new_access_token(body:RefreshTokenRequestSchema,
                            user_service : UserService = Depends(get_user_service)):# без зависимости get_verified_user, т. к этому времени еще не юзер еше не авторизовался в системе и будет ошибка
    '''по текущему refresh токену если он валиден и юзер есть и активен - выдает новый access токен юзера'''
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate refresh token",
        headers={"WWW-Authenticate": "Bearer"})
    current_refresh_token = body.refresh_token
    try:
        payload = jwt.decode(current_refresh_token, project_settings.SECRET_KEY, algorithms=[project_settings.ALGORITHM])
        user_email: str | None = payload.get("sub")
        token_type: str | None = payload.get("token_type")
        if user_email is None or token_type != 'refresh':
            raise credentials_exception
    except jwt.ExpiredSignatureError:
        # refresh-токен истёк
        raise credentials_exception
    except jwt.PyJWTError:
        # подпись неверна или токен повреждён
        raise credentials_exception
    except BaseException:
        raise ValueError("общая ошибка при обновлении рефреш токена")
    current_user = await user_service.get_object_by_params(email=user_email, is_active=True)
    if current_user is None:
        raise credentials_exception
    user_validated_data = {"sub": current_user.email, "full_name" : current_user.full_name, "id": current_user.id}
    new_access_token = user_service.generate_access_token_for_user(user_data=user_validated_data)
    return {'new_access_token' : new_access_token, "token_type": "bearer"}

    



