from fastapi import FastAPI, HTTPException

from models.items import Item

app = FastAPI()

@app.get(path='/')
def read_hello_world():
    return {'hello': 'World'}

@app.get("/item/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post('/items/create-item')
def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400, detail='Not valid') # валидация значений
    return {"item_name": item.name, "item_description": item.description, "price": item.price, "tax": item.tax}



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host='127.0.0.1', port=8000)
