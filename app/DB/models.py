from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.DB.database import Base
from datetime import datetime
from sqlalchemy import ForeignKey #añadimos llaves foraneas en otras tablas
from sqlalchemy.orm import relationship #agregamos relacion entre tablas

class User(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True,autoincrement=True, index=True)
    username = Column(String,unique=True)
    password = Column(String)
    nombre = Column(String, index=True)
    apellido = Column(String)
    direccion = Column(String)
    telefono = Column(Integer)
    correo = Column(String, unique=True, index=True)
    creacion = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    estado = Column(Boolean, default=False)
    Venta = relationship("Venta", backref="usuario",cascade="delete,merge")


class Venta(Base) :
    __tablename__ = "venta"
    id = Column(Integer,primary_key=True, autoincrement=True)
    usuario_id = Column(Integer,ForeignKey("usuario.id",ondelete="CASCADE"))
    venta = Column(Integer)
    ventas_productos = Column(Integer)