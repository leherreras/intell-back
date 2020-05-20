import flask_login
from flask import request, jsonify
from flask_classy import FlaskView

from .controller import create_user_platform, get_user, get_users


class UserView(FlaskView):
    # decorators = [flask_login.login_required]

    def post(self):
        data = request.form.to_dict()
        message = create_user_platform(data)
        return jsonify(message)

    def get(self, username):
        """
        Get the information of a user
        :param username: user's username
        :return:json with the user attributes.
        """
        user = get_user(username)
        return jsonify(user)

    def index(self):
        users = get_users()
        return jsonify(users)
