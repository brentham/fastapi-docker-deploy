from sqlalchemy import Column, Integer, String
from config.database import Base

class ProductSourceMap(Base):
    __tablename__ = "vmProductSourceMap"

    ID = Column (Integer, primary_key=True, index=True)
    Product_ID = Column (Integer, nullable=True, index=True)
    SourceName = Column(String, nullable=True)
    DGN_ID = Column (Integer, nullable=True, index=True)
    OS_ID = Column (Integer, nullable=True, index=True)
    MachineNameSourcePattern = Column(String, nullable=True)
    HypervisorIDs = Column(String, nullable=True)
    XDFarm_ID = Column (Integer, nullable=True, index=True)