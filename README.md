Perfect 👌 Your README is already good.

I will now give you an **updated professional version** that:

* ✅ Clearly mentions optional feature (Colorama)
* ✅ Mentions 91% coverage
* ✅ Mentions design patterns properly
* ✅ Looks more “A-grade level”
* ✅ Matches rubric expectations

You can replace your current README with this:

---

# Advanced Calculator Application

## Project Overview

This project is an advanced command-line calculator built in Python.

It supports multiple arithmetic operations, undo/redo functionality, logging, history management, CSV persistence, environment configuration, and automated testing with CI/CD integration.

The application follows professional software engineering practices including design patterns, object-oriented programming, automated testing, and DevOps principles.

---

# Core Features

## Arithmetic Operations

The calculator supports the following operations:

* add
* subtract
* multiply
* divide
* power
* root
* modulus
* int_divide
* percent
* abs_diff

Each operation takes exactly two numerical inputs and returns a computed result.

---

# History Management

* View calculation history
* Clear history
* Undo last operation
* Redo last undone operation

Undo/Redo functionality is implemented using the **Memento Design Pattern**.

---

# Data Persistence

* Save history to CSV using pandas
* Load history from CSV
* Automatic history saving (configurable)

Each CSV entry includes:

* Operation
* Operand 1
* Operand 2
* Result
* Timestamp

---

# Logging System

* Logs calculations and errors to file
* Uses Python's built-in logging module
* Supports INFO and ERROR levels

All operations and exceptions are recorded in the configured log file.

---

# Configuration Management

The application uses a `.env` file with `python-dotenv`.

Configurable parameters include:

* CALCULATOR_LOG_DIR
* CALCULATOR_HISTORY_DIR
* CALCULATOR_MAX_HISTORY_SIZE
* CALCULATOR_AUTO_SAVE
* CALCULATOR_PRECISION
* CALCULATOR_MAX_INPUT_VALUE
* CALCULATOR_DEFAULT_ENCODING

If environment variables are not set, default values are applied.

---

# Design Patterns Implemented

This project applies several software design patterns:

* Factory Pattern → Creates arithmetic operation objects dynamically
* Memento Pattern → Enables undo/redo functionality
* Observer Pattern → Used for logging and auto-saving history
* REPL Pattern → Command-line interaction loop

---

# Optional Feature (For A Grade)

## Color-Coded Command-Line Output

This project implements color-coded terminal output using the **Colorama** library:

* Green → Successful results
* Red → Errors
* Cyan → System messages

This improves readability and enhances the user experience.

---

# Project Structure

```
project_root/
│
├── app/
│   ├── calculator.py
│   ├── operations.py
│   ├── history.py
│   ├── logger.py
│   └── ...
│
├── tests/
├── .env
├── requirements.txt
├── README.md
└── .github/workflows/python-app.yml
```

---

# Installation

## 1. Clone Repository

```
git clone https://github.com/ttreddy2911/advanced-calculator.git
cd advanced-calculator
```

## 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

# Running the Calculator

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

# Example Commands

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

# Running Tests

To execute unit tests with coverage enforcement:

```
pytest --cov=app --cov-fail-under=90
```

Current test coverage: **91%**

All tests pass successfully.

---

# Continuous Integration (CI/CD)

GitHub Actions is configured to:

* Install dependencies
* Run pytest
* Enforce minimum 90% coverage
* Trigger on push or pull request to main branch

Workflow file location:

```
.github/workflows/python-app.yml
```

---

# Error Handling

Custom exceptions implemented:

* ValidationError
* OperationError
* HistoryError

The application gracefully handles:

* Division by zero
* Invalid operations
* Invalid input types
* CSV read/write errors
* Exceeding maximum input value

---

# Technologies Used

* Python 3
* pandas
* pytest
* pytest-cov
* python-dotenv
* colorama
* logging module
* Git
* GitHub Actions

---

# Learning Outcomes Covered

This project demonstrates:

* Git version control and clear commit history
* Linux command-line execution
* Python OOP development
* Automated testing with pytest
* CI/CD using GitHub Actions
* CSV manipulation using pandas
* Application of software design patterns

---

# Author

Advanced Calculator Project
Software Engineering Assignment

