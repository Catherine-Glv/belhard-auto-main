from email import message

from fastapi.testclient import TestClient
from lesson_10.class_materials.fast_api_aplication_for_test.main2 import app

clint = TestClient(app=app)

def test_create_item():
    body = {
        "id": 2,
        "name": "Name1",
        "description": 'new',
        "price": 2.2,
        "tax": 4.4
    }
    actual_id = body.get('id')
    response = clint.post(url="/create-item", json=body)
    result = response.json()
    id_from_resp = result.get('id')
    message = result.get("message")
    assert response.status_code == 200, f'Ожидали статус 200, но вернулось {response.status_code}'
    assert actual_id == id_from_resp, f'Ожидали id - {actual_id}, но вернулось {id_from_resp}'
    assert message == 'Item created'
