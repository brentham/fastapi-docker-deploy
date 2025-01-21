from pydantic import BaseModel

class Hypervisor(BaseModel):

    Hypervisor_ID: int
    Hypervisor_Name: str | None = None
    XDFarm_ID: int | None = None