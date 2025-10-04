
# FastAPI Product Inventory Management System

A full-stack product inventory management application built with **FastAPI** (Python backend), **React** (frontend), and **PostgreSQL** (database). This project demonstrates comprehensive CRUD operations, database integration with SQLAlchemy, CORS handling, and modern API development practices.

## 🚀 Learning Focus: FastAPI

This project was created as a hands-on learning experience for **FastAPI**, covering:
- Building RESTful APIs with automatic OpenAPI documentation
- Dependency injection and database session management
- Pydantic models for data validation
- SQLAlchemy ORM for database interactions
- CORS middleware for frontend integration
- Error handling and response models

## ✨ Features

### Backend API Endpoints
- **GET /**: Welcome message
- **GET /products**: Retrieve all products
- **GET /product/{id}**: Get a specific product by ID
- **POST /product**: Create a new product
- **PUT /product**: Update an existing product
- **DELETE /product**: Delete a product by ID

### Database Integration
- PostgreSQL database with SQLAlchemy ORM
- Automatic table creation and data seeding
- Session management with dependency injection

### Frontend
- React application for product management UI
- CORS-enabled communication with FastAPI backend

## 🛠️ Tech Stack

- **Backend**: FastAPI, SQLAlchemy, Pydantic, Uvicorn
- **Database**: PostgreSQL
- **Frontend**: React
- **Development**: Python virtual environment, npm

## 📁 Project Structure

```
FastAPI - Project - Telusko/
├── main.py                 # FastAPI application with all endpoints
├── models.py               # Pydantic data models
├── database.py             # Database configuration and session setup
├── database_models.py      # SQLAlchemy database models
├── create_tables.py        # Script to initialize database tables
├── frontend/               # React frontend application
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
├── myenv/                  # Python virtual environment
├── .vscode/                # VS Code project settings
├── .gitignore
└── README.md
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js and npm
- PostgreSQL server running locally

### 1. Backend Setup

1. **Clone the repository and navigate to the project directory**

2. **Create and activate virtual environment:**
   ```bash
   python -m venv myenv
   # Windows:
   myenv\Scripts\activate
   # macOS/Linux:
   source myenv/bin/activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2 pydantic
   ```

4. **Database Setup:**
   - Ensure PostgreSQL is running
   - Create a database named `nikhil-fastapi-tuts`
   - Update connection details in `database.py` if needed

5. **Initialize database tables:**
   ```bash
   python create_tables.py
   ```

6. **Run the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

7. **Access the API:**
   - API Base: http://localhost:8000
   - Interactive API Docs: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc

### 2. Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the React development server:**
   ```bash
   npm start
   ```

4. **Access the frontend:**
   - React App: http://localhost:3000

## 📡 API Usage Examples

### Get All Products
```bash
curl http://localhost:8000/products
```

### Get Product by ID
```bash
curl http://localhost:8000/product/1
```

### Create a New Product
```bash
curl -X POST "http://localhost:8000/product" \
     -H "Content-Type: application/json" \
     -d '{
       "id": 3,
       "name": "Wireless Mouse",
       "description": "Ergonomic wireless mouse",
       "price": 29.99,
       "quantity": 50
     }'
```

### Update a Product
```bash
curl -X PUT "http://localhost:8000/product" \
     -H "Content-Type: application/json" \
     -d '{
       "id": 1,
       "name": "Updated Product Name",
       "description": "Updated description",
       "price": 149.99,
       "quantity": 25
     }'
```

### Delete a Product
```bash
curl -X DELETE "http://localhost:8000/product?id=1"
```

## 🗄️ Database Models

### Product Table
- `id`: Integer (Primary Key)
- `name`: String (Product name)
- `description`: String (Product description)
- `price`: Float (Product price)
- `quantity`: Integer (Available quantity)

## 🔧 Key FastAPI Concepts Demonstrated

1. **Application Setup**: Creating FastAPI instance with middleware
2. **Routing**: Defining endpoints with HTTP methods
3. **Dependency Injection**: Database session management
4. **Data Validation**: Using Pydantic models
5. **ORM Integration**: SQLAlchemy for database operations
6. **CORS Handling**: Enabling cross-origin requests for frontend
7. **Automatic Documentation**: Swagger UI and ReDoc generation
8. **Error Handling**: Proper response formatting

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [React Documentation](https://reactjs.org/)

## 🤝 Contributing

This is a learning project. Feel free to explore, modify, and experiment with the code to deepen your understanding of FastAPI and full-stack development.

---

**Built with ❤️ for learning FastAPI**