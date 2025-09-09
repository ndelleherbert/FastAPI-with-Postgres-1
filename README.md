Perfect ✅ Let’s extend the project with a **requirements.txt** so anyone can install the dependencies easily.

---

# 📖 Blog API – FastAPI + PostgreSQL

A simple CRUD (Create, Read, Update, Delete) REST API for managing blog users using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

---

## 🚀 Features

* Create a new blog user
* Get all blogs
* Get a single blog by ID
* Update blog details
* Delete a blog
* Auto-generated Swagger UI for testing

---

## 🛠️ Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/) – Web framework
* [SQLAlchemy](https://www.sqlalchemy.org/) – ORM
* [PostgreSQL](https://www.postgresql.org/) – Database
* [Pydantic](https://docs.pydantic.dev/) – Data validation
* [Uvicorn](https://www.uvicorn.org/) – ASGI server

---

## 📂 Project Structure

```
📦 blog-api
├── main.py          # Entry point of the application
├── database.py      # Database configuration
├── model.py         # SQLAlchemy models
├── schema.py        # Pydantic schemas
├── blog.py          # CRUD service functions
├── router.py        # API routes
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/blog-api.git
cd blog-api
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Edit `database.py` and update the connection string with your PostgreSQL credentials:

```python
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/blog"
```

### 5. Run the Application

```bash
uvicorn main:app --reload
```

---

## 📑 API Endpoints

| Method | Endpoint                 | Description             |
| ------ | ------------------------ | ----------------------- |
| POST   | `/blog/create_blog`      | Create a new blog       |
| GET    | `/blog/get_all_blogs`    | Get all blogs           |
| GET    | `/blog/get_blog/{id}`    | Get a single blog by ID |
| PUT    | `/blog/update_blog/{id}` | Update a blog by ID     |
| DELETE | `/blog/delete_blog/{id}` | Delete a blog by ID     |

---

## 📝 Example Request

### Create Blog

```json
POST /blog/create_blog
Content-Type: application/json

{
  "user_name": "Ndelle Herbert",
  "user_email": "ndelleh04@gmail.com",
  "user_password": "HerbertGlory",
  "user_age": 26,
  "user_address": "Buea",
  "user_phone": 677602125,
  "on_offer": true
}
```

---

## 📖 Documentation

Once the app is running, visit:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📦 requirements.txt

```txt
fastapi==0.111.0
uvicorn[standard]==0.30.1
sqlalchemy==2.0.31
psycopg2-binary==2.9.9
pydantic==2.8.2
```

---

## 🤝 Contributing

Feel free to fork this repo and submit pull requests!

---

## 📜 License

This project is licensed under the MIT License.

---
