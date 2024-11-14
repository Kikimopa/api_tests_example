import sys

from loguru import logger
from requests import Request, Response

logger.remove()
logger.add(sys.stdout, format="\n[{time:HH::mm:ss}] <lvl>{message}</lvl>", level="INFO")


def log_request(logger: logger, request: Request):

    logger.info(f"REQUEST URL:{request.method} {request.url}\n" f"BODY: {request.body}")
    return logger


def log_response(logger: logger, response: Response):
    logger.info(f"RESPONSE URL: {response.url}\n" f"STATUS CODE: {response.status_code}\n" f"BODY: {response.json()}")
    return logger
