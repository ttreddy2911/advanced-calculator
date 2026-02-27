from app.operations import OperationFactory
from app.input_validators import validate_number, validate_range
from app.calculation import Calculation
from app.history import History
from app.calculator_memento import Caretaker
from app.calculator_config import CalculatorConfig
from app.logger import CalculatorLogger
from app.exceptions import OperationError, ValidationError, HistoryError


class Calculator:
    """
    Main Calculator class that connects all components.
    """

    def __init__(self):
        self.config = CalculatorConfig()
        self.history = History(self.config.MAX_HISTORY_SIZE)
        self.caretaker = Caretaker()
        self.logger = CalculatorLogger(self.config.LOG_FILE)
        self.observers = []

    # ==========================
    # Observer Pattern
    # ==========================

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, calculation):
        for observer in self.observers:
            observer.update(calculation)

    # ==========================
    # Core Operation Execution
    # ==========================

    def perform_operation(self, operation_name, value1, value2):
        try:
            # Validate inputs
            a = validate_number(value1)
            b = validate_number(value2)

            validate_range(a, self.config.MAX_INPUT_VALUE)
            validate_range(b, self.config.MAX_INPUT_VALUE)

            # Save current state before change (for undo)
            self.caretaker.save(self.history.get_all())

            # Create operation using Factory
            operation = OperationFactory.create_operation(operation_name)
            result = operation.execute(a, b)

            # Apply precision
            result = round(result, self.config.PRECISION)

            # Create calculation record
            calculation = Calculation(operation_name, a, b, result)

            # Add to history
            self.history.add(calculation)

            # Log
            self.logger.log_info(
                f"{operation_name}({a}, {b}) = {result}"
            )

            # Notify observers
            self.notify_observers(calculation)

            return result

        except (OperationError, ValidationError) as e:
            self.logger.log_error(str(e))
            raise

    # ==========================
    # Undo / Redo
    # ==========================

    def undo(self):
        new_state = self.caretaker.undo(self.history.get_all())
        self.history._history = new_state
        return "Undo successful."

    def redo(self):
        new_state = self.caretaker.redo(self.history.get_all())
        self.history._history = new_state
        return "Redo successful."

    # ==========================
    # History Management
    # ==========================

    def get_history(self):
        return self.history.get_all()

    def clear_history(self):
        self.history.clear()
        return "History cleared."

    def save_history(self):
        try:
            self.history.save_to_csv(self.config.HISTORY_FILE)
            return "History saved successfully."
        except HistoryError as e:
            self.logger.log_error(str(e))
            raise

    def load_history(self):
        try:
            self.history.load_from_csv(self.config.HISTORY_FILE)
            return "History loaded successfully."
        except HistoryError as e:
            self.logger.log_error(str(e))
            raise


# ==========================
# Observers Implementation
# ==========================

class LoggingObserver:
    def __init__(self, logger):
        self.logger = logger

    def update(self, calculation):
        self.logger.log_info(
            f"Observer Log: {calculation.operation} "
            f"{calculation.operand1}, {calculation.operand2} = {calculation.result}"
        )


class AutoSaveObserver:
    def __init__(self, history, config):
        self.history = history
        self.config = config

    def update(self, calculation):
        if self.config.AUTO_SAVE:
            self.history.save_to_csv(self.config.HISTORY_FILE)