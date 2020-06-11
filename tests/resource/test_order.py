import json
import unittest
from unittest.mock import patch

from flask_restful import marshal

from app.flask_application import FlaskApplication
from app.model.order import Order, order_fields
from app.repository.order_repository import OrderRepository
from tests.test_config import TestConfig

app = FlaskApplication.create_app(TestConfig)


class OrderResourceTests(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.test_client = app.test_client()

    def test_get_orders_request_should_return_status_code_200(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.test_client.get('/orders')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    @patch('app.resource.order.order_repository')
    def test_get_orders_request_should_return_list_of_orders_in_response_body(self, order_repository: OrderRepository):
        order1 = Order("1", 1000.0)
        order2 = Order("2", 50.0)

        order_repository.get_orders.return_value = [order1, order2]

        # sends HTTP GET request to the application
        # on the specified path
        result = self.test_client.get('/orders')
        actual_response = json.loads(result.get_data(as_text=True))

        expected_json = marshal([order1, order2], fields=order_fields)
        # assert the data in the response
        self.assertEqual(expected_json, actual_response)
