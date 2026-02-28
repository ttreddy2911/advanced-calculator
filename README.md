# Advanced Calculator Application

## Project Overview

This project is an advanced command-line calculator built in Python.  
It supports multiple arithmetic operations, undo/redo functionality, logging, history management, CSV persistence, environment configuration, and automated testing with CI/CD integration.

The application follows professional software development practices including design patterns, unit testing, and Git version control.

---

## Features

### Arithmetic Operations
- add
- subtract
- multiply
- divide
- power
- root
- modulus
- int_divide
- percent
- abs_diff

### History Management
- View history
- Clear history
- Undo last operation
- Redo last undone operation

### Data Persistence
- Save history to CSV using pandas
- Load history from CSV

### Logging
- Logs calculations and errors to file
- Uses Python logging module

### Configuration
- Uses `.env` file with python-dotenv
- Configurable:
  - Log directory
  - History directory
  - Precision
  - Max input value
  - Max history size
  - Auto-save option

### Design Patterns Used
- Factory Pattern (OperationFactory)
- Memento Pattern (Undo/Redo)
- Observer Pattern (Logging and AutoSave)

---

## Project Structure

```
project_root/
│
├── app/
├── tests/
├── .env
├── requirements.txt
├── README.md
└── .github/workflows/python-app.yml
```

---

## Installation

### 1. Clone Repository

```
git clone https://github.com/ttreddy2911/advanced-calculator.git
cd advanced-calculator
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## Running the Calculator

Run the application using:

```
python -m app.calculator
```

You will see:

```
Advanced Calculator Started!
Type 'help' to see available commands.
```

---

## Example Commands

```
add 5 3
power 2 4
history
undo
redo
save
load
exit
```

---

## Running Tests

To run unit tests with coverage:

```
pytest --cov=app --cov-fail-under=90
```

Current test coverage: **91%**

---

## CI/CD

GitHub Actions is configured to:

- Install dependencies
- Run pytest
- Enforce 90% test coverage
- Automatically run on push to main branch

Workflow file location:

```
.github/workflows/python-app.yml
```

---

## Error Handling

Custom exceptions:
- ValidationError
- OperationError

The application handles:
- Division by zero
- Invalid operations
- Invalid input types
- CSV read/write errors

---

## Technologies Used

- Python 3
- pandas
- pytest
- pytest-cov
- python-dotenv
- logging module
- Git & GitHub Actions

---

## Author

Advanced Calculator Project  
Software Engineering Assignment