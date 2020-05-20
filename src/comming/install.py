from apps.manage_users.controller import create_user_platform, get_users


def first_user():
    users = get_users()
    if not users:
        data = {
            "username": "intell",
            "password": "12345",
            "first_name": "Intell",
            "last_name": "Next",
        }
        create_user_platform(data)
