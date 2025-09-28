"""Test module for input validator."""

import pytest
from src.calculator.validator import Validator
from src.calculator.exceptions import InvalidOperationError, InvalidNumberError


class TestValidator:
    """Test cases for input validation."""

    @pytest.mark.parametrize(
        "operation, expected",
        [
            ("+", "+"),
            ("-", "-"),
            ("*", "*"),
            ("/", "/"),
            (" + ", "+"),
            (" - ", "-"),
            (" * ", "*"),
            (" / ", "/"),
        ],
    )
    def test_validate_operation_valid(self, operation: str, expected: str) -> None:
        """Test validation of valid operations."""
        result = Validator.validate_operation(operation)
        assert result == expected

    @pytest.mark.parametrize(
        "invalid_operation",
        [
            "^",
            "%",
            "//",
            "**",
            "mod",
            "power",
            "",
            " ",
            "add",
            "plus",
            "subtract",
            "multiply",
            "divide",
            "1",
            "0",
            "abc",
        ],
    )
    def test_validate_operation_invalid(self, invalid_operation: str) -> None:
        """Test validation of invalid operations."""
        with pytest.raises(InvalidOperationError) as exc_info:
            Validator.validate_operation(invalid_operation)

        assert exc_info.value.operation == invalid_operation.strip()
        expected_message = f"Invalid operation: '{invalid_operation.strip()}'. Supported operations: +, -, *, /"
        assert exc_info.value.message == expected_message

    @pytest.mark.parametrize(
        "number_str, expected",
        [
            ("5", 5.0),
            ("3.14", 3.14),
            ("-5", -5.0),
            ("-3.14", -3.14),
            ("0", 0.0),
            ("0.0", 0.0),
            (" 5 ", 5.0),
            (" 3.14 ", 3.14),
            ("1000000", 1000000.0),
            ("0.001", 0.001),
            ("5e2", 500.0),
            ("1.23e-4", 0.000123),
            ("inf", float("inf")),
            ("-inf", float("-inf")),
        ],
    )
    def test_validate_number_valid(self, number_str: str, expected: float) -> None:
        """Test validation of valid numbers."""
        result = Validator.validate_number(number_str)
        if expected == float("inf") or expected == float("-inf"):
            assert result == expected
        else:
            assert pytest.approx(result, rel=1e-10) == expected

    @pytest.mark.parametrize(
        "invalid_number",
        [
            "abc",
            "5abc",
            "abc5",
            "5.5.5",
            "5..5",
            "--5",
            "++5",
            "5-",
            "5+",
            "",
            " ",
            "   ",
            "5 3",
            "five",
            "3.14.159",
            "1,000",
            "$5",
            "5%",
        ],
    )
    def test_validate_number_invalid(self, invalid_number: str) -> None:
        """Test validation of invalid numbers."""
        with pytest.raises(InvalidNumberError) as exc_info:
            Validator.validate_number(invalid_number)

        assert exc_info.value.value == invalid_number.strip()
        expected_message = (
            f"Invalid number: '{invalid_number.strip()}'. Please enter a valid number."
        )
        assert exc_info.value.message == expected_message

    @pytest.mark.parametrize(
        "command, expected",
        [
            ("quit", True),
            ("exit", True),
            ("q", True),
            ("QUIT", True),
            ("EXIT", True),
            ("Q", True),
            (" quit ", True),
            (" exit ", True),
            (" q ", True),
            ("Quit", True),
            ("Exit", True),
            ("qUiT", True),
            ("eXiT", True),
        ],
    )
    def test_is_quit_command_true(self, command: str, expected: bool) -> None:
        """Test quit command detection for valid quit commands."""
        result = Validator.is_quit_command(command)
        assert result == expected

    @pytest.mark.parametrize(
        "command, expected",
        [
            ("+", False),
            ("5", False),
            ("hello", False),
            ("qu", False),
            ("ex", False),
            ("quite", False),
            ("exiting", False),
            ("", False),
            (" ", False),
            ("stop", False),
            ("end", False),
            ("finish", False),
            ("quit me", False),
            ("exit now", False),
        ],
    )
    def test_is_quit_command_false(self, command: str, expected: bool) -> None:
        """Test quit command detection for non-quit commands."""
        result = Validator.is_quit_command(command)
        assert result == expected

    @pytest.mark.parametrize(
        "user_input, expected",
        [
            ("Hello World", "hello world"),
            ("  TRIM ME  ", "trim me"),
            ("MiXeD cAsE", "mixed case"),
            ("", ""),
            ("   ", ""),
            ("123", "123"),
            ("Special!@#Characters", "special!@#characters"),
            ("QUIT", "quit"),
            ("  +  ", "+"),
        ],
    )
    def test_sanitize_input(self, user_input: str, expected: str) -> None:
        """Test input sanitization."""
        result = Validator.sanitize_input(user_input)
        assert result == expected

    def test_valid_operations_constant(self) -> None:
        """Test that VALID_OPERATIONS contains the expected operations."""
        expected_operations = {"+", "-", "*", "/"}
        assert Validator.VALID_OPERATIONS == expected_operations

    def test_validator_methods_are_static(self) -> None:
        """Test that all validator methods are static and work without instantiation."""
        # Test that methods can be called without creating an instance
        assert Validator.validate_operation("+") == "+"
        assert Validator.validate_number("5") == 5.0
        assert Validator.is_quit_command("quit") is True
        assert Validator.sanitize_input("  TEST  ") == "test"
