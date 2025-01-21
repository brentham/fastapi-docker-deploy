from pydantic import BaseModel

class DGN(BaseModel):

    DGN_ID: int
    DGN_Description: str
    DGN_NTGroup: str | None = None
    XDFarm_ID: int