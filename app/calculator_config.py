import os
from dotenv import load_dotenv


class CalculatorConfig:
    """
    Loads and stores configuration settings from .env file.
    """

    def __init__(self):
        load_dotenv()

        # Base Directories
        self.LOG_DIR = os.getenv("CALCULATOR_LOG_DIR", "logs")
        self.HISTORY_DIR = os.getenv("CALCULATOR_HISTORY_DIR", "history")

        # History Settings
        self.MAX_HISTORY_SIZE = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 100))
        self.AUTO_SAVE = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"

        # Calculation Settings
        self.PRECISION = int(os.getenv("CALCULATOR_PRECISION", 2))
        self.MAX_INPUT_VALUE = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1_000_000))
        self.DEFAULT_ENCODING = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")

        # Ensure directories exist
        os.makedirs(self.LOG_DIR, exist_ok=True)
        os.makedirs(self.HISTORY_DIR, exist_ok=True)

    @property
    def LOG_FILE(self):
        return os.path.join(self.LOG_DIR, "calculator.log")

    @property
    def HISTORY_FILE(self):
        return os.path.join(self.HISTORY_DIR, "history.csv")