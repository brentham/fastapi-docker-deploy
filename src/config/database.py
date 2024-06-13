from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import Settings

settings = Settings()

db_type = settings.DB_TYPE
db_username = settings.DB_USERNAME
db_password = settings.DB_PASSWORD
db_url = settings.DB_URL
db_name = settings.DB_NAME

URL_DATABASE = f'{db_type}://{db_username}:{db_password}@{db_url}/{db_name}'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker (autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()