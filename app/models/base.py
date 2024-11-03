from sqlalchemy import Column, DateTime, Boolean
from datetime import datetime

from app.db.database_init import Base

class BaseModel(Base):
    __abstract__ = True

    is_deleted = Column(Boolean, default = False)
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now, onupdate = datetime.now)