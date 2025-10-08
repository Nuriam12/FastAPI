from sqlalchemy.orm import Session
from app.DB import models
from fastapi import HTTPException,status
from app.hashing import hash



def crear_usuario(usuario,DB:Session):
    usuario  = usuario.model_dump()#model_dump se usa para convertir la informacion en un diccionario
    try: 
        nuevo_usuario = models.User( #creamos el usuario y se inserta en la tabla user
            username= usuario["username"],
            password= hash.hash_password(usuario["password"]), #constraseña encriptada
            nombre= usuario["nombre"],
            apellido= usuario["apellido"],
            direccion= usuario["direccion"],
            telefono= usuario["telefono"],
            correo= usuario["correo"],
        )
        DB.add(nuevo_usuario)
        DB.commit()
        DB.refresh(nuevo_usuario)
    except Exception as e :
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail=f"Error creando usuario{e}"
        )


def obtener_usuarios(DB:Session):
    data = DB.query(models.User).all()
    return data


def obtener_usuario(user_id,DB:Session):
    usuario = DB.query (models.User).filter(models.User.id == user_id).first()
    if not usuario :
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"no existe el usuario con el id {user_id}"
        )
    return usuario


def eliminar_usuario(user_id,DB:Session):
    usuario = DB.query (models.User).filter(models.User.id == user_id)
    if not usuario.first() :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"no existe el usuario con el id {user_id} por lo tanto no se elimina "
        )
    usuario.delete(synchronize_session=False)
    DB.commit()    
    return {"respuesta":"usuario eliminado exitosamente"}


def actualizar_user(user_id,updateUser,DB:Session):
    usuario = DB.query (models.User).filter(models.User.id == user_id)
    if not usuario.first() :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"no existe el usuario con el id {user_id} por lo que no se puede actualizar "
        )
    usuario.update(updateUser.model_dump(exclude_unset=True))
    DB.commit()
    return {"respuesta":"usuario actualizado correctamente"}
