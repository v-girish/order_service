from flask_restful import reqparse


class OrderRequestParser:
    __parser = reqparse.RequestParser()

    @classmethod
    def create_order_parser(cls):
        cls.__parser.add_argument('order_id', type=str, required=True)
        cls.__parser.add_argument('total_price', type=float, required=True)
        return cls.__parser.copy()


order_parser = OrderRequestParser.create_order_parser()
