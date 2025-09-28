"""Input validation module for the calculator application."""

from .exceptions import InvalidNumberError, InvalidOperationError


class Validator:
    """Handles input validation for the calculator."""

    VALID_OPERATIONS = {"+", "-", "*", "/"}

    @staticmethod
    def validate_operation(operation: str) -> str:
        """
        Validate that the operation is supported.

        Args:
            operation: The operation string to validate.

        Returns:
            The validated operation string.

        Raises:
            InvalidOperationError: If the operation is not supported.
        """
        operation = operation.strip()
        if operation not in Validator.VALID_OPERATIONS:
            raise InvalidOperationError(operation)
        return operation

    @staticmethod
    def validate_number(value: str) -> float:
        """
        Validate and convert a string to a number.

        Args:
            value: The string value to validate and convert.

        Returns:
            The validated number as a float.

        Raises:
            InvalidNumberError: If the value cannot be converted to a number.
        """
        value = value.strip()
        if not value:
            raise InvalidNumberError(value)

        try:
            return float(value)
        except ValueError:
            raise InvalidNumberError(value)

    @staticmethod
    def is_quit_command(command: str) -> bool:
        """
        Check if the command is a quit command.

        Args:
            command: The command to check.

        Returns:
            True if it's a quit command, False otherwise.
        """
        return command.strip().lower() in {"quit", "exit", "q"}

    @staticmethod
    def sanitize_input(user_input: str) -> str:
        """
        Sanitize user input by stripping whitespace and converting to lowercase.

        Args:
            user_input: The raw user input.

        Returns:
            The sanitized input string.
        """
        return user_input.strip().lower()
