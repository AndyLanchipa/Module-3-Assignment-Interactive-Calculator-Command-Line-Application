# Calculator CLI Project

This is a robust command-line calculator application with comprehensive testing and CI/CD integration.

## Project Overview

A Python calculator with REPL interface, supporting basic arithmetic operations (+, -, *, /) with comprehensive error handling and 100% test coverage.

## Key Features

- REPL (Read-Eval-Print Loop) interface
- Input validation and error handling  
- Division by zero protection
- 100% test coverage with pytest
- GitHub Actions CI/CD pipeline
- Code formatting with Black
- Linting with flake8
- Type checking with mypy

## Development Commands

Use VS Code tasks or run directly:

- **Run Calculator**: `.\venv\Scripts\python.exe -m src.calculator.main`
- **Run Tests**: `.\venv\Scripts\python.exe -m pytest --cov=src --cov-report=term-missing --cov-fail-under=100 -v`
- **Format Code**: `.\venv\Scripts\python.exe -m black src tests`
- **Lint Code**: `.\venv\Scripts\python.exe -m flake8 src tests`
- **Type Check**: `.\venv\Scripts\python.exe -m mypy src`

## Project Structure

- `src/calculator/` - Main application code
- `tests/` - Comprehensive test suite with 197 test cases
- `docs/` - Documentation and usage guide
- `.github/workflows/` - CI/CD pipeline configuration
- `pyproject.toml` - Project configuration and dependencies