from sqlalchemy import Column, Integer, String
from config.database import Base

class VmStatus(Base):
    __tablename__ = "vmStatus"

    vmStatus_ID = Column (Integer, primary_key=True, index=True)
    vmStatus_Name = Column(String, nullable=True)