from pydantic import Field   # env에 해당하는 값을 가져온다.
from pydantic_settings import BaseSettings
# 해당 모듈을 사용하면 dot_env 와 달리 타입 검증도 가능하다.

class DatabaseConfig(BaseSettings):
    url: str = Field(env = 'DATABASE_URL')

    class Config:
        env_file = ".env"

database_config = DatabaseConfig()