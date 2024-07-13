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
# Debug Code: from .debuglog import Debug_log


# models.Base.metadata.create_all(bind=engine)
#
# app = FastAPI()
#
# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#             {"title": "favorite foods", "content": "I like pizza", "id": 2}]
#
# # ============== psycopg2 ==================== #
#
#
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',  # I know hardcoding bad
#                                 password='password123', cursor_factory=RealDictCursor)  # Will change in future
#         cursor = conn.cursor()
#         print("Connected to PostgreSQL")
#         break
#     except Exception as e:
#         print("Failed to connect to PostgreSQL")
#         print(e)
#         time.sleep(2)
#
#
# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
#
# # ============== Main Code ==================== #
#
#
# @app.get("/")
# def hello():
#     return {"message": "welcome to API"}
#
#
# # @app.get("/sqlalchemy")
# # def test_post(db: Session = Depends(get_db)):
# #     posts = db.query(models.Post).all()
# #     print(posts)
# #     return {"data": posts}
#
#
# # Find all posts
# @app.get("/posts", response_model=List[schemas.Post])
# def get_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     # cursor.execute("""SELECT * FROM posts""")
#     # posts = cursor.fetchall()
#     return posts
#
#
# # Create posts
# @app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
#     #                (post.title, post.content, post.published))
#     # new_post = cursor.fetchone()
#     # conn.commit()
#     new_post = models.Post(**post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#
#     return new_post
#
#
# # Get one post
# @app.get("/posts/{id}", response_model=schemas.Post)
# def get_post(id: int, db: Session = Depends(get_db)):
#     # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id), None))  # Passing null for a parameter
#     # post = cursor.fetchone()
#
#     post = db.query(models.Post).filter(models.Post.id == id).first()  # equivalent of doing a where
#
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id {id} not found")
#     return post
#
#
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i
#
#
# # Delete posts
# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):
#     # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id), None))
#     # deleted_post = cursor.fetchone()
#     # conn.commit()
#
#     post = db.query(models.Post).filter(models.Post.id == id)
#     if post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
#     post.delete(synchronize_session=False)
#     db.commit()
#
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
#
#
# # Update posts
# @app.put("/posts/{id}", response_model=schemas.Post)
# def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
#     #                (post.title, post.content, post.published, str(id),))
#     # updated_post = cursor.fetchone()
#     # conn.commit()
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     post = post_query.first()
#     post_query.update(updated_post.dict(), synchronize_session=False)
#
#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
#     db.commit()
#
#     return post_query.first()
#
#
# # Create users
# @app.post("/users/create", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#
#     # Hashing our password - user.password
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#
#     return new_user
#
#
# @app.get('/users/{id}', response_model=schemas.UserOut)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"user with id {id} not found")
#     return user
#
#
#
# # Debug Code
# #   if __name__ == "__main__":
# #       import uvicorn
# #       uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
#