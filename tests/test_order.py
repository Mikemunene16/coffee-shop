# tests/test_order.py
from coffee import Coffee
from customer import Customer
from order import Order

def test_order_creation():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.5
