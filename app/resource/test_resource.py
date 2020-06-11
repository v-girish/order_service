from flask_restful import Resource

from app.exception.custom_exception import OrderDoesNotExist


class TestResource(Resource):
    def get(self):
        raise OrderDoesNotExist("Order does not exist")
