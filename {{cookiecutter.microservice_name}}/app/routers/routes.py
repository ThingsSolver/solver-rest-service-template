# Endpoints, you can create multiple files if is necessary and include them into main.py

from fastapi import APIRouter, Request

from app.api.services import Basic
from app.api.models import CustomerInfo

api = APIRouter()


@api.get("/healthcheck")
async def health_check(request: Request):
    message = {"HEALTH": "OK"}

    return message


@api.get("/test/{uid}", response_model=CustomerInfo)
async def parse_input(uid: str):
    return Basic().get_customer_info(uid)
    # return Recommender.get_recommended_items(uid)
