from sqlalchemy import Column, Integer, Text, String, DateTime
from database.database import Base

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    title = Column(String(150))
    content = Column(Text())
    date = Column(DateTime())

    def __repr__(self):
        return self.title
