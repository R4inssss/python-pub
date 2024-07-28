from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app import schemas
from app.config import settings


SQLALCHEMY_DATABASE_URL = (f'postgresql://{settings.database_username}:{settings.database_password}'
                           f'@{settings.database_hostname}:{settings.database_port}/{settings.database_name}')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Gets session from database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



client = TestClient(app)

def test_root():
    res = client.get("/")
    print(res.status_code)
    print(res.json())
    assert res.status_code == 200
    assert res.json().get('message') == 'Volume Bind with tags'

def test_create_user():
    res = client.post("/users/create", json=
                      {"email": "test123@example.com", "password": "password123", "phone_number": "12345"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "test123@example.com"
    assert res.status_code == 201
