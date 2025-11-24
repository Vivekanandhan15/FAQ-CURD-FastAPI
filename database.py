from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")  # replace it your Actual Db connection string

engine = create_engine(DB_URL)
sessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()    


