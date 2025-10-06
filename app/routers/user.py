from fastapi import APIRouter, Depends
from app.schemas import User,UserId #importamos el esquema (parametros)
from app.DB.database import get_DB #importamos la funcion de la base de datos
from sqlalchemy.orm import Session
from app.DB import models

user_router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

usuarios = []

@user_router.get('/ruta1')
def ruta1():
    return{"mensaje":"Me gusta la pinga del lepras :3 "}

@user_router.get('/')
def obtener_usuarios(DB:Session = Depends(get_DB)):
    data = d
    return usuarios

@user_router.post('/') #creamos usuario 
def  crear_usuario(user:User):
    usuario  = user.model_dump()#model_dump se usa para convertir la informacion en un diccionario
    usuarios.append(usuario) 
    print(usuario)
    return {"respuesta":"usuario creado satisfactoriamente"}

@user_router.get('/{user_id}') #obtenemos informaacion del usuario con el id
def obtener_usuario(user_id:int):
    for user in usuarios :
        print(user,type(user))
        if user["id"] == user_id:
            return {"usuario" : user}
    return{"respuesta":"usuario no encontrado"}

@user_router.post('/obtener_usuario') #segundo metodo para obtener usuario
def obtener_usuario_2(user_id:UserId):
    for user in usuarios :
        print(user,type(user))
        if user["id"] == user_id.id:
            return {"usuario" : user}
    return{"respuesta":"usuario no encontrado"}

@user_router.delete('/') #eliminamos usuario
def eliminar_usuario(user_id:int):
    for index,user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios.pop(index)
            return{"respuesta":"usuario eliminado correctamente"}
    return {"respuesta":"usuario no encontrado"}

@user_router.put('/{user_id}') #ACTUALIZAMOS INFORMACION DEL USUARIO 
def actualizar_usuario(user_id:int,updateUser:User):
    for index,user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios[index]["id"] = updateUser.model_dump()["id"]
            usuarios[index]["nombre"] = updateUser.model_dump()["nombre"]
            usuarios[index]["apellido"] = updateUser.model_dump()["apellido"]
            usuarios[index]["direccion"] = updateUser.model_dump()["direccion"]
            usuarios[index]["telefono"] = updateUser.model_dump()["telefono"]
            return {"respuesta":"usuario actualizado correctamente"}
    return {"respuesta":"usuario no encontrado"}
