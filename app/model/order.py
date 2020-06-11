from __future__ import annotations

from flask_restful import fields


class Order:
    def __init__(self, order_id: str, total_price: float):
        self.__order_id = order_id
        self.__total_price = total_price

    @property
    def order_id(self) -> str: return self.__order_id

    @property
    def total_price(self) -> float: return self.__total_price

    def __str__(self):
        return f'{{order_id: {self.__order_id}, total_price: {self.__total_price}}}'

    def __repr__(self):
        return self.__str__()


order_fields = {
    'order_id': fields.String,
    'total_price': fields.Float
}


