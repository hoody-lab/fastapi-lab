from pydantic import BaseSettings, Field   # env에 해당하는 값을 가져온다.

class DatabaseConfig(BaseSettings):
    database_url: str = Field(env = 'DATABASE_URL')