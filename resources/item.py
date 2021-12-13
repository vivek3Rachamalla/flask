from flask_restful import Resource, Api, reqparse
from flask_jwt import jwt_required
from model.itemModel import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="field cant be empty"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="field cant be empty"
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return {'message': "no item with name '{}'".format(name)}

    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {'message': "item with name '{}' already exists".format(name)}, 404
        data = Item.parser.parse_args()
        new_item = ItemModel(name, **data)
        new_item.insert_item()
        return new_item.json()

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item is None:
            return {'message': "there is no item with name '{}".format(name)}
        item.delete_item()
        return {'message': 'item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            try:
                new_item = ItemModel(name, **data)
                new_item.insert_item()
            except:
                return {'message': 'some thing went wrong'}
        else:
            try:
                item.price = data['price']
                item.update_item()
            except:
                return {'message': 'some thing went wrong'}
        return {'message': 'changes saved'}


class ItemsList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
