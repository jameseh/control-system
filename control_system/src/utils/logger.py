import logging
from typing import Optional


class Logger:
    """
    A class to manage logging operations.

    Args:
        name (str): The name of the logger.
        level (str, optional): The logging level. Defaults to 'INFO'.

    Attributes:
        logger (logging.Logger): The logger object.
    """

    _instance = None

    @classmethod
    def __new__(
            cls,
            *args,
            **kwargs
            ):
        """
        Make the class a singleton.
        """

        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(
            self,
            name: str,
            level: Optional[str] = 'INFO',
            filename: Optional[str] = 'app.log'
    ) -> None:
        """
        Initialize the logger.
        """

        self.logger = logging.getLogger(name)
        self.set_level(level)

        handler = logging.FileHandler(filename)
        formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def set_level(
            self,
            level: str
    ) -> None:
        """
        Set the logging level.

        Args:
            level (str): The logging level.
        """

        levels = {
                'CRITICAL': logging.CRITICAL,
                'ERROR'   : logging.ERROR,
                'WARNING' : logging.WARNING,
                'INFO'    : logging.INFO,
                'DEBUG'   : logging.DEBUG
        }
        self.logger.setLevel(levels.get(level, logging.INFO))

    def log(
            self,
            level: str,
            message: str
    ) -> None:
        """
        Log a message.

        Args:
            level (str): The logging level.
            message (str): The message to log.
        """

        levels = {
                'CRITICAL': self.logger.critical,
                'ERROR'   : self.logger.error,
                'WARNING' : self.logger.warning,
                'INFO'    : self.logger.info,
                'DEBUG'   : self.logger.debug
        }
        log_method = levels.get(level, self.logger.info)
        log_method(message)
