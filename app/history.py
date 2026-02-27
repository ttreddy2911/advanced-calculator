import os
import pandas as pd
from app.calculation import Calculation
from app.exceptions import HistoryError


class History:
    """
    Manages calculation history including save and load operations.
    """

    def __init__(self, max_size=100):
        self._history = []
        self.max_size = max_size

    def add(self, calculation):
        """
        Add a new calculation to history.
        """
        if len(self._history) >= self.max_size:
            self._history.pop(0)  # remove oldest entry

        self._history.append(calculation)

    def get_all(self):
        """
        Return all history entries.
        """
        return self._history

    def clear(self):
        """
        Clear history.
        """
        self._history.clear()

    # ========================
    # CSV SAVE / LOAD (Pandas)
    # ========================

    def save_to_csv(self, file_path):
        try:
            data = [calc.to_dict() for calc in self._history]
            df = pd.DataFrame(data)
            df.to_csv(file_path, index=False)
        except Exception as e:
            raise HistoryError(f"Failed to save history: {e}")

    def load_from_csv(self, file_path):
        if not os.path.exists(file_path):
            raise HistoryError("History file does not exist.")

        try:
            df = pd.read_csv(file_path)
            self._history.clear()

            for _, row in df.iterrows():
                calc = Calculation(
                    row["operation"],
                    row["operand1"],
                    row["operand2"],
                    row["result"],
                )
                self._history.append(calc)

        except Exception as e:
            raise HistoryError(f"Failed to load history: {e}")