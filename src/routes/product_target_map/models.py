from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base

class ProductTargetMap(Base):
    __tablename__ = "vw_vmProductTargetMap"

    Product_ID = Column (Integer, primary_key=True, index=True)
    Product_Description = Column(String, nullable=True)
    XDFarm_ID = Column (Integer, nullable=True)
    XDFarm = Column(String, nullable=True)
    MachineSource_ID = Column (Integer, nullable=True)
    MachineSource = Column(String, nullable=True)
    MachineType_ID = Column (Integer, nullable=True)
    MachineType = Column(String, nullable=True)
    Catalog_ID = Column (Integer, nullable=True)
    CatalogName = Column(String, nullable=True)
    DGN_ID = Column (Integer, nullable=True)
    DGN_Description = Column(String, nullable=True)
    DGN_NTGroup = Column(String, nullable=True)