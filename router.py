from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
import database, schema, blog

Router = APIRouter(prefix="/blog", tags=["blog"])

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Blog
@Router.post("/create_blog", response_model=schema.Blog)
async def create_blog(my_blog: schema.CreateBlog, db: Session = Depends(get_db)):
    return blog.create_blog(db, my_blog)

# Get All Blogs
@Router.get("/get_all_blogs", response_model=list[schema.Blog])
async def get_all_blog(db: Session = Depends(get_db)):
    return blog.get_all_blog(db)

# Get One Blog
@Router.get("/get_blog/{id}", response_model=schema.Blog)
async def get_blog(id: int, db: Session = Depends(get_db)):
    return blog.get_blog(db, id)

# Update Blog
@Router.put("/update_blog/{id}", response_model=schema.Blog)
async def update_blog(id: int, my_blog: schema.UpdateBlog, db: Session = Depends(get_db)):
    return blog.update_blog(db, id, my_blog)

# Delete Blog
@Router.delete("/delete_blog/{id}")
async def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog.delete_blog(db, id)
