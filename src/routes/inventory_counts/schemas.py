from pydantic import BaseModel

class VmInventoryQueue(BaseModel):
    Product_ID: int
    Product_Description: str

class VmProduct(BaseModel):
    Product_ID: int
    Product_Description: str
    Product_Total: int