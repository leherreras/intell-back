from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from entities import Entity, Base


class Comment(Entity, Base):
    __tablename__ = 'comments'

    id_comment = Column(Integer, primary_key=True)
    text = Column(String)
    id_book = Column(Integer, ForeignKey('books.id_book'))
    id_user = Column(Integer, ForeignKey('users.id_user'))

    def __init__(self, text, id_book, id_user):
        Entity.__init__(self)
        self.text = text
        self.id_book = id_book
        self.id_user = id_user


class CommentSchema(Schema):
    id_comment = fields.Number()
    text = fields.Str()
    id_book = fields.Int()
    id_user = fields.Int()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
