from fastapi import FastAPI
from models import Product
from database import session, engine
import database_models

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


@app.get("/products")
def get_all_products():
    db = session()
    db.query()
    return products


@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product

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
