import pytest
from app.calculator import Calculator, start_repl
from app.exceptions import OperationError, ValidationError


# ==========================
# Basic Operation Tests
# ==========================

def test_perform_add_operation():
    calc = Calculator()
    result = calc.perform_operation("add", 5, 3)
    assert result == 8
    assert len(calc.get_history()) == 1


def test_perform_subtract_operation():
    calc = Calculator()
    result = calc.perform_operation("subtract", 10, 4)
    assert result == 6


def test_invalid_operation():
    calc = Calculator()
    with pytest.raises(OperationError):
        calc.perform_operation("invalid", 5, 3)


def test_invalid_input():
    calc = Calculator()
    with pytest.raises(ValidationError):
        calc.perform_operation("add", "abc", 3)


# ==========================
# Undo / Redo Tests
# ==========================

def test_undo_functionality():
    calc = Calculator()
    calc.perform_operation("add", 5, 3)
    assert len(calc.get_history()) == 1

    calc.undo()
    assert len(calc.get_history()) == 0


def test_redo_functionality():
    calc = Calculator()
    calc.perform_operation("add", 5, 3)
    calc.undo()
    calc.redo()
    assert len(calc.get_history()) == 1


def test_undo_without_operations():
    calc = Calculator()
    message = calc.undo()
    assert "Undo" in message


def test_redo_without_operations():
    calc = Calculator()
    message = calc.redo()
    assert "Redo" in message


# ==========================
# History Management Tests
# ==========================

def test_clear_history():
    calc = Calculator()
    calc.perform_operation("add", 5, 3)
    calc.clear_history()
    assert len(calc.get_history()) == 0


def test_multiple_operations_history():
    calc = Calculator()
    calc.perform_operation("add", 1, 2)
    calc.perform_operation("multiply", 2, 3)
    assert len(calc.get_history()) == 2


def test_history_max_size_limit():
    calc = Calculator()
    calc.config.MAX_HISTORY_SIZE = 1
    calc.history.max_size = 1

    calc.perform_operation("add", 1, 1)
    calc.perform_operation("add", 2, 2)

    assert len(calc.get_history()) == 1


# ==========================
# Save / Load CSV Tests
# ==========================

def test_save_and_load_history(tmp_path):
    calc = Calculator()
    calc.perform_operation("add", 5, 3)

    file_path = tmp_path / "history.csv"

    calc.history.save_to_csv(file_path)
    calc.history.clear()
    assert len(calc.get_history()) == 0

    calc.history.load_from_csv(file_path)
    assert len(calc.get_history()) == 1


def test_save_history_method(tmp_path):
    calc = Calculator()
    calc.perform_operation("add", 10, 5)

    calc.config.HISTORY_DIR = tmp_path
    result = calc.save_history()
    assert "saved" in result.lower()


def test_load_history_wrapper(tmp_path):
    calc = Calculator()
    calc.perform_operation("add", 8, 2)

    file_path = tmp_path / "history.csv"
    calc.history.save_to_csv(file_path)
    calc.history.clear()

    calc.config.HISTORY_DIR = tmp_path
    calc.load_history()

    assert isinstance(calc.get_history(), list)


def test_load_nonexistent_history():
    calc = Calculator()
    with pytest.raises(Exception):
        calc.history.load_from_csv("fake_file.csv")


def test_save_history_error_handling(monkeypatch):
    calc = Calculator()

    def fake_save(*args, **kwargs):
        raise Exception("forced error")

    monkeypatch.setattr(calc.history, "save_to_csv", fake_save)

    with pytest.raises(Exception):
        calc.save_history()


# ==========================
# Observer Coverage Tests
# ==========================

def test_notify_observers_called():
    calc = Calculator()

    class DummyObserver:
        def __init__(self):
            self.called = False

        def update(self, calculation):
            self.called = True

    observer = DummyObserver()
    calc.register_observer(observer)

    calc.perform_operation("add", 3, 3)
    assert observer.called is True


# ==========================
# Extra Tiny Boost Tests
# ==========================

def test_get_history_returns_list():
    calc = Calculator()
    calc.perform_operation("add", 1, 1)
    history = calc.get_history()
    assert isinstance(history, list)


def test_calculation_repr():
    calc = Calculator()
    calc.perform_operation("add", 2, 2)
    history = calc.get_history()
    assert "add" in repr(history[0])


# ==========================
# Edge Case Tests
# ==========================

def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(OperationError):
        calc.perform_operation("divide", 5, 0)


def test_root_invalid_case():
    calc = Calculator()
    with pytest.raises(OperationError):
        calc.perform_operation("root", -9, 2)


# ==========================
# Config Coverage Tests
# ==========================

def test_config_values_loaded():
    calc = Calculator()
    assert calc.config.MAX_HISTORY_SIZE > 0
    assert calc.config.PRECISION >= 0
    assert calc.config.MAX_INPUT_VALUE > 0


# ==========================
# REPL Coverage Tests
# ==========================

def test_repl_help_and_exit(monkeypatch):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    start_repl()


def test_repl_add_operation(monkeypatch):
    inputs = iter(["add 2 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    start_repl()


def test_repl_invalid_command(monkeypatch):
    inputs = iter(["unknowncommand", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    start_repl()


def test_repl_history_command(monkeypatch):
    inputs = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    start_repl()