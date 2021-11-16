from pydantic import BaseModel

class Hero(BaseModel):
    name: str
    ranking: str
    