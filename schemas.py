from typing import List

from pydantic import BaseModel

class UserCreatInput(BaseModel):
    name: str

class StandartOutput(BaseModel):
    message: str

class FavoriteUserAddInput(BaseModel):
    user_id: int
    symbol: str

class Favorite(BaseModel):
    id: int
    symbol: str
    user_id: int

    class Config:
        orm_mode = True

class UserListOutput(BaseModel):
    id: int
    name: str
    favorites: List[Favorite]

    class Config:
        orm_mode = True

class DaySummaryOutput(BaseModel):
    highest: float
    lowest: float
    symbol: str