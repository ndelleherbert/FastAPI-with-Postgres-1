import model
import schema
from sqlalchemy.orm import session


def create_blog(db:session, my_blog:schema.create_blog):
    blog = model.Blog(**my_blog.model_dump())

    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def get_all_blogs(db:session):
    blog = db.query(model.Blog).all()
    return blog

def get_blog(db:session,id:int):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()

    return blog

def update_blog(id:int,my_blog:schema.update_blog,db:session):
    blog = get_blog(db,id)
    if blog:
        for key, value in my_blog.model_dump().items:
            setattr(blog,key,value)

            db.commit()
            db.refresh(blog)
    return blog

def delete_blog(id:int, db:session):
    blog = get_blog(db,id)
    db.delete(blog)
    db.commit()
    db.refresh(blog)
    return "Blog deleted"