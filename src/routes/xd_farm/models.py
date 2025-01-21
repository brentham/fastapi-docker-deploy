from sqlalchemy import Column, Integer, String
from config.database import Base

class VmXDFarm(Base):
    __tablename__ = "vmXDFarm"

    XDFarm_ID = Column (Integer, primary_key=True, index=True)
    XDFarm = Column(String)