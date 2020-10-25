from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    first_name = Column(String(64))
    last_name = Column(String(64))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
class Business(Base):
    __tablename__ = "businesses"
    id  = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    name = Column(String(64), index=True, unique = True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    
    def __repr__(self):
        return '<{}>'.format(self.name)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Comment(Base):
    __tablename__ = "comments"
    id  = Column(Integer, primary_key=True)
    text = Column(String(256))
    user_id = Column(Integer)
    
    def __repr__(self):
        return self.text
        
class BusinessComment(Base):
    __tablename__ = "business_comments"
    id = Column(Integer,primary_key=True)
    text = Column(String(256))
    business_id = Column(Integer)
    
    def __repr__(self):
        return self.text