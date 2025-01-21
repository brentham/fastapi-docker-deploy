from sqlalchemy import Column, Integer, String
from config.database import Base

class VmMachineType(Base):
    __tablename__ = "vmMachineType"

    MachineType_ID = Column (Integer, primary_key=True, index=True)
    MachineType = Column(String, nullable=True)