from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    user_name: str
    user_email: str
    user_password: str
    user_age: int
    user_address: Optional[str] = None
    user_phone: Optional[int] = None
    on_offer: Optional[bool] = False


class sub_blog(Blog):
    id : int

class create_blog(Blog):
    pass

class update_blog(Blog):
    pass

class delete_blog(Blog):
    pass

class get_blog(sub_blog):
    pass




    class Config:
        orm_mode = True
    