from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.DB.database import Base
from datetime import datetime


class Usuario(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True,autoincrement=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String)
    direccion = Column(String)
    telefono = Column(Integer)
    correo = Column(String, unique=True, index=True)
    creacion = Column(DateTime,default=datetime.now,onupdate=datetime)
    estado = Column(Boolean)