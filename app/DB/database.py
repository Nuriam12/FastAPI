from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",  # nombre de la variable de entorno
    "postgresql://postgres:123456@localhost:5433/fastapi_db"  # valor por defecto
)
print(DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_DB():
    DB = SessionLocal()
    try:
        yield DB 
    finally :
        DB.close ()
