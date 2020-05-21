from flask import Flask, url_for, redirect
from flask_cors import CORS
from flask_login import LoginManager

from apps.authentication.api import LoginView
from apps.manage_books.api import BookView
from apps.manage_users.api import UserView
from comming.install import first_user
from entities import Base, engine

app = Flask(__name__)
CORS(app)

app.secret_key = b'_6#y2L"F4Q9z\n\xec]/'

login_manager = LoginManager()
login_manager.init_app(app)

# if needed, generate database schema
Base.metadata.create_all(engine)

first_user()


@app.route('/')
def root():
    return redirect(url_for("BookView:index"))


LoginView.register(app)
UserView.register(app)
BookView.register(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
