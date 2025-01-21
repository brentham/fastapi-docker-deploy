from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class VmInventoryQueue(Base):
    __tablename__ = "vmInventoryQueue"

    Product_ID = Column (Integer, ForeignKey("vmProducts.Product_ID"), primary_key=True, index=True)
    product = relationship("VmProduct", back_populates="inventory_queue")
    
    
class VmProduct(Base):
    __tablename__ = "vmProducts"

    Product_ID = Column (Integer, primary_key=True, index=True)
    Product_Description = Column(String)
    inventory_queue = relationship("VmInventoryQueue", back_populates="product")