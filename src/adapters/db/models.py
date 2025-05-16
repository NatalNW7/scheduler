from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Time
from sqlalchemy.ext.declarative import declarative_base

from src.core.domain.job import Job

Base = declarative_base()


class JobModel(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    branch = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    scheduled_at = Column(Time, nullable=False)
    status = Column(String, nullable=False, default='pending')
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    @staticmethod
    def from_entity(job: Job):
        return JobModel(
            id=job.id,
            url=job.url,
            branch=job.branch,
            platform=job.platform,
            status=job.status,
            scheduled_at=job.scheduled_at,
        )

    def to_entity(self) -> Job:
        return Job(
            id=self.id,
            url=self.url,
            branch=self.branch,
            platform=self.platform,
            status=self.status,
            scheduled_at=self.scheduled_at,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
