import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(10), unique=True, nullable=False)
    email = Column(String(25), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    likes = relationship ("Like")
    posts = relationship('Post')
    follower = relationship('Follower', foreign_keys='Follower.user_to_id')
    following = relationship('Follower', foreign_keys='Follower.user_from_id')
    comment = relationship('Comment')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    media = relationship('Media')
    comments = relationship('Comment')
    likes = relationship('Like')
   


class Media(Base):
    __tablename__ = 'Media'   
    id = Column(Integer,primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    media_type = Column(String(50), nullable=False)
    url = Column(String(250), nullable=False)
    post = relationship('Post')



class Follower (Base):
    __tablename__='follower'
    id = Column(Integer,primary_key = True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)  
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False) 
    follower_user = relationship('User', foreign_keys=[user_from_id])
    followed_user = relationship('User', foreign_keys=[user_to_id])


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    post = relationship('Post')
    

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    post = relationship('Post')    
    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
