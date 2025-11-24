from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

Base = declarative_base()

class Faq(Base):

    __tablename__ = "faq_manager"

    Question_id = Column(Integer,primary_key=True)
    Question = Column(String)
    Answer = Column(String)