import logging


def setup_logger(log_file: str) -> logging.Logger:
    """
    Set up and configure a logger.

    Args:
        log_file (str): The name of the log file

    Returns:
        logging.Logger: A configured logger object
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(message)s")
    file_handler = logging.FileHandler(log_file, mode="w")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
