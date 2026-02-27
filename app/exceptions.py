class OperationError(Exception):
    """Raised when an invalid mathematical operation occurs."""
    pass


class ValidationError(Exception):
    """Raised when user input validation fails."""
    pass


class HistoryError(Exception):
    """Raised when history-related errors occur."""
    pass