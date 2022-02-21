import logging


def print_vs_logging():
    """Instead of using print statements, use logging"""
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.error("This is an error message")


def main():
    """We can define out own logging format"""
    level = logging.DEBUG
    fmt = "%(asctime)s %(levelname)s %(message)s"
    logging.basicConfig(level=level, format=fmt)
