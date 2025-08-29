from sqlalchemy import Column, String, Integer, Boolean
from database import Base

class Blog(Base):
    __tablename__ = "Blog"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255), nullable=False, unique=True)
    user_email = Column(String, nullable=False, unique=True)
    user_password = Column(String, nullable=False, unique=True)
    user_age = Column(Integer, nullable=False)
    user_address = Column(String)
    user_phone = Column(Integer)
    on_offer = Column(Boolean, default = False)

    # representational method for our object model of our blog class
    def __repr__(self):
        return f"Blog(user_id={self.user_id}, user_name={self.user_name}, user_email={self.user_email}, user_password={self.user_password}, user_age={self.user_age}, user_address={self.user_address}, user_phone={self.user_phone}, on_offer={self.on_offer})"