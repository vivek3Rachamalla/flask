from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'user1', 'pass1')
]

username_mappnig = {u.username: u for u in users}
id_mapping = {u.id: u for u in users}


def authentication(username, password):
    user = username_mappnig.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return id_mapping.get(user_id, None)
