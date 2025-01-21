from pydantic import BaseModel

class ProductSourceMap(BaseModel):
    
    ID: int
    Product_ID: int | None = None
    SourceName: str | None = None
    DGN_ID: int | None = None
    OS_ID: int | None = None
    MachineNameSourcePattern: str | None = None
    HypervisorIDs: str | None = None
    XDFarm_ID: int | None = None