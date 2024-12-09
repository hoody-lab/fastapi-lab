from fastapi import FastAPI

from .api.board_api import board_router

app = FastAPI(
    docs_url = "/api/docs",
    openapi_url = "/api/openapi.json",
)

app.include_router(board_router, prefix = "/api/v1")