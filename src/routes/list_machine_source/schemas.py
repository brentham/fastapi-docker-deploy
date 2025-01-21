from pydantic import BaseModel

class VmMachineSource(BaseModel):
    MachineSource_ID: int
    MachineSource: str
