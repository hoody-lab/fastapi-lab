from sqlalchemy import Column, Text, String

from .base import BaseModel

class Board(BaseModel):
    __abstract__ = False

    title = Column(String(255), nullable = False)
    content = Column(Text, nullable = False)