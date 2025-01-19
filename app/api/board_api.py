from fastapi import APIRouter

from app.db.init import connect_database
from app.curd.board import board_service

board_router = APIRouter(
    prefix = "/boards",
    tags = ["board"]
)

# 게시판 전체 목록 반환
@board_router.get("/")
def get_boards():
    results = board_service.find_boards()
    return results
