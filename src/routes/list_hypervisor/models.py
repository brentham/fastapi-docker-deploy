from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base

class Hypervisor(Base):
    __tablename__ = "vmHypervisor"

    Hypervisor_ID = Column (Integer, primary_key=True, index=True)
    Hypervisor_Name = Column(String)
    XDFarm_ID = Column(Integer)