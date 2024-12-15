import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger(log_file):
    """
    Set up application logging. Creates the log directory if it does not exist.
    :param log_file: Path to the log file.
    """
    # Ensure the logs directory exists
    log_path = Path(log_file).parent
    log_path.mkdir(parents=True, exist_ok=True)

    # Configure logging
    logger = logging.getLogger("api_logger")
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=3)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    logger.addHandler(handler)
    return logger
