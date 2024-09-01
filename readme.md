# Example Flask Microservice

This repository contains a skeleton for a Flask-based microservice, designed with best practices in mind, including automated testing, OpenAPI documentation generation, and Docker support.

## Project Structure

```plaintext
microservice/
├── app/
│   ├── __init__.py          # Application factory
│   ├── main.py              # Entry point for running the app
│   ├── routes.py            # API route definitions
│   ├── models.py            # Data models (optional)
│   ├── config.py            # Configuration settings
│   └── openapi.py           # Script to generate OpenAPI spec
├── tests/
│   ├── __init__.py          # Test package initialization
│   ├── test_main.py         # Tests for main app
│   └── test_routes.py       # Tests for routes
├── openapi/
│   └── openapi.yaml         # Generated OpenAPI spec
├── Makefile                 # Makefile for automation tasks
├── tox.ini                  # Tox configuration for testing and linting
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
└── Dockerfile               # Dockerfile for containerization
```

## Requirements
*  `Python` 3.12+
*  `pip` for installing dependencies
*  `tox` for running tests and linting
*  `Docker` (optional, for containerization)

# Setup Instructions
## 1. Install Dependencies

To install the required dependencies, run:
```
make install
```
This will install both production and development dependencies.

## 2. Running the Application
To start the Flask application locally:
```
make run
```
The application will be available at `http://127.0.0.1:5000`.

## 3. Running Tests
To run the test suite:
```make test```
This command will execute the tests defined in the tests/ directory using tox.

## 4. Linting the Code
To lint the codebase using flake8:
```make lint```

## 5. Generating OpenAPI Specification
To generate the OpenAPI specification (openapi.yaml):
```make generate-spec```
The specification file will be generated in the openapi/ directory.

## 6. Validating OpenAPI Specification
To validate the generated openapi.yaml file:
```make validate-spec```
This ensures that the OpenAPI specification complies with the standard.

## 7. Containerization
To build and run the application inside a Docker container:
```
docker build -t flask-microservice .
docker run -p 5000:5000 flask-microservice
```

## 8. Customizing Configuration
The application uses a default configuration located in app/config.py. You can customize it according to your needs.

# Additional Information
## Tox Configuration
*  `tox.ini` is configured to handle both testing and linting. The testenv section manages the environment, and the `validate-spec` environment is dedicated to validating the OpenAPI specification.

## Makefile
The `Makefile` provides convenient shortcuts for common development tasks. The primary targets include:

*  `install`: Install all dependencies.
*  `run`: Start the Flask application.
*  `test`: Run all tests.
*  `lint`: Lint the codebase.
*  `generate-spec`: Generate the OpenAPI specification.
*  `validate-spec`: Validate the OpenAPI specification.

## OpenAPI Specification
The `openapi.yaml` file is automatically generated by the `app/openapi.py` script, which scans the Flask app's routes and converts them into OpenAPI format. The specification is validated to ensure it adheres to the OpenAPI standard.
