from typing import Optional
from datetime import datetime
from pydantic import BaseModel




class Client(BaseModel):
	name: str
	surname: str
	phone_number: str


class TableReservation(BaseModel):
    client_id: int
    table_id: int
    # reservation_date: str  /date will be assigned automatically
    target_reservation_date: str


class Table(BaseModel):
    manager_id : int
    table_number : int
    location : str

class Order(BaseModel):
    table_id : int
    order_date : str
    
class Request(BaseModel):
    order_id : int
    dish_id : int


class Manager(BaseModel):
    name : Optional[str]
    surname : Optional[str]
    phone_number : Optional[str]

class Menu(BaseModel):
    name : str
    price : int
    origin : str
