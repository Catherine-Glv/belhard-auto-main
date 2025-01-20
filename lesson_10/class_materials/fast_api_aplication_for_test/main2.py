from fastapi import FastAPI
from lesson_10.class_materials.fast_api_aplication_for_test.routers import item

app = FastAPI()

app.include_router(router=item.router_item)