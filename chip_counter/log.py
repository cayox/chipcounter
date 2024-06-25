import logging
from logging.handlers import RotatingFileHandler


class PrettyFormatter(logging.Formatter):
    """Custom formatter to output a prettier and more informative log message."""

    def __init__(self):
        super().__init__()
        self.fmt = "{asctime} - {levelname} - {message}"
        self.datefmt = "%Y-%m-%d %H:%M:%S"
        self.style = "{"

    def format(self, record: logging.LogRecord) -> str:  # noqa: D102
        # Setting the default format for the message before adding extras
        format_orig = self.fmt
        format_orig = "[{filename}:{lineno} ({funcName})] " + format_orig

        formatter = logging.Formatter(
            format_orig,
            datefmt=self.datefmt,
            style=self.style,
        )
        return formatter.format(record)


def setup_basic_logger(log_file_path: str) -> None:
    """Configures the basic logging setup to use both terminal and rotating log file output with custom formatting.

    Args:
    log_file_path (str): Path to the log file.
    """
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()

    # Clear all existing handlers to avoid duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()

    # Stream handler for terminal logging
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(PrettyFormatter())

    # File handler setup
    file_handler = RotatingFileHandler(log_file_path, maxBytes=2**18, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(PrettyFormatter())

    # Adding handlers to the root logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    logging.getLogger("urllib3").setLevel(logging.CRITICAL)
