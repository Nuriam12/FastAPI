from sqlalchemy.orm import Session
from app.DB import models


def crear_usuario(usuario,DB:Session):
    usuario  = usuario.model_dump()#model_dump se usa para convertir la informacion en un diccionario
    nuevo_usuario = models.User( #creamos el usuario y se inserta en la tabla user
        username= usuario["username"],
        password= usuario["password"],
        nombre= usuario["nombre"],
        apellido= usuario["apellido"],
        direccion= usuario["direccion"],
        telefono= usuario["telefono"],
        correo= usuario["correo"],
    )
    DB.add(nuevo_usuario)
    DB.commit()
    DB.refresh(nuevo_usuario)


def obtener_usuarios(DB:Session):
    data = DB.query(models.User).all()
    return data


def obtener_usuario(user_id,DB:Session):
    usuario = DB.query (models.User).filter(models.User.id == user_id).first()
    if not usuario :
        return {"Respuesta" : "usuario no encontrado!!"}
    return usuario


def eliminar_usuario(user_id,DB:Session):
    usuario = DB.query (models.User).filter(models.User.id == user_id)
    if not usuario.first() :
        return {"Respuesta" : "usuario no encontrado!!"}
    usuario.delete(synchronize_session=False)
    DB.commit()    
    return {"respuesta":"usuario eliminado exitosamente"}


def actualizar_user(user_id,updateUser,DB:Session):
    usuario = DB.query (models.User).filter(models.User.id == user_id)
    if not usuario.first() :
        return {"Respuesta" : "usuario no encontrado!!"}
    usuario.update(updateUser.model_dump(exclude_unset=True))
    DB.commit()
    return {"respuesta":"usuario actualizado correctamente"}
