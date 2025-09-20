# Changelog

All notable changes to the Rose Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2024-01-20

### Changed
- **Python Version Support**: Now requires Python 3.11+ (previously supported 3.8+)
- **CI/CD**: Updated GitHub Actions to test only Python 3.11 and 3.12

### Added
- Complete role management system with permission-based access control
- Comprehensive dataset management with schema validation
- Advanced pipeline management with scenario-based configuration
- Batch data processing for large datasets
- Schema inference and validation utilities
- High-level helper functions for common operations
- Comprehensive error handling with specific exception classes
- Complete documentation and examples
- Type safety with Pydantic models
- Support for all Rose API endpoints

### Features
- **Role Management**: Create, manage, and assign roles with granular permissions
- **Dataset Management**: Full CRUD operations with schema validation
- **Pipeline Management**: Create and manage recommendation pipelines
- **Batch Operations**: Efficient handling of large datasets
- **Schema Management**: Automatic schema inference and validation
- **Helper Functions**: Quick operations for common tasks
- **Error Handling**: Detailed exception classes for different error scenarios

### Examples
- Role management examples with permission building
- Dataset creation and management examples
- Records management with CRUD operations
- Batch data upload examples
- Pipeline creation and management examples
- Complete end-to-end recommendation system setup

### Documentation
- Getting started guide
- Complete API reference
- Comprehensive examples guide
- Troubleshooting section
- Best practices

## [1.0.0] - 2024-01-01

### Added
- Initial release of Rose Python SDK
- Basic client implementation
- Core data models
- Basic API integration

### Features
- Client initialization and authentication
- Basic dataset operations
- Simple pipeline management
- Basic error handling

---

## Development

### Unreleased Changes
- Async support (planned)
- Additional helper functions
- Performance optimizations
- Extended documentation

### Known Issues
- None currently known

### Breaking Changes
- None in current version

---

For more information about changes, see the [GitHub repository](https://github.com/your-org/rose-python-sdk).
