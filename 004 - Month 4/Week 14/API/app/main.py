from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]

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


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/")
def hello():
    return {"message": "welcome to API"}


# Find all posts
@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}


# Create posts
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


# Get one post
@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id), None))  # Passing null for a parameter
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} not found")
    return {"post_detail": post}


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


# Delete posts
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id), None))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)



# Update posts
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
    (post.title, post.content, post.published, str(id),))
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")

    return {"data": updated_post}
