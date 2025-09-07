from fastapi import FastAPI, Depends
from models import Product
from database import SessionLocal, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)


@app.get("/")
def greet():
    return "Welcome to Telusko Trac"


products = [
    Product(
        id=1,
        name="Fortixion Hyunyan v0 Phone",
        description="Flagship Model",
        price=99,
        quantity=10,
    ),
    Product(
        id=2,
        name="ASUS ROG Gaming Laptop",
        description="Flagship Premium Model",
        price=999,
        quantity=5,
    ),
]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = SessionLocal()

    count = db.query(database_models.Product).count

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

        db.commit()


init_db()


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products


@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )

    if db_product:
        return db_product

    return "Product Not Found!!"


@app.post("/product")
def add_product(product: Product):
    products.append(product)


@app.delete("/product")
def del_product():
    products.pop()


@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Updated Successfully"

    return "No Product Found"
