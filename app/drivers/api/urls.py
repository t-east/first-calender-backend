from fastapi import APIRouter

from app.drivers.api.endpoints import user, event, tag

api_router = APIRouter()

api_router.include_router(user.router, prefix="/api/users", tags=["user"])
api_router.include_router(event.router, prefix="/api/events", tags=["event"])
api_router.include_router(tag.router, prefix="/api/tags", tags=["tag"])
