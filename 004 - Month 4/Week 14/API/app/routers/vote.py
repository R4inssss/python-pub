from fastapi import FastAPI, HTTPException, Response, status, Depends, APIRouter
from .. import models, schemas, oauth2, database
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED) #response_model=schemas.Vote)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db),
         current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {vote.post_id} not found")

    # print(f"Received vote: {vote}, current user: {current_user.id}")  # Debug code
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,
                                              models.Vote.user_id == current_user.id)

    found_vote = vote_query.first()
    # print(f"Found vote: {found_vote}")  # Debug code

    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"User {current_user.id} has already voted on {vote.post_id}")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Vote added"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Vote deleted"}

# Debug Code
# @router.get("/test")
# def test_endpoint():
#     return {"message": "Router is working"}

