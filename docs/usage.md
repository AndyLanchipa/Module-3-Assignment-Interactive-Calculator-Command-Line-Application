# Calculator CLI Usage Guide

## Overview

The Calculator CLI is a command-line application that provides a Read-Eval-Print Loop (REPL) interface for performing basic arithmetic operations. This guide covers all aspects of using the calculator effectively.

## Getting Started

### Launching the Calculator

You can start the calculator in two ways:

1. **Using the installed command:**
   ```bash
   calculator
   ```

2. **Running the module directly:**
   ```bash
   python -m src.calculator.main
   ```

### Initial Interface

When you start the calculator, you'll see:

```
Welcome to the Calculator CLI!
Available operations: +, -, *, /
Type 'quit' or 'exit' to exit.

Enter operation (+, -, *, /):
```

## Supported Operations

The calculator supports four basic arithmetic operations:

- **Addition (`+`)**: Adds two numbers
- **Subtraction (`-`)**: Subtracts the second number from the first
- **Multiplication (`*`)**: Multiplies two numbers
- **Division (`/`)**: Divides the first number by the second

## User Interaction Flow

### 1. Choose Operation

First, you'll be prompted to enter an operation:

```
Enter operation (+, -, *, /): +
```

### 2. Enter First Number

Next, enter the first number:

```
Enter first number: 10
```

### 3. Enter Second Number

Then, enter the second number:

```
Enter second number: 5
```

### 4. View Result

The calculator displays the result:

```
Result: 15.0
```

### 5. Continue or Exit

After each calculation, you'll be prompted for the next operation. You can:
- Enter another operation to perform more calculations
- Type `quit`, `exit`, or `q` to exit the program

## Input Validation and Error Handling

### Valid Number Formats

The calculator accepts various number formats:

- **Integers**: `5`, `-10`, `0`
- **Decimals**: `3.14`, `-2.5`, `0.001`
- **Scientific notation**: `1.23e4`, `5e-3`
- **Special values**: `inf`, `-inf`

### Error Scenarios

#### Invalid Operations

```
Enter operation (+, -, *, /): ^
Error: Invalid operation: '^'. Supported operations: +, -, *, /
Enter operation (+, -, *, /):
```

#### Invalid Numbers

```
Enter first number: abc
Error: Invalid number: 'abc'. Please enter a valid number.
Enter first number:
```

#### Division by Zero

```
Enter operation (+, -, *, /): /
Enter first number: 10
Enter second number: 0
Error: Division by zero is not allowed.

Enter operation (+, -, *, /):
```

## Exiting the Program

You can exit the calculator at any prompt by typing:

- `quit`
- `exit`
- `q`

These commands are case-insensitive and work with surrounding whitespace.

## Example Sessions

### Basic Calculations

```
Welcome to the Calculator CLI!
Available operations: +, -, *, /
Type 'quit' or 'exit' to exit.

Enter operation (+, -, *, /): +
Enter first number: 15
Enter second number: 25
Result: 40.0

Enter operation (+, -, *, /): *
Enter first number: 6
Enter second number: 7
Result: 42.0

Enter operation (+, -, *, /): /
Enter first number: 100
Enter second number: 4
Result: 25.0

Enter operation (+, -, *, /): quit
Thank you for using Calculator CLI!
```

### Error Recovery

```
Enter operation (+, -, *, /): %
Error: Invalid operation: '%'. Supported operations: +, -, *, /
Enter operation (+, -, *, /): +
Enter first number: five
Error: Invalid number: 'five'. Please enter a valid number.
Enter first number: 5
Enter second number: 3
Result: 8.0
```

### Working with Decimals

```
Enter operation (+, -, *, /): *
Enter first number: 3.14159
Enter second number: 2
Result: 6.28318

Enter operation (+, -, *, /): /
Enter first number: 22
Enter second number: 7
Result: 3.142857142857143
```

### Working with Negative Numbers

```
Enter operation (+, -, *, /): +
Enter first number: -10
Enter second number: 5
Result: -5.0

Enter operation (+, -, *, /): -
Enter first number: -5
Enter second number: -3
Result: -2.0
```

## Tips and Best Practices

### Input Flexibility

- **Whitespace**: Leading and trailing whitespace in inputs is automatically trimmed
- **Case sensitivity**: Quit commands (`quit`, `exit`, `q`) are case-insensitive
- **Number formats**: Use any valid Python number format including scientific notation

### Keyboard Shortcuts

- **Ctrl+C**: Force quit the program (same as typing `quit`)
- **Ctrl+D**: EOF signal, also exits the program

### Precision Notes

- Results are displayed as floating-point numbers
- Very large or very small numbers may use scientific notation
- Floating-point precision limitations apply (standard IEEE 754)

## Troubleshooting

### Common Issues

1. **Calculator doesn't start**
   - Ensure Python 3.8+ is installed
   - Verify the calculator package is properly installed
   - Try running with `python -m src.calculator.main`

2. **Unexpected behavior with very large numbers**
   - Python handles arbitrarily large integers, but floating-point operations have precision limits
   - Results may be displayed in scientific notation for very large or small values

3. **Unicode or encoding issues**
   - Ensure your terminal supports Unicode
   - Use standard ASCII characters for input

### Getting Help

If you encounter issues:

1. Check that all dependencies are installed
2. Verify Python version compatibility (3.8+)
3. Review the error messages for specific guidance
4. Consult the project documentation or GitHub repository

## Development and Testing

For developers working on the calculator:

- Run tests: `pytest`
- Check coverage: `pytest --cov=src`
- Format code: `black src tests`
- Lint code: `flake8 src tests`
- Type check: `mypy src`

## Version Information

Current version: 1.0.0

For updates and more information, visit the project repository.