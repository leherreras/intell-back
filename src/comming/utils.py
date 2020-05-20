import base64
from hashlib import md5


def encrypt_password(password):
    return base64.b64encode(md5(password.encode()).digest()).decode()


def password_validate(password_plain, password_2):
    """
    Check if the passwords match
    :param password_plain:
    :param password_2:
    :return:
    """
    password_1 = encrypt_password(password_plain)
    return password_2 == password_1
