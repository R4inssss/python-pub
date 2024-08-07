from app import schemas
import pytest
from jose import jwt
from app.config import settings

# def test_root(client):
#     res = client.get("/")
#     print(res.status_code)
#     print(res.json())
#     assert res.status_code == 200
#     assert res.json().get('message') == 'Volume Bind with tags'


def test_create_user(client):
    res = client.post("/users/create", json=
                      {"email": "test123@example.com", "password": "password123", "phone_number": "12345"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "test123@example.com"
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post(
        "/login/", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = int(payload.get("user_id"))
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@wrong.com', 'passwordEEEE', 403),
    ('test123@example.com', 'wrongPassword', 403),
    ('wrongwrong@wrong.wrong', 'wrongpassword', 403),
    (None, 'password123', 422),
    ('test123@example.com', None, 422)
])
def test_incorrect_login(client, test_user, email, password, status_code):
    res = client.post(
        "/login/", data={"username": email, "password": password}
    )
    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Credentials invalid'

