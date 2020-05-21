from entities import Session
from entities.users import UserSchema, User


def create_user_platform(data):
    posted_user = UserSchema(only=('username', 'password', 'first_name', 'last_name'))\
        .load(data)

    user = User(**posted_user)
    user.set_password(data['password'])

    session = Session()

    user_objects = session.query(User).filter_by(username=data['username']).limit(1)
    schema = UserSchema(many=True)
    user_old = schema.dump(user_objects)
    if user_old:
        return

    session.add(user)
    session.commit()

    new_user = UserSchema().dump(user)
    session.close()

    return {'info': 'Save user in DB'}


def get_user(username):
    session = Session()
    user_objects = session.query(User).filter_by(username=username).limit(1)

    schema = UserSchema(many=True)
    user = schema.dump(user_objects)
    session.close()
    return user


def get_users():
    session = Session()
    users_objects = session.query(User).all()

    schema = UserSchema(many=True)
    users = schema.dump(users_objects)
    session.close()
    return users
