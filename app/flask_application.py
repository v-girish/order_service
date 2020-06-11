import logging
import os
from logging.config import fileConfig
from typing import Type

import yaml
from flask import Flask
from flask_restful import Api

from app.exception.error_handler import errors
from app.resource.order import OrderResource
from app.resource.test_resource import TestResource
from app.config.config import Config


class FlaskApplication:

    @staticmethod
    def create_app(config: Type[Config]):
        FlaskApplication.setup_logging()

        app = Flask(__name__)
        app.config.from_object(config)

        FlaskApplication.add_resources(app)

        return app

    @staticmethod
    def add_resources(app):
        api = Api(app, errors=errors)
        api.add_resource(OrderResource, '/orders')
        api.add_resource(TestResource, '/test')

    @staticmethod
    def setup_logging():
        path = os.path.dirname(os.path.realpath(__file__))

        # Config file relative to this file
        logging_conf = open(f'{path}/logging_config.yaml', 'r')
        logging.config.dictConfig(yaml.load(logging_conf, Loader=yaml.FullLoader))
        logging_conf.close()
