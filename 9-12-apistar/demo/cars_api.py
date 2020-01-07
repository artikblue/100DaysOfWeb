from apistar import App, Route, types, validators
from apistar_mongoengine.components import MongoClientComponent
from apistar_mongoengine.models import Document
from mongoengine import StringField, IntField
from json import JSONEncoder

class Car(Document):
    meta = {"collection":"cars1"}
    id_ = IntField(db_field='id')
    car_model = StringField()
    car_make = StringField()
    car_color = StringField()
    car_vin = StringField()


def list_items():
    return [item.to_json() for item in Car.objects.all()]

routes = [
    Route(url='/', method='GET', handler=list_items),
]
components = [
    MongoClientComponent(host='mongodb://localhost:27017/cars'),
]

app = App(routes=routes, components=components)

if __name__ == '__main__':
    app.serve(host='127.0.0.1', port=5000, debug=True)