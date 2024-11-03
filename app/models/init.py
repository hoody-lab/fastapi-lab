from app.db.init import engine, Base
from .board import Board  # 모델 임포트하여 테이블 생성 보장

# Base에 등록된 모든 테이블을 생성
Base.metadata.create_all(bind=engine)