from sqlalchemy import Column, Integer, String
from config.database import Base

class ListOS(Base):
    __tablename__ = "vmOS"

    OS_ID = Column (Integer, primary_key=True, index=True)
    OS_Name = Column(String)