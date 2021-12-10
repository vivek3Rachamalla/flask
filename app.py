from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authentication, identity

app = Flask(__name__)
app.secret_key = 'vivek'
api = Api(app)

jwt = JWT(app, authentication, identity)

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="field cant be empty"
                        )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'items': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "item with name '{}' already exists".format(name)}, 404

        data = Item.parser.parse_args()
        new_item = {
            'name': name,
            'price': data['price']
        }
        items.append(new_item)
        return new_item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            new_item = {'name': name, 'price': data['price']}
            items.append(new_item)
        else:
            item.update(data)
        return item


class ItemsList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemsList, '/item')

app.run(port=5000)
