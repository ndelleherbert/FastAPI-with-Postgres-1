from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    user_id: int
    user_name: str
    user_email: str
    user_password: str
    user_age: int
    user_address: Optional[str] = None
    user_phone: Optional[int] = None
    on_offer: Optional[bool] = False

    class Config:
        orm_mode = True
    