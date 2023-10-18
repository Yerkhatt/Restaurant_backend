from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = '8888'
POSTGRES_SERVER = 'localhost'
POSTGRES_PORT = 5432
POSTGRES_DB = 'restaurant'
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
#"jdbc:postgresql://localhost:5432/BankDB"  example
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()