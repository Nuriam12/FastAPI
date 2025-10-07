from pydantic import BaseModel #pydantic : Librería para validación y serialización de datos. // BaseModel Clase base de la que heredan tus modelos para definir los esquemas y validaciones
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

 #--------------------------------------------------

 #update Model
class UpdateUser(BaseModel): #esquema
    username: Optional[str] = None
    password: Optional[str] = None
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[int] = None
    correo: Optional[str] = "LNF@gmail.com"

class UserId(BaseModel):
    id:int

#GET : traemos informacion
#POST : enviamos informacion
#PUT : actualizamos informacion
#DELETE : eliminamoos informacion

#------------------------------------------------------------------------------------
class ShowUser(BaseModel) :
    username: str
    nombre:str
    correo:str