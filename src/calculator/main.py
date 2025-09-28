"""Main module for the Calculator CLI application."""

from typing import Optional

from .operations import Operations
from .validator import Validator
from .exceptions import (
    DivisionByZeroError,
    InvalidOperationError,
    InvalidNumberError,
)


class CalculatorCLI:
    """Calculator command-line interface with REPL functionality."""

    def __init__(self) -> None:
        """Initialize the calculator CLI."""
        self.operations = Operations()
        self.validator = Validator()

    def display_welcome(self) -> None:
        """Display welcome message and instructions."""
        print("Welcome to the Calculator CLI!")
        print("Available operations: +, -, *, /")
        print("Type 'quit' or 'exit' to exit.")
        print()

    def display_goodbye(self) -> None:
        """Display goodbye message."""
        print("Thank you for using Calculator CLI!")

    def get_operation(self) -> Optional[str]:
        """
        Get operation input from user.

        Returns:
            The validated operation string, or None if quit command.
        """
        while True:
            try:
                operation_input = input("Enter operation (+, -, *, /): ")

                if self.validator.is_quit_command(operation_input):
                    return None

                return self.validator.validate_operation(operation_input)

            except InvalidOperationError as e:
                print(f"Error: {e.message}")
            except KeyboardInterrupt:
                print("\nExiting...")
                return None
            except EOFError:
                print("\nExiting...")
                return None

    def get_number(self, prompt: str) -> Optional[float]:
        """
        Get number input from user.

        Args:
            prompt: The prompt to display to the user.

        Returns:
            The validated number, or None if quit command.
        """
        while True:
            try:
                number_input = input(prompt)

                if self.validator.is_quit_command(number_input):
                    return None

                return self.validator.validate_number(number_input)

            except InvalidNumberError as e:
                print(f"Error: {e.message}")
            except KeyboardInterrupt:
                print("\nExiting...")
                return None
            except EOFError:
                print("\nExiting...")
                return None

    def perform_calculation(
        self, operation: str, first_num: float, second_num: float
    ) -> None:
        """
        Perform calculation and display result.

        Args:
            operation: The operation to perform.
            first_num: First number.
            second_num: Second number.
        """
        try:
            result = self.operations.calculate(operation, first_num, second_num)
            print(f"Result: {result}")
        except DivisionByZeroError as e:
            print(f"Error: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def run_single_calculation(self) -> bool:
        """
        Run a single calculation cycle.

        Returns:
            True to continue, False to exit.
        """
        # Get operation
        operation = self.get_operation()
        if operation is None:
            return False

        # Get first number
        first_num = self.get_number("Enter first number: ")
        if first_num is None:
            return False

        # Get second number
        second_num = self.get_number("Enter second number: ")
        if second_num is None:
            return False

        # Perform calculation
        self.perform_calculation(operation, first_num, second_num)
        print()  # Empty line for readability

        return True

    def run(self) -> None:
        """Run the calculator REPL (Read-Eval-Print Loop)."""
        self.display_welcome()

        try:
            while True:
                if not self.run_single_calculation():
                    break
        except KeyboardInterrupt:
            print("\nExiting...")
        finally:
            self.display_goodbye()


def main() -> None:
    """Main entry point for the calculator application."""
    calculator = CalculatorCLI()
    calculator.run()


if __name__ == "__main__":
    main()
