from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Date

class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    origin = Column(String)

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    gender = Column(String)
    phone_number = Column(Integer)

class TableReservation(Base):
    __tablename__ = 'TableReservation'
    id = Column(Integer, primary_key=True, index=True)
    table_id = Column(Integer, ForeignKey(''))
    date = Column(Date)

class Table(Base):
    id = Column(Integer, primary_key=True, index=True)
    manager_id = (Integer, ForeignKey(''))
    location = Column(String)

class Order()