from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.drivers.api.urls import api_router
from app.drivers.rdb.base import Base, ENGINE

app = FastAPI()

# CORSを回避するために設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
Base.metadata.create_all(bind=ENGINE, checkfirst=False)
