#! python3
# JWT oauth main
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')  # login endpoint

SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# def create_access_token(data: dict):  # here, data is our payload
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({'exp': expire})  # Here, JWT is telling when it expires
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Pass our data and use jwt.encode method
#
#     return encoded_jwt

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode['user_id'] = str(to_encode['user_id'])

    print(f"Data to be encoded in token: {to_encode}") #  Debug code, will remove as needed

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        print(f"Payload: {payload}")
        print(f"ID extracted from token: {id}, Type: {type(id)}")  # Debug code
        if id is None:
            raise credentials_exception
        print(f"ID extracted from token: {id}, Type: {type(id)}")  # Debug code
        token_data = schemas.TokenData(id=id)
    except JWTError as e:
        print(f"JWTError: {e}")  # Print the JWTError if it occurs
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials.",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user
