from fastapi import APIRouter

from app.api.endpoints import (
    user,
    event,
)

api_router = APIRouter()

api_router.include_router(user.router, prefix="/api/user", tags=["user"])
api_router.include_router(event.router, prefix="/api/event", tags=["event"])
