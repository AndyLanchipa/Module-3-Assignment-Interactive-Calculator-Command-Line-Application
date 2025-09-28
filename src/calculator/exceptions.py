"""Custom exceptions for the calculator application."""


class CalculatorError(Exception):
    """Base exception class for calculator errors."""

    pass


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""

    def __init__(self, message: str = "Division by zero is not allowed.") -> None:
        self.message = message
        super().__init__(self.message)


class InvalidOperationError(CalculatorError):
    """Raised when an invalid operation is provided."""

    def __init__(self, operation: str) -> None:
        self.operation = operation
        self.message = (
            f"Invalid operation: '{operation}'. Supported operations: +, -, *, /"
        )
        super().__init__(self.message)


class InvalidNumberError(CalculatorError):
    """Raised when an invalid number is provided."""

    def __init__(self, value: str) -> None:
        self.value = value
        self.message = f"Invalid number: '{value}'. Please enter a valid number."
        super().__init__(self.message)
