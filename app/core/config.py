from pydantic import BaseSettings, Field   # env에 해당하는 값을 가져온다.
# 해당 모듈을 사용하면 dot_env 와 달리 타입 검증도 가능하다.

class DatabaseConfig(BaseSettings):
    url: str = Field(env = 'DATABASE_URL')

database_config = DatabaseConfig()