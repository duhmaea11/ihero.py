from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bson.objectid import ObjectId

router = APIRouter(tags=["Users"])

@router.get('/user')
async def find_all_user():
    print(conn.user.find())
    print(usersEntity(conn.user.find()))
    return usersEntity(conn.user.find())

@router.get('/user/{id}')
async def find_all_users(id):
     return userEntity(conn.user.find_one({"_id":ObjectId(id)}))


@router.post('/user')
async def create_users(user: User):
    conn.user.insert_one(dict(user))
    return usersEntity(conn.user.find())

@router.put('/user/{id}')
async def update_users(id,user: User):
    conn.user.find_one_and_update({"_id":ObjectId(id)},
        {"$set":dict(user)
    })
    return userEntity(conn.user.find_one({"_id":ObjectId(id)}))
    
@router.delete('/user/{id}')
async def delete_users(id,user: User):
     userEntity(conn.user.find_one_and_delete({"_id":ObjectId(id)}))
     return {"User deleted successfully"}