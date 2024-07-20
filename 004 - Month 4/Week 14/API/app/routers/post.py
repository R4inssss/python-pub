from fastapi import FastAPI, HTTPException, Response, status, Depends, APIRouter
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional
from sqlalchemy import func

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


# Find all posts
# @router.get("/", response_model=List[schemas.Post])
# @router.get("/", response_model=List[schemas.PostWithVotes])
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # Query Parameters for limit and skip (offset)
    print(limit)
    # posts = db.query(models.Post).all()

    # Query for post only when logged in
    # posts = (db.query(models.Post).filter(
    #     models.Post.owner_id == current_user.id).filter(models.Post.title.contains(search))
    #          .limit(limit).offset(skip).all())
    # Query for all post
    # posts = db.query(models.Post).filter(
    #     models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # print(posts) DEBUG CODE
    posts = (((db.query(models.Post, func.count(models.Vote.post_id).label('votes'))
               .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)).group_by(models.Post.id)).
             filter(models.Post.title.contains(search)).limit(limit).offset(skip).all())
    # print(results) DEBUG CODE

    # Optional filters: Filtering for post title, limiting posts, and skipping post
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    return posts


# Create posts
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
    #                (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    # print(current_user.id)     # debug code
    # print(current_user.email)  # debug code
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


# Get one post
@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # post = db.query(models.Post).filter(models.Post.id == id).first()  # equivalent of doing a where
    post = (((db.query(models.Post, func.count(models.Vote.post_id).label('votes'))
              .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)).group_by(models.Post.id)).
            filter(models.Post.id == id).first())

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} not found")
    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail=f"You do not have permission to view this post")
    return post


# Debug Code
# @router.get("/{id}", response_model=schemas.Post)
# def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
#     print(f"Post Retrieved: {post}")
#     print(f"Post Owner ID: {post.owner_id}")
#     print(f"Current User ID: {current_user.id}")
#     if post.owner_id != current_user.id:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
#     return post


# Delete posts
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"You do not have permission to delete this post")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Update posts
@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    post_query.update(updated_post.dict(), synchronize_session=False)

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"You do not have permission to update this post")

    db.commit()

    return post_query.first()
