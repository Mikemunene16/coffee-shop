# Coffee Shop Domain Model

This project is a domain modeling exercise for a Coffee Shop using Object-Oriented Programming principles in Python. The goal is to represent the relationships between **Customers**, **Coffee**, and **Orders** in the system while applying clean code practices, ensuring validation, and handling data interactions effectively.

## Project Structure

The project consists of three main classes:
- **Customer**: Represents a coffee shop customer who can place multiple orders.
- **Coffee**: Represents a coffee that can be ordered multiple times by different customers.
- **Order**: Represents an individual order which links a customer, a coffee, and the price paid for that coffee.

### File Structure:
```
coffee_shop/
│
├── customer.py    # Contains the Customer class
├── coffee.py      # Contains the Coffee class
├── order.py       # Contains the Order class
├── tests/         # Contains test files for unit testing
│   ├── test_customer.py
│   ├── test_coffee.py
│   ├── test_order.py
├── README.md      # This README file
├── Pipfile        # Pipenv configuration file
├── Pipfile.lock   # Pipenv lock file
└── debug.py       # Optional file for manual testing and debugging
```

## Classes and Relationships

### 1. `Customer`
- **Attributes**:
  - `name`: A string representing the customer's name (1-15 characters).
- **Methods**:
  - `orders()`: Returns a list of all `Order` instances associated with the customer.
  - `coffees()`: Returns a unique list of `Coffee` instances the customer has ordered.
  - `create_order(coffee, price)`: Creates a new `Order` instance for the customer.

### 2. `Coffee`
- **Attributes**:
  - `name`: A string representing the coffee's name (minimum of 3 characters).
- **Methods**:
  - `orders()`: Returns a list of all `Order` instances for that coffee.
  - `customers()`: Returns a unique list of `Customer` instances who have ordered that coffee.
  - `num_orders()`: Returns the total number of orders for that coffee.
  - `average_price()`: Returns the average price for that coffee based on its orders.

### 3. `Order`
- **Attributes**:
  - `customer`: A `Customer` instance.
  - `coffee`: A `Coffee` instance.
  - `price`: A float representing the price (between 1.0 and 10.0).
- **Methods**:
  - `customer`: Returns the associated `Customer` instance.
  - `coffee`: Returns the associated `Coffee` instance.
  - `price`: Returns the price of the order.
- **Class Methods**:
  - `all_orders()`: Returns a list of all `Order` instances created.

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Mikemunene16/coffee-shop
cd coffee-shop
```

### 2. Set up Virtual Environment with Pipenv
Make sure you have `pipenv` installed, then run:
```bash
pipenv install
pipenv shell
```

### 3. Run the Tests
Unit tests for each class are provided in the `tests/` directory. You can run the tests using `pytest`:
```bash
pipenv install pytest
pytest
```

## Running the Debugger
You can use the `debug.py` file to test and debug code interactively.

## Features
- Object-Oriented Design principles
- Proper validation for attributes
- Supports customer-coffee ordering with real-time tracking of orders
- Aggregate methods for number of orders and average price per coffee
- Easy to extend and modify

## Bonus Features
A `most_aficionado(coffee)` method can be implemented in the `Customer` class to return the customer who has spent the most on a given coffee.
