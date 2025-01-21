from pydantic import BaseModel

class VmXDFarm(BaseModel):
    XDFarm_ID: int
    XDFarm: str
