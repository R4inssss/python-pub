from fastapi import FastAPI, HTTPException, Response, status, Depends
from fastapi.params import Body
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user
# Debug Code: from .debuglog import Debug_log


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ============== psycopg2 and functions ==================== #


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',  # I know hardcoding bad
                                password='password123', cursor_factory=RealDictCursor)  # Will change in future
        cursor = conn.cursor()
        print("Connected to PostgreSQL")
        break
    except Exception as e:
        print("Failed to connect to PostgreSQL")
        print(e)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

# ============== Main Code ==================== #


app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
def hello():
    return {"message": "welcome to API"}



# Delete posts

# Debug Code
#   if __name__ == "__main__":
#       import uvicorn
#       uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
