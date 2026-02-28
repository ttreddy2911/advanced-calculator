import pytest
from app.calculator import Calculator
from app.exceptions import OperationError


def test_perform_operation():
    calc = Calculator()
    result = calc.perform_operation("add", 5, 3)
    assert result == 8


def test_invalid_input():
    calc = Calculator()
    with pytest.raises(Exception):
        calc.perform_operation("add", "abc", 3)


def test_undo_redo():
    calc = Calculator()
    calc.perform_operation("add", 5, 3)
    calc.undo()
    assert len(calc.get_history()) == 0
    calc.redo()
    assert len(calc.get_history()) == 1