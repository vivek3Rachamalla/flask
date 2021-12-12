from werkzeug.security import safe_str_cmp
from user import User


def authentication(username, password):
    user = User.find_by_user(username)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
