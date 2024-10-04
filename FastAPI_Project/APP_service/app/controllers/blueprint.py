"""
File contains routes of endpoints in this service.
"""
from fastapi import APIRouter

from FastAPI_Project.APP_service.app.controllers.service1_controller import router as service1_router


router = APIRouter()

router.include_router(service1_router)

