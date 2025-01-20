from pydantic import BaseModel

class ItemRequest(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    tax: float = None

class ItemResponse(BaseModel):
    message: str
    id: int
