from visa.logger import logging
from visa.exception import USvisaException
import sys

logging.info("check logger")

try:
    a = 2/0
except Exception as e:
    raise USvisaException(e, sys)
