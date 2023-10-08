from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    lastname = Column(String(25), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    birth_date = Column(Date, nullable=False)




