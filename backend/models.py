from sqlalchemy import Column, Integer, String
from database import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)
    text = Column(String)
