from datetime import datetime


class Calculation:
    """
    Represents a single calculation performed by the calculator.
    """

    def __init__(self, operation, operand1, operand2, result):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result
        self.timestamp = datetime.now()

    def to_dict(self):
        """
        Convert calculation to dictionary format for pandas DataFrame.
        """
        return {
            "operation": self.operation,
            "operand1": self.operand1,
            "operand2": self.operand2,
            "result": self.result,
            "timestamp": self.timestamp,
        }

    def __repr__(self):
        return (
            f"{self.operation}({self.operand1}, {self.operand2}) = "
            f"{self.result} at {self.timestamp}"
        )