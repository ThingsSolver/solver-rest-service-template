# Endpoints, you can create multiple files if is necessary and include them into main.py

from fastapi import APIRouter, Request

from app.api.services import Basic
from app.api.models import Example

api = APIRouter()


@api.get("/healthcheck")
async def health_check(request: Request):
    message = {"HEALTH": "OK"}

    return message


@api.get("/test/{uid}", response_model=Example)
async def parse_input(uid: str):
    return Basic().get_data(uid)
