from flask_restful import Resource
from flask_restful import marshal_with

from app.model.order import order_fields, Order
from app.parser.order_request_parser import order_parser
from app.repository.order_repository import order_repository
import logging


class OrderResource(Resource):

    def __init__(self):
        self.logger = logging.getLogger()

    @marshal_with(order_fields)
    def get(self):
        self.logger.info("Getting list of orders from repository")
        return order_repository.get_orders()

    @marshal_with(order_fields)
    def put(self):
        args = order_parser.parse_args()
        new_order = Order(**args)
        order_repository.save_order(new_order)
        return new_order
