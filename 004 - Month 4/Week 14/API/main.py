from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def hello():
    return {"message": "welcome to API"}


@app.get("/home")
def get_posts():
    return {"message": "Home"}


@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.dict())  # Converts to dictionary
    return {"data": post}

