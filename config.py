import logging
from pathlib import Path

log_file = Path(__file__).resolve().parent / "logs" / 'log.txt'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(log_file, mode='w')
handler.setLevel(logging.INFO)
log_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(log_format)
logger.addHandler(handler)


def printing_and_logging(message, log=True, print_console=True):
    if log:
        logger.info(message)
    if print_console:
        print(message)
