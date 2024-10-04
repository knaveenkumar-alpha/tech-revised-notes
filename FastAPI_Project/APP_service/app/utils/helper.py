"""File contains Sanitization of input data and perform request to service1"""
import json
import logging as LOGGER
from json import JSONDecodeError

import requests
from FastAPI_Project.APP_service.app.utils.exceptions import CustomException

LOGGER = LOGGER.getLogger("App-Service")


def fetch_data(req_data):
    """
    Responsible to validate and convert into python object.
    :param req_data: input json payload.
    :return: required input python object.
    """
    req_lc_data = {}
    try:
        if not isinstance(req_data, dict):
            req_lc_data = json.loads(req_data)
    except JSONDecodeError as err:
        LOGGER.exception(
            "Uploaded load channel is not a valid json formate."
            " Failed with error %s.", err
        )
        raise CustomException(
            payload={
                "detail": "Uploaded load channel is not a valid json formate."
                          " Please check the load channel."
            },
            status_code=400
        )
    if not bool(req_lc_data):
        LOGGER.exception("Uploaded/input load channel payload is an empty json: %s",
                         req_lc_data)
        raise CustomException(
            payload={
                "detail": f"Uploaded/input load channel payload is an "
                          f"empty json: {req_lc_data}"
            }
        )
    return req_lc_data


def process_input_files(load_channel_raw_data, load_channel_files, lc_filenames=None):
    """
    Responsible for checking input files data and also read the file data.

    :param load_channel_raw_data:
    :param load_channel_files:
    :param lc_filenames:
    :return:
    """
    load_channel_data = []
    if bool(load_channel_files):
        if any(lc_filename.split('.')[-1] != "json" for lc_filename in lc_filenames):
            raise CustomException(
                payload={
                    "detail": "Service only supports json format as of yet."
                }, status_code=400
            )
        LOGGER.info("Retrieving fields needed for performing service1")
        for lc_data in load_channel_files:
            # process input files
            load_channel_data.append(lc_data)
    else:
        lc_raw_data = load_channel_raw_data.get("content")
        load_channel_data.append(lc_raw_data)

    return load_channel_data
