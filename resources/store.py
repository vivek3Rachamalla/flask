from flask_restful import Resource, Api, reqparse
from model.storeModel import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': "no store with name '{}'".format(name)}

    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message': "store with name '{}' already exists".format(name)}

        store = StoreModel(name)
        try:
            store.insert_store()
        except:
            return {'message': 'some thing went wrong'}

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_store()
            return {'message': 'store deleted'}

        return {'message': "store with name '{}' does not exist".format(name)}
