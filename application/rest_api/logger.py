import logging
from logging.handlers import RotatingFileHandler
import sys

# Create a logger instance
logger = logging.getLogger('rest_variantValidator')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M")

# Create handler for stdout 
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG) # Log debug and higher to stdout
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Create handler for stderr
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.ERROR)  # Log errors and higher to stderr
stderr_handler.setFormatter(formatter)
logger.addHandler(stderr_handler)

# Create a file handler that logs debug and higher level messages
file_handler = RotatingFileHandler('rest_variantValidator.log', maxBytes=500000, backupCount=5)


file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



