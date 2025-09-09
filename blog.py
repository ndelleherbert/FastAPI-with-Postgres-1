import model,schema
from sqlalchemy.orm import Session


def create_blog(db:Session, my_blog:schema.CreateBlog):
    blogs = model.Blog(**my_blog.model_dump())

    db.add(blogs)
    db.commit()
    db.refresh(blogs)
    return blogs

def get_all_blog(db:Session):
    blogs = db.query(model.Blog).all()
    return blogs

def get_blog(db:Session,id:int):
    blogs = db.query(model.Blog).filter(model.Blog.user_id == id).first()
    return blogs

def update_blog(id:int,my_blog:schema.UpdateBlog,db:Session):
    blogs = get_blog(db,id)
    if blogs:
        for key, value in my_blog.model_dump().items():
            setattr(blogs,key,value)
            db.add(blogs)
            db.commit()
            db.refresh(blogs)
    return blogs

def delete_blog(id:int, db:Session):
    blogs = get_blog(db,id)
    db.delete(blogs)
    db.commit()
    return "Blog deleted"