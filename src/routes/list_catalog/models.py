from sqlalchemy import Column, Integer, String
from config.database import Base

class Catalog(Base):
    __tablename__ = "vmCatalog"

    Catalog_ID = Column (Integer, primary_key=True, index=True)
    CatalogName = Column(String)
    XDFarm_ID = Column (Integer, nullable=True, index=True)