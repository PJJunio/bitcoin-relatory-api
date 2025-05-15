from asyncio import gather
from typing import List

from fastapi import APIRouter, HTTPException

from schemas import UserCreatInput, StandartOutput, FavoriteUserAddInput, UserListOutput, DaySummaryOutput
from services import UserService, FavoriteService, AssetService

user_router = APIRouter(prefix='/users')
assets_router = APIRouter(prefix='/assets')


@user_router.post('/create', response_model=StandartOutput)
async def create_users(user_input: UserCreatInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandartOutput(message='OK')
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@user_router.delete('/delete/{user_id}', response_model=StandartOutput)
async def delete_users(user_id: int):
    try:
        await UserService.delete_user(user_id=user_id)
        return StandartOutput(message='OK')
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@user_router.post('/favorite/add', response_model=StandartOutput)
async def add_favorite(favorite_input: FavoriteUserAddInput):
    try:
        await FavoriteService.add_favorite(user_id=favorite_input.user_id, symbol=favorite_input.symbol)
        return StandartOutput(message='OK')
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@user_router.delete('/favorite/remove/{user_id}', response_model=StandartOutput)
async def remove_favorite(user_id: int, symbol: str):
    try:
        await FavoriteService.remove_favorite(user_id=user_id, symbol=symbol)
        return StandartOutput(message='OK')
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@user_router.get('/list', response_model=List[UserListOutput])
async def list_users():
    try:
        return await UserService.list_users()
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@assets_router.get('/day_summary/{user_id}', response_model=List[DaySummaryOutput])
async def day_summary(user_id: int):
    try:
        user = await UserService.get_by_id(user_id)
        favorite_symbols = [favorite.symbol for favorite in user.favorites]
        task = [AssetService.day_summary(symbol=symbol) for symbol in favorite_symbols]
        return await gather(*task)
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))