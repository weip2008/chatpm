import logging

"""
Logging is using Elastic APM
"""
LOG_FORMAT = "%(asctime)s %(levelname)8s - %(message)s"
logging.basicConfig(filename=r"jwang.log", level=logging.WARNING,format=LOG_FORMAT)
logger = logging.getLogger("Huaxia")

logger.debug("My first debug message")
logger.info("My first info message")
logger.warning("My first warn message")
logger.error("My first error message")
logger.critical("My first fatal message")
print(logger.level)