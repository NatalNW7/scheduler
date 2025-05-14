from sqlalchemy.orm import Session
from datetime import time
from typing import List

from src.ports.job_repository import JobsRepository
from src.core.domain.job import Job
from src.adapters.db.models import JobModel
from src.adapters.db.mappers import job_mapper


class PostgreaJobRepository(JobsRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, job: Job) -> Job:
        model = JobModel(
            branch=job.branch,
            url=job.url,
            platform=job.platform,
            status=job.status,
            scheduled_at=job.scheduled_at
        )

        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)

        job.id = model.id
        job.created_at = model.created_at
        job.updated_at = model.updated_at

        return job
    
    def find_job(self, job_id: int) -> Job:
        job = self.session.query(JobModel).get(job_id)

        if job:
            return job_mapper(job)