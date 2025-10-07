from fastapi import APIRouter, Depends
from app.schemas import User,ShowUser,UpdateUser #importamos el esquema (parametros)
from app.DB.database import get_DB # Dependencia que genera la sesión con la BD
from sqlalchemy.orm import Session
from typing import List #importamos formato de lista
from app.repository import user


user_router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

usuarios = []


#obtenemos la informacion de todos los usuarios creados
 
@user_router.get('/' ,response_model=List[ShowUser]) #usamos list[] y response para entregar informacion especifica que marca el esquema y lo entregamos en formato de lista
def obtener_usuarios(DB:Session = Depends(get_DB)):
    data = user.obtener_usuarios(DB)
    return data


@user_router.post('/')
def  crear_usuario(usuario:User,DB:Session = Depends(get_DB)):
    user.crear_usuario(usuario,DB)
    return {"respuesta":"usuario creado satisfactoriamente"}




@user_router.get('/{user_id}',response_model=ShowUser   ) #usamos response model con el esquema "ShowUser" , para entregar informacion especifica al usuario
def obtener_usuario(user_id:int,DB:Session = Depends(get_DB)):
    usuario=user.obtener_usuario(user_id,DB)
    return usuario




@user_router.delete('/') 
def eliminar_usuario(user_id:int,DB:Session = Depends(get_DB)):
    res= user.eliminar_usuario(user_id,DB)
    return res




@user_router.patch('/{user_id}')  
def actualizar_user(user_id:int,updateUser:UpdateUser,DB:Session = Depends(get_DB)):
    res = user.actualizar_user(user_id,updateUser,DB)
    return res