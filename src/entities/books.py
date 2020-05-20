from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, DateTime

from entities import Entity, Base


class Book(Entity, Base):
    __tablename__ = 'books'

    id_book = Column(Integer, primary_key=True)
    title = Column(String)
    publication_date = Column(DateTime)

    def __init__(self, title, publication_date):
        Entity.__init__(self)
        self.title = title
        self.publication_date = publication_date


class BookSchema(Schema):
    id_book = fields.Number()
    title = fields.Str()
    publication_date = fields.DateTime()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
