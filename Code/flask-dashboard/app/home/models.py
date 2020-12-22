from sqlalchemy import Column, Integer, String
from app import db

class Video(db.Model):

    __tablename__ = 'Video'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    path = Column(String, unique=True)

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __repr__(self):
        return str(self.name)
