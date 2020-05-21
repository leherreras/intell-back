import flask_login

from entities import Session
from entities.users import User, UserSchema


def authenticate(username, password):
    if not username:
        return None
    # fetching from the database
    session = Session()
    user_objects = session.query(User).filter_by(username=username).limit(1)

    schema = UserSchema(many=True)
    user = schema.dump(user_objects)
    session.close()
    if not user:
        return None
    user_internal = User(**user[0])
    if user_internal.check_password(password):
        flask_login.login_user(user_internal)
        return user[0]

