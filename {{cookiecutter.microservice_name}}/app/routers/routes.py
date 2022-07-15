# Endpoints, you can create multiple files if is necessary and include them into main.py

from fastapi import APIRouter

from app.api.services import Basic
from app.api.models import Example

api = APIRouter()


@api.get("/health-check")
async def health_check():
    return {"HEALTH": "OK"}


@api.get("/test/{uid}", response_model=Example)
async def parse_input(uid: str):
    return Basic().get_data(uid)
