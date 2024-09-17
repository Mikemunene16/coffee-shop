
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_creation():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.5
