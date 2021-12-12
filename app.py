from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from register import Register
from security import authentication, identity
from item import Item, ItemsList

app = Flask(__name__)
app.secret_key = 'vivek'
api = Api(app)

jwt = JWT(app, authentication, identity)

api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemsList, '/item')
api.add_resource(Register, '/register')

app.run(port=5000)
