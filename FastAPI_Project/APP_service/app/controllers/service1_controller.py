"""
File contains endpoint of service1.
"""
import logging as LOGGER
from json import JSONDecodeError
from typing import List

from fastapi import File, Request, UploadFile
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from FastAPI_Project.APP_service.app.utils.exceptions import CustomException
from FastAPI_Project.APP_service.app.utils.helper import process_input_files, fetch_data

router = APIRouter()
LOGGER = LOGGER.getLogger("App-Service")


@router.post("/service1")
async def perform_service1(request: Request, load_channel_files: List[UploadFile] = File(None)):
    """Perform service1 of application."""
    LOGGER.info("Requested Service1")
    if load_channel_files:
        lc_filenames = [lc_data.filename for lc_data in load_channel_files]

        load_channel_data = [fetch_data(lc_data) for lc_data in
                             [await lc_file.read() for lc_file in load_channel_files]]
        load_channel_raw_data = None
        result = process_input_files(load_channel_raw_data, load_channel_data, lc_filenames)
    else:
        try:
            load_channel_raw_data = await request.json()
        except JSONDecodeError as err:
            LOGGER.exception("Input load channel is not a valid json format."
                             " Failed with error %s", err)
            raise CustomException(
                payload={
                    "detail": "Input load channel is not a valid json format. "
                              "Please check the load channel."
                }, status_code=400
            )
        load_channel_files = None
        result = process_input_files(load_channel_raw_data, load_channel_files)
    return JSONResponse({"Service1_response": result}, status_code=200)
