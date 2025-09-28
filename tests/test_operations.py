"""Parameterized test module for calculator operations."""

import pytest
from src.calculator.operations import Operations
from src.calculator.exceptions import DivisionByZeroError


class TestOperations:
    """Test cases for arithmetic operations with parameterized tests."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (5.0, 3.0, 8.0),
            (0.0, 0.0, 0.0),
            (-5.0, 3.0, -2.0),
            (5.0, -3.0, 2.0),
            (-5.0, -3.0, -8.0),
            (0.5, 0.3, 0.8),
            (1000000.0, 2000000.0, 3000000.0),
            (3.14159, 2.71828, 5.85987),
        ],
    )
    def test_add_parameterized(self, a: float, b: float, expected: float) -> None:
        """Test addition with various number combinations."""
        result = Operations.add(a, b)
        assert pytest.approx(result, rel=1e-5) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (5.0, 3.0, 2.0),
            (0.0, 0.0, 0.0),
            (-5.0, 3.0, -8.0),
            (5.0, -3.0, 8.0),
            (-5.0, -3.0, -2.0),
            (0.8, 0.3, 0.5),
            (1000000.0, 999999.0, 1.0),
            (3.14159, 2.71828, 0.42331),
        ],
    )
    def test_subtract_parameterized(self, a: float, b: float, expected: float) -> None:
        """Test subtraction with various number combinations."""
        result = Operations.subtract(a, b)
        assert pytest.approx(result, rel=1e-5) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (5.0, 3.0, 15.0),
            (0.0, 5.0, 0.0),
            (5.0, 0.0, 0.0),
            (-5.0, 3.0, -15.0),
            (5.0, -3.0, -15.0),
            (-5.0, -3.0, 15.0),
            (0.5, 0.4, 0.2),
            (1000.0, 1000.0, 1000000.0),
            (3.14159, 2.0, 6.28318),
        ],
    )
    def test_multiply_parameterized(self, a: float, b: float, expected: float) -> None:
        """Test multiplication with various number combinations."""
        result = Operations.multiply(a, b)
        assert pytest.approx(result, rel=1e-5) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (6.0, 3.0, 2.0),
            (0.0, 5.0, 0.0),
            (-6.0, 3.0, -2.0),
            (6.0, -3.0, -2.0),
            (-6.0, -3.0, 2.0),
            (1.0, 4.0, 0.25),
            (7.0, 2.0, 3.5),
            (1000000.0, 1000.0, 1000.0),
            (3.14159, 2.0, 1.570795),
        ],
    )
    def test_divide_parameterized(self, a: float, b: float, expected: float) -> None:
        """Test division with various number combinations."""
        result = Operations.divide(a, b)
        assert pytest.approx(result, rel=1e-5) == expected

    @pytest.mark.parametrize(
        "dividend",
        [0.0, 5.0, -5.0, 3.14159, 1000000.0],
    )
    def test_divide_by_zero_parameterized(self, dividend: float) -> None:
        """Test division by zero with various dividends."""
        with pytest.raises(DivisionByZeroError) as exc_info:
            Operations.divide(dividend, 0.0)

        assert exc_info.value.message == "Division by zero is not allowed."

    @pytest.mark.parametrize(
        "operation, a, b, expected",
        [
            ("+", 5.0, 3.0, 8.0),
            ("-", 5.0, 3.0, 2.0),
            ("*", 5.0, 3.0, 15.0),
            ("/", 6.0, 3.0, 2.0),
            ("+", -5.0, 3.0, -2.0),
            ("-", -5.0, 3.0, -8.0),
            ("*", -5.0, 3.0, -15.0),
            ("/", -6.0, 3.0, -2.0),
            ("+", 0.0, 0.0, 0.0),
            ("*", 0.0, 5.0, 0.0),
        ],
    )
    def test_calculate_parameterized(
        self, operation: str, a: float, b: float, expected: float
    ) -> None:
        """Test calculate method with various operations and values."""
        result = Operations.calculate(operation, a, b)
        assert pytest.approx(result, rel=1e-5) == expected

    def test_calculate_division_by_zero(self) -> None:
        """Test calculate method with division by zero."""
        with pytest.raises(DivisionByZeroError):
            Operations.calculate("/", 5.0, 0.0)

    @pytest.mark.parametrize(
        "invalid_operation",
        ["^", "%", "//", "**", "mod", "power", "sqrt", "", " ", "add"],
    )
    def test_calculate_invalid_operation_parameterized(
        self, invalid_operation: str
    ) -> None:
        """Test calculate method with invalid operations."""
        with pytest.raises(ValueError) as exc_info:
            Operations.calculate(invalid_operation, 5.0, 3.0)

        assert f"Unsupported operation: {invalid_operation}" in str(exc_info.value)

    def test_operations_are_static_methods(self) -> None:
        """Test that all operation methods are static and work without instantiation."""
        # Test that methods can be called without creating an instance
        assert Operations.add(2, 3) == 5
        assert Operations.subtract(5, 3) == 2
        assert Operations.multiply(4, 3) == 12
        assert Operations.divide(6, 3) == 2
        assert Operations.calculate("+", 2, 3) == 5


class TestOperationsEdgeCases:
    """Test edge cases for operations."""

    def test_very_large_numbers(self) -> None:
        """Test operations with very large numbers."""
        large_num = 1e10
        result = Operations.add(large_num, large_num)
        assert result == 2e10

    def test_very_small_numbers(self) -> None:
        """Test operations with very small numbers."""
        small_num = 1e-10
        result = Operations.multiply(small_num, 2)
        assert pytest.approx(result) == 2e-10

    def test_precision_floating_point(self) -> None:
        """Test floating point precision issues."""
        # This test demonstrates that we handle floating point precision correctly
        result = Operations.add(0.1, 0.2)
        # Due to floating point precision, this is approximately 0.3
        assert pytest.approx(result, rel=1e-10) == 0.3

    @pytest.mark.parametrize(
        "operation, a, b",
        [
            ("+", float("inf"), 1.0),
            ("-", float("inf"), 1.0),
            ("*", float("inf"), 2.0),
            ("/", float("inf"), 2.0),
        ],
    )
    def test_infinity_operations(self, operation: str, a: float, b: float) -> None:
        """Test operations with infinity values."""
        result = Operations.calculate(operation, a, b)
        # These should not raise exceptions and should handle infinity appropriately
        assert result is not None
