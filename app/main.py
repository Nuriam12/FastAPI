from typing import Union
from app.routers.user import user_router
from fastapi import FastAPI
from app.DB.database import Base,engine
from app.routers import user



def create_tables():
    Base.metadata.create_all(bind=engine)
create_tables()

app = FastAPI()
app.include_router(user_router)

