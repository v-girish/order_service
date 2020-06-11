from typing import List

from app.model.order import Order

order1 = Order("1", 100.0)
order2 = Order("2", 150.0)
orders = [order1, order2]


class OrderRepository:

    def get_orders(self) -> List[Order]:
        return orders

    def save_order(self, order: Order):
        orders.append(order)


order_repository = OrderRepository()
