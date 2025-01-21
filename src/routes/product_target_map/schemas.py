from pydantic import BaseModel

class ProductTargetMap(BaseModel):

    Product_ID: int
    Product_Description: str | None = None
    XDFarm_ID: int | None = None
    XDFarm: str | None = None
    MachineSource_ID: int | None = None
    MachineSource: str | None = None
    MachineType_ID: int | None = None
    MachineType: str | None = None
    Catalog_ID: int | None = None
    CatalogName: str | None = None
    DGN_ID: int | None = None
    DGN_Description: str | None = None
    DGN_NTGroup: str | None = None