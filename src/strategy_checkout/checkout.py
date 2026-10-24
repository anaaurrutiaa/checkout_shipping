
from .models import Order
from .shipping import ShippingCostStrategy


class Checkout:

    def __init__(self, strategy: ShippingCostStrategy):
        self.strategy = strategy

    def shipping_cost(self, order: Order) -> float:
        return self.strategy.calculate(order)

    def total(self, order: Order) -> float:
        return order.subtotal + self.shipping_cost(order)
