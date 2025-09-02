# FastAPI with PostgreSQL

[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/ndelleherbert/FastAPI-with-Postgres-1)

This repository contains a simple REST API built with FastAPI that performs CRUD (Create, Read, Update, Delete) operations for blog entries stored in a PostgreSQL database.

## Features

*   **FastAPI Framework**: Leverages the high-performance FastAPI web framework.
*   **PostgreSQL Database**: Uses PostgreSQL as the backend database.
*   **SQLAlchemy ORM**: Interacts with the database using the SQLAlchemy Core and ORM.
*   **Pydantic Models**: Enforces data validation and serialization for requests and responses.
*   **CRUD Operations**: Provides endpoints to manage blog resources.

## Project Structure

```
.
├── create_db.py     # Script to initialize database tables
├── database.py      # Database connection and session management
├── main.py          # Main FastAPI application with API routes
├── main_model.py    # Pydantic model for data validation
└── model.py         # SQLAlchemy ORM model for the 'Blog' table
```

## Prerequisites

*   Python 3.8+
*   PostgreSQL
*   pip

## Setup and Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/ndelleherbert/fastapi-with-postgres-1.git
    cd fastapi-with-postgres-1
    ```

2.  **Install the required Python packages:**
    ```sh
    pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
    ```

3.  **Set up the PostgreSQL Database:**
    *   Make sure you have PostgreSQL installed and running.
    *   Create a new database named `blog`.
    *   The application uses the following connection string, which is hardcoded in `database.py`:
        ```
        postgresql://postgres:admin@localhost/blog
        ```
    *   If your PostgreSQL username, password, or host differs, please update this line in `database.py` accordingly.

4.  **Create the Database Table:**
    Run the `create_db.py` script to create the `Blog` table in your database based on the SQLAlchemy model.
    ```sh
    python create_db.py
    ```

## Running the Application

Start the development server using Uvicorn. The `--reload` flag will automatically restart the server upon code changes.

```sh
uvicorn main:app --reload --port 6000
```

The API will be available at `http://127.0.0.1:6000`. You can access the interactive API documentation (Swagger UI) at `http://127.0.0.1:6000/docs`.

## API Endpoints

The following endpoints are available to interact with the blog data.

| Method | Endpoint             | Description                            |
| :----- | :------------------- | :------------------------------------- |
| `GET`  | `/blog`              | Retrieve a list of all blog entries.   |
| `GET`  | `/blog/{user_id}`    | Retrieve a single blog entry by its ID.|
| `POST` | `/add_blog`          | Create a new blog entry.               |
| `PUT`  | `/blog/{user_id}`    | Update an existing blog entry by its ID.|
| `DELETE`| `/blog/{user_id}`  | Delete a blog entry by its ID.         |

### Example Payloads

**`POST /add_blog`** or **`PUT /blog/{user_id}`**

```json
{
  "user_id": 1,
  "user_name": "example_user",
  "user_email": "user@example.com",
  "user_password": "securepassword123",
  "user_age": 30,
  "user_address": "123 Main St",
  "user_phone": 1234567890,
  "on_offer": false
}
