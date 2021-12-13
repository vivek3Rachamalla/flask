from model.user import UserModule


def authentication(username, password):
    user = UserModule.find_by_user(username)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModule.find_by_id(user_id)
