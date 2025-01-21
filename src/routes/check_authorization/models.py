from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, CHAR,TIMESTAMP
from sqlalchemy.orm import relationship
from config.database import Base

# class ListOS(Base):
#     __tablename__ = "pr_vmServices_OS"

#     OS_ID = Column (Integer, primary_key=True, index=True)
#     OS_Name = Column(String)