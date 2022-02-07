from fastapi import APIRouter

from app.drivers.api.endpoints import (
    user,
    event,
    tag
)

api_router = APIRouter()

api_router.include_router(user.router, prefix="/api/user", tags=["user"])
api_router.include_router(event.router, prefix="/api/event", tags=["event"])
api_router.include_router(tag.router, prefix="/api/tag", tags=["tag"])
