from app.models.board import Board

class BoardService:
    def get_boards():
        return board_repository.find_boards()

class BoardRepository(BaseRepository):
    def find_boards(self):
        # 자원을 획득하고 반납해야 하는 경우 with를 사용한다.
        with self.db:
            boards = db.query(Board).all()

        return boards

board_service = BoardService()
board_repository = BoardRepository()