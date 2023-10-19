from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Date

class Menu(Base):
    __tablename__ = 'Menu'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    origin = Column(String)

class Client(Base):
    __tablename__ = 'Client'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(String)

class Manager(Base):
    __tablename__ = 'Manager'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(String)


class TableReservation(Base):
    __tablename__ = 'TableReservation'
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('Client.id'))
    table_id = Column(Integer, ForeignKey('Table.id'))
    reservation_date = Column(DateTime)
    target_reservation_date = Column(DateTime) 
    

class Table(Base):
    __tablename__ = "Table"
    id = Column(Integer, primary_key=True, index=True)
    table_number = Column(Integer)
    manager_id = Column(Integer, ForeignKey('Manager.id'))
    location = Column(String)

class Order(Base):
    __tablename__ = 'Order'
    id = Column(Integer, primary_key=True, index=True)
    table_id = Column(Integer, ForeignKey('Table.id'))
    order_date = Column(DateTime)

class Request(Base):
    __tablename__ = 'Request'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('Order.id', ondelete='CASCADE'))
    dish_id = Column(Integer, ForeignKey('Menu.id'))

