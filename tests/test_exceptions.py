"""Test module for calculator exceptions."""

import pytest
from src.calculator.exceptions import (
    CalculatorError,
    DivisionByZeroError,
    InvalidOperationError,
    InvalidNumberError,
)


class TestCalculatorError:
    """Test cases for CalculatorError base exception."""

    def test_calculator_error_is_exception(self) -> None:
        """Test that CalculatorError is an Exception."""
        error = CalculatorError("Test error")
        assert isinstance(error, Exception)
        assert str(error) == "Test error"


class TestDivisionByZeroError:
    """Test cases for DivisionByZeroError."""

    def test_division_by_zero_error_default_message(self) -> None:
        """Test DivisionByZeroError with default message."""
        error = DivisionByZeroError()
        assert error.message == "Division by zero is not allowed."
        assert str(error) == "Division by zero is not allowed."
        assert isinstance(error, CalculatorError)

    def test_division_by_zero_error_custom_message(self) -> None:
        """Test DivisionByZeroError with custom message."""
        custom_message = "Cannot divide by zero!"
        error = DivisionByZeroError(custom_message)
        assert error.message == custom_message
        assert str(error) == custom_message


class TestInvalidOperationError:
    """Test cases for InvalidOperationError."""

    def test_invalid_operation_error(self) -> None:
        """Test InvalidOperationError with operation."""
        operation = "^"
        error = InvalidOperationError(operation)
        expected_message = "Invalid operation: '^'. Supported operations: +, -, *, /"

        assert error.operation == operation
        assert error.message == expected_message
        assert str(error) == expected_message
        assert isinstance(error, CalculatorError)

    def test_invalid_operation_error_empty_string(self) -> None:
        """Test InvalidOperationError with empty string."""
        operation = ""
        error = InvalidOperationError(operation)
        expected_message = "Invalid operation: ''. Supported operations: +, -, *, /"

        assert error.operation == operation
        assert error.message == expected_message
        assert str(error) == expected_message


class TestInvalidNumberError:
    """Test cases for InvalidNumberError."""

    def test_invalid_number_error(self) -> None:
        """Test InvalidNumberError with invalid value."""
        value = "abc"
        error = InvalidNumberError(value)
        expected_message = "Invalid number: 'abc'. Please enter a valid number."

        assert error.value == value
        assert error.message == expected_message
        assert str(error) == expected_message
        assert isinstance(error, CalculatorError)

    def test_invalid_number_error_empty_string(self) -> None:
        """Test InvalidNumberError with empty string."""
        value = ""
        error = InvalidNumberError(value)
        expected_message = "Invalid number: ''. Please enter a valid number."

        assert error.value == value
        assert error.message == expected_message
        assert str(error) == expected_message

    def test_invalid_number_error_special_characters(self) -> None:
        """Test InvalidNumberError with special characters."""
        value = "12@34"
        error = InvalidNumberError(value)
        expected_message = "Invalid number: '12@34'. Please enter a valid number."

        assert error.value == value
        assert error.message == expected_message
        assert str(error) == expected_message
