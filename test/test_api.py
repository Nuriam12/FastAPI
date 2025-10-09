from fastapi.testclient import TestClient
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app.main import app
from app.DB.models import Base

# ✅ CORREGIDO: paréntesis en el lugar correcto
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test.db')
db_uri = f"sqlite:///{db_path}"

engine_test = create_engine(db_uri, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine_test, autocommit=False, autoflush=False)
Base.metadata.create_all(bind=engine_test)

cliente = TestClient(app)

def test_crear_usuario():
    usuario = {
        "username": "pfsafa",
        "password": "string",
        "nombre": "string",
        "apellido": "string",
        "direccion": "string",
        "telefono": 0,
        "correo": "mfksns",
        "creacion": "2025-10-09T11:21:24.140178"
    }

    # response = cliente.post('/user/',json=usuario)
    # assert response.status_code == 201
    # assert response.json()["respuesta"] == 'usuario creado satisfactoriamente'
    # pass
