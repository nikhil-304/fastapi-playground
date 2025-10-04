from database import engine
import database_models

# Create all tables
database_models.Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
