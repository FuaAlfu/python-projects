#to be..
#TODO

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self,name):
        data=request.get_json()
        item=next(filter(lambda x:x['name']==name ,items),None)
        if item is None:
            item={'name':name,'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        
api.add_resource(Item,'/item/<string:name>')

app.run(port=5000)