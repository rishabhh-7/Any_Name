"""Simple math operations and class demo for pylint workflow."""

import math


def add_numbers(a: int, b: int) -> int:
    """Return sum of two integers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return difference of two integers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return product of two integers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return division result, handles division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed")
        return float("inf")


def circle_area(radius: float) -> float:
    """Return area of a circle given radius."""
    return math.pi * radius * radius


class MyClass:
    """Demo class with value attribute."""

    def __init__(self, value: int):
        self.value = value

    def print_value(self) -> None:
        """Print stored value."""
        print("Value is:", self.value)


def main() -> None:
    """Run sample operations and class demo."""
    a, b = 10, 0
    print(add_numbers(a, b))
    print(subtract(a, b))
    print(multiply(a, b))
    print(divide(a, b))
    obj = MyClass(42)
    obj.print_value()


if __name__ == "__main__":
    main()

