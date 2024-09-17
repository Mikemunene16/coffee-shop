# customer.py

class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Customer name must be a string between 1 and 15 characters.")
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        from order import Order  # Delayed import to avoid circular imports
        return [order for order in Order.all_orders() if order.customer == self]

    def coffees(self):
        from order import Order  # Delayed import to avoid circular imports
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from order import Order  # Delayed import to avoid circular imports
        return Order(self, coffee, price)
