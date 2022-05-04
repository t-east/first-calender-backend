from fastapi import APIRouter

from app.drivers.api.endpoints import user, event, tag
from app.drivers.user_auth.driver.endpoint import auth

api_router = APIRouter()

api_router.include_router(user.router, prefix="/api/users", tags=["user"])
api_router.include_router(event.router, prefix="/api/events", tags=["event"])
api_router.include_router(tag.router, prefix="/api/tags", tags=["tag"])
api_router.include_router(auth.router, prefix="/api/tokens", tags=["auth"])
