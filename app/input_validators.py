from app.exceptions import ValidationError


def validate_number(value):
    """
    Validates that the input is a number.
    Converts to float if valid.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid input '{value}'. Please enter a numeric value.")


def validate_range(value, max_value):
    """
    Validates that the number does not exceed maximum allowed value.
    """
    if abs(value) > max_value:
        raise ValidationError(
            f"Input value {value} exceeds maximum allowed limit of {max_value}."
        )
    return value