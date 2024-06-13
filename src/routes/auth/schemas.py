from pydantic import BaseModel
from typing import List, Annotated, Union, Optional


class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str