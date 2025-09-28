# Calculator CLI

A robust command-line calculator application with a REPL (Read-Eval-Print Loop) interface, comprehensive testing, and CI/CD integration.

## Features

- **REPL Interface**: Interactive command-line interface for continuous calculations
- **Arithmetic Operations**: Addition, subtraction, multiplication, and division
- **Input Validation**: Robust input validation with clear error messages
- **Error Handling**: Graceful handling of invalid inputs and division by zero
- **Comprehensive Testing**: 100% test coverage with pytest
- **Type Safety**: Full type annotations with mypy validation
- **Code Quality**: Formatted with Black, linted with flake8
- **CI/CD**: Automated testing and coverage enforcement with GitHub Actions

## Project Structure

```
calculator-cli/
├── src/
│   └── calculator/
│       ├── __init__.py
│       ├── main.py          # Entry point and REPL
│       ├── operations.py    # Arithmetic operations
│       ├── validator.py     # Input validation
│       └── exceptions.py    # Custom exceptions
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_operations.py   # Parameterized tests
│   ├── test_validator.py
│   └── test_exceptions.py
├── docs/
│   └── usage.md
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions workflow
├── pyproject.toml           # Project configuration
├── requirements-dev.txt     # Development dependencies
├── .gitignore
└── README.md
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd calculator-cli
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install development dependencies:**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Install the package in development mode:**
   ```bash
   pip install -e .
   ```

## Usage

### Running the Calculator

1. **Start the REPL interface:**
   ```bash
   python -m src.calculator.main
   ```
   or
   ```bash
   calculator
   ```

2. **Follow the prompts to perform calculations:**
   ```
   Welcome to the Calculator CLI!
   Available operations: +, -, *, /
   Type 'quit' or 'exit' to exit.

   Enter operation (+, -, *, /): +
   Enter first number: 10
   Enter second number: 5
   Result: 15.0

   Enter operation (+, -, *, /): /
   Enter first number: 10
   Enter second number: 0
   Error: Division by zero is not allowed.

   Enter operation (+, -, *, /): quit
   Thank you for using Calculator CLI!
   ```

## Development

### Running Tests

```bash
# Run all tests with coverage
pytest

# Run specific test file
pytest tests/test_operations.py

# Run with verbose output
pytest -v
```

### Code Quality

```bash
# Format code
black src tests

# Lint code
flake8 src tests

# Type checking
mypy src
```

### Test Coverage

The project enforces 100% test coverage. To check coverage:

```bash
pytest --cov=src --cov-report=html
# Open htmlcov/index.html to view detailed coverage report
```

## GitHub Actions CI/CD

The project includes a GitHub Actions workflow that:

- Runs tests on multiple Python versions (3.8, 3.9, 3.10, 3.11, 3.12)
- Enforces 100% test coverage
- Validates code formatting and linting
- Performs type checking

The CI pipeline will fail if:
- Any tests fail
- Test coverage is below 100%
- Code formatting is incorrect
- Linting issues are found
- Type checking fails

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure all tests pass and coverage is 100%
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Author

Your Name (your.email@example.com)