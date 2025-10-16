import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Settings:
    PROJECT_NAME:str = "PROYECTO-FAST-API"
    PROJECT_VERSION:str = "1.0"
    POSTGRES_DB:str = os.getenv('POSTGRES_DB')
    POSTGRES_USER:str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD:str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER:str = os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT:str = os.getenv('POSTGRES_PORT')
    #DATABASE_URL:str="postgresql://postgres:123456@localhost:5433/fastapi_db" 
    DATABASE_URL= f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()
