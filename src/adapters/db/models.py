from sqlalchemy import Column, Integer, String, Time, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class JobModel(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    branch = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    scheduled_at = Column(Time, nullable=False)
    status = Column(String, nullable=False, default="pending")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)