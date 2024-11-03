from sqlalchemy import Column, Integer, DateTime, Boolean
from datetime import datetime

from app.db.init import Base

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key = True, autoincrement = True)
    is_deleted = Column(Boolean, default = False)
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now, onupdate = datetime.now)