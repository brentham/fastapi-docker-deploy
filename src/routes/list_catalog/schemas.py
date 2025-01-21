from pydantic import BaseModel

class Catalog(BaseModel):
    Catalog_ID: int
    CatalogName: str
    XDFarm_ID: int
