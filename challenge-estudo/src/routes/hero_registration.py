from fastapi import APIRouter

from models.hero_registration import Hero
from config.db import conn
from schemas.hero_registration import heroEntity, heroesEntity
from bson.objectid import ObjectId

router = APIRouter(tags=["Heroes"])

@router.get('/hero')
async def find_all_hero():
    print(conn.hero_registration.find())
    print(heroesEntity(conn.hero_registration.find()))
    return heroesEntity(conn.hero_registration.find())

@router.get('/hero/{id}')
async def find_all_heroes(id):
     return heroEntity(conn.hero_registration.find_one({"_id":ObjectId(id)}))


@router.post('/hero')
async def create_heroes(hero: Hero):
    conn.hero_registration.insert_one(dict(hero))
    return heroesEntity(conn.hero_registration.find())

@router.put('/hero/{id}')
async def update_heroes(id,hero: Hero):
    conn.hero_registration.find_one_and_update({"_id":ObjectId(id)},
        {"$set":dict(hero)
    })
    return heroEntity(conn.hero_registration.find_one({"_id":ObjectId(id)}))
    
@router.delete('/hero/{id}')
async def delete_heroes(id,hero: Hero):
     return heroEntity(conn.hero_registration.find_one_and_delete({"_id":ObjectId(id)}))
