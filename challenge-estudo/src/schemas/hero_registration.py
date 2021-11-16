def heroEntity(item) -> dict:
    return{
        "id":str(item['_id']),
        "name":item['name'],
        "ranking":item["ranking"]
    }

def heroesEntity(entity) -> list:
    return [heroEntity(item) for item in entity]