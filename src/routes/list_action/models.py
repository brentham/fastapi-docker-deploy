from sqlalchemy import Column, Integer, String
from config.database import Base

class VmAction(Base):
    __tablename__ = "vmAction"

    vmAction_ID = Column (Integer, primary_key=True, index=True)
    vmAction_Name = Column(String)