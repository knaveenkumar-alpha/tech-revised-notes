"""
Contains custom exception schema for application.
"""
from fastapi import Request
from fastapi.responses import JSONResponse


class CustomException(Exception):
    """
    Exception with custom schema to have a uniformity throughout application.
    """

    def __init__(self, payload: dict, status_code: int = 500) -> None:
        """
        Prepare payload with required info.
        :param payload:
        :param status_code:
        """
        self.payload = payload
        self.status_code = status_code


async def custom_exception_handler(request: Request, exc: CustomException):
    """
    Handle custom exception and outputs json formatted details.
    :param request: request
    :param exc: user exception class CustomException.
    :return: Json response with content and status code.
    """
    return JSONResponse(content=exc.payload, status_code=exc.status_code)

