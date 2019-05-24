from sqlalchemy import Column, Integer, Text, String, DateTime
from .database import Base

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    content = Column(Text())
    date = Column(DateTime())
