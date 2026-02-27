from abc import ABC, abstractmethod
from app.exceptions import OperationError


# =========================
# Base Operation (Abstract)
# =========================
class BaseOperation(ABC):
    """
    Abstract base class for all operations.
    """

    @abstractmethod
    def execute(self, a, b):
        pass


# =========================
# Operation Implementations
# =========================

class AddOperation(BaseOperation):
    def execute(self, a, b):
        return a + b


class SubtractOperation(BaseOperation):
    def execute(self, a, b):
        return a - b


class MultiplyOperation(BaseOperation):
    def execute(self, a, b):
        return a * b


class DivideOperation(BaseOperation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Division by zero is not allowed.")
        return a / b


class PowerOperation(BaseOperation):
    def execute(self, a, b):
        return a ** b


class RootOperation(BaseOperation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot calculate zeroth root.")
        if a < 0 and b % 2 == 0:
            raise OperationError("Even root of negative number is not allowed.")
        return a ** (1 / b)


class ModulusOperation(BaseOperation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Modulus by zero is not allowed.")
        return a % b


class IntDivideOperation(BaseOperation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Integer division by zero is not allowed.")
        return a // b


class PercentOperation(BaseOperation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot calculate percentage with zero denominator.")
        return (a / b) * 100


class AbsDiffOperation(BaseOperation):
    def execute(self, a, b):
        return abs(a - b)


# =========================
# Factory Pattern
# =========================

class OperationFactory:
    """
    Factory class to create operation instances.
    """

    _operations = {
        "add": AddOperation,
        "subtract": SubtractOperation,
        "multiply": MultiplyOperation,
        "divide": DivideOperation,
        "power": PowerOperation,
        "root": RootOperation,
        "modulus": ModulusOperation,
        "int_divide": IntDivideOperation,
        "percent": PercentOperation,
        "abs_diff": AbsDiffOperation,
    }

    @classmethod
    def create_operation(cls, operation_name):
        operation_name = operation_name.lower()

        if operation_name not in cls._operations:
            raise OperationError(f"Operation '{operation_name}' is not supported.")

        return cls._operations[operation_name]()