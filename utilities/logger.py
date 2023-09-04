import logging


class Logger:
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO  # Set your desired log level here.
    )

    @staticmethod
    def info(message):
        logger = logging.getLogger(__name__)
        logger.info(message)

    @staticmethod
    def warning(message):
        logger = logging.getLogger(__name__)
        logger.warning(message)

    @staticmethod
    def error(message):
        logger = logging.getLogger(__name__)
        logger.error(message)

    @staticmethod
    def debug(message):
        logger = logging.getLogger(__name__)
        logger.debug(message) 