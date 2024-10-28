from sqlalchemy import create_engine
from src.config.init import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    pool_size = 5,    # database connection pool
    echo = True     # SQLAlchemy가 실행하는 SQL 쿼리를 콘솔에 출력하도록 설정(개발 단계)
)

Base = declarative_base()