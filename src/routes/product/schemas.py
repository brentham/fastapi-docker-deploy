from pydantic import BaseModel

class Product(BaseModel):

    Product_ID: int
    Product_Description: str | None = None