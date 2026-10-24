
import pytest

from strategy_checkout.checkout import Checkout
from strategy_checkout.models import Order
from strategy_checkout.shipping import (
    StandardShipping,
    ExpressShipping,
    PickupShipping,
    SameDayShipping,
)


def test_standard_shipping():
    order = Order(subtotal=500, weight_kg=2)
    checkout = Checkout(StandardShipping())

    assert checkout.shipping_cost(order) == 49.0
    assert checkout.total(order) == 549.0


def test_standard_shipping_free():
    order = Order(subtotal=1000, weight_kg=2)
    checkout = Checkout(StandardShipping())

    assert checkout.shipping_cost(order) == 0.0
    assert checkout.total(order) == 1000.0


def test_express_shipping():
    order = Order(subtotal=500, weight_kg=2)
    checkout = Checkout(ExpressShipping())

    assert checkout.shipping_cost(order) == 123.0
    assert checkout.total(order) == 623.0


def test_pickup_shipping():
    order = Order(subtotal=500, weight_kg=2)
    checkout = Checkout(PickupShipping())

    assert checkout.shipping_cost(order) == 0.0
    assert checkout.total(order) == 500.0


def test_same_day_shipping():
    order = Order(subtotal=500, weight_kg=3)
    checkout = Checkout(SameDayShipping())

    assert checkout.shipping_cost(order) == 203.0
    assert checkout.total(order) == 703.0
