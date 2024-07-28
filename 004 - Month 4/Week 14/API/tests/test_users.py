from app import schemas
from .database import client, session


def test_root(client):
    res = client.get("/")
    print(res.status_code)
    print(res.json())
    assert res.status_code == 200
    assert res.json().get('message') == 'Volume Bind with tags'

def test_create_user(client):
    res = client.post("/users/create", json=
                      {"email": "test123@example.com", "password": "password123", "phone_number": "12345"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "test123@example.com"
    assert res.status_code == 201
