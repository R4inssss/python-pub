from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth
from .config import settings
# Debug Code: from .debuglog import Debug_log


# ============== Main Code ==================== #

print(settings.database_username)

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def hello():
    return {"message": "welcome to API"}


# ============== Debug Code ==================== #


# Debug Code
#   if __name__ == "__main__":
#       import uvicorn
#       uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
