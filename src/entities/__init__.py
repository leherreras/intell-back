from datetime import datetime

from sqlalchemy import create_engine, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB = 'intell_db'
DB_ENGINE_SQLITE = f'sqlite:///{DB}'
engine = create_engine(DB_ENGINE_SQLITE)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Entity:
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
