from pydantic import BaseModel
from typing import Optional
from datetime  import  datetime

#Que es un esquema ? : Un esquema define los parametros y tipos de datos con lo que la API va a trabajar , en este caso definimos los parametros
#y tipos de datos con lo que se va a trabajar el manejo de "USUARIO"

#user Model
class User(BaseModel): #esquema
    username: str
    password:str
    nombre:str
    apellido:str
    direccion:Optional[str]= None
    telefono:int
    correo:str
    creacion:datetime= datetime.now()

class UserId(BaseModel):
    id:int

#GET : traemos informacion
#POST : enviamos informacion
#PUT : actualizamos informacion
#DELETE : eliminamoos informacion