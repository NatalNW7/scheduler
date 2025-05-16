from sqlalchemy import update, delete
from sqlalchemy.orm import Session
from datetime import time
from typing import List

from src.ports.job_repository import JobsRepository
from src.core.domain.job import Job
from src.core.execptions import JobNotFoundException
from src.adapters.db.models import JobModel


class PostgresJobRepository(JobsRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, job: Job) -> Job:
        model = JobModel.from_entity(job)

        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)

        return model.to_entity()
    
    def save_batch(self, jobs: List[Job]) -> List[Job]:
        models = [JobModel.from_entity(job) for job in jobs]
        
        self.session.add_all(models)
        self.session.flush()

        return [job_model.to_entity() for job_model in models]
        
    
    def find(self, job_id: int) -> Job:
        job: JobModel = self.session.query(JobModel).get(job_id)

        if job is None:
            raise JobNotFoundException(job_id)
            
        return job.to_entity()
        
    def update_status(self, job_id: int, status: str):
        stmt = (
            update(JobModel)
            .where(JobModel.id == job_id)
            .values(status=status)
        )

        result = self.session.execute(stmt)

        if result.rowcount == 0:
            raise JobNotFoundException(job_id)

        return self.find(job_id)
    
    def delete(self, job_id: int):
        stmt = (
            delete(JobModel)
            .where(JobModel.id == job_id)
        )

        result = self.session.execute(stmt)

        if result.rowcount == 0:
            raise JobNotFoundException(job_id)
