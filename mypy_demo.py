"""
This module contains utility functions for basic arithmetic operations and greeting.
It demonstrates the use of type hints and docstrings for better code documentation.
"""

def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b


def greet(name: str) -> str:
    """Greets the person with the provided name."""
    return f"Hello, {name}!"


def divide(a: int, b: int) -> float:
    """Divides a by b and returns a float."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# Function calls
print(add(3, 5))  # Expected output: 8
print(greet("Alice"))  # Expected output: "Hello, Alice!"
print(divide(10, 2))  # Expected output: 5.0
