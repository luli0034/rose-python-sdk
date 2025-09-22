# Rose Python SDK

<div align="center">
  <img src="./assets/images/rose-logo.png" alt="Rose Python SDK" width="200" />
</div>

> A comprehensive Python SDK for interacting with the Rose Recommendation Service API

[![PyPI version](https://badge.fury.io/py/rose-python-sdk.svg)](https://badge.fury.io/py/rose-python-sdk)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- 🚀 **Complete API Coverage** - Full support for all Rose Recommendation Service endpoints
- 🛡️ **Type Safety** - Built with Pydantic for robust data validation and type hints
- ⚡ **Comprehensive Error Handling** - Detailed exception classes for different error scenarios
- 📦 **Batch Operations** - Efficient batch data processing and upload capabilities
- 🔧 **Schema Management** - Automatic schema inference and validation
- 🔄 **Pipeline Management** - Intuitive pipeline creation and management tools
- 👥 **Role-Based Access Control** - Complete permission and role management system
- 🛠️ **Helper Functions** - High-level utilities for common operations

## Quick Start

```python
from rose_sdk import RoseClient

# Initialize the client
client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="your_access_token"
)

# Create a dataset
dataset = client.datasets.create(
    name="user_interactions",
    schema={"user_id": "str", "item_id": "str", "rating": "float"}
)

# Get recommendations
recommendations = client.recommendations.get(
    query_id="your_query_id",
    parameters={"user_id": "user123"}
)
```

## Installation

```bash
pip install rose-python-sdk
```

## Documentation

- [Getting Started](getting-started.md) - Learn the basics
- [API Reference](api-reference/overview.md) - Complete API documentation
- [Examples](examples/basic-examples.md) - Code examples and tutorials

## Links

- [GitHub Repository](https://github.com/luli0034/rose-python-sdk)
- [PyPI Package](https://pypi.org/project/rose-python-sdk/)
- [Issue Tracker](https://github.com/luli0034/rose-python-sdk/issues)

## License

This project is licensed under the MIT License - see the [License](license.md) file for details.

---

**Made with ❤️ for the Rose community**
