from sqlalchemy import Column, Integer, String
from config.database import Base

class DGN(Base):
    __tablename__ = "vmDGN"

    DGN_ID = Column (Integer, primary_key=True, index=True)
    DGN_Description = Column(String)
    DGN_NTGroup = Column(String, nullable=True)
    XDFarm_ID = Column (Integer, index=True)