import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    create = Column(DateTime)
    update = Column(DateTime)
    active = Boolean

class Album(Base):
    __tablename__= "album"
    id = Column(Integer, primary_key=True)
    tittle = Column(String(250), nullable=False)
    description = Column(String(250))
    id_user = Column (Integer, ForeignKey("user.id"))
    user = relationship(User)

class Post(Base):
    __tablename__= "post"
    id = Column(Integer, primary_key=True)
    tittle = Column(String(250), nullable=False)
    description = Column(String(250))
    create = Column(DateTime)
    update = Column(DateTime)
    id_user = Column (Integer, ForeignKey("user.id"))
    user = relationship(User)
    id_album = Column (Integer, ForeignKey("album.id"))
    album = relationship(Album)
    photo_url = Column(String(250))
    type = Column(String(250))
    total_likes = Column(Integer)
    total_comments = Column(Integer)


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    content = Column(String(250))
    post_date = Column(DateTime)
    id_user = Column (Integer, ForeignKey("user.id"))
    user = relationship(User)
    id_post = Column (Integer, ForeignKey("post.id"))
    post = relationship(Post)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e