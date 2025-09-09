from fastapi import Depends, APIRouter
from sqlalchemy.orm import session
import database,schema,blog




Router = APIRouter(prefix="/blog", tags =["blog"])

def get_db():
    db = database.SessionLocal
    try:
        yield db
    finally:
        db.close()


@Router.post("/", response_model = schema.Blog)
async def create_blog(my_blog:schema.create_blog,db:session=Depends(get_db)):
    return blog.create_blog(db,my_blog)



@Router.get("/", response_model=schema.Blog)
async def get_blog(id:int, db:session = Depends(get_db)):
    return blog.get_blog(db,id)



@Router.get("/", response_model=schema.Blog)
async def get_all_blog(db:session=Depends(get_db)):
    return blog.get_all_blogs(db)



@Router.put("/", response_model = schema.Blog)
async def update_blog(my_blog:schema.update_blog,id:int,db:session = Depends(get_db)):
    return blog.update_blog(db,id,my_blog)



@Router.delete("/", response_model =schema.Blog)
async def delete_blog(db:session=Depends(get_db)):
    return blog.delete_blog(db,id)