from fastapi import FastAPI
from sqlalchemy import String
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from app.drivers.api.urls import api_router

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


@app.get("/")
async def root() -> String:
    return {"message": "Hello Calendere Applications!"}
