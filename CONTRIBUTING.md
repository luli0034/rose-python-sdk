# Contributing to Rose Python SDK

Thank you for your interest in contributing to the Rose Python SDK! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)

## Code of Conduct

This project follows a code of conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to luli@kkcompany.com.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature
4. Make your changes
5. Add tests for your changes
6. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip
- git

### Setup

1. Clone the repository:
```bash
git clone https://github.com/your-org/rose-python-sdk.git
cd rose-python-sdk
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -e .[dev]
```

4. Install pre-commit hooks:
```bash
pre-commit install
```

## Contributing Guidelines

### Types of Contributions

- **Bug fixes**: Fix existing issues
- **New features**: Add new functionality
- **Documentation**: Improve or add documentation
- **Tests**: Add or improve test coverage
- **Examples**: Add or improve examples
- **Performance**: Optimize existing code

### Before You Start

1. Check existing issues and pull requests
2. Discuss major changes in an issue first
3. Ensure your changes align with the project goals
4. Follow the coding standards

## Pull Request Process

### Before Submitting

1. **Test your changes**: Run all tests and ensure they pass
2. **Update documentation**: Update relevant documentation
3. **Add examples**: Add examples for new features
4. **Update changelog**: Add entries to CHANGELOG.md
5. **Check code style**: Run linting and formatting tools

### Pull Request Template

When creating a pull request, please include:

- **Description**: Clear description of changes
- **Type**: Type of change (bug fix, feature, documentation, etc.)
- **Testing**: How you tested the changes
- **Breaking Changes**: Any breaking changes
- **Related Issues**: Link to related issues

### Review Process

1. All pull requests require review
2. Address feedback promptly
3. Keep pull requests focused and small
4. Respond to review comments

## Issue Reporting

### Before Creating an Issue

1. Search existing issues
2. Check if the issue is already reported
3. Ensure you're using the latest version

### Issue Template

When creating an issue, please include:

- **Description**: Clear description of the problem
- **Steps to Reproduce**: How to reproduce the issue
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Environment**: Python version, OS, SDK version
- **Code Sample**: Minimal code to reproduce the issue

## Coding Standards

### Python Style

- Follow PEP 8
- Use type hints
- Write docstrings for all public functions
- Use meaningful variable and function names

### Code Formatting

We use Black for code formatting:

```bash
black rose_sdk/
```

### Linting

We use flake8 for linting:

```bash
flake8 rose_sdk/
```

### Type Checking

We use mypy for type checking:

```bash
mypy rose_sdk/
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=rose_sdk

# Run specific test file
pytest tests/test_client.py
```

### Writing Tests

- Write tests for all new functionality
- Aim for high test coverage
- Use descriptive test names
- Test both success and error cases
- Mock external dependencies

### Test Structure

```python
def test_function_name_success_case():
    """Test that function works correctly in success case."""
    # Arrange
    # Act
    # Assert

def test_function_name_error_case():
    """Test that function handles errors correctly."""
    # Arrange
    # Act
    # Assert
```

## Documentation

### Code Documentation

- Write docstrings for all public functions
- Use Google style docstrings
- Include type hints
- Provide examples in docstrings

### Example Docstring

```python
def example_function(param1: str, param2: int) -> bool:
    """
    Example function that does something.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When param1 is invalid
        
    Example:
        >>> result = example_function("test", 123)
        >>> print(result)
        True
    """
    pass
```

### Documentation Updates

- Update relevant documentation for new features
- Add examples for new functionality
- Update API reference if needed
- Keep examples up to date

## Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] Changelog updated
- [ ] Version number updated
- [ ] Release notes prepared
- [ ] Package built and tested

## Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **Email**: luli@kkcompany.com for general questions
- **Documentation**: Check the docs/ directory

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the Rose Python SDK! 🚀
