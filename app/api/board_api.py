from fastapi import APIRouter

board_router = APIRouter(
    prefix = "/boards",
    tags = ["board"]
)

# 게시판 목록 반환
@board_router.get("/")
def get_boards():
    return "hello"
