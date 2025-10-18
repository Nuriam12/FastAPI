from typing import Union
from app.routers.user import user_router
from app.routers.auth import auth_router
from app.routers import web 
from fastapi import FastAPI
from app.DB.database import Base,engine
from app.DB.models import User
import uvicorn


# def create_tables():
#     Base.metadata.create_all(bind=engine)
# create_tables()

app = FastAPI()
app.include_router(user_router)

app.include_router(auth_router)

app.include_router(web.router)

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)

