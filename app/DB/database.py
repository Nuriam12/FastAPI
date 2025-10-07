from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

import os

# DATABASE_URL = os.getenv(
#     "DATABASE_URL",  
#     "postgresql://postgres:123456@localhost:5433/fastapi_db" 
# )
DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_DB():
    DB = SessionLocal()
    try:
        yield DB 
    finally :
        DB.close ()
