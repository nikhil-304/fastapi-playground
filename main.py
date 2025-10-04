from fastapi import (
    FastAPI,
    Depends,
)  # Import FastAPI for creating the app and Depends for dependency injection
from fastapi.middleware.cors import CORSMiddleware
from models import Product  # Import the Pydantic Product model for data validation
from database import (
    SessionLocal,
    engine,
)  # Import the database session and engine for database connection
import database_models  # Import the database models to interact with the database
from sqlalchemy.orm import Session  # Import Session for database session management

app = FastAPI()  # Create an instance of the FastAPI application

app.add_middleware(
    CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["*"]
)

# Create all database tables defined in database_models if they don't exist
database_models.Base.metadata.create_all(bind=engine)


@app.get("/")  # Define a GET endpoint at the root URL
# Function to handle requests to the root URL
# Returns a welcome message
def greet():
    return "Welcome to Telusko Trac"  # Response returned to the client


# Sample product data to populate the database
products = [
    Product(
        id=1,  # Product ID
        name="Fortixion Hyunyan v0 Phone",  # Product name
        description="Flagship Model",  # Product description
        price=99,  # Product price
        quantity=10,  # Product quantity
    ),
    Product(
        id=2,  # Product ID
        name="ASUS ROG Gaming Laptop",  # Product name
        description="Flagship Premium Model",  # Product description
        price=999,  # Product price
        quantity=5,  # Product quantity
    ),
]


# Dependency to get a database session
def get_db():
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Provide the session to the caller
    finally:
        db.close()  # Close the session after use


# Function to initialize the database with sample data
def init_db():
    db = SessionLocal()  # Create a new database session

    # Count the number of products in the database
    count = db.query(database_models.Product).count()

    # If no products exist in the database
    if count == 0:
        # Iterate over the sample products
        for product in products:  # Add each product to the database
            db.add(database_models.Product(**product.model_dump()))

        db.commit()  # Commit the transaction to save changes to the database


init_db()  # Initialize the database with sample data


@app.get("/products")  # Define a GET endpoint to retrieve all products
def get_all_products(
    db: Session = Depends(get_db),
):  # Dependency injection to get the database session
    db_products = db.query(
        database_models.Product
    ).all()  # Query to get all products from the database
    return db_products  # Return the list of products


@app.get("/products/{id}")  # Define a GET endpoint to retrieve a product by its ID
def get_product_by_id(
    id: int, db: Session = Depends(get_db)
):  # Dependency injection to get the database session
    # Query to get the product with the specified ID
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )

    if db_product:  # If the product is found
        return db_product  # Return the product details

    return (
        "Product Not Found!!"  # Return a not found message if the product doesn't exist
    )


@app.post("/products")  # Define a POST endpoint to add a new product
def add_product(
    product: Product, db: Session = Depends(get_db)
):  # db: Session = Depends(get_db) means dependency injection
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product


@app.delete("/products")  # Define a DELETE endpoint to remove a product
def del_product(id: int, db: Session = Depends(get_db)):
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )

    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted Successfully!"
    else:
        return "Product Not Found!"


@app.put("/products/{id}")  # Define a PUT endpoint to update an existing product
def update_product(
    id: int, product: Product, db: Session = Depends(get_db)
):  # Product ID and updated data are received in the request
    # Iterate over the sample products to find the product to update
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product Updated"
    else:
        return "No Product Found"  # Return a not found message if the product doesn't exist
