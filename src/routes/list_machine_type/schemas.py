from pydantic import BaseModel

class VmMachineType(BaseModel):
    MachineType_ID: int
    MachineType: str | None = None
