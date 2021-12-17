from fastapi import FastAPI

# from typing import Dict
# from app.drivers.api.endpoints import user, event

from app.driver.api.urls import api_router

app = FastAPI()

app.include_router(api_router)
