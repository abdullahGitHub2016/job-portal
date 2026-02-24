from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace 'username', 'password', and 'db_name' with your MySQL details
# Format: mysql+pymysql://<user>:<password>@<host>:<port>/<db_name>
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/job_portal"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get the database session in your routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()