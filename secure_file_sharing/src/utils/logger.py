import logging
import sys
from src.config import LOG_FILE


def setup_logger():
    #create custom logger
    logger=logging.getLogger("FileServer")
    logger.setLevel(logging.DEBUG)

    #log message format
    formatter= logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    #Handler 1 : Output to console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    #Handler 2 : Output to a file

    file_handler= logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


    return logger


logger = setup_logger()


