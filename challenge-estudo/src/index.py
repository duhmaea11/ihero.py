from fastapi import FastAPI
from routes.user import router as routerUser
from routes.hero_registration import router as routerHero

app = FastAPI()

app.include_router(routerUser)
app.include_router(routerHero)