from pydantic import BaseModel

class VmAction(BaseModel):
    vmAction_ID: int
    vmAction_Name: str
