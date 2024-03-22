# routes.py

from fastapi import HTTPException, APIRouter
from typing import List
from models.models import User

router = APIRouter()

# Примерные данные пользователей
fake_users_db = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"},
]

@router.get("/users/", response_model=List[User])
async def read_users():
    return fake_users_db

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    user = next((user for user in fake_users_db if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/", response_model=User)
async def create_user(user: User):
    fake_users_db.append(user.dict())
    return user

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    user_index = next((index for index, u in enumerate(fake_users_db) if u["id"] == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    fake_users_db[user_index] = user.dict()
    return user

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    user_index = next((index for index, u in enumerate(fake_users_db) if u["id"] == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    del fake_users_db[user_index]
    return {"message": "User deleted successfully"}
