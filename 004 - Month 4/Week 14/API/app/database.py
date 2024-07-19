from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password123@localhost/fastapi'  # Teehee password
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

# Reference for raw sql

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
