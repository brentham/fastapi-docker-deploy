from pydantic import BaseModel

class VmStatus(BaseModel):
    vmStatus_ID: int
    vmStatus_Name: str | None = None
