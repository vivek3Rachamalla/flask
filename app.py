from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.register import Register
from security import authentication, identity
from resources.item import Item, ItemsList
from resources.store import Store

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'vivek'
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app, authentication, identity)

api.add_resource(Item, '/items/<string:name>')
api.add_resource(Store, '/stores/<string:name>')
api.add_resource(ItemsList, '/item')
api.add_resource(Register, '/register')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000)
