import sqlite3

from flask import Flask, request
from flask_restful import Resource, reqparse
from model.user import UserModule


class Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="username field cant be empty"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="password field cant be empty"
                        )

    def post(self):
        data = Register.parser.parse_args()
        user = UserModule.find_by_user(data['username'])
        if user:
            return {'message': "username with '{}' already exists".format(data['username'])}

        user = UserModule(None, **data)
        user.insert_into()

        return {'message': 'you have been registered'}, 201
