from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.repository import user
from app.DB.database import get_DB
from app.schemas import Login 
from app.repository import auth
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

auth_router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

@auth_router.post('/',status_code=status.HTTP_200_OK) 
def login(usuario:Annotated[OAuth2PasswordRequestForm, Depends()],DB:Session = Depends(get_DB)):
    auth_Token = auth.auth_user(usuario,DB)
    return auth_Token
