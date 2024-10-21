from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import Settings
import pyodbc

settings = Settings()

db_type = settings.DB_TYPE
db_username = settings.DB_USERNAME
db_password = settings.DB_PASSWORD
db_url = settings.DB_URL
db_name = settings.DB_NAME

URL_DATABASE = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={db_url};DATABASE={db_name};UID={db_username};PWD={db_password};TrustServerCertificate=yes')
engine = create_engine('mssql+pyodbc://', creator=lambda: URL_DATABASE)
SessionLocal = sessionmaker (autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()