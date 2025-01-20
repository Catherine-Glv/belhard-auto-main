from fastapi import APIRouter, HTTPException
from lesson_10.class_materials.fast_api_aplication_for_test.models.item import ItemRequest, ItemResponse

router_item = APIRouter()
items = {}

@router_item.post(path="/create-item", response_model=ItemResponse)
def create_item(item: ItemRequest):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.id] = item
    return ItemResponse(
        message='Item created',
        id=item.id
    )
