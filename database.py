from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://localhost:5432/nikhil"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
