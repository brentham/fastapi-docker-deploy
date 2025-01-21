from pydantic import BaseModel

class ListOS(BaseModel):
    OS_ID: int
    OS_Name: str
