from customer import Customer
from coffee import Coffee
from order import Order

john = Customer("John")
latte = Coffee("Latte")
john.create_order(latte, 5.0)

print(john.orders())
print(latte.customers())
