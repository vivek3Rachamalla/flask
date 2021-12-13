import sqlite3

from flask import Flask, request
from flask_restful import Resource


class Register(Resource):
    def post(self):
        data = request.get_json()
        connection = sqlite3.Connection('data.db')
        cursor = connection.cursor()

        all_users = "SELECT * FROM users WHERE username = ?"
        row = cursor.execute(all_users, (data['username'],))
        if row:
            return {'message': "username with '{}' already exists".format(data['username'])}

        user_insert = "INSERT INTO users VALUES(NULL, ?, ?)"
        cursor.execute(user_insert, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {'message': 'you have been registered'}, 201
