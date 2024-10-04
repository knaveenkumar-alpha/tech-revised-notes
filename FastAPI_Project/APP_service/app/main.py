"""
File contains code related to creating fastapi application.
"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from ..app.controllers.blueprint import router as api_router
from ..app.middleware import catch_exceptions_middleware
from ..app.utils.config import settings
from ..app.utils.events import create_start_app_handler
from ..app.utils.exceptions import CustomException, custom_exception_handler


def get_application() -> FastAPI:
    """
    Responsible for creating the FastAPI Application.
    :return: application
    """
    application = FastAPI(title="App-Service", debug=True, version="v1")
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["0.0.0.0", "*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    application.add_event_handler("startup", create_start_app_handler())
    application.include_router(api_router, tags=["App-Service"], prefix=settings.API_PREFIX)
    application.exception_handler(CustomException)(custom_exception_handler)
    application.middleware("http")(catch_exceptions_middleware)

    return application


app = get_application()
