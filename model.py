from sqlalchemy import Column, String, Integer, Boolean
from database import Base

class Blog(Base):
    __tablename__ = "Blog"

    user_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_name = Column(String(255), nullable=False, unique=True, index=True)
    user_email = Column(String, nullable=False, unique=True)
    user_password = Column(String, nullable=False)
    user_age = Column(Integer, nullable=False)
    user_address = Column(String)
    user_phone = Column(Integer)
    on_offer = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Blog(user_id={self.user_id}, user_name={self.user_name})>"
