from flask_login import UserMixin
from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer

from comming.utils import encrypt_password, password_validate
from entities import Entity, Base


class User(UserMixin, Entity, Base):
    __tablename__ = 'users'

    id_user = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, username, password, first_name, last_name, **kwargs):
        Entity.__init__(self)
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def get_id(self):
        return self.id_user

    def set_password(self, password):
        self.password = encrypt_password(password)

    def check_password(self, password_plain):
        return password_validate(password_plain, self.password)


class UserSchema(Schema):
    id_user = fields.Number()
    username = fields.Str()
    password = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
