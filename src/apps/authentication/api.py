from flask import request, jsonify, abort
from flask_classy import FlaskView

from .controller import authenticate


class LoginView(FlaskView):

    def post(self):
        """
        Send the private information for login
        :return: confirmation message
        """
        result = authenticate(request.form.get('username'), request.form.get('password'))
        if result:
            result.pop('password')
            return jsonify(result)
        else:
            return abort(401)

# class LogoutView(FlaskView):
#     decorators = [flask_login.login_required]
#
#     @route('/', methods=['POST', 'GET'])
#     def index(self):
#         """
#         Logout the user from the platform
#         :return:
#         """
#         flask_login.logout_user()
#         return redirect({}, url_for('LoginView:index'))
