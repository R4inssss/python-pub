from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

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

# Reference for raw sql

# while True:
#     try:
#         conn = psycopg2.connect(host=f'{}', database=f'{}', user=f'{}',
#                                 password=f'{}', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Connected to PostgreSQL")
#         break
#     except Exception as e:
#         print("Failed to connect to PostgreSQL")
#         print(e)
#         time.sleep(2)
