"""
File contains custom middlewares for application.
"""
import logging as LOGGER

from starlette.requests import Request
from starlette.responses import JSONResponse

LOGGER = LOGGER.getLogger("App-Service")


async def catch_exceptions_middleware(request: Request, call_next):
    """
    Middleware to handle any unhandled exceptions in the service.

    :param request: actual request
    :param call_next: next callable method.
    :return: return value of respective request.
    """
    try:
        return await call_next(request)
    except Exception as err:
        LOGGER.exception("Request failed with error: %s", err)
        return JSONResponse({
            "detail": "Internal Server Error"
        }, status_code=500)
