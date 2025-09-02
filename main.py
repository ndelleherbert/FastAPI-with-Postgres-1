from typing import List, Optional
from fastapi import FastAPI
from database import SessionLocal
from main_model import Blog
import main_model
import model
import uvicorn


#An instance of our fastAPI
app = FastAPI(title="FastAPI with Postgresql")

#Base.metadata.create_all(bind=engine)

db = SessionLocal()


@app.get("/blog", response_model=List[Blog], status_code=200)
async def get_all_blogs():
    blogs = db.query(model.Blog).all()
    return list[blogs]


@app.get("/blog/{user_id}", response_model=main_model.sub_blog, status_code=200)
async def get_a_blog():
    blogs = db.query(model.Blog).all()
    return blogs


@app.post("/add_blog", response_model=main_model.sub_blog, status_code=200)
async def create_a_blog(blog: main_model.Blog ):
    blogs = model.Blog(
        name=blog.user_name,
        uemail=blog.user_email,
        password=blog.user_password,
        age=blog.user_age,
        address=blog.user_address,
        phone=blog.user_phone,
        on_offer=blog.on_offer
    )

    db.add(blogs)
    db.commit()
    db.refresh(blogs)

    return blogs


@app.put("/blog/{user_id}", response_model=Blog, status_code=200)
async def update_a_blog(user_id: int, blog: Blog):
    blog_to_update = db.query(model.Blog).filter(model.Blog.id == user_id).update()
    blog_to_update.user_id = blog.user_id
    blog_to_update.user_name = blog.user_name
    blog_to_update.user_email = blog.user_email
    blog_to_update.user_password = blog.user_password
    blog_to_update.user_age = blog.user_age
    blog_to_update.user_address = blog.user_address
    blog_to_update.user_phone = blog.user_phone
    blog_to_update.on_offer = blog.on_offer

    db.commit()

    return blog_to_update


@app.delete("/blog/{user_id}", response_model=Blog, status_code=200)
async def delete_a_blog(user_id: int, blog: Blog):
    blogs = db.query(model.Blog).filter(model.Blog.id == user_id).first()

    db.commit()

    return f"Item with id {blogs.user_id} has been deleted"
