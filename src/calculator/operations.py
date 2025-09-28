"""Mathematical operations module for the calculator application."""

from .exceptions import DivisionByZeroError


class Operations:
    """Handles arithmetic operations for the calculator."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Add two numbers.

        Args:
            a: First number.
            b: Second number.

        Returns:
            The sum of a and b.
        """
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """
        Subtract the second number from the first.

        Args:
            a: First number (minuend).
            b: Second number (subtrahend).

        Returns:
            The difference of a and b.
        """
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """
        Multiply two numbers.

        Args:
            a: First number.
            b: Second number.

        Returns:
            The product of a and b.
        """
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """
        Divide the first number by the second.

        Args:
            a: First number (dividend).
            b: Second number (divisor).

        Returns:
            The quotient of a and b.

        Raises:
            DivisionByZeroError: If b is zero.
        """
        if b == 0:
            raise DivisionByZeroError()
        return a / b

    @staticmethod
    def calculate(operation: str, a: float, b: float) -> float:
        """
        Perform the specified operation on two numbers.

        Args:
            operation: The operation to perform (+, -, *, /).
            a: First number.
            b: Second number.

        Returns:
            The result of the calculation.

        Raises:
            DivisionByZeroError: If dividing by zero.
            ValueError: If operation is not supported.
        """
        operations_map = {
            "+": Operations.add,
            "-": Operations.subtract,
            "*": Operations.multiply,
            "/": Operations.divide,
        }

        if operation not in operations_map:
            raise ValueError(f"Unsupported operation: {operation}")

        return operations_map[operation](a, b)
