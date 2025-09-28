"""Test module for the main calculator CLI application."""

import pytest
from unittest.mock import Mock, patch, call
from io import StringIO
from src.calculator.main import CalculatorCLI, main
from src.calculator.exceptions import (
    DivisionByZeroError,
    InvalidOperationError,
    InvalidNumberError,
)


class TestCalculatorCLI:
    """Test cases for the CalculatorCLI class."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.calculator = CalculatorCLI()

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_welcome(self, mock_stdout: StringIO) -> None:
        """Test welcome message display."""
        self.calculator.display_welcome()
        output = mock_stdout.getvalue()

        assert "Welcome to the Calculator CLI!" in output
        assert "Available operations: +, -, *, /" in output
        assert "Type 'quit' or 'exit' to exit." in output

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_goodbye(self, mock_stdout: StringIO) -> None:
        """Test goodbye message display."""
        self.calculator.display_goodbye()
        output = mock_stdout.getvalue()

        assert "Thank you for using Calculator CLI!" in output

    @patch("builtins.input")
    def test_get_operation_valid(self, mock_input: Mock) -> None:
        """Test getting valid operation input."""
        mock_input.return_value = "+"
        result = self.calculator.get_operation()
        assert result == "+"

    @patch("builtins.input")
    def test_get_operation_quit_commands(self, mock_input: Mock) -> None:
        """Test quit commands in get_operation."""
        quit_commands = ["quit", "exit", "q", "QUIT", "EXIT"]

        for command in quit_commands:
            mock_input.return_value = command
            result = self.calculator.get_operation()
            assert result is None

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_operation_invalid_then_valid(
        self, mock_stdout: StringIO, mock_input: Mock
    ) -> None:
        """Test invalid operation followed by valid one."""
        mock_input.side_effect = ["^", "+"]
        result = self.calculator.get_operation()

        assert result == "+"
        output = mock_stdout.getvalue()
        assert "Invalid operation: '^'. Supported operations: +, -, *, /" in output

    @patch("builtins.input", side_effect=KeyboardInterrupt)
    def test_get_operation_keyboard_interrupt(self, mock_input: Mock) -> None:
        """Test KeyboardInterrupt in get_operation."""
        result = self.calculator.get_operation()
        assert result is None

    @patch("builtins.input", side_effect=EOFError)
    def test_get_operation_eof_error(self, mock_input: Mock) -> None:
        """Test EOFError in get_operation."""
        result = self.calculator.get_operation()
        assert result is None

    @patch("builtins.input")
    def test_get_number_valid(self, mock_input: Mock) -> None:
        """Test getting valid number input."""
        mock_input.return_value = "5.5"
        result = self.calculator.get_number("Enter number: ")
        assert result == 5.5

    @patch("builtins.input")
    def test_get_number_quit_commands(self, mock_input: Mock) -> None:
        """Test quit commands in get_number."""
        quit_commands = ["quit", "exit", "q"]

        for command in quit_commands:
            mock_input.return_value = command
            result = self.calculator.get_number("Enter number: ")
            assert result is None

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_number_invalid_then_valid(
        self, mock_stdout: StringIO, mock_input: Mock
    ) -> None:
        """Test invalid number followed by valid one."""
        mock_input.side_effect = ["abc", "5"]
        result = self.calculator.get_number("Enter number: ")

        assert result == 5.0
        output = mock_stdout.getvalue()
        assert "Invalid number: 'abc'. Please enter a valid number." in output

    @patch("builtins.input", side_effect=KeyboardInterrupt)
    def test_get_number_keyboard_interrupt(self, mock_input: Mock) -> None:
        """Test KeyboardInterrupt in get_number."""
        result = self.calculator.get_number("Enter number: ")
        assert result is None

    @patch("builtins.input", side_effect=EOFError)
    def test_get_number_eof_error(self, mock_input: Mock) -> None:
        """Test EOFError in get_number."""
        result = self.calculator.get_number("Enter number: ")
        assert result is None

    @patch("sys.stdout", new_callable=StringIO)
    def test_perform_calculation_success(self, mock_stdout: StringIO) -> None:
        """Test successful calculation performance."""
        self.calculator.perform_calculation("+", 5.0, 3.0)
        output = mock_stdout.getvalue()
        assert "Result: 8.0" in output

    @patch("sys.stdout", new_callable=StringIO)
    def test_perform_calculation_division_by_zero(self, mock_stdout: StringIO) -> None:
        """Test division by zero error handling."""
        self.calculator.perform_calculation("/", 5.0, 0.0)
        output = mock_stdout.getvalue()
        assert "Error: Division by zero is not allowed." in output

    @patch("sys.stdout", new_callable=StringIO)
    def test_perform_calculation_unexpected_error(self, mock_stdout: StringIO) -> None:
        """Test unexpected error handling."""
        # Mock the operations to raise an unexpected error
        with patch.object(self.calculator.operations, "calculate") as mock_calc:
            mock_calc.side_effect = RuntimeError("Unexpected error")
            self.calculator.perform_calculation("+", 5.0, 3.0)

        output = mock_stdout.getvalue()
        assert "Unexpected error: Unexpected error" in output

    @patch.object(CalculatorCLI, "get_operation")
    @patch.object(CalculatorCLI, "get_number")
    @patch.object(CalculatorCLI, "perform_calculation")
    @patch("sys.stdout", new_callable=StringIO)
    def test_run_single_calculation_success(
        self,
        mock_stdout: StringIO,
        mock_perform: Mock,
        mock_get_number: Mock,
        mock_get_operation: Mock,
    ) -> None:
        """Test successful single calculation run."""
        mock_get_operation.return_value = "+"
        mock_get_number.side_effect = [5.0, 3.0]

        result = self.calculator.run_single_calculation()

        assert result is True
        mock_get_operation.assert_called_once()
        assert mock_get_number.call_count == 2
        mock_perform.assert_called_once_with("+", 5.0, 3.0)

    @patch.object(CalculatorCLI, "get_operation")
    def test_run_single_calculation_quit_on_operation(
        self, mock_get_operation: Mock
    ) -> None:
        """Test quitting during operation input."""
        mock_get_operation.return_value = None

        result = self.calculator.run_single_calculation()
        assert result is False

    @patch.object(CalculatorCLI, "get_operation")
    @patch.object(CalculatorCLI, "get_number")
    def test_run_single_calculation_quit_on_first_number(
        self, mock_get_number: Mock, mock_get_operation: Mock
    ) -> None:
        """Test quitting during first number input."""
        mock_get_operation.return_value = "+"
        mock_get_number.return_value = None

        result = self.calculator.run_single_calculation()
        assert result is False

    @patch.object(CalculatorCLI, "get_operation")
    @patch.object(CalculatorCLI, "get_number")
    def test_run_single_calculation_quit_on_second_number(
        self, mock_get_number: Mock, mock_get_operation: Mock
    ) -> None:
        """Test quitting during second number input."""
        mock_get_operation.return_value = "+"
        mock_get_number.side_effect = [5.0, None]

        result = self.calculator.run_single_calculation()
        assert result is False

    @patch.object(CalculatorCLI, "display_welcome")
    @patch.object(CalculatorCLI, "display_goodbye")
    @patch.object(CalculatorCLI, "run_single_calculation")
    def test_run_normal_exit(
        self,
        mock_single: Mock,
        mock_goodbye: Mock,
        mock_welcome: Mock,
    ) -> None:
        """Test normal program exit."""
        mock_single.side_effect = [True, True, False]  # Two calculations, then quit

        self.calculator.run()

        mock_welcome.assert_called_once()
        mock_goodbye.assert_called_once()
        assert mock_single.call_count == 3

    @patch.object(CalculatorCLI, "display_welcome")
    @patch.object(CalculatorCLI, "display_goodbye")
    @patch.object(CalculatorCLI, "run_single_calculation")
    @patch("sys.stdout", new_callable=StringIO)
    def test_run_keyboard_interrupt(
        self,
        mock_stdout: StringIO,
        mock_single: Mock,
        mock_goodbye: Mock,
        mock_welcome: Mock,
    ) -> None:
        """Test KeyboardInterrupt during run."""
        mock_single.side_effect = KeyboardInterrupt()

        self.calculator.run()

        mock_welcome.assert_called_once()
        mock_goodbye.assert_called_once()
        output = mock_stdout.getvalue()
        assert "Exiting..." in output

    @patch.object(CalculatorCLI, "run")
    def test_main_function(self, mock_run: Mock) -> None:
        """Test main function creates calculator and runs it."""
        main()
        mock_run.assert_called_once()


class TestCalculatorCLIIntegration:
    """Integration tests for the CalculatorCLI class."""

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_full_calculation_flow(
        self, mock_stdout: StringIO, mock_input: Mock
    ) -> None:
        """Test complete calculation flow integration."""
        # Simulate user input: operation "+", first number "5", second number "3", then quit
        mock_input.side_effect = ["+", "5", "3", "quit"]

        calculator = CalculatorCLI()
        result = calculator.run_single_calculation()

        # Should complete one calculation successfully
        assert result is True

        # Check that result was displayed
        output = mock_stdout.getvalue()
        assert "Result: 8.0" in output

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_error_recovery_flow(self, mock_stdout: StringIO, mock_input: Mock) -> None:
        """Test error recovery and continuation."""
        # Simulate: invalid operation, then valid operation, invalid number, valid numbers
        mock_input.side_effect = ["^", "+", "abc", "10", "2"]

        calculator = CalculatorCLI()
        result = calculator.run_single_calculation()

        assert result is True
        output = mock_stdout.getvalue()

        # Should show error messages and final result
        assert "Invalid operation: '^'" in output
        assert "Invalid number: 'abc'" in output
        assert "Result: 12.0" in output

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_division_by_zero_handling(
        self, mock_stdout: StringIO, mock_input: Mock
    ) -> None:
        """Test division by zero error handling."""
        mock_input.side_effect = ["/", "10", "0"]

        calculator = CalculatorCLI()
        result = calculator.run_single_calculation()

        assert result is True
        output = mock_stdout.getvalue()
        assert "Error: Division by zero is not allowed." in output


class TestMainFunction:
    """Test cases for the main function."""

    @patch("src.calculator.main.CalculatorCLI")
    def test_main_creates_and_runs_calculator(
        self, mock_calculator_class: Mock
    ) -> None:
        """Test that main function creates calculator instance and runs it."""
        mock_calculator_instance = Mock()
        mock_calculator_class.return_value = mock_calculator_instance

        main()

        mock_calculator_class.assert_called_once()
        mock_calculator_instance.run.assert_called_once()

    def test_calculator_cli_initialization(self) -> None:
        """Test CalculatorCLI initialization creates required components."""
        calculator = CalculatorCLI()

        assert hasattr(calculator, "operations")
        assert hasattr(calculator, "validator")
        assert calculator.operations is not None
        assert calculator.validator is not None
