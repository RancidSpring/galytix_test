import logging
import sys


def initialize_logger(name: str, log_level: int = logging.DEBUG) -> logging.Logger:
    """
    Initializes a logger with the given name and level. Adds a console handler if none exists.
    :params name: (str): Name of the logger.
    :params log_level (int): Logging level, e.g., logging.DEBUG, logging.INFO.
    :return: logging.Logger: Configured logger.

    Example:
        logger = initialize_logger(__name__, logging.INFO)
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)
        console_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)-8s - %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger