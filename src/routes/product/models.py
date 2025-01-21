from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base

class Product(Base):
    __tablename__ = "vw_vmProducts"

    Product_ID = Column (Integer, primary_key=True, index=True)
    Product_Description = Column(String, nullable=True)