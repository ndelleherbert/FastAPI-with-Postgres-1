from typing import List, Optional
from fastapi import FastAPI
from database import SessionLocal
from model import Blog
import model

#An instance of our fastAPI
app = FastAPI(title = "FastAPI with Postgresql")

#Base.metadata.create_all(bind=engine)

db = SessionLocal()


@app.get("/blog", response_model=List[Blog], status_code=200)
async def get_all_blogs():
    blogs = db.query(model.Blog).all()

    return blogs

@app.get("/blog/{user_id}")
async def get_a_blog(user_id: int) -> int:
    pass

@app.post("/blog")
async def create_a_blog():
    pass

@app.put("/blog/{user_id}")
async def update_a_blog(user_id:int):
    pass

@app.delete("/blog/{user_id}")
async def delete_a_blog(user_id:int):
    pass


