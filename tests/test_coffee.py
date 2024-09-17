# tests/test_coffee.py
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_creation():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_orders():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    order = Order(customer, coffee, 5.5)
    assert coffee.num_orders() == 1
    assert coffee.average_price() == 5.5
