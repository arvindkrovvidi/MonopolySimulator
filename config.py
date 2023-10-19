import logging
from pathlib import Path

log_directory = Path("logs")
log_file = log_directory / "log.txt"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(log_file, mode='w')
handler.setLevel(logging.INFO)
log_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(log_format)
logger.addHandler(handler)
