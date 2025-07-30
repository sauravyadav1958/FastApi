

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHAMY_DATABASE_URL = 'sqlite:///./app.db'
engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

# MYSQL_DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/app"
# engine = create_engine(MYSQL_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
