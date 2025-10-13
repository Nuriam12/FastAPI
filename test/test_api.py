from fastapi.testclient import TestClient
import sys
import os
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app.main import app
from app.DB.models import Base
from app.hashing import hash
from app.DB.database import get_DB
import time

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test.db'))
 # creamos la direccion de la carpeta de la base de datos 
db_uri = f"sqlite:///{db_path}"
DATABASE_URL= db_uri

engine_test = create_engine(db_uri, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine_test, autocommit=False, autoflush=False)
Base.metadata.create_all(bind=engine_test) #creara la tablas

cliente = TestClient(app)

def insertar_usuario_prueba(): # prueba de insercion de usuario
    password_hash = hash.hash_password('prueba12')
    with engine_test.connect() as conn :
        conn.execute(text(
    f"""
    INSERT INTO usuario(username,password,nombre,apellido,direccion,telefono,correo)
    values
    ('prueba', '{password_hash}' , 'p.nombre' , 'p.apellido' , 'p.direccion' , '926299253','prueba@gmail.com')
    """
        ))
        conn.commit()
insertar_usuario_prueba()    


def override_get_DB():
    DB = TestingSessionLocal()
    try:
        yield DB 
    finally :
        DB.close ()

app.dependency_overrides[get_DB] = override_get_DB


def test_crear_usuario(): # test para crear usuario
    time.sleep(2)
    usuario = {
        "username": "asdas",
        "password": "prugfdgdfeba12",
        "nombre": "string",
        "apellido": "string",
        "direccion": "string",
        "telefono": 0,
        "correo": "mfksns",
        "creacion": "2025-10-09T11:21:24.140178"
    }
    response = cliente.post('/user/',json=usuario)
    assert response.status_code==401

    usuario_login = {
        "username" : "prueba",
        "password" : "prueba12"
    }

    response_token = cliente.post('/login/',data=usuario_login)
    assert response_token.status_code == 200
    assert response_token.json()["token_type"] == "bearer"
    
    headers = {
        "Authorization" : f"Bearer {response_token.json()['access_token']}"
    }

    response=cliente.post('/user/',json=usuario,headers = headers)
    assert response.status_code == 201
    assert response.json()["respuesta"] == "usuario creado satisfactoriamente"

def test_obtener_usuarios():
    usuario_login = {
        "username" : "prueba",
        "password" : "prueba12"
    }
    response_token = cliente.post('/login/',data=usuario_login)
    assert response_token.status_code == 200
    assert response_token.json()["token_type"] == "bearer"
    
    headers = {
        "Authorization" : f"Bearer {response_token.json()['access_token']}"
    }
    response = cliente.get('/user/' ,headers=headers )
    assert len(response.json()) == 2

def test_obtener_usuario():
    response = cliente.get('/user/1')
    assert response.json()["username"] == "prueba"


def test_eliminar_usuario():
    response = cliente.delete('/user/1')
    assert response.json()["respuesta"] == "usuario eliminado exitosamente"

def test_actualizar_usuario():
    usuario = {
    "username": "andres1_actualizado",
    }
    response = cliente.patch('/user/2',json=usuario)
    assert response.json()["respuesta"] == "usuario actualizado correctamente"

    response_user = cliente.get ('/user/2')
    assert response_user.json() ["username"] == "andres1_actualizado"

def test_no_encuentra_usuario():
    usuario = {
    "username": "andres1_actualizado",
    }
    response = cliente.patch('/user/12',json=usuario)
    assert response.json()["detail"] == "no existe el usuario con el id 12 por lo que no se puede actualizar "


def test_delete_database():
    # Cerrar todas las conexiones
    engine_test.dispose()

    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test.db'))
    os.remove(db_path)
