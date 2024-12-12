from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

