from flask import Flask
from flask_login import LoginManager

from apps.authentication.api import LoginView
from apps.manage_books.api import BookView
from apps.manage_users.api import UserView
from comming.install import first_user
from entities import Base, engine

app = Flask(__name__)

app.secret_key = b'_6#y2L"F4Q9z\n\xec]/'

login_manager = LoginManager()
login_manager.init_app(app)

# if needed, generate database schema
Base.metadata.create_all(engine)

first_user()


@app.route('/')
def hello_world():
    return 'Hello World!'


LoginView.register(app)
UserView.register(app)
BookView.register(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
