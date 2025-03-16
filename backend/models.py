from sqlalchemy import Column, Integer, String
from database import Base

class Storyboard(Base):
    __tablename__ = "storyboards"

    id = Column(Integer, primary_key = True, indes = True)
    title = Column(String, index = True)
    descripton = Column(String)