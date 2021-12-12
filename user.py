import sqlite3


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_user(cls, username):
        connection = sqlite3.Connection('data.db')
        curser = connection.cursor()

        sql = "SELECT * FROM users WHERE username = ?"
        result = curser.execute(sql, (username,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.Connection('data.db')
        curser = connection.cursor()

        sql = "SELECT * FROM users WHERE id = ?"
        result = curser.execute(sql, (_id,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user
