from sqlalchemy import Column, Integer, String
from config.database import Base

class VmMachineSource(Base):
    __tablename__ = "vmMachineSource"

    MachineSource_ID = Column (Integer, primary_key=True, index=True)
    MachineSource = Column(String)