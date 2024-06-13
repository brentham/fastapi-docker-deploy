from pydantic import BaseModel
from typing import List, Annotated, Union, Optional


class Listing(BaseModel):
    title: str
    company: str
    location: str
    description: str
    logo: str
    tags: str
    email: str
    # timestamp: str